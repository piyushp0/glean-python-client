# CollectionItemMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The optional name of the Collection item. | [optional] 
**description** | **str** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**icon** | **str** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Example

```python
from openapi_client.models.collection_item_mutable_properties import CollectionItemMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionItemMutableProperties from a JSON string
collection_item_mutable_properties_instance = CollectionItemMutableProperties.from_json(json)
# print the JSON string representation of the object
print(CollectionItemMutableProperties.to_json())

# convert the object into a dict
collection_item_mutable_properties_dict = collection_item_mutable_properties_instance.to_dict()
# create an instance of CollectionItemMutableProperties from a dict
collection_item_mutable_properties_from_dict = CollectionItemMutableProperties.from_dict(collection_item_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


