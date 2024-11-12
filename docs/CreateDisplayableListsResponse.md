# CreateDisplayableListsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DisplayableList]**](DisplayableList.md) |  | 

## Example

```python
from openapi_client.models.create_displayable_lists_response import CreateDisplayableListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDisplayableListsResponse from a JSON string
create_displayable_lists_response_instance = CreateDisplayableListsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDisplayableListsResponse.to_json())

# convert the object into a dict
create_displayable_lists_response_dict = create_displayable_lists_response_instance.to_dict()
# create an instance of CreateDisplayableListsResponse from a dict
create_displayable_lists_response_from_dict = CreateDisplayableListsResponse.from_dict(create_displayable_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


