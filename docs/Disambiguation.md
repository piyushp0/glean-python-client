# Disambiguation

A disambiguation between multiple entities with the same name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the ambiguous entity | [optional] 
**id** | **str** | The unique id of the entity in the knowledge graph | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 

## Example

```python
from openapi_client.models.disambiguation import Disambiguation

# TODO update the JSON string below
json = "{}"
# create an instance of Disambiguation from a JSON string
disambiguation_instance = Disambiguation.from_json(json)
# print the JSON string representation of the object
print(Disambiguation.to_json())

# convert the object into a dict
disambiguation_dict = disambiguation_instance.to_dict()
# create an instance of Disambiguation from a dict
disambiguation_from_dict = Disambiguation.from_dict(disambiguation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


