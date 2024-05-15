# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name. | 
**obfuscated_id** | **str** | An opaque identifier that can be used to request metadata for a Person. | 
**related_documents** | [**List[RelatedDocuments]**](RelatedDocuments.md) | A list of documents related to this person. | [optional] 
**metadata** | [**PersonMetadata**](PersonMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


