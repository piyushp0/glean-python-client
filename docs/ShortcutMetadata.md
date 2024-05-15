# ShortcutMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**Person**](Person.md) |  | [optional] 
**create_time** | **datetime** | The time the shortcut was created in ISO format (ISO 8601). | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**update_time** | **datetime** | The time the shortcut was updated in ISO format (ISO 8601). | [optional] 
**destination_document** | [**Document**](Document.md) |  | [optional] 
**intermediate_url** | **str** | The URL from which the user is then redirected to the destination URL. Full replacement for https://go/&lt;inputAlias&gt;. | [optional] 
**view_prefix** | **str** | The part of the shortcut preceding the input alias when used for showing shortcuts to users. Should end with \&quot;/\&quot;. e.g. \&quot;go/\&quot; for native shortcuts. | [optional] 
**is_external** | **bool** | Indicates whether a shortcut is native or external. | [optional] 
**edit_url** | **str** | The URL using which the user can access the edit page of the shortcut. | [optional] 

## Example

```python
from openapi_client.models.shortcut_metadata import ShortcutMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutMetadata from a JSON string
shortcut_metadata_instance = ShortcutMetadata.from_json(json)
# print the JSON string representation of the object
print(ShortcutMetadata.to_json())

# convert the object into a dict
shortcut_metadata_dict = shortcut_metadata_instance.to_dict()
# create an instance of ShortcutMetadata from a dict
shortcut_metadata_from_dict = ShortcutMetadata.from_dict(shortcut_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


