# ShortcutMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_alias** | **str** | Link text following go/ prefix as entered by the user. | [optional] 
**destination_url** | **str** | Destination URL for the shortcut. | [optional] 
**destination_document_id** | **str** | Glean Document ID for the URL, if known. | [optional] 
**description** | **str** | A short, plain text blurb to help people understand the intent of the shortcut. | [optional] 
**unlisted** | **bool** | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only. | [optional] 
**url_template** | **str** | For variable shortcuts, contains the URL template; note, &#x60;destinationUrl&#x60; contains default URL. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles added for the Shortcut. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles removed for the Shortcut. | [optional] 

## Example

```python
from openapi_client.models.shortcut_mutable_properties import ShortcutMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutMutableProperties from a JSON string
shortcut_mutable_properties_instance = ShortcutMutableProperties.from_json(json)
# print the JSON string representation of the object
print(ShortcutMutableProperties.to_json())

# convert the object into a dict
shortcut_mutable_properties_dict = shortcut_mutable_properties_instance.to_dict()
# create an instance of ShortcutMutableProperties from a dict
shortcut_mutable_properties_from_dict = ShortcutMutableProperties.from_dict(shortcut_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


