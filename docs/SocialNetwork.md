# SocialNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Possible values are \&quot;twitter\&quot;, \&quot;linkedin\&quot;. | 
**profile_name** | **str** | Human-readable profile name. | [optional] 
**profile_url** | **str** | Link to profile. | 

## Example

```python
from openapi_client.models.social_network import SocialNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of SocialNetwork from a JSON string
social_network_instance = SocialNetwork.from_json(json)
# print the JSON string representation of the object
print(SocialNetwork.to_json())

# convert the object into a dict
social_network_dict = social_network_instance.to_dict()
# create an instance of SocialNetwork from a dict
social_network_from_dict = SocialNetwork.from_dict(social_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


