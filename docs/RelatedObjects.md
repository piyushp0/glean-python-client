# RelatedObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_objects** | [**Dict[str, RelatedObjectEdge]**](RelatedObjectEdge.md) | A list of objects related to a source object. | [optional] 

## Example

```python
from openapi_client.models.related_objects import RelatedObjects

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedObjects from a JSON string
related_objects_instance = RelatedObjects.from_json(json)
# print the JSON string representation of the object
print(RelatedObjects.to_json())

# convert the object into a dict
related_objects_dict = related_objects_instance.to_dict()
# create an instance of RelatedObjects from a dict
related_objects_from_dict = RelatedObjects.from_dict(related_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


