def create_listing_context(listing_dict):
    # Handle missing data
    def get_value(key, default="unknown"):
        return listing_dict.get(key, default)
    
    # Rental information
    if get_value('is_rented'):
        rental_info = (
            f"The property is currently rented from {get_value('rented_from')} "
            f"until {get_value('rented_until')}, with a monthly rent of €{get_value('lease_charges_per_month')}."
        )
    else:
        rental_info = "The property is not rented and is available for immediate move-in."
    
    # Lease information
    if get_value('on_lease'):
        lease_info = (
            f"The property is on lease, with the lease starting on {get_value('lease_start_date')} "
            f"and ending on {get_value('lease_end_date')}. The lease duration is {get_value('lease_duration')} years."
        )
    else:
        lease_info = "The property is not on lease."
    
    # Move-in date
    move_in_info = f"The property will be vacant from {get_value('vacant_from')}." if get_value('vacant_from') else "The move-in date is currently unavailable."
    
    # Amenities
    amenities = []
    if get_value('with_garden'):
        amenities.append("garden")
    if get_value('with_terrace'):
        amenities.append("terrace")
    if get_value('with_balcony'):
        amenities.append("balcony")
    if get_value('with_pool'):
        amenities.append("pool")
    if get_value('furnished'):
        amenities.append("furnished")
    if get_value('air_conditioning'):
        amenities.append("air conditioning")
    if get_value('elevator'):
        amenities.append("elevator")
    if get_value('storage_room'):
        amenities.append("storage room")
    if get_value('cellar'):
        amenities.append("cellar")
    
    amenities_info = "The property includes: " + ", ".join(amenities) + "." if amenities else "No special amenities are available."
    
    # Property condition
    condition_info = (
        f"The property is in {get_value('condition')} condition. "
        f"It was last renovated in {get_value('renovation_year')}, "
        f"and {'needs renovation' if get_value('needs_renovation') else 'does not need renovation'}."
    )
    
    # Location information
    location_info = (
        f"The property is located at {get_value('house_number')} {get_value('street')}, "
        f"{get_value('city')}, {get_value('state')}, {get_value('zipcode')}, {get_value('country')}."
    )
    
    # Energy information
    energy_info = (
        f"Energy type: {get_value('energy_type')}, "
        f"energy source: {get_value('energy_source')}, "
        f"energy consumption: {get_value('energy_consumption')} kWh/m², "
        f"energy efficiency class: {get_value('energy_efficieny_class')}."
    )
    
    # Price and fees
    price_info = (
        f"The asking price is €{get_value('price')}. "
        f"Buyer commission: {get_value('buyer_commission_percentage')}%, "
        f"notary fee: {get_value('notary_fee')}%, "
        f"monthly maintenance charges: €{get_value('monthly_maintenance_charges')}."
    )
    
    # Property features
    features_info = (
        f"The property has {get_value('n_rooms')} rooms, "
        f"including {get_value('n_bedrooms')} bedrooms and {get_value('n_bathrooms')} bathrooms. "
        f"It covers an area of {get_value('area')} square meters, and it is on floor {get_value('propertys_floor')} "
        f"out of {get_value('n_floors')} floors. There are {get_value('n_parking_spaces')} parking spaces available."
    )
    
    extra_charges = (
        f"Extra charges: property taxes {get_value('property_taxes')}, "
        f"distance to transport: {get_value('distance_to_transport')} minutes, "
        f"distance to city center: {get_value('distance_to_city_center')} minutes."
    )

    viewing_info = (
        f"Viewing: the property can be viewed on {get_value('viewing_date')} between {get_value('viewing_start_time')} and {get_value('viewing_end_time')}."
        f"Please click on this link http://localhost:3000/schedule-viewing/{get_value('listing_id')} for scheduling a viewing appointment."

    )
    # Combine all the information into one context
    # context = f"{rental_info} {lease_info} {move_in_info} {amenities_info} {condition_info} {location_info} {energy_info} {price_info} {features_info}"
    context = [rental_info] + [lease_info] + [move_in_info] + [amenities_info] + [condition_info] + [location_info] + [energy_info] + [price_info] + [features_info] + [extra_charges] + [viewing_info]
    
    return context




