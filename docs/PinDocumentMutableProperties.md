# PinDocumentMutableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | The query strings for which the pinned result will show. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 

## Example

```python
from openapi_client.models.pin_document_mutable_properties import PinDocumentMutableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PinDocumentMutableProperties from a JSON string
pin_document_mutable_properties_instance = PinDocumentMutableProperties.from_json(json)
# print the JSON string representation of the object
print(PinDocumentMutableProperties.to_json())

# convert the object into a dict
pin_document_mutable_properties_dict = pin_document_mutable_properties_instance.to_dict()
# create an instance of PinDocumentMutableProperties from a dict
pin_document_mutable_properties_from_dict = PinDocumentMutableProperties.from_dict(pin_document_mutable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


