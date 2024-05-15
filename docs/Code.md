# Code


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_name** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 
**lines** | [**List[CodeLine]**](CodeLine.md) |  | [optional] 
**is_last_match** | **bool** | Last file match for a repo | [optional] 

## Example

```python
from openapi_client.models.code import Code

# TODO update the JSON string below
json = "{}"
# create an instance of Code from a JSON string
code_instance = Code.from_json(json)
# print the JSON string representation of the object
print(Code.to_json())

# convert the object into a dict
code_dict = code_instance.to_dict()
# create an instance of Code from a dict
code_from_dict = Code.from_dict(code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


