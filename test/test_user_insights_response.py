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

from openapi_client.models.user_insights_response import UserInsightsResponse

class TestUserInsightsResponse(unittest.TestCase):
    """UserInsightsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserInsightsResponse:
        """Test UserInsightsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserInsightsResponse`
        """
        model = UserInsightsResponse()
        if include_optional:
            return UserInsightsResponse(
                last_log_timestamp = 56,
                activity_insights = [
                    openapi_client.models.user_activity_insight.UserActivityInsight(
                        user = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        activity = 'ALL', 
                        last_activity_timestamp = 56, 
                        activity_count = openapi_client.models.count_info.CountInfo(
                            count = 56, 
                            period = openapi_client.models.period.Period(
                                min_days_from_now = 56, 
                                max_days_from_now = 56, 
                                start = openapi_client.models.time_point.TimePoint(
                                    epoch_seconds = 56, 
                                    days_from_now = 56, ), 
                                end = openapi_client.models.time_point.TimePoint(
                                    epoch_seconds = 56, 
                                    days_from_now = 56, ), ), 
                            org = '', ), 
                        active_day_count = openapi_client.models.count_info.CountInfo(
                            count = 56, 
                            org = '', ), )
                    ],
                inactive_insights = [
                    openapi_client.models.user_activity_insight.UserActivityInsight(
                        user = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        activity = 'ALL', 
                        last_activity_timestamp = 56, 
                        activity_count = openapi_client.models.count_info.CountInfo(
                            count = 56, 
                            period = openapi_client.models.period.Period(
                                min_days_from_now = 56, 
                                max_days_from_now = 56, 
                                start = openapi_client.models.time_point.TimePoint(
                                    epoch_seconds = 56, 
                                    days_from_now = 56, ), 
                                end = openapi_client.models.time_point.TimePoint(
                                    epoch_seconds = 56, 
                                    days_from_now = 56, ), ), 
                            org = '', ), 
                        active_day_count = openapi_client.models.count_info.CountInfo(
                            count = 56, 
                            org = '', ), )
                    ],
                total_teammates = 56,
                total_active_users = 56,
                departments = [
                    ''
                    ]
            )
        else:
            return UserInsightsResponse(
        )
        """

    def testUserInsightsResponse(self):
        """Test UserInsightsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
