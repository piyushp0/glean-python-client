# ReferenceRange

Each text range from the response can correspond to an array of snippets from the citation source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_range** | [**TextRange**](TextRange.md) |  | 
**snippets** | [**List[SearchResultSnippet]**](SearchResultSnippet.md) |  | [optional] 

## Example

```python
from openapi_client.models.reference_range import ReferenceRange

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceRange from a JSON string
reference_range_instance = ReferenceRange.from_json(json)
# print the JSON string representation of the object
print(ReferenceRange.to_json())

# convert the object into a dict
reference_range_dict = reference_range_instance.to_dict()
# create an instance of ReferenceRange from a dict
reference_range_from_dict = ReferenceRange.from_dict(reference_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


