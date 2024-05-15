# DocumentSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the document section (e.g. the section header). | [optional] 
**url** | **str** | The permalink of the document section. | [optional] 

## Example

```python
from openapi_client.models.document_section import DocumentSection

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSection from a JSON string
document_section_instance = DocumentSection.from_json(json)
# print the JSON string representation of the object
print(DocumentSection.to_json())

# convert the object into a dict
document_section_dict = document_section_instance.to_dict()
# create an instance of DocumentSection from a dict
document_section_from_dict = DocumentSection.from_dict(document_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


