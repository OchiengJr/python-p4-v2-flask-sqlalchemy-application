# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Route to fetch all pets
@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    pet_list = [{'id': pet.id, 'name': pet.name, 'species': pet.species} for pet in pets]
    return jsonify(pet_list)

# Route to fetch a specific pet by ID
@app.route('/pets/<int:id>', methods=['GET'])
def get_pet(id):
    pet = Pet.query.get_or_404(id)
    return jsonify({'id': pet.id, 'name': pet.name, 'species': pet.species})

# Route to create a new pet
@app.route('/pets', methods=['POST'])
def create_pet():
    data = request.json
    name = data.get('name')
    species = data.get('species')
    if not name or not species:
        return make_response(jsonify({'error': 'Name and species are required'}), 400)
    
    new_pet = Pet(name=name, species=species)
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({'id': new_pet.id, 'name': new_pet.name, 'species': new_pet.species}), 201

# Route to update an existing pet
@app.route('/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    pet = Pet.query.get_or_404(id)
    data = request.json
    pet.name = data.get('name', pet.name)
    pet.species = data.get('species', pet.species)
    db.session.commit()
    return jsonify({'id': pet.id, 'name': pet.name, 'species': pet.species})

# Route to delete a pet
@app.route('/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': 'Pet deleted'}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
