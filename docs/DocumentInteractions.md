# DocumentInteractions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_comments** | **int** | The count of comments (thread replies in the case of slack). | [optional] 
**num_reactions** | **int** | The count of reactions on the document. | [optional] 
**reactions** | **List[str]** | To be deprecated in favor of reacts. A (potentially non-exhaustive) list of reactions for the document. | [optional] 
**reacts** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**shares** | [**List[Share]**](Share.md) | Describes instances of someone posting a link to this document in one of our indexed datasources. | [optional] 
**visitor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_interactions import DocumentInteractions

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInteractions from a JSON string
document_interactions_instance = DocumentInteractions.from_json(json)
# print the JSON string representation of the object
print(DocumentInteractions.to_json())

# convert the object into a dict
document_interactions_dict = document_interactions_instance.to_dict()
# create an instance of DocumentInteractions from a dict
document_interactions_from_dict = DocumentInteractions.from_dict(document_interactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


