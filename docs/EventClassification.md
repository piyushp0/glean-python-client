# EventClassification

A generated classification of a given event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**EventClassificationName**](EventClassificationName.md) |  | [optional] 
**strategies** | [**List[EventStrategyName]**](EventStrategyName.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_classification import EventClassification

# TODO update the JSON string below
json = "{}"
# create an instance of EventClassification from a JSON string
event_classification_instance = EventClassification.from_json(json)
# print the JSON string representation of the object
print(EventClassification.to_json())

# convert the object into a dict
event_classification_dict = event_classification_instance.to_dict()
# create an instance of EventClassification from a dict
event_classification_from_dict = EventClassification.from_dict(event_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


