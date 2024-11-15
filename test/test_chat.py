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

from openapi_client.models.chat import Chat

class TestChat(unittest.TestCase):
    """Chat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Chat:
        """Test Chat
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Chat`
        """
        model = Chat()
        if include_optional:
            return Chat(
                messages = [
                    openapi_client.models.chat_message.ChatMessage(
                        agent_config = openapi_client.models.agent_config.AgentConfig(
                            agent = 'DEFAULT', 
                            mode = 'DEFAULT', ), 
                        author = 'USER', 
                        citations = [
                            openapi_client.models.chat_message_citation.ChatMessageCitation(
                                tracking_token = '', 
                                source_document = openapi_client.models.document.Document(
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
                                        ], ), 
                                source_file = openapi_client.models.chat_file.ChatFile(
                                    id = 'FILE_1234', 
                                    url = 'www.google.com', 
                                    name = 'sample.pdf', ), 
                                source_person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                                reference_ranges = [
                                    openapi_client.models.reference_range.ReferenceRange(
                                        text_range = openapi_client.models.text_range.TextRange(
                                            start_index = 56, 
                                            end_index = 56, 
                                            type = 'BOLD', 
                                            url = '', 
                                            document = , ), 
                                        snippets = [
                                            {"snippet":"snippet","mimeType":"mimeType"}
                                            ], )
                                    ], )
                            ], 
                        uploaded_file_ids = [
                            ''
                            ], 
                        fragments = [
                            null
                            ], 
                        ts = '', 
                        message_id = '', 
                        message_tracking_token = '', 
                        message_type = 'CONTENT', 
                        has_more_fragments = True, )
                    ],
                id = '',
                create_time = 56,
                created_by = {"name":"George Clooney","obfuscatedId":"abc123"},
                update_time = 56,
                name = '',
                application_id = ''
            )
        else:
            return Chat(
        )
        """

    def testChat(self):
        """Test Chat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
