""" service document retrieval and extraction """

import json
import requests

from token import get_auth_document


def get_service_document(service_name, endpoint, username, password=None,
                         api_key=None):

    results = get_auth_document(endpoint, username, password=password,
                                api_key=api_key)

    for service in results['access']['serviceCatalog']:
        if service['name'] == service_name:
            return service
    else:
        return None


def get_service_endpoint(region, service_name, endpoint, username,
                         password=None, api_key=None):

    service = get_service_document(service_name, endpoint, username,
                                   password=password, api_key=api_key)

    if service:
        for endpoint in service.get('endpoints', []):
            if endpoint.get('region', '').lower() == region.lower():
                return endpoint.get('publicURL', None)
    else:
        return None
