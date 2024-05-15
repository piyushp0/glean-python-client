# CreateCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the Collection. | 
**description** | **str** | A brief summary of the Collection&#39;s contents. | [optional] 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**icon** | **str** | The emoji icon of this Collection. | [optional] 
**admin_locked** | **bool** | Indicates whether edits are allowed for everyone or only admins. | [optional] 
**parent_id** | **int** | The parent of this Collection, or 0 if it&#39;s a top-level Collection. | [optional] 
**thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**allowed_datasource** | **str** | The datasource type this Collection can hold. | [optional] 
**new_next_item_id** | **str** | The (optional) ItemId of the next CollectionItem in sequence. If omitted, will be added to the end of the Collection. Only used if parentId is specified. | [optional] 

## Example

```python
from openapi_client.models.create_collection_request import CreateCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionRequest from a JSON string
create_collection_request_instance = CreateCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionRequest.to_json())

# convert the object into a dict
create_collection_request_dict = create_collection_request_instance.to_dict()
# create an instance of CreateCollectionRequest from a dict
create_collection_request_from_dict = CreateCollectionRequest.from_dict(create_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


