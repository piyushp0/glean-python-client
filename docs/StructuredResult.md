# StructuredResult

A single object that can support any object in the work graph. Only a single object will be populated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**Document**](Document.md) |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**custom_entity** | [**CustomEntity**](CustomEntity.md) |  | [optional] 
**answer** | [**Answer**](Answer.md) |  | [optional] 
**extracted_qn_a** | [**ExtractedQnA**](ExtractedQnA.md) |  | [optional] 
**app** | [**AppResult**](AppResult.md) |  | [optional] 
**collection** | [**Collection**](Collection.md) |  | [optional] 
**answer_board** | [**AnswerBoard**](AnswerBoard.md) |  | [optional] 
**code** | [**Code**](Code.md) |  | [optional] 
**shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**query_suggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**related_documents** | [**List[RelatedDocuments]**](RelatedDocuments.md) | A list of documents related to this structured result. | [optional] 
**related_question** | [**RelatedQuestion**](RelatedQuestion.md) |  | [optional] 
**snippets** | [**List[SearchResultSnippet]**](SearchResultSnippet.md) | Any snippets associated to the populated object. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**prominence** | **str** | The level of visual distinction that should be given to a result. | [optional] 
**source** | **str** | Source context for this result. Possible values depend on the result type. | [optional] 

## Example

```python
from openapi_client.models.structured_result import StructuredResult

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredResult from a JSON string
structured_result_instance = StructuredResult.from_json(json)
# print the JSON string representation of the object
print(StructuredResult.to_json())

# convert the object into a dict
structured_result_dict = structured_result_instance.to_dict()
# create an instance of StructuredResult from a dict
structured_result_from_dict = StructuredResult.from_dict(structured_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


