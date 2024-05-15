# DocumentInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**Document**](Document.md) |  | 
**view_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**visitor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_insight import DocumentInsight

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInsight from a JSON string
document_insight_instance = DocumentInsight.from_json(json)
# print the JSON string representation of the object
print(DocumentInsight.to_json())

# convert the object into a dict
document_insight_dict = document_insight_instance.to_dict()
# create an instance of DocumentInsight from a dict
document_insight_from_dict = DocumentInsight.from_dict(document_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


