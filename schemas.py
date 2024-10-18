from typing import Optional
from pydantic import BaseModel

class ChatbotQuestion(BaseModel):
    listing_id: int
    title: str

    price: Optional[float] = None
    area: Optional[float] = None
    property_type: Optional[str] = None
    n_rooms: Optional[int] = None
    n_bedrooms: Optional[int] = None
    n_bathrooms: Optional[int] = None
    n_floors: Optional[int] = None
    propertys_floor: Optional[int] = None
    with_garden: Optional[bool] = None
    with_terrace: Optional[bool] = None
    with_balcony: Optional[bool] = None
    # fitted_kitchen: Optional[bool] = None   
    n_parking_spaces: Optional[int] = None
    parking_space_price: Optional[float] = None
    monthly_maintenance_charges: Optional[float] = None
    buyer_commission_percentage: Optional[float] = None
    buyer_commission_comments: Optional[str] = None
    notary_fee: Optional[float] = None

    # Property amenities
    with_pool: Optional[bool] = None
    furnished: Optional[bool] = None
    elevator: Optional[bool] = None
    air_conditioning: Optional[bool] = None
    storage_room: Optional[bool] = None
    cellar: Optional[bool] = None
    heating_type: Optional[str] = None
    heating_source: Optional[str] = None
    flooring_type: Optional[str] = None

    # Property condition
    condition: Optional[str] = None
    needs_renovation: Optional[bool] = None
    renovation_year: Optional[int] = None

    # Property location
    zipcode: Optional[int] = None
    house_number: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    # Property energy
    energy_type: Optional[str] = None
    energy_source: Optional[str] = None
    energy_consumption: Optional[float] = None
    energy_efficieny_class: Optional[str] = None
    is_energy_certificate_available: Optional[bool] = None
    year_of_construction_according_to_energy_certificate: Optional[int] = None

    # Property availability
    is_rented: Optional[bool] = None
    rented_from: Optional[str] = None
    rented_until: Optional[str] = None
    vacant_from: Optional[str] = None
    on_lease: Optional[bool] = None
    lease_start_date: Optional[str] = None
    lease_end_date: Optional[str] = None
    lease_duration: Optional[int] = None
    lease_charges_per_month: Optional[float] = None

    # Property construction year and media
    construction_year: Optional[int] = None


    # Contact details
    contact_person: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None