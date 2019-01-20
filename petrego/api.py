"""Module containing implementation of the API baseclass."""
from flask import Blueprint, request, jsonify

class API(Blueprint):
    """Base class implementing common API endpoints.
    Version specific API can be implemented in respective subclasses.
    """

    def __init__(self, dbhelper, output_formatter,
                    name, import_name, **kwargs):
        """Register the common API endpoint handlers.
        """
        Blueprint.__init__(self, name, import_name, **kwargs)

        self.dbhelper = dbhelper
        self.output_formatter = output_formatter

        # Add routes
        # Routes for retrieving all animal records
        self.add_url_rule(
            '/animals/',
            view_func=self.getanimals, methods=['GET'])
        # Routes for creating, updating and retrieving animal-food records
        self.add_url_rule(
            '/animalfoods/<animal>/<food>/',
            view_func=self.insertanimalfood, methods=['POST'])
        self.add_url_rule(
            '/animalfoods/<animal>/<food>/',
            view_func=self.updateanimalfood, methods=['PUT'])
        self.add_url_rule(
            '/animalfoods/<animal>/',
            view_func=self.getanimalfood, methods=['GET'])
        # Route for creating owner records
        self.add_url_rule(
            '/owners/<first_name>/<last_name>/',
            view_func=self.insertowner, methods=['POST'])
        # Route for retrieving all owner records
        self.add_url_rule(
            '/owners/',
            view_func=self.getowners, methods=['GET'])
        # Routes for creating, retrieving and deleting pet records
        self.add_url_rule(
            '/pets/<pet_name>/<pet_type>/<first_name>/<last_name>/',
            view_func=self.insertpet, methods=['POST'])
        self.add_url_rule(
            '/pets/<first_name>/<last_name>/',
            view_func=self.getpets, methods=['GET'])
        self.add_url_rule(
            '/pets/<pet_name>/<first_name>/<last_name>/',
            view_func=self.deletepet, methods=['DELETE'])


    def insertanimalfood(self, animal, food):
        """Insert animal and food record in database and create a relation
        between the two.
        """
        error = ''
        if not self.dbhelper.insert_animal_food(animal, food, error):
            return self.output_formatter.format_response(422)

        return self.output_formatter.format_response(201,
            [('animals/', 'animals.all', 'GET'),
            ('animalfoods/{}/'.format(animal), 'animalfoods.search', 'GET'),
            ('animalfoods/{}/<food>'.format(animal), 'animalfoods.update', 'PUT')])

    def updateanimalfood(self, animal, food):
        """Update food an animal eats.
        """
        error = ''
        if not self.dbhelper.update_animal_food(animal, food, error):
            return self.output_formatter.format_response(422)

        return self.output_formatter.format_response(201,
            [('animals/', 'animals.all', 'GET'),
            ('animalfoods/{}/'.format(animal), 'animalfoods.search', 'GET')])

    def getanimalfood(self, animal):
        """Get the food an animal eatsself.
        """
        res = self.dbhelper.get_animal_food(animal)
        columns = ['animal', 'food']
        return self.output_formatter.format_data(columns, res)

    def getanimals(self):
        """Get the list of all animals.
        """
        res = self.dbhelper.get_animals()
        columns = ['name']
        return self.output_formatter.format_data(columns, res)

    def insertowner(self, first_name, last_name):
        """Insert an owner's record in the database.
        """
        error = ''
        if not self.dbhelper.insert_owner(first_name, last_name, error):
            return self.output_formatter.format_response(422)

        return self.output_formatter.format_response(201,
            [('owners/', 'owners.all', 'GET')])

    def getowners(self):
        """Get a list of all owners.
        """
        res = self.dbhelper.get_owners()
        columns = ['first_name', 'last_name']
        return self.output_formatter.format_data(columns, res)

    def insertpet(self, pet_name, pet_type, first_name, last_name):
        """Insert pet record in the database. An owner record must already exist or
        this request will fail.
        """
        error = ''
        if not self.dbhelper.insert_pet(first_name, last_name,
            pet_name, pet_type, error):
            return self.output_formatter.format_response(422)

        return self.output_formatter.format_response(201,
            [('pets/{}/{}/'.format(first_name, last_name), 'pets.get', 'GET')])

    def getpets(self, first_name, last_name):
        """Get a list of all pets.
        """
        res = self.dbhelper.get_pets(first_name, last_name)
        columns = ['first_name', 'last_name', 'pet_name', 'pet_type']
        return self.output_formatter.format_data(columns, res)

    def deletepet(self, pet_name, first_name, last_name):
        """Delete a pet.
        """
        error = ''
        if not self.dbhelper.delete_pet(pet_name, first_name, last_name):
            return self.output_formatter.format_response(422)

        return self.output_formatter.format_response(202,
            [('pets/{}/{}/'.format(first_name, last_name), 'pets.get', 'GET')])
