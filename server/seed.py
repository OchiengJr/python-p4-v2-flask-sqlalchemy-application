#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

def seed_pets(num_pets=10):
    """
    Seed the 'pets' table with random data using Faker.

    Args:
        num_pets (int): Number of pets to create (default is 10).
    """
    with app.app_context():
        # Create and initialize a Faker generator
        fake = Faker()

        # Delete all existing rows in the "pets" table
        Pet.query.delete()

        # List of species to choose from
        species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

        # Generate and add Pet instances to the session
        pets = []
        for _ in range(num_pets):
            pet = Pet(name=fake.first_name(), species=rc(species))
            pets.append(pet)
            db.session.add(pet)

        try:
            # Commit the session to persist changes
            db.session.commit()
            print(f'Successfully seeded {num_pets} pets.')
        except Exception as e:
            db.session.rollback()
            print(f'Error occurred during seeding: {e}')

if __name__ == '__main__':
    seed_pets()
