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
from carp_tests.test_carp_auth_service import header_access_token_nocache
from carp_tests.test_carp_deployment_service import deployment_id
from carp_tests.test_carp_study_service import study_id

# Data Point
datapoint_deployment_id: str = deployment_id
datapoint_id = '1'
datapoint_query: str = ''.join(['carp_header.study_id==', study_id, ';'])

"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_create_data_point(self):).
"""


class DatapointTestCase(unittest.TestCase):
    """
       DATA ENDPOINTS - UNITTESTS
    """
    def create_data_point(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points"])
        payload = json.dumps({
            "carp_header": {
                "study_id": "8",
                "user_id": "user@dtu.dk",
                "device_role_name": "Patient's phone",
                "trigger_id": "task1",
                "data_format": {
                    "namepace": "carp",
                    "name": "location"
                },
                "start_time": "2018-11-08T15:30:40.721748Z"
            },
            "carp_body": {
                "classname": "LocationDatum",
                "id": "3fdd1760-bd30-11e8-e209-ef7ee8358d2f",
                "timestamp": "2018-11-08T15:30:40.721748Z",
                "device_info": {},
                "latitude": 23454.345,
                "longitude": 23.4,
                "altitude": 43.3,
                "accuracy": 12.4,
                "speed": 2.3,
                "speed_accuracy": 12.3
            }
        })
        response = requests.request("POST", url, headers=header_access_token_nocache, data=payload)
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def create_many_data_points_as_batch(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points/batch"])
        payload = {}
        files = [('file', ('file', open('/path/to/file', 'rb'), 'application/octet-stream'))]
        response = requests.request("POST", url, headers=header_access_token, data=payload, files=files)
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_one_data_point(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points/", datapoint_id])
        response = requests.request("GET", url, headers=header_access_token_nocache, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_data_points(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points"])
        response = requests.request("GET", url, headers=header_access_token_nocache, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_data_points_pageable(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points?page=0"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_data_points_sorted(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points?sort=created_at,asc"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_data_point_nested_query(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points?query=", datapoint_query])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_count_data_points(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points/count"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def delete_data_point(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployments/", datapoint_deployment_id, "/data-points/", datapoint_id])
        response = requests.request("DELETE", url, headers=header_access_token, data={})
        print(f'Datapoint URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
