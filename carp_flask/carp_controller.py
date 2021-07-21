"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from flask import request, Response, render_template

import json

from carp import account_service as account
from carp import collection_service as collection
from carp import consent_service as consent
from carp import datapoint_service as data_point
from carp import deployment_service as deployment
from carp import document_service as document
from carp import file_service as file
from carp import protocol_service as protocol
from carp import study_service as study
from carp import monitor_service as monitor

from carp_flask import app


"""""""""""""""
    CARP ENVIRONMENTS
"""""""""""""""
# BASE URL
BASE_URL = {
    # Local
    "local": "http://localhost:8080",
    # Server
    "test": "https://cans.cachet.dk:443/test",
    "development": "https://cans.cachet.dk:443/dev",
    "staging": "https://cans.cachet.dk:443/stage",
    "production": "https://cans.cachet.dk:443"
}

"""""""""""""""
    MAIN
"""""""""""""""


@app.route("/")
def home():
    return render_template('home.html')


"""""""""""""""
    AUTH / ACCOUNT
"""""""""""""""


@app.route('/client/oauth/token', methods=['POST'])
def login():
    """
    Endpoint: [login]
    :return: The login tokens.
    """
    print(request.form.get('username'))
    auth_response = account.login(BASE_URL["production"], request)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/oauth/refresh/token', methods=['POST'])
def refresh_token():
    """
    Endpoint: [login_refresh_token]
    :return: The refresh token.
    """
    auth_response = account.refresh_token(BASE_URL["production"], request)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/users/current', methods=['GET'])
def get_current_user():
    """
    Endpoint: [get_current_user]
    :return: The current user account information.
    """
    auth_response = account.current_user(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/users/register', methods=['POST'])
def register_user():
    """
    Endpoint: [register_user]
    :return: The registered user.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.register_user(BASE_URL["production"], request.headers['Authorization'], request_body)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/accounts/<role>', methods=['POST'])
def invite_account(role=None):
    """
    Endpoint: [invite_account]
    :param role: The [role] to assign the account.
        i.e. roles: PARTICIPANT, STUDY_OWNER
    :return: This request doesn't return a response body.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.invite_user(BASE_URL["production"], request.headers['Authorization'], request_body, role)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/users/forgotten-password/send', methods=['POST'])
def send_forgotten_password_email():
    """
    Endpoint: [password_recovery]
    :return: This request doesn't return a response request_body.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.send_forgotten_password(BASE_URL["production"], request.headers['Authorization'],
                                                    password_body=request_body)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/users/forgotten-password/save', methods=['POST'])
def send_new_password_for_token():
    """
    Endpoint: [send_forgotten_password]
    :return: This request doesn't return a response request_body.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.send_new_password_for_token(BASE_URL["production"], request.headers['Authorization'],
                                                        password_body=request_body)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/accounts/unlock', methods=['POST'])
def unlock_account():
    """
    Endpoint: [unlock_account]
    :return: This request doesn't return a response request_body.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.unlock_account(BASE_URL["production"], request.headers['Authorization'],
                                           email_body=request_body)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/users/password', methods=['PUT'])
def change_password():
    """
    Endpoint: [change_password]
    :return: This request doesn't return a response request_body.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    auth_response = account.change_password(BASE_URL["production"], request.headers['Authorization'],
                                            password_body=request_body)
    return Response(json.dumps(auth_response), mimetype='application/json')


@app.route('/client/api/accounts/<account_id>/study-manager', methods=['GET'])
def get_studies_for_researcher_accounts(account_id):
    """
    Endpoint: [get_studies_for_researcher_accounts]
    @param: The existing [account_id] of the researcher.
    :return: This request doesn't return a response request_body.
    """
    auth_response = account.get_studies_for_researcher(BASE_URL["production"], request.headers['Authorization'],
                                                       account_id)
    return Response(json.dumps(auth_response), mimetype='application/json')


"""""""""""""""
    DATA POINT
"""""""""""""""


