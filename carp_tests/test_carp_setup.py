""""
Auth
"""
auth_client_id: str = 'carp'
auth_client_secret: str = 'carp'
auth_client_password_grant_type: str = 'password'
auth_client_refresh_token_grant_type: str = 'refresh_token'
auth_client_researcher_username: str = 'ossi0004@gmail.com'
auth_client_researcher_password: str = 'xxxx'
auth_client_researcher_new_password: str = 'xxxx'
auth_access_token: str = 'c877be77-8060-430f-b566-xxxx'
auth_refresh_token: str = 'b83dbfaa-8250-4d87-91d0-xxxx'

""""
Account
"""
account_id: str = '5221c3be-0534-4988-a77d-fa64d4404c39'
account_invite_researcher: str = 'xxx@dtu.dk'
account_invite_carp_admin: str = 'xxx@dtu.dk'
account_invite_carp_participant: str = 'xxx@dtu.dk'
# Headers
account_header_auth = {'Authorization': 'Basic Y2FycDpjYXJw', 'Accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}
account_header_access_token = {'Authorization': 'Bearer ' + auth_access_token, 'Content-Type': 'application/json'}
account_header_access_token_nocache = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'Authorization': 'Bearer ' + auth_access_token}

""""
Protocol
"""
protocol_is_master_device: str = 'true'
protocol_name: str = 'something'
protocol_version_tag: str = '1970-01-19T21:14:54.862Z'

""""
Study
"""
invited_researcher_email: str = 'almax@dtu.dk'
study_id: str = "b41cd7a7-3d31-4c17-b293-f145518497cd"
participant_email: str = 'alban.q.maxhuni@gmail.com'
participant_id: str = '67be384d-adea-4d89-b11c-4eaee06c37a2'
group_id: str = 'xxx'

""""
FILE
"""
file_study_id: str = study_id
file_id = '1'
file_query: str = ''.join(['?query=created_by_user_id==', file_id])

""""
DOCUMENTS
"""
document_study_id: str = study_id
document_id = '1'
document_sort_created_at: str = '?sort=created_at,asc'
document_name: str = 'test'
document_query: str = ''.join(['?query=name==', document_name])

""""
DEPLOYMENT
"""
deployment_id: str = '5b1c3929-2670-4cbf-b685-9e4070c91fb3'
deployment_owner_id: str = '5221c3be-0534-4988-a77d-fa64d4404c39'
deployment_is_master_device: str = 'true'
deployment_participant_email: str = 'alban.q.maxhuni@gmail.com'

""""
DATA POINT
"""
datapoint_id = '22036'
datapoint_query: str = ''.join(['carp_header.study_id==', study_id, ';'])

""""
DATA POINT
"""
consent_id: str = '38'


""""
COLLECTION DOCUMENT
"""
collection_study_id: str = study_id
collection_name: str = 'xxx'
collection_document_name: str = 'xxx'
collection_id = '1'
collection_query: str = ''.join(['?query=', 'id==', collection_id])
