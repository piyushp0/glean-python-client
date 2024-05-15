# PersonObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name. | 
**obfuscated_id** | **str** | An opaque identifier that can be used to request metadata for a Person. | 

## Example

```python
from openapi_client.models.person_object import PersonObject

# TODO update the JSON string below
json = "{}"
# create an instance of PersonObject from a JSON string
person_object_instance = PersonObject.from_json(json)
# print the JSON string representation of the object
print(PersonObject.to_json())

# convert the object into a dict
person_object_dict = person_object_instance.to_dict()
# create an instance of PersonObject from a dict
person_object_from_dict = PersonObject.from_dict(person_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


