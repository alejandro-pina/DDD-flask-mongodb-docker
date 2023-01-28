import unittest
from flask import current_app, url_for
from app import create_app
import json
from base64 import b64encode

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def req_post_headers(self):
        return {
            'Content-Type': 'application/json'
        }

    def passed_test(self, name, list_check):
        print('###START_TEST###')
        print('\033[90m ***********************************************************************')
        print('\033[32m ✅ {0} '.format(name))
        print('\033[90m ***********************************************************************')
        for item in list_check:
            print('\033[32m  ✔️  {0} '.format(item))
        print('\033[90m ***********************************************************************')
        print('\033[0m')
        print('###ERROR_TEST###')

    def test_endopoint(self):
        list_check = []
        list_ep_get = []
        list_ep_post = []

        for rule in self.app.url_map.iter_rules():
            endpoint = str(rule)
            if '/static/' not in endpoint:
                if 'GET' in rule.methods:
                    list_ep_get.append(endpoint)
                if 'POST' in rule.methods and not 'GET' in rule.methods:
                    list_ep_post.append(endpoint)
        
        for ep in list_ep_get:
            response = self.client.get(ep)
            status_required = [200,401]
            status_code = response.status_code 
            self.assertTrue(status_code in status_required)
            list_check.append('GET ' + str(response.status_code) + ' - ' + ep)

        self.passed_test('test_endopoint', list_check)