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

from openapi_client.models.edit_answer_request import EditAnswerRequest

class TestEditAnswerRequest(unittest.TestCase):
    """EditAnswerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditAnswerRequest:
        """Test EditAnswerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditAnswerRequest`
        """
        model = EditAnswerRequest()
        if include_optional:
            return EditAnswerRequest(
                id = 3,
                doc_id = 'ANSWERS_answer_3',
                question = 'Why is the sky blue?',
                question_variations = [
                    ''
                    ],
                body_text = 'From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.',
                board_id = 56,
                audience_filters = [
                    {"fieldName":"type","values":[{"value":"Spreadsheet","relationType":"EQUALS"},{"value":"Presentation","relationType":"EQUALS"}]}
                    ],
                added_roles = [
                    openapi_client.models.user_role_specification.UserRoleSpecification(
                        source_document_spec = null, 
                        person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        group = openapi_client.models.group.Group(
                            type = 'DEPARTMENT', 
                            id = '', 
                            name = '', ), 
                        role = 'OWNER', )
                    ],
                removed_roles = [
                    openapi_client.models.user_role_specification.UserRoleSpecification(
                        source_document_spec = null, 
                        person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        group = openapi_client.models.group.Group(
                            type = 'DEPARTMENT', 
                            id = '', 
                            name = '', ), 
                        role = 'OWNER', )
                    ],
                roles = [
                    openapi_client.models.user_role_specification.UserRoleSpecification(
                        source_document_spec = null, 
                        person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        group = openapi_client.models.group.Group(
                            type = 'DEPARTMENT', 
                            id = '', 
                            name = '', ), 
                        role = 'OWNER', )
                    ],
                source_document_spec = None,
                source_type = 'DOCUMENT',
                added_collections = [
                    56
                    ],
                removed_collections = [
                    56
                    ],
                combined_answer_text = openapi_client.models.structured_text_mutable_properties.StructuredTextMutableProperties(
                    text = 'From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.', )
            )
        else:
            return EditAnswerRequest(
                id = 3,
        )
        """

    def testEditAnswerRequest(self):
        """Test EditAnswerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
