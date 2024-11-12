# EditDocumentCollectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_collections** | **List[int]** | IDs of Collections to which a document is added. | [optional] 
**removed_collections** | **List[int]** | IDs of Collections from which a document is removed. | [optional] 
**document_id** | **str** | The Glean Document ID of the item being added to or removed from Collections if it&#39;s an indexed document. | [optional] 
**url** | **str** | The URL of the item being added to or removed from Collections. | [optional] 
**name** | **str** | Custom title of the document if adding a non-indexed URL. | [optional] 
**description** | **str** | The description of this CollectionItem. | [optional] 

## Example

```python
from openapi_client.models.edit_document_collections_request import EditDocumentCollectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDocumentCollectionsRequest from a JSON string
edit_document_collections_request_instance = EditDocumentCollectionsRequest.from_json(json)
# print the JSON string representation of the object
print(EditDocumentCollectionsRequest.to_json())

# convert the object into a dict
edit_document_collections_request_dict = edit_document_collections_request_instance.to_dict()
# create an instance of EditDocumentCollectionsRequest from a dict
edit_document_collections_request_from_dict = EditDocumentCollectionsRequest.from_dict(edit_document_collections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


