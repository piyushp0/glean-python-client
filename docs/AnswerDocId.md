# AnswerDocId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 

## Example

```python
from openapi_client.models.answer_doc_id import AnswerDocId

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerDocId from a JSON string
answer_doc_id_instance = AnswerDocId.from_json(json)
# print the JSON string representation of the object
print(AnswerDocId.to_json())

# convert the object into a dict
answer_doc_id_dict = answer_doc_id_instance.to_dict()
# create an instance of AnswerDocId from a dict
answer_doc_id_from_dict = AnswerDocId.from_dict(answer_doc_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


