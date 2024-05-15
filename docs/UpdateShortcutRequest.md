# UpdateShortcutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the user generated content. | 
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
from openapi_client.models.update_shortcut_request import UpdateShortcutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShortcutRequest from a JSON string
update_shortcut_request_instance = UpdateShortcutRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShortcutRequest.to_json())

# convert the object into a dict
update_shortcut_request_dict = update_shortcut_request_instance.to_dict()
# create an instance of UpdateShortcutRequest from a dict
update_shortcut_request_from_dict = UpdateShortcutRequest.from_dict(update_shortcut_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


