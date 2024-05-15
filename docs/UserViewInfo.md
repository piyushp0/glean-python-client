# UserViewInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** | Unique Glean Document ID of the associated document. | [optional] 
**doc_title** | **str** | Title of associated document. | [optional] 
**doc_url** | **str** | URL of associated document. | [optional] 

## Example

```python
from openapi_client.models.user_view_info import UserViewInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserViewInfo from a JSON string
user_view_info_instance = UserViewInfo.from_json(json)
# print the JSON string representation of the object
print(UserViewInfo.to_json())

# convert the object into a dict
user_view_info_dict = user_view_info_instance.to_dict()
# create an instance of UserViewInfo from a dict
user_view_info_from_dict = UserViewInfo.from_dict(user_view_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