@app.route('/client/api/deployments/<deployment_id>/data-points', methods=['POST'])
def create_data_point(deployment_id):
    """
    Endpoint: [create_data_point]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The new create data point by its [deployment_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    datapoint_response = data_point.create_data_point(BASE_URL["production"], request.headers['Authorization'],
                                                      deployment_id, data_points_body=request_body)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points/<data_point_id>', methods=['GET'])
def get_one_data_point(deployment_id, data_point_id):
    """
    Endpoint: [get_one_data_point]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param data_point_id: The [data_point_id] assigned in the data point.
    :return: The data point by its [data_point_id] and [data_point_id].
    """
    datapoint_response = data_point.get_data_point(BASE_URL["production"], request.headers['Authorization'],
                                                   deployment_id, data_point_id)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points', methods=['GET'])
def get_all_data_points(deployment_id):
    """
    Endpoint: [get_all_data_points]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The data points by their [deployment_id].
    """
    datapoint_response = data_point.get_all_data_points(BASE_URL["production"], request.headers['Authorization'],
                                                        deployment_id)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points?page=<page_number>', methods=['GET'])
def get_all_data_points_pageable(deployment_id, page_number):
    """
    Endpoint: [get_all_data_points_pageable]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param page_number: The [page_number] of the data point.
    :return: The data points by their [deployment_id] and [page_number].
    """
    datapoint_response = data_point.get_all_data_points_pageable(BASE_URL["production"],
                                                                 request.headers['Authorization'], deployment_id,
                                                                 page_number)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points?sort=<sort>', methods=['GET'])
def get_all_data_points_sorted(deployment_id, sort):
    """
    Endpoint: [get_all_data_points_sorted]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param sort: The [sort] parameter to order the data points (asc, desc).
    :return: The data points sorted by their [deployment_id] and the [sort] parameter.
    """
    datapoint_response = data_point.get_all_data_points_sorted(BASE_URL["production"], request.headers['Authorization'],
                                                               deployment_id, sort)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points?query=<query>', methods=['GET'])
def get_all_data_points_with_query(deployment_id, query):
    """
    Endpoint: [get_all_data_points_with_query]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param query: The [query] parameters to retrieve the data point.
    :return: The data points by their [deployment_id] and the [query] parameter.
    """
    datapoint_response = data_point.get_all_nested_query(BASE_URL["production"], request.headers['Authorization'],
                                                         deployment_id, query)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points/batch', methods=['POST'])
def create_many_data_points(deployment_id):
    """
    Endpoint: [create_many_data_points]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The new created data points.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    datapoint_response = data_point.create_many_data_points(BASE_URL["production"], request.headers['Authorization'],
                                                            deployment_id, data_points_body=request_body)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points/<data_point_id>', methods=['DELETE'])
