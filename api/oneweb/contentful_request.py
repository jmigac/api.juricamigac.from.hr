import requests

from api.oneweb.oneweb_constants import (GRAPHQL_QUERY, GRAPHQL_VARIABLES, HOME_PAGE, PROJECT_COLLECTION,
                                         EXPERIENCE_COLLECTION, APPLICATION_JSON, BEARER, GRAPHQL_DATA, GRAPHQL_ITEMS,
                                         EXPERTISES_COLLECTION)
from api.oneweb.oneweb_payloads import Payload


class ContentfulRequest:

    def __init__(self, space_id, environment, token, response_limit, homepage_id):
        self.space_id = space_id
        self.environment = environment
        self.token = token
        self.base_url = f"https://graphql.contentful.com/content/v1/spaces/{self.space_id}/environments/{self.environment}"
        self.payloads = Payload(response_limit=response_limit,
                                homepage_id=homepage_id)

    def get_homepage(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.HOME_PAGE_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_single_content(response=response,
                                                             field_name=HOME_PAGE)

    def get_projects(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.PROJECTS_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_content(response=response,
                                                      field_name=PROJECT_COLLECTION)

    def get_experiences(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.EXPERIENCES_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_content(response=response,
                                                      field_name=EXPERIENCE_COLLECTION)

    def get_expertises(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.EXPERTISES_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_content(response=response,
                                                      field_name=EXPERTISES_COLLECTION)

    def get_footer(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.FOOTER_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_single_content(response=response,
                                                             field_name=HOME_PAGE)

    def get_about_me(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.ABOUT_ME_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_single_content(response=response,
                                                             field_name=HOME_PAGE)

    def get_teaser(self):
        headers = self.get_headers()
        response = requests.post(self.base_url,
                                 json={GRAPHQL_QUERY: self.payloads.TEASER_PAYLOAD, GRAPHQL_VARIABLES: {}},
                                 headers=headers)
        return ContentfulRequest.get_response_single_content(response=response,
                                                             field_name=HOME_PAGE)

    def get_headers(self):
        return {
            'Content-Type': APPLICATION_JSON,
            'Authorization': f"{BEARER} {self.token}"
        }

    @staticmethod
    def get_response_content(response, field_name):
        return response.json()[GRAPHQL_DATA][field_name][GRAPHQL_ITEMS]

    @staticmethod
    def get_response_single_content(response, field_name):
        return response.json()[GRAPHQL_DATA][field_name]
