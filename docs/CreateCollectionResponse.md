# CreateCollectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the Collection. | 
**description** | **str** | A brief summary of the Collection&#39;s contents. | 
**added_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**removed_roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**icon** | **str** | The emoji icon of this Collection. | [optional] 
**admin_locked** | **bool** | Indicates whether edits are allowed for everyone or only admins. | [optional] 
**parent_id** | **int** | The parent of this Collection, or 0 if it&#39;s a top-level Collection. | [optional] 
**thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**allowed_datasource** | **str** | The datasource type this Collection can hold. | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**id** | **int** | The unique ID of the Collection. | 
**create_time** | **datetime** |  | [optional] 
**update_time** | **datetime** |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**item_count** | **int** | The number of items currently in the Collection. Separated from the actual items so we can grab the count without items. | [optional] 
**child_count** | **int** | The number of children Collections. Separated from the actual children so we can grab the count without children. | [optional] 
**items** | [**List[CollectionItem]**](CollectionItem.md) | The items in this Collection. | [optional] 
**pin_metadata** | [**CollectionPinnedMetadata**](CollectionPinnedMetadata.md) |  | [optional] 
**shortcuts** | **List[str]** | The names of the shortcuts (Go Links) that point to this Collection. | [optional] 
**children** | [**List[Collection]**](Collection.md) | The children Collections of this Collection. | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of user roles for the Collection. | [optional] 
**error_code** | **str** |  | 
**collection** | [**Collection**](Collection.md) |  | [optional] 
**error** | [**CollectionError**](CollectionError.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_collection_response import CreateCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionResponse from a JSON string
create_collection_response_instance = CreateCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionResponse.to_json())

# convert the object into a dict
create_collection_response_dict = create_collection_response_instance.to_dict()
# create an instance of CreateCollectionResponse from a dict
create_collection_response_from_dict = CreateCollectionResponse.from_dict(create_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


