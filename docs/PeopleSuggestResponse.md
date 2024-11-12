# PeopleSuggestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions** | [**List[PersonSuggestionList]**](PersonSuggestionList.md) | Information about people suggestions for asked categories. | [optional] 

## Example

```python
from openapi_client.models.people_suggest_response import PeopleSuggestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSuggestResponse from a JSON string
people_suggest_response_instance = PeopleSuggestResponse.from_json(json)
# print the JSON string representation of the object
print(PeopleSuggestResponse.to_json())

# convert the object into a dict
people_suggest_response_dict = people_suggest_response_instance.to_dict()
# create an instance of PeopleSuggestResponse from a dict
people_suggest_response_from_dict = PeopleSuggestResponse.from_dict(people_suggest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


