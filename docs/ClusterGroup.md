# ClusterGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clustered_results** | [**List[SearchResult]**](SearchResult.md) | A list of results that should be displayed as associated with this result. | [optional] 
**cluster_type** | [**ClusterTypeEnum**](ClusterTypeEnum.md) |  | [optional] 
**visible_count_hint** | **int** | The default number of results to display before truncating and showing a \&quot;see more\&quot; link | 

## Example

```python
from openapi_client.models.cluster_group import ClusterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroup from a JSON string
cluster_group_instance = ClusterGroup.from_json(json)
# print the JSON string representation of the object
print(ClusterGroup.to_json())

# convert the object into a dict
cluster_group_dict = cluster_group_instance.to_dict()
# create an instance of ClusterGroup from a dict
cluster_group_from_dict = ClusterGroup.from_dict(cluster_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


