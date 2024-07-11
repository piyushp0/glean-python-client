# coding: utf-8

"""
    Glean Client API

    # Introduction These are the public APIs to enable implementing a custom client interface to the Glean system.  # Usage guidelines This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along with a 6-month sunset period for anything that requires developers to adopt the new versions.  # SDK Client bindings for the API can be generated for most popular languages (Python, Java, NodeJS, etc). To do so:  Download the OpenAPI specification for the API, by clicking on one of the following options: 1. [Download JSON specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.json?branch=main&download=true) 2. [Download YAML specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.yaml?branch=main&download=true)  Use [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) to generate bindings for your language of choice, for example: ```bash shell $ npx @openapitools/openapi-generator-cli@latest generate -i client_api.yaml -g go ```  To see available languages: ```bash shell $ npx @openapitools/openapi-generator-cli@latest list ```  Determine the host you need to connect to. This will be the URL of the backend for your Glean deployment, for example, customer-be.glean.com 

    The version of the OpenAPI document: 0.9.0
    Contact: support@glean.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ask_request import AskRequest

class TestAskRequest(unittest.TestCase):
    """AskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AskRequest:
        """Test AskRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AskRequest`
        """
        model = AskRequest()
        if include_optional:
            return AskRequest(
                detect_only = True,
                ask_experimental_metadata = openapi_client.models.ask_experimental_metadata.AskExperimentalMetadata(
                    query_has_mentions = True, 
                    query_is_length_appropriate = True, 
                    query_is_answerable = True, ),
                search_request = {"trackingToken":"trackingToken","query":"vacation policy","pageSize":10,"requestOptions":{"facetFilters":[{"fieldName":"type","values":[{"value":"article","relationType":"EQUALS"},{"value":"document","relationType":"EQUALS"}]},{"fieldName":"department","values":[{"value":"engineering","relationType":"EQUALS"}]}]}},
                excluded_document_specs = [
                    null
                    ],
                operators = '',
                backend = 'SEARCH',
                chat_application_id = ''
            )
        else:
            return AskRequest(
                search_request = {"trackingToken":"trackingToken","query":"vacation policy","pageSize":10,"requestOptions":{"facetFilters":[{"fieldName":"type","values":[{"value":"article","relationType":"EQUALS"},{"value":"document","relationType":"EQUALS"}]},{"fieldName":"department","values":[{"value":"engineering","relationType":"EQUALS"}]}]}},
        )
        """

    def testAskRequest(self):
        """Test AskRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
