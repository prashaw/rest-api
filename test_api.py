import unittest
import os
import tempfile
from restaurant_api import app
import json
from flask import jsonify

class TestRestaurantApi(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.get_data(), "Hello World!")

    def test_get_restaurant(self):
        response = self.app.get('/restaurant/kfc')
        self.assertEqual(response.status_code, 200)
        assert b'kfc' in response.data

    def test_get_menuitem(self):
        response = self.app.get('/menuitem/fried chicken')
        self.assertEqual(response.status_code, 200)
        assert b'kfc' in response.data
        assert b'mc' in response.data

    def test_post_restaurant(self):
        response = self.app.post('/restaurant/subway')
        assert b'Restaurant succesfully added' in response.data

    def test_post_menuitem(self):
        self.app.post('/menuitem/kfc/drinks/mountain dew')
        response = self.app.get('/restaurant/kfc')
        assert b'mountain dew' in response.data

        self.app.post('/restaurant/chipotle')
        self.app.post('/menuitem/chipotle/drinks/apple juice')
        response = self.app.get('/restaurant/chipotle')
        assert b'apple juice' in response.data

    def test_delete_restaurant(self):
        response = self.app.delete('/restaurant/panda')
        assert b'Restaurant not in database' in response.data
        self.app.post('/restaurant/panera')
        response = self.app.get('/restaurant/panera')
        assert b'panera' in response.data
        response = self.app.delete('/restaurant/panera')
        assert b'Restaurant deleted successfully' in response.data


    def test_delete_menuitem(self):
        response = self.app.delete('/menuitem/jimmy john/drinks/coke')
        assert b'Restaurant does not exist' in response.data
        response = self.app.post('/restaurant/jimmy john')
        assert b'Restaurant succesfully added' in response.data
        response = self.app.post('/menuitem/jimmy john/drinks/mountain dew')
        assert b'Menuitem for restaurant succesfully added' in response.data
        response = self.app.delete('/menuitem/jimmy john/drinks/mountain dew')
        assert b'Menu item deleted successfully' in response.data

    def test_put_restaurant(self):
        response = self.app.post('/restaurant/pop eyes')
        assert b'Restaurant succesfully added' in response.data
        self.app.put('restaurant/pop eyes/new pop eyes')
        response = self.app.get('restaurant/pop eyes')
        assert b'Restaurant does not exist' in response.data
        response = self.app.get('restaurant/new pop eyes')
        assert b'new pop eyes' in response.data

if __name__ == "__main__":
    unittest.main()
