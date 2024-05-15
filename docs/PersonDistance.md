# PersonDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name. | 
**obfuscated_id** | **str** | An opaque identifier that can be used to request metadata for a Person. | 
**distance** | **float** | Distance to person, refer to PeopleDistance pipeline on interpretation of the value. | 

## Example

```python
from openapi_client.models.person_distance import PersonDistance

# TODO update the JSON string below
json = "{}"
# create an instance of PersonDistance from a JSON string
person_distance_instance = PersonDistance.from_json(json)
# print the JSON string representation of the object
print(PersonDistance.to_json())

# convert the object into a dict
person_distance_dict = person_distance_instance.to_dict()
# create an instance of PersonDistance from a dict
person_distance_from_dict = PersonDistance.from_dict(person_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


