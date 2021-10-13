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
from carp_tests.test_carp_deployment_service import owner_id

# Protocol
owner_id: str = owner_id
is_master_device: str = 'true'

"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_add(self):).
"""


class ProtocolTestCase(unittest.TestCase):
    """
    PROTOCOL ENDPOINTS - UNITTESTS
    """

    def test_add(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.Add",
            "protocol": {
                "ownerId": owner_id,
                "name": "Test protocol",
                "description": "",
                "creationDate": "2021-01-21T09:30:11.910Z",
                "masterDevices": [
                    {
                        "$type": "dk.cachet.carp.protocols.domain.devices.Smartphone",
                        "isMasterDevice": is_master_device,
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
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_add_version(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
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
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_by(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetBy",
            "protocolId": {
                "ownerId": owner_id,
                "name": "Test protocol"
            },
            "versionTag": "2021-01-21T09:37:18.896Z"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_protocol_without_version(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetBy",
            "protocolId": {
                "ownerId": owner_id,
                "name": "Test protocol"
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_for(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetAllFor",
            "ownerId": owner_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_version_history_for(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolServiceRequest.GetVersionHistoryFor",
            "protocolId": {
                "ownerId": owner_id,
                "name": "Test protocol"
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_update_participant_data_configuration(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-service"])
        payload = {
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
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    PROTOCOL FACTORY SERVICE ENDPOINTS - UNITTESTS
    """

    def test_create_custom_protocol(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/protocol-factory-service"])
        payload = {
            "$type": "dk.cachet.carp.protocols.infrastructure.ProtocolFactoryServiceRequest.CreateCustomProtocol",
            "ownerId": owner_id,
            "name": "name",
            "customProtocol": "customProtocol",
            "description": "description"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'PROTOCOL >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
