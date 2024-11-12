# ChatRestrictionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | Specifications for containers that should be used as part of the restriction (include/exclude). Memberships are recursively defined for a subset of datasources (currently: SharePoint, OneDrive, Google Drive, and Confluence). Please contact the Glean team to enable this for more datasources. Recursive memberships do not apply for Collections. | [optional] 
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


