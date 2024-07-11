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

from openapi_client.models.search_response_metadata import SearchResponseMetadata

class TestSearchResponseMetadata(unittest.TestCase):
    """SearchResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchResponseMetadata:
        """Test SearchResponseMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchResponseMetadata`
        """
        model = SearchResponseMetadata()
        if include_optional:
            return SearchResponseMetadata(
                rewritten_query = '',
                searched_query = '',
                searched_query_ranges = [
                    openapi_client.models.text_range.TextRange(
                        start_index = 56, 
                        end_index = 56, 
                        type = 'BOLD', 
                        url = '', 
                        document = openapi_client.models.document.Document(
                            id = '', 
                            datasource = '', 
                            connector_type = 'API_CRAWL', 
                            doc_type = '', 
                            content = openapi_client.models.document_content.DocumentContent(
                                full_text_list = [
                                    ''
                                    ], ), 
                            container_document = openapi_client.models.document.Document(
                                id = '', 
                                datasource = '', 
                                doc_type = '', 
                                parent_document = , 
                                title = '', 
                                url = '', 
                                metadata = {"container":"container","parentId":"JIRA_EN-1337","createTime":"2000-01-23T04:56:07.000Z","datasource":"datasource","author":{"name":"name"},"documentId":"documentId","updateTime":"2000-01-23T04:56:07.000Z","mimeType":"mimeType","objectType":"Feature Request","components":["Backend","Networking"],"status":["Done"],"customData":{"someCustomField":"someCustomValue"}}, 
                                sections = [
                                    openapi_client.models.document_section.DocumentSection(
                                        title = '', 
                                        url = '', )
                                    ], ), 
                            parent_document = , 
                            title = '', 
                            url = '', 
                            metadata = {"container":"container","parentId":"JIRA_EN-1337","createTime":"2000-01-23T04:56:07.000Z","datasource":"datasource","author":{"name":"name"},"documentId":"documentId","updateTime":"2000-01-23T04:56:07.000Z","mimeType":"mimeType","objectType":"Feature Request","components":["Backend","Networking"],"status":["Done"],"customData":{"someCustomField":"someCustomValue"}}, 
                            sections = [
                                openapi_client.models.document_section.DocumentSection(
                                    title = '', 
                                    url = '', )
                                ], ), )
                    ],
                original_query = '',
                query_suggestion = {"query":"app:github type:pull author:mortimer","label":"Mortimer's PRs","datasource":"github"},
                additional_query_suggestions = openapi_client.models.query_suggestion_list.QuerySuggestionList(
                    suggestions = [
                        {"query":"app:github type:pull author:mortimer","label":"Mortimer's PRs","datasource":"github"}
                        ], 
                    person = {"name":"George Clooney","obfuscatedId":"abc123"}, ),
                negated_terms = [
                    ''
                    ],
                modified_query_was_used = True,
                original_query_had_no_results = True,
                search_warning = openapi_client.models.search_warning.SearchWarning(
                    warning_type = 'LONG_QUERY', 
                    last_used_term = '', 
                    quotes_ignored_query = '', 
                    ignored_terms = [
                        ''
                        ], ),
                triggered_expert_detection = True
            )
        else:
            return SearchResponseMetadata(
        )
        """

    def testSearchResponseMetadata(self):
        """Test SearchResponseMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
