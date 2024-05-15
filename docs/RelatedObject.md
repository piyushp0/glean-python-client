# RelatedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the related object | 
**metadata** | [**RelatedObjectMetadata**](RelatedObjectMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.related_object import RelatedObject

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedObject from a JSON string
related_object_instance = RelatedObject.from_json(json)
# print the JSON string representation of the object
print(RelatedObject.to_json())

# convert the object into a dict
related_object_dict = related_object_instance.to_dict()
# create an instance of RelatedObject from a dict
related_object_from_dict = RelatedObject.from_dict(related_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


