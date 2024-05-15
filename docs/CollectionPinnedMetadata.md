# CollectionPinnedMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_pins** | [**List[CollectionPinTarget]**](CollectionPinTarget.md) | List of targets this Collection is pinned to. | [optional] 
**eligible_pins** | [**List[CollectionPinMetadata]**](CollectionPinMetadata.md) | List of targets this Collection can be pinned to, excluding the targets this Collection is already pinned to. We also include Collection ID already is pinned to each eligible target, which will be 0 if the target has no pinned Collection. | [optional] 

## Example

```python
from openapi_client.models.collection_pinned_metadata import CollectionPinnedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionPinnedMetadata from a JSON string
collection_pinned_metadata_instance = CollectionPinnedMetadata.from_json(json)
# print the JSON string representation of the object
print(CollectionPinnedMetadata.to_json())

# convert the object into a dict
collection_pinned_metadata_dict = collection_pinned_metadata_instance.to_dict()
# create an instance of CollectionPinnedMetadata from a dict
collection_pinned_metadata_from_dict = CollectionPinnedMetadata.from_dict(collection_pinned_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


