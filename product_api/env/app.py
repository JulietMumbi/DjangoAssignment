from flask import Flask, request, jsonify

app = Flask(__name__)

products = []
product_id_counter = 1

@app.route('/products', methods=['POST'])
def create_product():
    global product_id_counter
    data = request.get_json()

    if 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    product = {
        'id': product_id_counter,
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    product_id_counter += 1
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)