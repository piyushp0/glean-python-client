# ListShortcutsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcuts** | [**List[Shortcut]**](Shortcut.md) | List of all shortcuts accessible to the user | 
**facet_results** | [**List[FacetResult]**](FacetResult.md) |  | [optional] 
**meta** | [**ShortcutsPaginationMetadata**](ShortcutsPaginationMetadata.md) |  | 

## Example

```python
from openapi_client.models.list_shortcuts_paginated_response import ListShortcutsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListShortcutsPaginatedResponse from a JSON string
list_shortcuts_paginated_response_instance = ListShortcutsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ListShortcutsPaginatedResponse.to_json())

# convert the object into a dict
list_shortcuts_paginated_response_dict = list_shortcuts_paginated_response_instance.to_dict()
# create an instance of ListShortcutsPaginatedResponse from a dict
list_shortcuts_paginated_response_from_dict = ListShortcutsPaginatedResponse.from_dict(list_shortcuts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


