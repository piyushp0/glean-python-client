# FeedbackCustomizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_channels** | [**List[FeedbackChannel]**](FeedbackChannel.md) | The channels to which feedback will be sent for any feature that does not have specific configuration. | [optional] 
**feature_channels** | **Dict[str, List[FeedbackChannel]]** | The channels to which feedback will be sent for individual features. The keys of the map will match the values in FeedbackFeature. Features not present in the map should use defaultChannels. | [optional] 
**disclaimer** | **str** | A custom message shown to users during the in-product feedback flow, e.g. to warn users against sending sensitive or personally-identifying information. | [optional] 
**company_privacy_policy_link** | **str** | An optional link to a privacy policy provided by the users&#39; company that will be shown to them during the in-product feedback flow if their company will receive their feedback. Glean&#39;s policy will also be shown if Glean is receiving the feedback. | [optional] 
**support_message** | **str** | User visible text shown when seeking support to guide them to their company&#39;s internal support page when appropriate | [optional] 
**support_link_text** | **str** | User visible text that will link to the user&#39;s company&#39;s internal support page | [optional] 
**support_link** | **str** | URL to the user&#39;s company&#39;s internal suport page | [optional] 

## Example

```python
from openapi_client.models.feedback_customizations import FeedbackCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackCustomizations from a JSON string
feedback_customizations_instance = FeedbackCustomizations.from_json(json)
# print the JSON string representation of the object
print(FeedbackCustomizations.to_json())

# convert the object into a dict
feedback_customizations_dict = feedback_customizations_instance.to_dict()
# create an instance of FeedbackCustomizations from a dict
feedback_customizations_from_dict = FeedbackCustomizations.from_dict(feedback_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


