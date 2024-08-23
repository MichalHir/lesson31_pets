from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

pets = [
    {
        "id": 1,
        "name": "Rex",
        "age": 7,
        "image": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
    },
    {
        "id": 2,
        "name": "Brown",
        "age": 3,
        "image": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
    },
    {
        "id": 3,
        "name": "Sunny",
        "age": 5,
        "image": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
    },
]
# Database connection parameters
# DB_PETS = {
#     'dbname': 'PET_dbname',
#     'AGE': 'your_user',
#     'password': 'your_password',
#     'host': 'localhost',
# }

# pet list
@app.route("/pets")
def pets_list():
    return pets


# ADD a pet
@app.route("/pets", methods=["POST"])
def add_pet():
    new_pet = request.get_json()
    pets.append(new_pet)
    return {"result": "added succesfuly"}


# SHOW a pet by ID
@app.route("/pets/<id>/")
def single_pet(id):
    try:
        for pet in pets:
            if pet["id"] == int(id):
                return pet
    except:
        print("error in id")
    return {"result": "Pet not found"}


# Delete a pet by ID
@app.route("/pets/<int:id>", methods=["DELETE"])
def delete_pet(id):
    global pets
    pets = [pet for pet in pets if pet["id"] != id]
    return jsonify({"result": "Pet deleted successfully"}), 200


# UPDATE a pet by ID
@app.route("/pets/<int:id>", methods=["PUT"])
def update_pet(id):
    for pet in pets:
        if pet["id"] == int(id):
            updated_pet = request.get_json()
            pets.remove(pet)
            pets.append(updated_pet)
            return jsonify({"result": "Pet updated successfully"}), 200
    return jsonify({"result": "Pet not found"}), 400


if __name__ == "__main__":
    app.run(debug=True)
