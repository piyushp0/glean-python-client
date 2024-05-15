# PeopleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Person]**](Person.md) | A Person for each ID in the request, each with PersonMetadata populated. | [optional] 
**related_documents** | [**List[RelatedDocuments]**](RelatedDocuments.md) | A list of documents related to this people response. This is only included if DOCUMENT_ACTIVITY is requested and only 1 person is included in the request. | [optional] 
**errors** | **List[str]** | A list of IDs that could not be found. | [optional] 

## Example

```python
from openapi_client.models.people_response import PeopleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleResponse from a JSON string
people_response_instance = PeopleResponse.from_json(json)
# print the JSON string representation of the object
print(PeopleResponse.to_json())

# convert the object into a dict
people_response_dict = people_response_instance.to_dict()
# create an instance of PeopleResponse from a dict
people_response_from_dict = PeopleResponse.from_dict(people_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


