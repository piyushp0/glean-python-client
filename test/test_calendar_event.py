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

from openapi_client.models.calendar_event import CalendarEvent

class TestCalendarEvent(unittest.TestCase):
    """CalendarEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalendarEvent:
        """Test CalendarEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalendarEvent`
        """
        model = CalendarEvent()
        if include_optional:
            return CalendarEvent(
                time = openapi_client.models.time_interval.TimeInterval(
                    start = '', 
                    end = '', ),
                event_type = 'DEFAULT',
                id = '',
                url = '',
                attendees = openapi_client.models.calendar_attendees.CalendarAttendees(
                    people = [
                        openapi_client.models.calendar_attendee.CalendarAttendee(
                            is_organizer = True, 
                            is_in_group = True, 
                            person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                            group_attendees = [
                                openapi_client.models.calendar_attendee.CalendarAttendee(
                                    is_organizer = True, 
                                    is_in_group = True, 
                                    person = {"name":"George Clooney","obfuscatedId":"abc123"}, 
                                    response_status = 'ACCEPTED', )
                                ], 
                            response_status = 'ACCEPTED', )
                        ], 
                    is_limit = True, 
                    total = 56, 
                    num_accepted = 56, 
                    num_declined = 56, 
                    num_no_response = 56, 
                    num_tentative = 56, ),
                location = '',
                conference_data = openapi_client.models.conference_data.ConferenceData(
                    provider = 'ZOOM', 
                    uri = '', 
                    source = 'NATIVE_CONFERENCE', ),
                description = '',
                datasource = '',
                has_transcript = True,
                classifications = [
                    openapi_client.models.event_classification.EventClassification(
                        name = 'External Event', 
                        strategies = [
                            'customerCard'
                            ], )
                    ],
                generated_attachments = [
                    openapi_client.models.generated_attachment.GeneratedAttachment(
                        strategy_name = 'customerCard', 
                        documents = [
                            openapi_client.models.document.Document(
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
                                    ], )
                            ], 
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
                        external_links = [
                            openapi_client.models.structured_link.StructuredLink(
                                name = '', 
                                url = '', 
                                icon_config = {"color":"#343CED","key":"person_icon","iconType":"GLYPH","name":"user"}, )
                            ], 
                        content = [
                            {"displayHeader":"Action Items","content":"You said you'd send over the design document after the meeting."}
                            ], )
                    ]
            )
        else:
            return CalendarEvent(
                id = '',
                url = '',
        )
        """

    def testCalendarEvent(self):
        """Test CalendarEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
