from flask import Flask, jsonify, request

# Create an instance of the Flask class
app = Flask(__name__)

# Sample in-memory data
items = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Cherry"}
]

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, Flask API!'})

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    if not new_item or 'name' not in new_item:
        return jsonify({'error': 'Bad request, missing item name'}), 400

    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
