# ShortcutInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shortcut** | [**Shortcut**](Shortcut.md) |  | 
**visit_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**visitor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.shortcut_insight import ShortcutInsight

# TODO update the JSON string below
json = "{}"
# create an instance of ShortcutInsight from a JSON string
shortcut_insight_instance = ShortcutInsight.from_json(json)
# print the JSON string representation of the object
print(ShortcutInsight.to_json())

# convert the object into a dict
shortcut_insight_dict = shortcut_insight_instance.to_dict()
# create an instance of ShortcutInsight from a dict
shortcut_insight_from_dict = ShortcutInsight.from_dict(shortcut_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


