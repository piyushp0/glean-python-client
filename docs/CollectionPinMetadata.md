# CollectionPinMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Collection. | 
**target** | [**CollectionPinTarget**](CollectionPinTarget.md) |  | 

## Example

```python
from openapi_client.models.collection_pin_metadata import CollectionPinMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionPinMetadata from a JSON string
collection_pin_metadata_instance = CollectionPinMetadata.from_json(json)
# print the JSON string representation of the object
print(CollectionPinMetadata.to_json())

# convert the object into a dict
collection_pin_metadata_dict = collection_pin_metadata_instance.to_dict()
# create an instance of CollectionPinMetadata from a dict
collection_pin_metadata_from_dict = CollectionPinMetadata.from_dict(collection_pin_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


