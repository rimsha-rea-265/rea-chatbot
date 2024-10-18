import os 
from context import create_listing_context

from langchain_core.prompts import ChatPromptTemplate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain import HuggingFaceHub
from langchain.vectorstores import FAISS

from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
llm =HuggingFaceHub(repo_id="mistralai/Mistral-Small-Instruct-2409", model_kwargs={"temperature":0.5,"max_length":128},  task="text-generation")

# 2. Incorporate the retriever into a question-answering chain.
system_prompt = (
    "You are a chatbot answering questions about real estate listings."
    "Use the following pieces of retrieved information to answer "
    "the question about the listing. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise. Always start your answer with 'Assistant:'."
    "\n\n"
    "{context}"
)

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)


contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)



def data_retriever(listing_dict):
    data = create_listing_context(listing_dict)
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(data, embeddings)
    retriever = db.as_retriever()
    return retriever

def history_aware_retriever(retriever):
    return create_history_aware_retriever(llm, retriever, contextualize_q_prompt)


def get_rag_agent(listing_dict):
    retriever = data_retriever(listing_dict)

    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    
    rag_agent = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    return rag_agent