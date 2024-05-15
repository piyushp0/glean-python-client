# Shortcut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The opaque id of the user generated content. | [optional] 
**input_alias** | **str** | Link text following go/ prefix as entered by the user. | 
**destination_url** | **str** | Destination URL for the shortcut. | [optional] 
**destination_document_id** | **str** | Glean Document ID for the URL, if known. | [optional] 
**description** | **str** | A short, plain text blurb to help people understand the intent of the shortcut. | [optional] 
**unlisted** | **bool** | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only. | [optional] 
**url_template** | **str** | For variable shortcuts, contains the URL template; note, &#x60;destinationUrl&#x60; contains default URL. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles added for the Shortcut. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles removed for the Shortcut. | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**created_by** | [**Person**](Person.md) |  | [optional] 
**create_time** | **datetime** | The time the shortcut was created in ISO format (ISO 8601). | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**update_time** | **datetime** | The time the shortcut was updated in ISO format (ISO 8601). | [optional] 
**destination_document** | [**Document**](Document.md) |  | [optional] 
**intermediate_url** | **str** | The URL from which the user is then redirected to the destination URL. Full replacement for https://go/&lt;inputAlias&gt;. | [optional] 
**view_prefix** | **str** | The part of the shortcut preceding the input alias when used for showing shortcuts to users. Should end with \&quot;/\&quot;. e.g. \&quot;go/\&quot; for native shortcuts. | [optional] 
**is_external** | **bool** | Indicates whether a shortcut is native or external. | [optional] 
**edit_url** | **str** | The URL using which the user can access the edit page of the shortcut. | [optional] 
**alias** | **str** | canonical link text following go/ prefix where hyphen/underscore is removed. | [optional] 
**title** | **str** | Title for the Go Link | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the Go Link. | [optional] 

## Example

```python
from openapi_client.models.shortcut import Shortcut

# TODO update the JSON string below
json = "{}"
# create an instance of Shortcut from a JSON string
shortcut_instance = Shortcut.from_json(json)
# print the JSON string representation of the object
print(Shortcut.to_json())

# convert the object into a dict
shortcut_dict = shortcut_instance.to_dict()
# create an instance of Shortcut from a dict
shortcut_from_dict = Shortcut.from_dict(shortcut_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


