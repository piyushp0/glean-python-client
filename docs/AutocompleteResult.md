# AutocompleteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**keywords** | **List[str]** | A list of all possible keywords for given result. | [optional] 
**result_type** | **str** |  | [optional] 
**score** | **float** | Higher indicates a more confident match. | [optional] 
**operator_metadata** | [**OperatorMetadata**](OperatorMetadata.md) |  | [optional] 
**quicklink** | [**Quicklink**](Quicklink.md) |  | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**url** | **str** |  | [optional] 
**structured_result** | [**StructuredResult**](StructuredResult.md) |  | [optional] 
**tracking_token** | **str** | A token to be passed in /feedback events associated with this autocomplete result. | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | Subsections of the result string to which some special formatting should be applied (eg. bold) | [optional] 

## Example

```python
from openapi_client.models.autocomplete_result import AutocompleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteResult from a JSON string
autocomplete_result_instance = AutocompleteResult.from_json(json)
# print the JSON string representation of the object
print(AutocompleteResult.to_json())

# convert the object into a dict
autocomplete_result_dict = autocomplete_result_instance.to_dict()
# create an instance of AutocompleteResult from a dict
autocomplete_result_from_dict = AutocompleteResult.from_dict(autocomplete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


