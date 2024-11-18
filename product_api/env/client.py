import requests

# Endpoint URLs
base_url = 'http://127.0.0.1:5000/products'

# Add a new product
product_data = {
    'name': 'Sample Product',
    'description': 'This is a sample product',
    'price': 29.99
}
response = requests.post(base_url, json=product_data)
print(f"POST Response: {response.status_code}")
print(response.json())

# Retrieve all products
response = requests.get(base_url)
print(f"GET Response: {response.status_code}")
print(response.json())