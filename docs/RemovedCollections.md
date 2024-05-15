# RemovedCollections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_collections** | **List[int]** | IDs of Collections from which a document is removed. | [optional] 

## Example

```python
from openapi_client.models.removed_collections import RemovedCollections

# TODO update the JSON string below
json = "{}"
# create an instance of RemovedCollections from a JSON string
removed_collections_instance = RemovedCollections.from_json(json)
# print the JSON string representation of the object
print(RemovedCollections.to_json())

# convert the object into a dict
removed_collections_dict = removed_collections_instance.to_dict()
# create an instance of RemovedCollections from a dict
removed_collections_from_dict = RemovedCollections.from_dict(removed_collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


