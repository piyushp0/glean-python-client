# SearchRequestInputDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_copy_paste** | **bool** | Whether the associated query was at least partially copy-pasted.  If subsequent requests are issued after a copy-pasted query is constructed (e.g. with facet modifications), this bit should continue to be set for those requests. | [optional] 

## Example

```python
from openapi_client.models.search_request_input_details import SearchRequestInputDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestInputDetails from a JSON string
search_request_input_details_instance = SearchRequestInputDetails.from_json(json)
# print the JSON string representation of the object
print(SearchRequestInputDetails.to_json())

# convert the object into a dict
search_request_input_details_dict = search_request_input_details_instance.to_dict()
# create an instance of SearchRequestInputDetails from a dict
search_request_input_details_from_dict = SearchRequestInputDetails.from_dict(search_request_input_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


