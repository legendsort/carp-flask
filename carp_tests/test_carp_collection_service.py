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
from carp_tests.test_carp_auth_service import environment
from carp_tests.test_carp_auth_service import header_access_token
from carp_tests.test_carp_study_service import study_id

# Collection Document
collection_study_id: str = study_id
collection_name: str = 'xxx'
document_name: str = 'xxx'
collection_id = '1'
collection_query: str = ''.join(['?query=', 'id==', collection_id])
# Utils
SLASH = '/'

"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_create_collection_document(self):).
"""


class CollectionTestCase(unittest.TestCase):
    """
       COLLECTION ENDPOINTS - UNITTESTS
    """
    def create_collection_document(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/", collection_name, document_name])
        payload = json.dumps({
            "firstName": "Alban",
            "lastName": "Maxhuni",
            "email": "almax@dtu.dk",
            "phoneNumber": "+45 50 11 22 33",
            "cprNumber": "112233-4455"
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def create_nested_collection_document(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/", collection_name,
             document_name])
        payload = json.dumps({
            "firstName": "Alban",
            "lastName": "Maxhuni",
            "email": "almax@dtu.dk",
            "phoneNumber": "+45 50 11 22 33",
            "cprNumber": "112233-4455",
            "nextConsultationDate": "2020-06-11T15:47:11.794680",
            "consultationDates": [
                "2020-06-11T15:47:11.794680",
                "2020-06-11T15:47:11.794680",
                "2020-06-11T15:47:11.794680"
            ],
            "height": 175
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_one_collection(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/", collection_name,
             SLASH, document_name])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def get_collection_with_nested_query(self): # TODO: CHECK WHY IS FAILING
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections", collection_query])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_collection_by_study_id_and_collection_name(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/", collection_name])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_collection_by_collection_name_and_document_name(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/", collection_name, SLASH, document_name])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_collection_by_study_id_and_collection_id(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/id/", collection_id])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def update_collection_name(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/id/", collection_id])
        payload = json.dumps({
            "name": "Updated name"
        })
        response = requests.request("PUT", url, headers=header_access_token, data=payload)
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def delete_collection(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", collection_study_id, "/collections/id/", collection_id])
        response = requests.request("DELETE", url, headers=header_access_token, data=payload)
        print(f'COLLECTION >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
