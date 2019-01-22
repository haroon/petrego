"""Test cases for the version 1 of the API.
"""
import sys
sys.path.append('..')

import os
import tempfile
import unittest
import json
from petrego import create_app, db


class Tests(unittest.TestCase):
    """Test case for the v1 API."""

    def setUp(self):
        """Set up test fixtures.
        """
        self.test_db, test_db_name = tempfile.mkstemp()
        test_config = dict(
            ENV='development',
            TESTING=True,
            SECRET_KEY='test',
            DATABASE=test_db_name,
            DEBUG = True)
        self.app = create_app(test_config=test_config)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.init_db()

    def tearDown(self):
        """Clean up.
        """
        os.close(self.test_db)
        os.unlink(self.app.config['DATABASE'])

    def test_animalfood(self):
        """Test animalfoods end points.
        """

        """POST"""
        res = self.client.post('/api/v1/animalfoods/snake/mice/')
        self.assertEqual(res.status_code, 201)

        """GET"""
        res = self.client.get('/api/v1/animalfoods/snake/')
        result = json.loads(res.data.decode())['data']
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['food'], 'mice')

        """PUT"""
        res = self.client.put('/api/v1/animalfoods/snake/rats/')
        self.assertEqual(res.status_code, 201)

        """GET"""
        res = self.client.get('/api/v1/animalfoods/snake/')
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode())['data']
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['food'], 'rats')
        
        self.assertTrue(False)

    def test_pets(self):
        """Test pets endpoint.
        """

        pets = self._prepare_pets()

        """GET"""
        # valid owner with some pets
        self._verify_pets(pets)

        # owner with no pets
        res = self.client.get('/api/v1/pets/f2/l2/')
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode())
        self.assertEqual(len(result), 0)

        # invalid pet owner
        res = self.client.get('/api/v1/pets/f5/l5/')
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode())
        self.assertEqual(len(result), 0)

    def test_delete_pets(self):
        """Test pets endpoint with DELETE.
        """
        pets = self._prepare_pets()

        delete_pets = pets.pop()

        """DELETE"""
        res = self.client.delete(
            '/api/v1/pets/{}/{}/{}/'.format(
            delete_pets[0], delete_pets[2], delete_pets[3]))
        self.assertEqual(res.status_code, 202)

        """GET"""
        # valid owner with some pets
        self._verify_pets(pets)


    def test_owners(self):
        """Test owners endpoint.
        """

        """POST"""
        # Create some owners
        owners = [('f1', 'l1'), ('f2', 'l2'), ('f3', 'l3'), ('f4', 'l4')]
        for owner in owners:
            res = self.client.post('/api/v1/owners/{}/{}/'.format(
                owner[0], owner[1]))
            self.assertEqual(res.status_code, 201)

        """GET"""
        # All available owners
        res = self.client.get('/api/v1/owners/')
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode())['data']
        self.assertEqual(len(result), len(owners))
        for r, o in zip(result, owners):
            self.assertEqual(r['first_name'], o[0])
            self.assertEqual(r['last_name'], o[1])


    def _prepare_pets(self):
        """Create some owners and pets for pet related tests.
        """

        """POST"""
        # Create a few animals and foods
        animal_foods = [('snake', 'mice'), ('chicken', 'corn'),
            ('cat', 'fish'), ('dog', 'bones')]
        for animal_food in animal_foods:
            res = self.client.post('/api/v1/animalfoods/{}/{}/'.format(
                animal_food[0], animal_food[1]))
            self.assertEqual(res.status_code, 201)

        # Create a couple of owners
        owners = [('f1', 'l1'), ('f2', 'l2'), ('f3', 'l3'), ('f4', 'l4')]
        for owner in owners:
            res = self.client.post('/api/v1/owners/{}/{}/'.format(
                owner[0], owner[1]))
            self.assertEqual(res.status_code, 201)

        # Create some pets
        pets = [('p1', 'snake', 'f1', 'l1'),
                ('p2', 'chicken', 'f1', 'l1'),
                ('p3', 'dog', 'f1', 'l1'),
                ('p4', 'cat', 'f1', 'l1'),
                ('p5', 'snake', 'f1', 'l1')]

        for pet in pets:
            res = self.client.post('/api/v1/pets/{}/{}/{}/{}/'.format(
                pet[0], pet[1], pet[2], pet[3]))
            self.assertEqual(res.status_code, 201)

        return pets

    def _verify_pets(self, pets):
        """Verify the pets endpoint with GET.
        """
        res = self.client.get('/api/v1/pets/f1/l1/')
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode())['data']
        self.assertEqual(len(result), len(pets))
        for r, p in zip(result, pets):
            self.assertEqual(r['first_name'], 'f1')
            self.assertEqual(r['last_name'], 'l1')
            self.assertEqual(r['first_name'], p[2])
            self.assertEqual(r['last_name'], p[3])

if __name__ == "__main__":
    unittest.main()
