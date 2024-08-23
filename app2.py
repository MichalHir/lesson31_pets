from flask import Flask, render_template


app = Flask(__name__)
# 'image':'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg'

pets = [
    {"id": 1, "name": "Rex", "age": 7},
    {
        "id": 2,
        "name": "Brown",
        "age": 3,
    },
    {
        "id": 3,
        "name": "Sunny",
        "age": 5,
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pets/")
def show_all_pets():
    return render_template("all_pets.html", pets=pets)


@app.route("/pets/<int:id>")
def show_pet(id):
    return render_template("pet.html", pets=pets, id=id)


if __name__ == "__main__":
    app.run(debug=True)
