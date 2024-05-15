# PersonSuggestionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**PeopleSuggestionCategory**](PeopleSuggestionCategory.md) |  | 
**people** | [**List[Person]**](Person.md) | Information about suggested users. | [optional] 

## Example

```python
from openapi_client.models.person_suggestion_list import PersonSuggestionList

# TODO update the JSON string below
json = "{}"
# create an instance of PersonSuggestionList from a JSON string
person_suggestion_list_instance = PersonSuggestionList.from_json(json)
# print the JSON string representation of the object
print(PersonSuggestionList.to_json())

# convert the object into a dict
person_suggestion_list_dict = person_suggestion_list_instance.to_dict()
# create an instance of PersonSuggestionList from a dict
person_suggestion_list_from_dict = PersonSuggestionList.from_dict(person_suggestion_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


