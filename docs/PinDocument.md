# PinDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | The query strings for which the pinned result will show. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 
**id** | **str** | The opaque id of the pin. | [optional] 
**document_id** | **str** | The document which should be a pinned result. | 
**attribution** | [**Person**](Person.md) |  | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**update_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.pin_document import PinDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PinDocument from a JSON string
pin_document_instance = PinDocument.from_json(json)
# print the JSON string representation of the object
print(PinDocument.to_json())

# convert the object into a dict
pin_document_dict = pin_document_instance.to_dict()
# create an instance of PinDocument from a dict
pin_document_from_dict = PinDocument.from_dict(pin_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


