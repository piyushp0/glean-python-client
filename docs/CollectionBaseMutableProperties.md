# CollectionBaseMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the Collection. | 
**description** | **str** | A brief summary of the Collection&#39;s contents. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 

## Example

```python
from openapi_client.models.collection_base_mutable_properties import CollectionBaseMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionBaseMutableProperties from a JSON string
collection_base_mutable_properties_instance = CollectionBaseMutableProperties.from_json(json)
# print the JSON string representation of the object
print(CollectionBaseMutableProperties.to_json())

# convert the object into a dict
collection_base_mutable_properties_dict = collection_base_mutable_properties_instance.to_dict()
# create an instance of CollectionBaseMutableProperties from a dict
collection_base_mutable_properties_from_dict = CollectionBaseMutableProperties.from_dict(collection_base_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


