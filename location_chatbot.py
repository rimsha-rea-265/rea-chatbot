import googlemaps

# use google maps to calculate the distance to nearest kindergartend from list_dict['house+number'] + list_dict['street'] + list_dict['zipcode'] + list_dict['city'] + list_dict['country']

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

# Construct the address from listing_dict
address = f"{listing_dict['house_number']} {listing_dict['street']}, {listing_dict['zipcode']} {listing_dict['city']}, {listing_dict['country']}"

# Geocode the address to get the latitude and longitude
geocode_result = gmaps.geocode(address)
location = geocode_result[0]['geometry']['location']
latitude, longitude = location['lat'], location['lng']

# Find the nearest kindergarten
places_result = gmaps.places_nearby(location=(latitude, longitude), radius=5000, type='school')

# Extract the distance to the nearest kindergarten
if places_result['results']:
    nearest_kindergarten = places_result['results'][0]
    kindergarten_location = nearest_kindergarten['geometry']['location']
    distance_matrix = gmaps.distance_matrix(origins=[(latitude, longitude)], destinations=[(kindergarten_location['lat'], kindergarten_location['lng'])])
    distance_to_kindergarten = distance_matrix['rows'][0]['elements'][0]['distance']['text']
else:
    distance_to_kindergarten = "No kindergarten found within 5 km radius"

print(f"Distance to nearest kindergarten: {distance_to_kindergarten}")