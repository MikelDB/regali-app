import unittest
import requests
import json
import string
import random
from requests.auth import HTTPBasicAuth

class TestGetFileNameEndPoint(unittest.TestCase):

    HOST = 'https://localhost:5000'
    USER_EMAIL = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@gmail.com"
    USER_PASSWORD = 'testpassword'

    def test_it_should_work_throw_the_happy_flow(self):
        self.__register_user()
        print('User registerd')
        self.__login_user()
        print('User Logged In')
        self.__post_list()
        print('List posted')
        self.__get_lists()
        print('Lists getted')
        self.__get_list()
        print('List getted')
        self.__post_element()
        print('Element posted')
        self.__delete_element()
        print('Element deleted')
        self.__delete_list()
        print('List deleted')

    def __register_user(self):
        url = self.HOST + "/authentication/register"

        payload = {
            "name": "Test User",
            "email":  self.USER_EMAIL,
            "password": self.USER_PASSWORD
        }
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False)
        print(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('User Created', response.json()['message'])

    def __login_user(self):
        url = self.HOST + "/authentication/login"

        response = requests.request("POST", url, headers={}, auth=(self.USER_EMAIL, self.USER_PASSWORD), verify=False)
        self.token = response.json()['token']
        self.assertEqual(200, response.status_code)

    def __post_list(self):
        url = self.HOST + '/giftlists'
        payload = {
            "name": "This is my list from postman new",
            "elements": [
                {
                    "name" : "this is an element",
                    "url" : "https://www.amazon.es"
                },
                {
                    "name" : "this is other element",
                    "url" : "https://www.amazon.es"
                }
            ]
        }

        headers = {
            'x-access-token': self.token
        }

        response = requests.request("POST", url, headers=headers, json=payload, verify=False)
        self.list_reference = response.json()['reference']
        self.element_reference = response.json()['elements'][0]['reference']
        self.assertEqual(200, response.status_code)


    def __get_lists(self):
        url = self.HOST + '/giftlists'
        headers = {
            'x-access-token': self.token
        }
        response = requests.request("GET", url, headers=headers, verify=False)

        self.assertEqual(200, response.status_code)

    def __get_list(self):
        url = self.HOST + '/giftlists/' + self.list_reference
        headers = {
            'x-access-token': self.token
        }
        response = requests.request("GET", url, headers=headers, verify=False)

        self.assertEqual(200, response.status_code)

    def __post_element(self):
        url = self.HOST + '/giftlists/' + self.list_reference + '/elements'
        headers = {
            'x-access-token': self.token
        }
        payload = {
            "name" : "this is an element",
            "url" : "https://www.amazon.es"
        }
        
        response = requests.request("POST", url, headers=headers, json=payload, verify=False)


        self.assertEqual(200, response.status_code)

    def __delete_element(self):
        url = self.HOST + '/giftlists/' + self.list_reference + '/elements/' + self.element_reference
        headers = {
            'x-access-token': self.token
        }
        
        response = requests.request("DELETE", url, headers=headers, verify=False)


        self.assertEqual(200, response.status_code)

    def __delete_list(self):
        url = self.HOST + '/giftlists/' + self.list_reference
        headers = {
            'x-access-token': self.token
        }
        
        response = requests.request("DELETE", url, headers=headers, verify=False)


        self.assertEqual(200, response.status_code)