# GetDisplayableListsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisplayableList]**](DisplayableList.md) |  | 

## Example

```python
from openapi_client.models.get_displayable_lists_response import GetDisplayableListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDisplayableListsResponse from a JSON string
get_displayable_lists_response_instance = GetDisplayableListsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDisplayableListsResponse.to_json())

# convert the object into a dict
get_displayable_lists_response_dict = get_displayable_lists_response_instance.to_dict()
# create an instance of GetDisplayableListsResponse from a dict
get_displayable_lists_response_from_dict = GetDisplayableListsResponse.from_dict(get_displayable_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


