# PeopleSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[PeopleSuggestionCategory]**](PeopleSuggestionCategory.md) | Categories of data requested. Request can include single or multiple categories. | 
**departments** | **List[str]** | Departments that the data is requested for. If empty, corresponds to whole company. | [optional] 

## Example

```python
from openapi_client.models.people_suggest_request import PeopleSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSuggestRequest from a JSON string
people_suggest_request_instance = PeopleSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(PeopleSuggestRequest.to_json())

# convert the object into a dict
people_suggest_request_dict = people_suggest_request_instance.to_dict()
# create an instance of PeopleSuggestRequest from a dict
people_suggest_request_from_dict = PeopleSuggestRequest.from_dict(people_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


