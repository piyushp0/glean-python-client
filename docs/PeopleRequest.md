# PeopleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone_offset** | **int** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**obfuscated_ids** | **List[str]** | The Person IDs to retrieve. If no IDs are requested, the current user&#39;s details are returned. | [optional] 
**email_ids** | **List[str]** | The email IDs to retrieve. The result is the deduplicated union of emailIds and obfuscatedIds. | [optional] 
**include_fields** | **List[str]** | List of PersonMetadata fields to return (that aren&#39;t returned by default) | [optional] 
**include_types** | **List[str]** | The types of people entities to include in the response in addition to those returned by default. | [optional] 
**source** | **str** | A string denoting the search surface from which the endpoint is called. | [optional] 

## Example

```python
from openapi_client.models.people_request import PeopleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleRequest from a JSON string
people_request_instance = PeopleRequest.from_json(json)
# print the JSON string representation of the object
print(PeopleRequest.to_json())

# convert the object into a dict
people_request_dict = people_request_instance.to_dict()
# create an instance of PeopleRequest from a dict
people_request_from_dict = PeopleRequest.from_dict(people_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


