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

from openapi_client.models.recommendations_response import RecommendationsResponse

class TestRecommendationsResponse(unittest.TestCase):
    """RecommendationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationsResponse:
        """Test RecommendationsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationsResponse`
        """
        model = RecommendationsResponse()
        if include_optional:
            return RecommendationsResponse(
                tracking_token = '',
                session_info = openapi_client.models.session_info.SessionInfo(
                    session_tracking_token = '', 
                    tab_id = '', 
                    last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_query = '', ),
                results = [
                    {"snippets":[{"snippet":"snippet","mimeType":"mimeType"}],"metadata":{"container":"container","createTime":"2000-01-23T04:56:07.000Z","datasource":"datasource","author":{"name":"name"},"documentId":"documentId","updateTime":"2000-01-23T04:56:07.000Z","mimeType":"mimeType","objectType":"objectType"},"title":"title","url":"https://example.com/foo/bar","nativeAppUrl":"slack://foo/bar","mustIncludeSuggestions":[{"missingTerm":"container","query":"container"}]}
                    ],
                structured_results = [
                    openapi_client.models.structured_result.StructuredResult(
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
                                ], ), 
                        person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        customer = openapi_client.models.customer.Customer(
                            id = '', 
                            domains = [
                                ''
                                ], 
                            company = openapi_client.models.company.Company(
                                name = '', 
                                profile_url = '', 
                                website_urls = [
                                    ''
                                    ], 
                                logo_url = '', 
                                location = 'New York City', 
                                phone = '', 
                                fax = '', 
                                industry = 'Finances', 
                                annual_revenue = 1.337, 
                                number_of_employees = 56, 
                                stock_symbol = '', 
                                founded_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                about = 'Financial, software, data, and media company headquartered in Midtown Manhattan, New York City', ), 
                            document_counts = {
                                'key' : 56
                                }, 
                            poc = [
                                {"name":"George Clooney","obfuscatedId":"abc123"}
                                ], 
                            merged_customers = [
                                openapi_client.models.customer.Customer(
                                    id = '', 
                                    company = openapi_client.models.company.Company(
                                        name = '', 
                                        profile_url = '', 
                                        logo_url = '', 
                                        location = 'New York City', 
                                        phone = '', 
                                        fax = '', 
                                        industry = 'Finances', 
                                        annual_revenue = 1.337, 
                                        number_of_employees = 56, 
                                        stock_symbol = '', 
                                        founded_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        about = 'Financial, software, data, and media company headquartered in Midtown Manhattan, New York City', ), 
                                    start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    contract_annual_revenue = 1.337, 
                                    notes = 'CIO is interested in trying out the product.', )
                                ], 
                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            contract_annual_revenue = 1.337, 
                            notes = 'CIO is interested in trying out the product.', ), 
                        team = null, 
                        custom_entity = null, 
                        answer = null, 
                        extracted_qn_a = openapi_client.models.extracted_qn_a.ExtractedQnA(
                            heading = '', 
                            question = '', 
                            question_result = {"snippets":[{"snippet":"snippet","mimeType":"mimeType"}],"metadata":{"container":"container","createTime":"2000-01-23T04:56:07.000Z","datasource":"datasource","author":{"name":"name"},"documentId":"documentId","updateTime":"2000-01-23T04:56:07.000Z","mimeType":"mimeType","objectType":"objectType"},"title":"title","url":"https://example.com/foo/bar","nativeAppUrl":"slack://foo/bar","mustIncludeSuggestions":[{"missingTerm":"container","query":"container"}]}, ), 
                        app = openapi_client.models.app_result.AppResult(
                            datasource = '', 
                            doc_type = '', 
                            mime_type = '', 
                            icon_url = '', ), 
                        collection = null, 
                        answer_board = null, 
                        code = {"repoName":"scio","fileName":"README.md","matches":[{"lineNumber":1,"content":"Welcome to the beginning","ranges":[]},{"lineNumber":2,"content":"Second line of the file","ranges":[]},{"lineNumber":3,"content":"hello world hello world","ranges":[{"startindex":0,"endIndex":5},{"startIndex":12,"endIndex":17}]}]}, 
                        shortcut = null, 
                        query_suggestions = openapi_client.models.query_suggestion_list.QuerySuggestionList(
                            suggestions = [
                                {"query":"app:github type:pull author:mortimer","label":"Mortimer's PRs","datasource":"github"}
                                ], ), 
                        related_documents = [
                            openapi_client.models.related_documents.RelatedDocuments(
                                relation = 'CASE', 
                                associated_entity_id = '', 
                                query_suggestion = {"query":"app:github type:pull author:mortimer","label":"Mortimer's PRs","datasource":"github"}, 
                                documents = [
                                    
                                    ], 
                                results = [
                                    {"snippets":[{"snippet":"snippet","mimeType":"mimeType"}],"metadata":{"container":"container","createTime":"2000-01-23T04:56:07.000Z","datasource":"datasource","author":{"name":"name"},"documentId":"documentId","updateTime":"2000-01-23T04:56:07.000Z","mimeType":"mimeType","objectType":"objectType"},"title":"title","url":"https://example.com/foo/bar","nativeAppUrl":"slack://foo/bar","mustIncludeSuggestions":[{"missingTerm":"container","query":"container"}]}
                                    ], )
                            ], 
                        related_question = openapi_client.models.related_question.RelatedQuestion(
                            question = '', 
                            ranges = [
                                openapi_client.models.text_range.TextRange(
                                    start_index = 56, 
                                    end_index = 56, 
                                    type = 'BOLD', 
                                    url = '', )
                                ], ), 
                        disambiguation = openapi_client.models.disambiguation.Disambiguation(
                            name = '', 
                            id = '', 
                            type = 'PERSON', ), 
                        snippets = [
                            {"snippet":"snippet","mimeType":"mimeType"}
                            ], 
                        tracking_token = '', 
                        prominence = 'HERO', 
                        source = 'EXPERT_DETECTION', )
                    ],
                generated_qna_result = openapi_client.models.generated_qna.GeneratedQna(
                    question = '', 
                    answer = '', 
                    follow_up_prompts = [
                        ''
                        ], 
                    followup_actions = [
                        openapi_client.models.followup_action.FollowupAction(
                            action_instance_id = '', )
                        ], 
                    ranges = [
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
                    status = 'COMPUTING', 
                    cursor = '', 
                    tracking_token = '', ),
                error_info = openapi_client.models.error_info.ErrorInfo(
                    bad_gmail_token = True, 
                    bad_outlook_token = True, 
                    invalid_operators = [
                        openapi_client.models.invalid_operator_value_error.InvalidOperatorValueError(
                            key = '', 
                            value = '', )
                        ], 
                    error_messages = [
                        openapi_client.models.error_message.ErrorMessage(
                            source = '', 
                            error_message = '', )
                        ], ),
                request_id = '',
                backend_time_millis = 1100
            )
        else:
            return RecommendationsResponse(
        )
        """

    def testRecommendationsResponse(self):
        """Test RecommendationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
