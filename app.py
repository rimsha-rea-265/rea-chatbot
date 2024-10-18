from fastapi import FastAPI, Depends, HTTPException
from chatbotworkflow import create_workflow
from detailedPageChatBot import get_rag_agent  
from database import engine , get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import model
import schemas

app = FastAPI()

# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",  "http://localhost:8000", ],  # Adjust to match your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Create the database tables
model.Base.metadata.create_all(bind=engine)


def get_config(db, user_id):
    config = db.query(model.Config).filter(model.Config.user_id == user_id).first()
    if not config:
        id =  db.query(model.Config).count() + 1
        config = model.Config(id  =  id , user_id=user_id)
        db.add(config)
        db.commit()
        db.refresh(config)
    return config

def update_chatbot_data(db, user_id, question, answer):
    config = get_config(db, user_id=user_id)
    chatbot = model.Chatbot(question=question, answer=answer, config_id=config.id)
    db.add(chatbot)
    db.commit()
    db.refresh(chatbot)
    return chatbot

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chatbot/")
def invoke_chatbot(user_id, question, data : schemas.ChatbotQuestion, db: Session = Depends(get_db),):
    data_dict = data.dict()
    
    data_dict["viewing_date"] = "2022-12-12"
    data_dict["viewing_start_time"] = "10:00"
    data_dict["viewing_end_time"] = "12:00"

    rag_agent = get_rag_agent(data_dict)
    chatbot = create_workflow(rag_agent)
    config = get_config(db, user_id=user_id )
    config = {"configurable": {"thread_id": str(config.user_id)}}
    result = chatbot.invoke(
        {"input": question.lower()},
        config=config,
    )

    print(result["answer"])
    update_chatbot_data(db, user_id, question, result["answer"])
    return {"answer" : result["answer"]}

    
