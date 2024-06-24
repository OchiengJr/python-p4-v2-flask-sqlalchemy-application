from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create metadata object for SQLAlchemy
metadata = MetaData()

# Initialize Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define Pet model inheriting from db.Model
class Pet(db.Model):
    """
    Model representing a pet in the database.

    Attributes:
        id (int): Primary key identifier for the pet.
        name (str): Name of the pet.
        species (str): Species of the pet.
    """
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Adjust the length as per your requirements
    species = db.Column(db.String(50))  # Adjust the length as per your requirements

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
