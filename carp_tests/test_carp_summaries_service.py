"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import unittest
import requests

from carp_main.resources import carp_environment as env
from carp_tests.test_carp_auth_service import environment
from carp_tests.test_carp_auth_service import header_access_token
from carp_tests.test_carp_study_service import study_id

# Summaries
study_id: str = study_id
summary_id: str = 'xxx'

"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_create_summaries(self):).
"""


class SummariesTestCase(unittest.TestCase):
    """
    SUMMARIES SERVICE ENDPOINTS - UNITTESTS
    """
    def create_summaries(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/summaries?studyId=", study_id])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'SUMMARIES >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_summaries(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/summaries/all"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'SUMMARIES >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_download_summaries(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/summaries/", summary_id, "/download"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'SUMMARIES >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_by_id_summaries(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/summaries/", summary_id, "/download"])
        response = requests.request("GET", url, headers=header_access_token, data={})
        print(f'SUMMARIES >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)
