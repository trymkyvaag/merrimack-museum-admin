# import requests


# def update_artwork(artwork_id, updated_data):

#     # Need to get data that is currently there before new is set
#     base_url = 'http://localhost:3000'
#     url = f'{base_url}/gallery/{artwork_id}/'
#     response = requests.put(url, json=updated_data)

#     if response.status_code == 200:
#         return "Artwork updated successfully."
#     else:
#         return f"Failed to update artwork: {response.status_code} - {response.text}"


# # Example usage of the function:
# artwork_id = 1  # Replace with the ID of the artwork you want to update
# updated_data = {
#     "title": "New Title",
#     "date_created_month": "May",
#     "date_created_year": 2023,
#     "comments": "Updated comments",
#     "width": 120,
#     "height": 80,
# }

# result = update_artwork(artwork_id, updated_data)
# print(result)
