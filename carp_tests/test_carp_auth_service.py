"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import json
import unittest

import requests

from carp_main.resources import carp_environment as env

environment: str = 'local'
# Auth
client_id: str = 'carp'
client_secret: str = 'carp'
client_password_grant_type: str = 'password'
client_refresh_token_grant_type: str = 'refresh_token'
client_researcher_username: str = 'xxx@cachet.dk'
client_researcher_password: str = 'xxx'
client_researcher_new_password: str = 'xxx'
access_token: str = 'xxx'
refresh_token: str = 'xxx'
# Account
account_id: str = 'xxx'
invite_researcher: str = 'xxx@dtu.dk'
invite_carp_admin: str = 'xxx@dtu.dk'
invite_carp_participant: str = 'xxx@dtu.dk'
# Headers
header_auth = {'Authorization': 'Basic Y2FycDpjYXJw', 'Accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}
header_access_token = {'Authorization': 'Bearer ' + access_token}
header_access_token_nocache = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'Authorization': 'Bearer ' + access_token}


"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_login(self):).
"""


class AuthTestCase(unittest.TestCase):
    """
    AUTH ENDPOINTS - UNITTESTS
    """
    def login(self):
        url = ''.join([env.BASE_URL[environment], "/client/oauth/token"])
        payload = 'client_id=' + client_id + \
                  '&client_secret=' + client_secret + \
                  '&grant_type=' + client_password_grant_type + \
                  '&username=' + client_researcher_username + \
                  '&password=' + client_researcher_password
        response = requests.request("POST", url, headers=header_auth, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def refresh_token(self):
        url = ''.join([env.BASE_URL[environment], "/client/oauth/refresh/token"])
        payload = 'client_id=' + client_id + \
                  '&client_secret=' + client_secret + \
                  '&grant_type=' + client_refresh_token_grant_type + \
                  '&refresh_token=' + refresh_token
        response = requests.request("POST", url, headers=header_auth, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_current_user(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/users/current"])
        payload = {}
        response = requests.request("GET", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def get_studies_for_researcher(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/accounts/", account_id, "/study-manager"])
        payload = {}
        response = requests.request("GET", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def register_user(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/users/register"])
        payload = json.dumps({
            "emailAddress": invite_researcher
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def send_forgotten_password(self):
        url = ''.join([env.BASE_URL[env], "/client/api/users/forgotten-password/send"])
        print(url)
        payload = json.dumps({
            "emailAddress": invite_researcher
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def change_password(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/users/password"])
        payload = json.dumps({
            "oldPassword": client_researcher_password,
            "newPassword": client_researcher_new_password
        })
        response = requests.request("PUT", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def unlock_account(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/accounts/unlock"])
        payload = json.dumps({
            "emailAddress": invite_researcher
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'AUTH >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
