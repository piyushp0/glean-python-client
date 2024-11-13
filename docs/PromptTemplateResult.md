# PromptTemplateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_template** | [**PromptTemplate**](PromptTemplate.md) |  | [optional] 
**tracking_token** | **str** | An opaque token that represents this prompt template | [optional] 
**favorite_info** | [**FavoriteInfo**](FavoriteInfo.md) |  | [optional] 
**run_count** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.prompt_template_result import PromptTemplateResult

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplateResult from a JSON string
prompt_template_result_instance = PromptTemplateResult.from_json(json)
# print the JSON string representation of the object
print(PromptTemplateResult.to_json())

# convert the object into a dict
prompt_template_result_dict = prompt_template_result_instance.to_dict()
# create an instance of PromptTemplateResult from a dict
prompt_template_result_from_dict = PromptTemplateResult.from_dict(prompt_template_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


