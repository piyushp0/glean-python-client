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

from openapi_client.models.feedback import Feedback

class TestFeedback(unittest.TestCase):
    """Feedback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Feedback:
        """Test Feedback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Feedback`
        """
        model = Feedback()
        if include_optional:
            return Feedback(
                id = '',
                category = 'ANNOUNCEMENT',
                tracking_tokens = [
                    ''
                    ],
                event = 'CLICK',
                position = 56,
                payload = '',
                session_info = openapi_client.models.session_info.SessionInfo(
                    session_tracking_token = '', 
                    tab_id = '', 
                    last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_query = '', ),
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = openapi_client.models.user.User(
                    user_id = '', 
                    orig_id = '', ),
                pathname = '',
                channels = [
                    'COMPANY'
                    ],
                url = '',
                ui_tree = [
                    ''
                    ],
                ui_element = '',
                manual_feedback_info = openapi_client.models.manual_feedback_info.ManualFeedbackInfo(
                    email = '', 
                    source = 'AUTOCOMPLETE', 
                    issue = '', 
                    image_urls = [
                        ''
                        ], 
                    query = '', 
                    obscured_query = '', 
                    active_tab = '', 
                    comments = '', 
                    search_results = [
                        ''
                        ], 
                    previous_messages = [
                        ''
                        ], 
                    num_queries_from_first_run = 56, 
                    vote = 'UPVOTE', 
                    rating = 56, 
                    rating_key = '', 
                    rating_scale = 56, ),
                seen_feedback_info = openapi_client.models.seen_feedback_info.SeenFeedbackInfo(
                    is_explicit = True, ),
                user_view_info = openapi_client.models.user_view_info.UserViewInfo(
                    doc_id = '', 
                    doc_title = '', 
                    doc_url = '', ),
                workflow_feedback_info = openapi_client.models.workflow_feedback_info.WorkflowFeedbackInfo(
                    source = 'ZERO_STATE', ),
                application_id = ''
            )
        else:
            return Feedback(
                tracking_tokens = [
                    ''
                    ],
                event = 'CLICK',
        )
        """

    def testFeedback(self):
        """Test Feedback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
