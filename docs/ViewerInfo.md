# ViewerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | DEPRECATED - use permissions instead. Viewer&#39;s role on the specific document. | [optional] 
**last_viewed_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.viewer_info import ViewerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerInfo from a JSON string
viewer_info_instance = ViewerInfo.from_json(json)
# print the JSON string representation of the object
print(ViewerInfo.to_json())

# convert the object into a dict
viewer_info_dict = viewer_info_instance.to_dict()
# create an instance of ViewerInfo from a dict
viewer_info_from_dict = ViewerInfo.from_dict(viewer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


