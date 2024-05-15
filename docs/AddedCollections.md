# AddedCollections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_collections** | **List[int]** | IDs of Collections to which a document is added. | [optional] 

## Example

```python
from openapi_client.models.added_collections import AddedCollections

# TODO update the JSON string below
json = "{}"
# create an instance of AddedCollections from a JSON string
added_collections_instance = AddedCollections.from_json(json)
# print the JSON string representation of the object
print(AddedCollections.to_json())

# convert the object into a dict
added_collections_dict = added_collections_instance.to_dict()
# create an instance of AddedCollections from a dict
added_collections_from_dict = AddedCollections.from_dict(added_collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


