# RelatedObjectMetadata

Some metadata of the object which can be displayed, while not having the actual object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Placeholder name of the object, not the relationship. | [optional] 

## Example

```python
from openapi_client.models.related_object_metadata import RelatedObjectMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedObjectMetadata from a JSON string
related_object_metadata_instance = RelatedObjectMetadata.from_json(json)
# print the JSON string representation of the object
print(RelatedObjectMetadata.to_json())

# convert the object into a dict
related_object_metadata_dict = related_object_metadata_instance.to_dict()
# create an instance of RelatedObjectMetadata from a dict
related_object_metadata_from_dict = RelatedObjectMetadata.from_dict(related_object_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


