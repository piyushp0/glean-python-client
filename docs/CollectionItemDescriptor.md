# CollectionItemDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the item being added. | [optional] 
**document_id** | **str** | The Glean Document ID of the item being added if it&#39;s an indexed document. | [optional] 
**new_next_item_id** | **str** | The (optional) ItemId of the next CollectionItem in sequence. If omitted, will be added to the end of the Collection | [optional] 
**item_type** | **str** |  | [optional] 
**name** | **str** | The optional name of the Collection item. | [optional] 
**description** | **str** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**icon** | **str** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Example

```python
from openapi_client.models.collection_item_descriptor import CollectionItemDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionItemDescriptor from a JSON string
collection_item_descriptor_instance = CollectionItemDescriptor.from_json(json)
# print the JSON string representation of the object
print(CollectionItemDescriptor.to_json())

# convert the object into a dict
collection_item_descriptor_dict = collection_item_descriptor_instance.to_dict()
# create an instance of CollectionItemDescriptor from a dict
collection_item_descriptor_from_dict = CollectionItemDescriptor.from_dict(collection_item_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


