# CreateDisplayableListsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisplayableList]**](DisplayableList.md) |  | 

## Example

```python
from openapi_client.models.create_displayable_lists_request import CreateDisplayableListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDisplayableListsRequest from a JSON string
create_displayable_lists_request_instance = CreateDisplayableListsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDisplayableListsRequest.to_json())

# convert the object into a dict
create_displayable_lists_request_dict = create_displayable_lists_request_instance.to_dict()
# create an instance of CreateDisplayableListsRequest from a dict
create_displayable_lists_request_from_dict = CreateDisplayableListsRequest.from_dict(create_displayable_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