def delete_data_point(deployment_id, data_point_id):
    """
    Endpoint: [delete_data_point]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param data_point_id: The [data_point_id] assigned in the data point.
    :return: The [data_point_id] of the delete data point.
    """
    deleted_data_point_response = data_point.delete_data_point(BASE_URL["production"], request.headers['Authorization'],
                                                               deployment_id, data_point_id)
    return Response(json.dumps(deleted_data_point_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/data-points/count?query=', methods=['GET'])
def get_count_of_data_points(deployment_id, query):
    """
    Endpoint: [get_all_data_points_with_query]
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param query: The [query] parameters to retrieve the data point.
    :return: The data points by their [deployment_id] and the [query] parameter.
    """
    datapoint_response = data_point.get_count_data_points(BASE_URL["production"], request.headers['Authorization'],
                                                          deployment_id, query)
    return Response(json.dumps(datapoint_response), mimetype='application/json')


"""""""""""""""
    COLLECTIONS
"""""""""""""""


@app.route('/client/api/studies/<study_id>/collections/<collection_name>/<document_name>', methods=['POST'])
def create_collection(study_id, collection_name, document_name):
    """
    Endpoint: [create_collection]
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] of the collection.
    :param document_name: The [document_name] of the collection.
    :return: The new created collection.
    """
    collection_body = json.loads(json.dumps(request.get_json()))
    collection_response = collection.create_collections(BASE_URL["production"], request.headers['Authorization'],
                                                        study_id, collection_name, document_name,
                                                        collections_body=collection_body)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections/<collection_name>/<document_name>', methods=['GET'])
def get_collection_by_collection_name_and_document_name(study_id, collection_name, document_name):
    """
    Endpoint: [get_collection_by_collection_name_and_document_name]
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] of the collection.
    :param document_name: The [document_name] of the collection.
    :return: The collection by its [study_id], [collection_name], [document_name].
    """
    collection_response = collection.get_collection_by_collection_name_and_document_name(BASE_URL["production"],
                                                                                         request.headers[
                                                                                             'Authorization'], study_id,
                                                                                         collection_name, document_name)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections/name/<collection_name>', methods=['GET'])
def get_collection_by_study_id_and_collection_name(study_id, collection_name):
    """
    Endpoint: [get_collection_by_collection_name]
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] of the collection.
    :return: The collection by its [study_id] and [collection_name].
    """
    collection_response = collection.get_collection_by_study_id_and_collection_name(BASE_URL["production"],
                                                                                    request.headers['Authorization'],
                                                                                    study_id,
                                                                                    collection_name)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections?query=<query>', methods=['GET'])
def get_collection_nested_query(study_id, query):
    """
    Endpoint: [get_collection_nested_query]
    :param study_id: The [study_id] of the study deployment.
    :param query: The [query] parameters to retrieve the collection.
    :return: The collection by its [study_id] and the [query] parameters.
    """
    collection_response = collection.get_collection_with_nested_query(BASE_URL["production"],
                                                                      request.headers['Authorization'],
                                                                      study_id, query)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections/id/<collection_id>', methods=['GET'])
def get_collection_by_study_id_and_collection_id(study_id, collection_id):
    """
    Endpoint: [get_collection_by_collection_id]
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: The collection by its [study_id] and [collection_id].
    """
    collection_response = collection.get_collection_by_study_id_and_collection_id(BASE_URL["production"],
                                                                                  request.headers['Authorization'],
                                                                                  study_id, collection_id)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections/id/<collection_id>', methods=['PUT'])
def update_collection_name_by_study_id_and_collection_id(study_id, collection_id):
    """
    Endpoint: [update_collection_name]
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: The updated collection by its [study_id] and [collection_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    collection_response = collection.update_collection_name(BASE_URL["production"], request.headers['Authorization'],
                                                            study_id, collection_id=collection_id,
                                                            collection_body=request_body)
    return Response(json.dumps(collection_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/collections/<collection_id>', methods=['DELETE'])
def delete_collection(study_id, collection_id):
    """
    Endpoint: [delete_collection]
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: This request doesn't return a response request_body.
    """
    collection_response = collection.delete_collection(BASE_URL["production"], request.headers['Authorization'],
                                                       study_id, collection_id)
    return Response(json.dumps(collection_response), mimetype='application/json')


"""""""""""""""
    DOCUMENTS
"""""""""""""""


@app.route('/client/api/studies/<study_id>/documents', methods=['POST'])
def create_document(study_id):
    """
    Endpoint: [create_document]
    :param study_id: The [study_id] of the study deployment.
    :return: The new created document.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    document_response = document.create_documents(BASE_URL["production"], request.headers['Authorization'], study_id,
                                                  document_body=request_body)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents/<document_id>', methods=['GET'])
def get_document(study_id, document_id):
    """
    Endpoint: [get_document`
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The document by its [study_id] and [document_id].
    """
    document_response = document.get_document(BASE_URL["production"], request.headers['Authorization'], study_id,
                                              document_id)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents', methods=['GET'])
def get_all_documents(study_id):
    """
    Endpoint: [get_all_documents]
    :param study_id: The [study_id] of the study deployment.
    :return: The documents requested by their [study_id].
    """
    document_response = document.get_all_documents(BASE_URL["production"], request.headers['Authorization'], study_id)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents?sort=created_at,<sort>', methods=['GET'])
def get_all_documents_sorted(study_id, sort):
    """
    Endpoint: [get_all_documents_sorted]
    :param study_id: The [study_id] of the study deployment.
    :param sort: The [sort] parameter to sort the document (asc, desc).
    :return: The documents by their [study_id] and [sort].
    """
    document_response = document.get_all_documents_sorted(BASE_URL["production"], request.headers['Authorization'],
                                                          study_id, sort)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents?query=<query>', methods=['GET'])
def get_all_documents_by_query(study_id, query):
    """
    Endpoint: [get_all_documents_by_query]
    :param study_id: The [study_id] of the study deployment.
    :param query: The [query] parameters to retrieve the document.
    :return: The documents by their [study_id] and the [query] parameters.
    """
    document_response = document.get_all_documents_query(BASE_URL["production"], request.headers['Authorization'],
                                                         study_id, query)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents/<document_id>', methods=['PUT'])
def update_documents(study_id, document_id):
    """
    Endpoint: [update_documents]
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The updated documents by its [study_id] and [document_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    document_response = document.update_documents(BASE_URL["production"], request.headers['Authorization'], study_id,
                                                  document_id, document_body=request_body)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents/<document_id>/append', methods=['PUT'])
def append_documents(study_id, document_id):
    """
    Endpoint: [append_documents]
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The updated documents with the list of documents by its [study_id] and [document_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    document_response = document.append_documents(BASE_URL["production"], request.headers['Authorization'], study_id,
                                                  document_id, document_body=request_body)
    return Response(json.dumps(document_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/documents/<document_id>', methods=['DELETE'])
def delete_documents(study_id, document_id):
    """
    Endpoint: [delete_documents]
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The [document_id] of the delete document.
    """
    document_response = document.delete_document(BASE_URL["production"], request.headers['Authorization'], study_id,
                                                 document_id)
    return Response(json.dumps(document_response), mimetype='application/json')


"""""""""""""""
    FILE
"""""""""""""""


@app.route('/client/api/studies/<study_id>/files', methods=['POST'])
def upload_file(study_id):
    """
    Endpoint: [upload_file]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: The uploaded file with a given [file_id].
    """
    file_to_upload = json.loads(json.dumps(request.form['file']))
    meta_data = json.loads(json.dumps(BASE_URL["production"], request.form['metadata']))
    file_response = file.upload_file(BASE_URL["production"], request.headers['Authorization'],
                                     file_to_upload=file_to_upload, study_id=study_id, meta_data=meta_data)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files/<file_id>/download')
def download_file(study_id, file_id):
    """
    Endpoint: [download_file]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: The downloaded file.
    """
    file_response = file.download_file(BASE_URL["production"], request.headers['Authorization'], study_id, file_id)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files/<file_id>', methods=['GET'])
def get_file(study_id, file_id):
    """
    Endpoint: [get_file]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: The existing file.
    """
    file_response = file.get_file(BASE_URL["production"], request.headers['Authorization'], study_id, file_id)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files')
def get_all_files(study_id):
    """
    Endpoint: [get_all]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: The files associated with the given [study_id].
    """
    file_response = file.get_all(BASE_URL["production"], request.headers['Authorization'], study_id)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files?query=metadata.<meta_data_query>')
def get_files_by_query(study_id, meta_data_query):
    """
    Endpoint: [get_files_by_query]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param meta_data_query: The [meta_data_query] parameters to retrieve a file.
    :return: The file by their [study_id] and the [meta_data_query] parameter(s).
    """
    file_response = file.get_files(BASE_URL["production"], request.headers['Authorization'], study_id,
                                   query=meta_data_query)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files?query=<query>')
def get_files_by_nested_query(study_id, query):
    """
    Endpoint: [get_files_by_nested_query]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param query: The nested [query] parameters to retrieve a file.
    :return: The files by their [study_id] and the [query] parameter(s).
    """
    file_response = file.get_files(BASE_URL["production"], request.headers['Authorization'], study_id, query)
    return Response(json.dumps(file_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/files/<file_id>')
def delete_file(study_id, file_id):
    """
    Endpoint: [delete_file]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: The [file_id] of the deleted file.
    """
    file_response = file.delete_file(BASE_URL["production"], request.headers['Authorization'], study_id, file_id)
    return Response(json.dumps(file_response), mimetype='application/json')


"""""""""""""""
    PROTOCOLS
"""""""""""""""


@app.route('/client/api/protocol-service', methods=['POST'])
def protocol_service():
    """
    Endpoint: [protocol_service]
    :return: The protocol related response.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    protocol_response = protocol.protocol_service(BASE_URL["production"], request.headers['Authorization'],
                                                  protocol_body=request_body)
    return Response(json.dumps(protocol_response), mimetype='application/json')


@app.route('/client/api/protocol-factory-service', methods=['POST'])
def protocol_factory_service():
    """
    Endpoint: [protocol_factory_service]
    :return: The protocol related response.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    protocol_response = protocol.protocol_factory_service(BASE_URL["production"], request.headers['Authorization'],
                                                          protocol_body=request_body)
    return Response(json.dumps(protocol_response), mimetype='application/json')


"""""""""""""""
    DEPLOYMENTS
"""""""""""""""


@app.route('/client/api/deployment-service', methods=['POST'])
def deployment_service():
    """
    Endpoint: [deployment_service]
    :return: The deployment-related response
    """
    request_body = json.loads(json.dumps(request.get_json()))
    deployment_response = deployment.deployment_service(BASE_URL["production"], request.headers['Authorization'],
                                                        deployment_body=request_body)
    return Response(json.dumps(deployment_response), mimetype='application/json')


@app.route('/client/api/participation-service', methods=['POST'])
def deployment_participation():
    """
    Endpoint: [deployment_participation]
    :return: The deployment-related response
    """
    request_body = json.loads(json.dumps(request.get_json()))
    deployment_response = deployment.deployment_participation(BASE_URL["production"], request.headers['Authorization'],
                                                              deployment_body=request_body)
    return Response(json.dumps(deployment_response), mimetype='application/json')


@app.route('/client/api/statistics', methods=['POST'])
def deployment_statistics():
    """
    Endpoint: [deployment_statistics]
    :return: The deployment statistics response
    """
    request_body = json.loads(json.dumps(request.get_json()))
    deployment_response = deployment.deployment_statistics(BASE_URL["production"], request.headers['Authorization'],
                                                           deployment_body=request_body)
    return Response(json.dumps(deployment_response), mimetype='application/json')


"""""""""""""""
    STUDY
"""""""""""""""


@app.route('/client/api/studies/<study_id>/researchers', methods=['POST'])
def add_researcher(study_id):
    """
    Endpoint: [add_researcher]
    :param study_id: The [study_id] of the study.
    :return: The new added participant into study deployment by its [study_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    study_response = study.add_researcher(BASE_URL["production"], request.headers['Authorization'], study_id,
                                          researcher_body=request_body)
    return Response(json.dumps(study_response), mimetype='application/json')


@app.route('/client/api/study-service', methods=['POST'])
def study_service():
    """
    Endpoint: [study_service]
    :return: The study service response according to its request.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    study_response = study.study_service(BASE_URL["production"], request.headers['Authorization'],
                                         study_body=request_body)
    return Response(json.dumps(study_response), mimetype='application/json')


@app.route('/client/api/participant-service', methods=['POST'])
def participant_service():
    """
    Endpoint: [participant_service]
    :return: The participant service response according to its request.
    """
    request_body = json.loads(json.dumps(request.get_json()))
    study_response = study.participant_service(BASE_URL["production"], request.headers['Authorization'],
                                               participant_body=request_body)
    return Response(json.dumps(study_response), mimetype='application/json')


@app.route('/client/api/studies/<study_id>/participants')
def get_participant_info(study_id):
    """
    Endpoint: [get_participant_info]
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: The files by their [study_id] and the [query] parameter(s).
    """
    file_response = study.get_participants_info(BASE_URL["production"], request.headers['Authorization'], study_id)
    return Response(json.dumps(file_response), mimetype='application/json')


"""""""""""""""
    CONSENTS
"""""""""""""""


@app.route('/client/api/deployments/<deployment_id>/consent-documents', methods=['POST'])
def create_consent(deployment_id):
    """
    Endpoint: [create_consent]
    :param deployment_id: The [deployment_id] of the consent document.
    :return: The newly created consent document by its [deployment_id].
    """
    request_body = json.loads(json.dumps(request.get_json()))
    consent_response = consent.create_consent(BASE_URL["production"], request.headers['Authorization'], deployment_id,
                                              consent_body=request_body)
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/consent-documents/<consent_id>', methods=['GET'])
def get_consent_document(deployment_id, consent_id):
    """
    Endpoint: [get_consent_document]
    :param deployment_id: The [deployment_id] of the consent document.
    :param consent_id: The [consent_id] of the consent document.
    :return: The consent document by its [deployment_id] and [consent_id].
    """
    consent_response = consent.get_consent_document(BASE_URL["production"], request.headers['Authorization'],
                                                    deployment_id, consent_id)
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/consent-documents', methods=['GET'])
def get_all_consent_documents(deployment_id):
    """
    Endpoint: [get_all_consent_documents]
    :param deployment_id: The [deployment_id] of the deployment.
    :return: The consent documents by its [deployment_id].
    """
    consent_response = consent.get_all_consent_documents(BASE_URL["production"], request.headers['Authorization'],
                                                         deployment_id)
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/deployments/<deployment_id>/consent-documents/<consent_id>', methods=['DELETE'])
def delete_consent_document(deployment_id, consent_id):
    """
    Endpoint: [delete_consent_document]
    :param deployment_id: The [deployment_id] of the study deployment.
    :param consent_id: The [consent_id] of the consent document.
    :return: The deleted deployment.
    """
    consent_response = consent.delete_consent(BASE_URL["production"], request.headers['Authorization'], deployment_id,
                                              consent_id)
    return Response(json.dumps(consent_response), mimetype='application/json')


"""""""""""""""
    MONITOR
"""""""""""""""


@app.route('/client/api/status/info', methods=['GET'])
def get_instance_info():
    """
    Endpoint: [get_instance_info]
    :return: Overall instance information.
    """
    consent_response = monitor.get_monitor_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/git', methods=['GET'])
def get_git_info():
    """
    Endpoint: [get_git_info]
    :return: The git commit information.
    """
    consent_response = monitor.get_git_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/flyway', methods=['GET'])
def get_flyway_info():
    """
    Endpoint: [get_flyway_info]
    :return: The flyway information.
    """
    consent_response = monitor.get_flyway_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health', methods=['GET'])
def get_health_info():
    """
    Endpoint: [get_health_info]
    :return: Only health information.
    """
    consent_response = monitor.get_health_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health/disk-space', methods=['GET'])
def get_disk_space_info():
    """
    Endpoint: [get_disk_space_info]
    :return: The only disk space information.
    """
    consent_response = monitor.get_disk_space_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health/db', methods=['GET'])
def get_db_info():
    """
    Endpoint: [get_db_info]
    :return: The database information.
    """
    consent_response = monitor.get_health_db_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health/rabbitmq', methods=['GET'])
def get_health_rabbitmq_info():
    """
    Endpoint: [get_health_rabbitmq_info]
    :return: The rabbitmq information.
    """
    consent_response = monitor.get_health_rabbit_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health/ping', methods=['GET'])
def get_health_ping_info():
    """
    Endpoint: [get_health_ping_info]
    :return: The ping health information.
    """
    consent_response = monitor.get_ping_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')


@app.route('/client/api/status/health/mail', methods=['GET'])
def get_mail_server_info():
    """
    Endpoint: [get_mail_server_info]
    :return: The mail server health information.
    """
    consent_response = monitor.get_mail_server_info(BASE_URL["production"], request.headers['Authorization'])
    return Response(json.dumps(consent_response), mimetype='application/json')

