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
from carp_tests.test_carp_setup import document_id, document_study_id, document_query, document_name, document_sort_created_at


"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_create_document(self):).
"""


class DocumentsTestCase(unittest.TestCase):
    """
    DOCUMENTS ENDPOINTS - UNITTESTS
    """
    def create_document(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents"])
        payload = json.dumps({
            "name": "test",
            "collection_id": 1,
            "collections": [],
            "data": {
                "event": {
                    "id": 562,
                    "date": "6/20/2019",
                    "time": "15:31",
                    "notes": "",
                    "source": "Self input",
                    "deleted": 0,
                    "activity": "Walking",
                    "duration": "33.0",
                    "symptoms": [
                        "adsafd",
                        "adsafd"
                    ],
                    "completed": 1
                }
            }
        })
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DOCUMENTS >> URL: {url}, method: create_document(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_one_document(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents/", document_id])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'DOCUMENTS >> URL: {url}, method: get_one_document(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_documents(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'DOCUMENTS >> URL: {url}, method: get_all_documents(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_documents_sorted(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents",
                       document_sort_created_at])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'DOCUMENTS >> URL: {url}, method: get_all_documents_sorted(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_documents_query(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents", document_query])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'DOCUMENTS >> URL: {url}, method: get_all_documents_query(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def update_overwrite_document(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents/", document_id])
        payload = json.dumps({
            "name": document_name,
            "data": {
                "event": {
                    "id": 5000,
                    "date": "6/20/2019",
                    "time": "17:31",
                    "notes": "",
                    "source": "New input",
                    "deleted": 0,
                    "activity": "Walking",
                    "duration": "33.0",
                    "symptoms": [
                        "sdfasdf",
                        "adsafd"
                    ],
                    "completed": 1
                }
            }
        })
        response = requests.request("PUT", url, headers=header_access_token, data=payload)
        print(f'DOCUMENTS >> URL: {url}, method: update_overwrite_document(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def update_append_document(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents/", document_id, "/append"])
        payload = json.dumps({
            "name": document_name,
            "data": {
                "event": {
                    "id": 5000,
                    "date": "6/20/2019",
                    "time": "17:31",
                    "notes": "",
                    "source": "New input",
                    "deleted": 0,
                    "activity": "Walking",
                    "duration": "33.0",
                    "symptoms": [
                        "sdfasdf",
                        "adsafd"
                    ],
                    "completed": 1
                }
            }
        })
        response = requests.request("PUT", url, headers=header_access_token, data=payload)
        print(f'DOCUMENTS >> Method: {requests.put}, URL: {url}, method: update_append_document(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def delete_document(self):
        url = ''.join(
            [env.BASE_URL[environment], "/client/api/studies/", document_study_id, "/documents/", document_id])
        response = requests.request("DELETE", url, headers=header_access_token, data={})
        print(f'DOCUMENTS >> URL: {url}, method: delete_document(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
