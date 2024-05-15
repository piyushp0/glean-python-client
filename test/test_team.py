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

from openapi_client.models.team import Team

class TestTeam(unittest.TestCase):
    """Team unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Team:
        """Test Team
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Team`
        """
        model = Team()
        if include_optional:
            return Team(
                related_objects = {
                    'key' : openapi_client.models.related_object_edge.RelatedObjectEdge(
                        objects = [
                            openapi_client.models.related_object.RelatedObject(
                                id = '', 
                                metadata = openapi_client.models.related_object_metadata.RelatedObject_metadata(
                                    name = '', ), )
                            ], )
                    },
                permissions = openapi_client.models.object_permissions.ObjectPermissions(
                    write = openapi_client.models.write_permission.WritePermission(
                        scope_type = 'GLOBAL', 
                        create = True, 
                        update = True, 
                        delete = True, ), ),
                id = '',
                name = '',
                description = '',
                business_unit = '',
                department = '',
                photo_url = '',
                banner_url = '',
                external_link = '',
                members = [
                    openapi_client.models.person_to_team_relationship.PersonToTeamRelationship(
                        person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                        relationship = 'MEMBER', 
                        custom_relationship_str = '', 
                        join_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                member_count = 56,
                emails = [
                    openapi_client.models.team_email.TeamEmail(
                        email = '', 
                        type = 'OTHER', 
                        is_user_generated = True, )
                    ],
                datasource_profiles = [
                    openapi_client.models.datasource_profile.DatasourceProfile(
                        datasource = 'github', 
                        handle = '', 
                        url = '', 
                        native_app_url = '', 
                        is_user_generated = True, )
                    ],
                datasource = '',
                created_from = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'PROCESSED',
                can_be_deleted = True,
                logging_id = ''
            )
        else:
            return Team(
                id = '',
                name = '',
        )
        """

    def testTeam(self):
        """Test Team"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
