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
from carp_tests.test_carp_setup import protocol_is_master_device, protocol_name, protocol_version_tag, deployment_owner_id as owner_id


"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_add(self):).
"""


class ProtocolTestCase(unittest.TestCase):
    """
    PROTOCOL ENDPOINTS - UNITTESTS
    """

    def add(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.Add",
            "protocol": {
                "ownerId": owner_id,
                "name": "Test protocol",
                "description": "",
                "creationDate": "2021-01-21T09:30:11.910Z",
                "masterDevices": [
                    {
                        "$type": "dk.cachet.carp.protocols.domain.devices.Smartphone",
                        "isMasterDevice": protocol_is_master_device,
                        "roleName": "phone",
                        "samplingConfiguration": {},
                        "supportedDataTypes": [
                            "dk.cachet.carp.geolocation",
                            "dk.cachet.carp.stepcount"
                        ]
                    }
                ],
                "connectedDevices": [],
                "connections": [],
                "tasks": [
                    {
                        "$type": "dk.cachet.carp.protocols.domain.tasks.ConcurrentTask",
                        "name": "task",
                        "measures": [
                            {
                                "$type": "dk.cachet.carp.protocols.domain.tasks.measures.PhoneSensorMeasure",
                                "type": "dk.cachet.carp.geolocation",
                                "duration": -1000
                            }
                        ]
                    }
                ],
                "triggers": {
                    "0": {
                        "$type": "dk.cachet.carp.protocols.domain.triggers.ElapsedTimeTrigger",
                        "sourceDeviceRoleName": "phone",
                        "elapsedTime": 10000
                    }
                },
                "triggeredTasks": [
                    {
                        "triggerId": 0,
                        "taskName": "task",
                        "targetDeviceRoleName": "phone"
                    }
                ],
                "expectedParticipantData": [
                    {
                        "$type": "dk.cachet.carp.common.users.ParticipantAttribute.DefaultParticipantAttribute",
                        "inputType": "dk.cachet.carp.input.sex"
                    }
                ]
            },
            "versionTag": "1.0"
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: add(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def add_version(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.AddVersion",
            "protocol": {
                "ownerId": owner_id,
                "name": "Test protocol",
                "description": "",
                "creationDate": "2021-01-21T09:37:18.895Z",
                "masterDevices": [],
                "connectedDevices": [],
                "connections": [],
                "tasks": [],
                "triggers": {},
                "triggeredTasks": [],
                "expectedParticipantData": []
            },
            "versionTag": "2021-01-21T09:37:18.896Z"
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: addVersion(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_by(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetBy",
            "protocolId": {
                "ownerId": owner_id,
                "name": protocol_name
            },
            "versionTag": protocol_version_tag
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: get_by(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_protocol_without_version(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetBy",
            "protocolId": {
                "ownerId": owner_id,
                "name": protocol_name
            }
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: get_protocol_without_version(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_for(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetAllFor",
            "ownerId": owner_id
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: get_all_for(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_version_history_for(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetVersionHistoryFor",
            "protocolId": {
                "ownerId": owner_id,
                "name": protocol_name
            }
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: get_version_history_for(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def update_participant_data_configuration(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.UpdateParticipantDataConfiguration",
            "protocolId": {
                "ownerId": owner_id,
                "name": "Test protocol"
            },
            "versionTag": "1.0",
            "expectedParticipantData": [
                {
                    "$type": "dk.cachet.carp.common.users.ParticipantAttribute.DefaultParticipantAttribute",
                    "inputType": "namespace.type"
                }
            ]
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: update_participant_data_configuration(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    PROTOCOL FACTORY SERVICE ENDPOINTS - UNITTESTS
    """

    def create_custom_protocol(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-factory-service"])
        payload = json.dumps({
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolFactoryServiceRequest.CreateCustomProtocol",
            "ownerId": owner_id,
            "name": protocol_name,
            "customProtocol": "customProtocol",
            "description": "description"
        }).encode("utf-8")
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, method: create_custom_protocol(), status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
