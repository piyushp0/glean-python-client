# PersonMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**first_name** | **str** | The first name of the person | [optional] 
**last_name** | **str** | The last name of the person | [optional] 
**title** | **str** | Job title. | [optional] 
**business_unit** | **str** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**department** | **str** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | [optional] 
**teams** | [**List[PersonTeam]**](PersonTeam.md) | Info about the employee&#39;s team(s). | [optional] 
**department_count** | **int** | The number of people in this person&#39;s department. | [optional] 
**email** | **str** | The user&#39;s primary email address | [optional] 
**alias_emails** | **List[str]** | Additional email addresses of this user beyond the primary, if any. | [optional] 
**location** | **str** | User facing string representing the person&#39;s location. | [optional] 
**structured_location** | [**StructuredLocation**](StructuredLocation.md) |  | [optional] 
**external_profile_link** | **str** | Link to a customer&#39;s internal profile page. This is set to &#39;#&#39; when no link is desired. | [optional] 
**manager** | [**Person**](Person.md) |  | [optional] 
**management_chain** | [**List[Person]**](Person.md) | The chain of reporting in the company as far up as it goes. The last entry is this person&#39;s direct manager. | [optional] 
**phone** | **str** | Phone number as a number string. | [optional] 
**timezone** | **str** | The timezone of the person. E.g. \&quot;Pacific Daylight Time\&quot;. | [optional] 
**timezone_offset** | **int** | The offset of the person&#39;s timezone in seconds from UTC. | [optional] 
**photo_url** | **str** | The URL of the person&#39;s avatar. Public, glean-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**unedited_photo_url** | **str** | The original photo URL of the person&#39;s avatar before any edits they made are applied | [optional] 
**banner_url** | **str** | The URL of the person&#39;s banner photo. | [optional] 
**reports** | [**List[Person]**](Person.md) |  | [optional] 
**start_date** | **date** | The date when the employee started. | [optional] 
**end_date** | **date** | If a former employee, the last date of employment. | [optional] 
**bio** | **str** | Short biography or mission statement of the employee. | [optional] 
**pronoun** | **str** | She/her, He/his or other pronoun. | [optional] 
**org_size_count** | **int** | The total recursive size of the people reporting to this person, or 1 | [optional] 
**direct_reports_count** | **int** | The total number of people who directly report to this person, or 0 | [optional] 
**preferred_name** | **str** | The preferred name of the person, or a nickname. | [optional] 
**social_network** | [**List[SocialNetwork]**](SocialNetwork.md) | List of social network profiles. | [optional] 
**datasource_profile** | [**List[DatasourceProfile]**](DatasourceProfile.md) | List of profiles this user has in different datasources / tools that they use. | [optional] 
**query_suggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**people_distance** | [**List[PersonDistance]**](PersonDistance.md) | List of people and distances to those people from this person. Optionally with metadata. | [optional] 
**invite_info** | [**InviteInfo**](InviteInfo.md) |  | [optional] 
**is_signed_up** | **bool** | Whether the user has signed into Glean at least once. | [optional] 
**last_extension_use** | **datetime** | The last time the user has used the Glean extension in ISO 8601 format. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldData]**](CustomFieldData.md) | User customizable fields for additional people information. | [optional] 
**logging_id** | **str** | The logging id of the person used in scrubbed logs, tracking GA metrics. | [optional] 
**start_date_percentile** | **float** | Percentage of the company that started strictly after this person. Between [0,100). | [optional] 
**busy_events** | [**List[AnonymousEvent]**](AnonymousEvent.md) | Intervals of busy time for this person, along with the type of event they&#39;re busy with. | [optional] 
**profile_bool_settings** | **Dict[str, bool]** | flag settings to indicate user profile settings for certain items | [optional] 
**badges** | [**List[Badge]**](Badge.md) | The badges that a user has earned over their lifetime. | [optional] 
**is_org_root** | **bool** | Whether this person is a \&quot;root\&quot; node in their organization&#39;s hierarchy. | [optional] 

## Example

```python
from openapi_client.models.person_metadata import PersonMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PersonMetadata from a JSON string
person_metadata_instance = PersonMetadata.from_json(json)
# print the JSON string representation of the object
print(PersonMetadata.to_json())

# convert the object into a dict
person_metadata_dict = person_metadata_instance.to_dict()
# create an instance of PersonMetadata from a dict
person_metadata_from_dict = PersonMetadata.from_dict(person_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


