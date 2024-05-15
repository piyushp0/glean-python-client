# DisplayableList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The type of data that backs this displayable list | [optional] 
**id** | **int** | Unique identifier of this list. Unique amongst only DisplayableLists, not unique amongst other types of UGC. | [optional] 
**source_id** | **str** | Unstructured identifier for the source to render (ID, URL, query). | [optional] 
**config** | [**DisplayableListConfig**](DisplayableListConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.displayable_list import DisplayableList

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayableList from a JSON string
displayable_list_instance = DisplayableList.from_json(json)
# print the JSON string representation of the object
print(DisplayableList.to_json())

# convert the object into a dict
displayable_list_dict = displayable_list_instance.to_dict()
# create an instance of DisplayableList from a dict
displayable_list_from_dict = DisplayableList.from_dict(displayable_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


