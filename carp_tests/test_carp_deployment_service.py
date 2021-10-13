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

# Deployment
deployment_id: str = 'xxx'
owner_id: str = 'xxx'
is_master_device: str = 'true'
participant_email = 'addParticipationTest@cachet.dk'
account_id = 'xxx'

"""
NOTE: To enable testing, add the prefix "test_" before the method (e.g. def test_create_study_deployment(self):).
"""


class DeploymentTestCase(unittest.TestCase):
    """
    DEPLOYMENTS SERVICE ENDPOINTS - UNITTESTS
    """
    def test_create_study_deployment(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.CreateStudyDeployment",
            "protocol": {
                "ownerId": owner_id,
                "name": "Test protocol",
                "description": "",
                "creationDate": "2021-01-21T13:38:53.010Z",
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
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_deployment_successful(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.DeploymentSuccessful",
            "studyDeploymentId": deployment_id,
            "masterDeviceRoleName": "phone",
            "deviceDeploymentLastUpdateDate": "2021-01-21T13:56:29.135Z"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_study_deployment(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.GetStudyDeploymentStatus",
            "studyDeploymentId": deployment_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_register_device(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.RegisterDevice",
            "studyDeploymentId": deployment_id,
            "deviceRoleName": "phone",
            "registration": {
                "$type": "dk.cachet.carp.protocols.domain.devices.DefaultDeviceRegistration",
                "registrationCreationDate": "2021-01-21T13:50:39.391Z",
                "deviceId": "114faa76-f00d-4665-b71b-d9b9508786d3"
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_device_deployment_for(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.GetDeviceDeploymentFor",
            "studyDeploymentId": deployment_id,
            "masterDeviceRoleName": "phone"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_unregister_device(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.UnregisterDevice",
            "studyDeploymentId": deployment_id,
            "deviceRoleName": "phone"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_stop(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.Stop",
            "studyDeploymentId": deployment_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_study_deployment_status_list(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.DeploymentServiceRequest.GetStudyDeploymentStatusList",
            "studyDeploymentIds": [
                deployment_id
            ]
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    PARTICIPATION SERVICE ENDPOINTS - UNITTESTS
    """
    def test_add_participation(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participation-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.ParticipationServiceRequest.AddParticipation",
            "studyDeploymentId": deployment_id,
            "deviceRoleNames": [
                "phone"
            ],
            "identity": {
                "$type": "dk.cachet.carp.common.users.EmailAccountIdentity",
                "emailAddress": participant_email
            },
            "invitation": {
                "name": "MockInvitation",
                "description": "Description",
                "applicationData": ""
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_active_participation_invitations(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participation-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.ParticipationServiceRequest.GetActiveParticipationInvitations",
            "accountId": account_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_set_participant_data(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participation-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.ParticipationServiceRequest.SetParticipantData",
            "studyDeploymentId": deployment_id,
            "inputDataType": "dk.cachet.carp.input.sex",
            "data": {
                "$type": "dk.cachet.carp.input.sex",
                "value": "Male"
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_participant_data(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participation-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.ParticipationServiceRequest.GetParticipantData",
            "studyDeploymentId": deployment_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_participant_data_list(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participation-service"])
        payload = {
            "$type": "dk.cachet.carp.deployment.infrastructure.ParticipationServiceRequest.GetParticipantDataList",
            "studyDeploymentIds": [
                deployment_id
            ]
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    DEPLOYMENT STATISTICS SERVICE ENDPOINTS - UNITTESTS
    """
    def test_get_participant_data_list(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/deployment-service/statistics"])
        payload = {
            "deploymentIds": [
                deployment_id,
                deployment_id
            ]
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'DEPLOYMENT >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
