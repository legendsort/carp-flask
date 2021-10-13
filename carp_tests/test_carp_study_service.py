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
from carp_tests.test_carp_auth_service import account_id
from carp_tests.test_carp_deployment_service import owner_id

# Study
account_id: str = account_id
study_id: str = 'xxx'
owner_id: str = owner_id
is_master_device: str = 'true'
participant_email: str = 'xxx@cachet.dk'
participant_id: str = 'xxx'
group_id: str = 'xxx'


class StudyTestCase(unittest.TestCase):
    """
    ADD RESEARCHER ENDPOINTS - UNITTESTS
    """
    def test_add_researcher(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", study_id, "/researchers"])
        payload = {"researcherAccountId": account_id}
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    STUDY SERVICE ENDPOINTS - UNITTESTS
    """
    def test_get_study_details(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {"$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.GetStudyDetails",
                   "studyId": study_id}
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_study_overview(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {"$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.GetStudiesOverview",
                   "owner": {"id": owner_id}}
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_set_study_protocol(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {{
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.SetProtocol",
            "studyId": study_id,
            "protocol": {
                "ownerId": owner_id,
                "name": "Study.setProtocolTest",
                "description": "",
                "creationDate": "2021-01-14T09:28:51.853Z",
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
        }}
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_go_live(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.GoLive",
            "studyId": study_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_set_internal_description(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.SetInternalDescription",
            "studyId": study_id,
            "name": "name",
            "description": "New description"
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_create_study(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.CreateStudy",
            "owner": {
                "id": owner_id
            },
            "name": "name",
            "description": "Description",
            "invitation": {
                "name": "",
                "description": "",
                "applicationData": ""
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_set_invitation(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.SetInvitation",
            "studyId": study_id,
            "invitation": {
                "name": "New Invitation",
                "description": "New Description",
                "applicationData": ""
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_study_status(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/study-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.StudyServiceRequest.GetStudyStatus",
            "studyId": study_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    PARTICIPANT SERVICE ENDPOINTS - UNITTESTS
    """
    def test_add_participant(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.AddParticipant",
            "studyId": study_id,
            "email": participant_email
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_participant(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.GetParticipant",
            "studyId": study_id,
            "participantId": participant_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_participants(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.GetParticipants",
            "studyId": study_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_deploy_participant_group(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.DeployParticipantGroup",
            "studyId": study_id,
            "group": [
                {
                    "participantId": participant_id,
                    "deviceRoleNames": [
                        "phone"
                    ]
                }
            ]
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_get_participant_group_status_list(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.GetParticipantGroupStatusList",
            "studyId": study_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_stop_participant_group(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.StopParticipantGroup",
            "studyId": study_id,
            "groupId": group_id
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    def test_set_particapnt_group_data(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/participant-service"])
        payload = {
            "$type": "dk.cachet.carp.studies.infrastructure.ParticipantServiceRequest.SetParticipantGroupData",
            "studyId": study_id,
            "groupId": group_id,
            "inputDataType": "dk.cachet.carp.input.sex",
            "data": {
                "$type": "dk.cachet.carp.input.sex",
                "value": "Male"
            }
        }
        response = requests.request("POST", url, headers=header_access_token, data=payload)
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)

    """
    GET PARTICIPANTS ENDPOINTS - UNITTESTS
    """
    def test_get_participant_info(self):
        url = ''.join([env.BASE_URL[environment], "/client/api/studies/", study_id, "/participants"])
        response = requests.request("POST", url, headers=header_access_token, data={})
        print(f'STUDY >> URL: {url}, status code: {response.status_code}, and the response body: {response.text}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
