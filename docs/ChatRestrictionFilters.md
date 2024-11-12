# ChatRestrictionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) |  | [optional] 
**datasource_instances** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.chat_restriction_filters import ChatRestrictionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRestrictionFilters from a JSON string
chat_restriction_filters_instance = ChatRestrictionFilters.from_json(json)
# print the JSON string representation of the object
print(ChatRestrictionFilters.to_json())

# convert the object into a dict
chat_restriction_filters_dict = chat_restriction_filters_instance.to_dict()
# create an instance of ChatRestrictionFilters from a dict
chat_restriction_filters_from_dict = ChatRestrictionFilters.from_dict(chat_restriction_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


