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

from openapi_client.models.person_metadata import PersonMetadata

class TestPersonMetadata(unittest.TestCase):
    """PersonMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonMetadata:
        """Test PersonMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonMetadata`
        """
        model = PersonMetadata()
        if include_optional:
            return PersonMetadata(
                type = 'FULL_TIME',
                first_name = '',
                last_name = '',
                title = '',
                business_unit = '',
                department = '',
                teams = [
                    openapi_client.models.person_team.PersonTeam(
                        id = '', 
                        name = '', 
                        external_link = '', 
                        relationship = 'MEMBER', 
                        join_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                department_count = 56,
                email = '',
                alias_emails = [
                    ''
                    ],
                location = '',
                structured_location = openapi_client.models.structured_location.StructuredLocation(
                    desk_location = '', 
                    timezone = '', 
                    address = '', 
                    city = '', 
                    state = '', 
                    region = '', 
                    zip_code = '', 
                    country = '', 
                    country_code = '', ),
                external_profile_link = '',
                manager = {"name":"George Clooney","obfuscatedId":"abc123"},
                management_chain = [
                    {"name":"George Clooney","obfuscatedId":"abc123"}
                    ],
                phone = '',
                timezone = '',
                timezone_offset = 56,
                photo_url = '',
                unedited_photo_url = '',
                banner_url = '',
                reports = [
                    {"name":"George Clooney","obfuscatedId":"abc123"}
                    ],
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                bio = '',
                pronoun = '',
                org_size_count = 56,
                direct_reports_count = 56,
                preferred_name = '',
                social_network = [
                    openapi_client.models.social_network.SocialNetwork(
                        name = '', 
                        profile_name = '', 
                        profile_url = '', )
                    ],
                datasource_profile = [
                    openapi_client.models.datasource_profile.DatasourceProfile(
                        datasource = 'github', 
                        handle = '', 
                        url = '', 
                        native_app_url = '', 
                        is_user_generated = True, )
                    ],
                query_suggestions = openapi_client.models.query_suggestion_list.QuerySuggestionList(
                    suggestions = [
                        {"query":"app:github type:pull author:mortimer","label":"Mortimer's PRs","datasource":"github"}
                        ], 
                    person = {"name":"George Clooney","obfuscatedId":"abc123"}, ),
                people_distance = [
                    openapi_client.models.person_distance.PersonDistance(
                        name = '', 
                        obfuscated_id = '', 
                        distance = 1.337, )
                    ],
                invite_info = openapi_client.models.invite_info.InviteInfo(
                    sign_up_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    invites = [
                        openapi_client.models.channel_invite_info.ChannelInviteInfo(
                            channel = 'COMMUNICATION_CHANNEL_EMAIL', 
                            is_auto_invite = True, 
                            inviter = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                            invite_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reminder_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    inviter = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                    invite_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    reminder_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                is_signed_up = True,
                last_extension_use = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                permissions = openapi_client.models.permissions.Permissions(
                    can_admin_search = True, 
                    can_admin_client_api_global_tokens = True, 
                    can_dlp = True, 
                    read = {
                        'key' : [
                            openapi_client.models.read_permission.ReadPermission(
                                scope_type = 'GLOBAL', )
                            ]
                        }, 
                    write = {
                        'key' : [
                            openapi_client.models.write_permission.WritePermission(
                                create = True, 
                                update = True, 
                                delete = True, )
                            ]
                        }, 
                    grant = {
                        'key' : [
                            openapi_client.models.grant_permission.GrantPermission()
                            ]
                        }, 
                    role = '', 
                    roles = [
                        ''
                        ], ),
                custom_fields = [
                    openapi_client.models.custom_field_data.CustomFieldData(
                        label = '', 
                        values = [
                            null
                            ], 
                        displayable = True, )
                    ],
                logging_id = '',
                start_date_percentile = 1.337,
                busy_events = [
                    openapi_client.models.anonymous_event.AnonymousEvent(
                        time = openapi_client.models.time_interval.TimeInterval(
                            start = '', 
                            end = '', ), 
                        event_type = 'DEFAULT', )
                    ],
                profile_bool_settings = {
                    'key' : True
                    },
                badges = [
                    {"key":"deployment_name_new_hire","displayName":"New hire","iconConfig":[{"$ref":"../../shared/common.yaml#/components/schemas/IconConfig/example"}]}
                    ],
                is_org_root = True
            )
        else:
            return PersonMetadata(
        )
        """

    def testPersonMetadata(self):
        """Test PersonMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
