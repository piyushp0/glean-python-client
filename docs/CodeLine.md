# CodeLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | Index ranges depicting matched sections of the line | [optional] 

## Example

```python
from openapi_client.models.code_line import CodeLine

# TODO update the JSON string below
json = "{}"
# create an instance of CodeLine from a JSON string
code_line_instance = CodeLine.from_json(json)
# print the JSON string representation of the object
print(CodeLine.to_json())

# convert the object into a dict
code_line_dict = code_line_instance.to_dict()
# create an instance of CodeLine from a dict
code_line_from_dict = CodeLine.from_dict(code_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


