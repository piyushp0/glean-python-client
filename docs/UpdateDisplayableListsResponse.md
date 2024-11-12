# UpdateDisplayableListsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisplayableList]**](DisplayableList.md) |  | 

## Example

```python
from openapi_client.models.update_displayable_lists_response import UpdateDisplayableListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDisplayableListsResponse from a JSON string
update_displayable_lists_response_instance = UpdateDisplayableListsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDisplayableListsResponse.to_json())

# convert the object into a dict
update_displayable_lists_response_dict = update_displayable_lists_response_instance.to_dict()
# create an instance of UpdateDisplayableListsResponse from a dict
update_displayable_lists_response_from_dict = UpdateDisplayableListsResponse.from_dict(update_displayable_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


