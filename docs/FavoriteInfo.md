# FavoriteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ugc_type** | [**UgcType**](UgcType.md) |  | [optional] 
**id** | **str** | Opaque id of the UGC. | [optional] 
**count** | **int** | Number of users this object has been favorited by. | [optional] 
**favorited_by_user** | **bool** | If the requesting user has favorited this object. | [optional] 

## Example

```python
from openapi_client.models.favorite_info import FavoriteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteInfo from a JSON string
favorite_info_instance = FavoriteInfo.from_json(json)
# print the JSON string representation of the object
print(FavoriteInfo.to_json())

# convert the object into a dict
favorite_info_dict = favorite_info_instance.to_dict()
# create an instance of FavoriteInfo from a dict
favorite_info_from_dict = FavoriteInfo.from_dict(favorite_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


