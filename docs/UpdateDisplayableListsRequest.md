# UpdateDisplayableListsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisplayableList]**](DisplayableList.md) |  | 

## Example

```python
from openapi_client.models.update_displayable_lists_request import UpdateDisplayableListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDisplayableListsRequest from a JSON string
update_displayable_lists_request_instance = UpdateDisplayableListsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDisplayableListsRequest.to_json())

# convert the object into a dict
update_displayable_lists_request_dict = update_displayable_lists_request_instance.to_dict()
# create an instance of UpdateDisplayableListsRequest from a dict
update_displayable_lists_request_from_dict = UpdateDisplayableListsRequest.from_dict(update_displayable_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


