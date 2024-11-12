# GeneratedQna


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Search query rephrased into a question. | [optional] 
**answer** | **str** | Answer generated for the given query or the generated question. | [optional] 
**follow_up_prompts** | **List[str]** | List of all follow-up prompts generated for the given query or the generated question. | [optional] 
**followup_actions** | [**List[FollowupAction]**](FollowupAction.md) | List of follow-up actions generated for the given query or the generated question. | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | Answer subsections to mark with special formatting (citations, bolding etc) | [optional] 
**status** | **str** | Status of backend generating the answer | [optional] 
**cursor** | **str** | An opaque cursor representing the search request | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 

## Example

```python
from openapi_client.models.generated_qna import GeneratedQna

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedQna from a JSON string
generated_qna_instance = GeneratedQna.from_json(json)
# print the JSON string representation of the object
print(GeneratedQna.to_json())

# convert the object into a dict
generated_qna_dict = generated_qna_instance.to_dict()
# create an instance of GeneratedQna from a dict
generated_qna_from_dict = GeneratedQna.from_dict(generated_qna_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


