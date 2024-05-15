# VerificationFeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Verification]**](Verification.md) | List of document infos that include verification related information for them. | [optional] 

## Example

```python
from openapi_client.models.verification_feed import VerificationFeed

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationFeed from a JSON string
verification_feed_instance = VerificationFeed.from_json(json)
# print the JSON string representation of the object
print(VerificationFeed.to_json())

# convert the object into a dict
verification_feed_dict = verification_feed_instance.to_dict()
# create an instance of VerificationFeed from a dict
verification_feed_from_dict = VerificationFeed.from_dict(verification_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


