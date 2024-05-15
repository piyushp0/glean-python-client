# SessionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_tracking_token** | **str** | A unique token for this session. A new session (and token) is created when the user issues a request from a new tab or when our server hasn&#39;t seen activity for more than 10 minutes from a tab. | [optional] 
**tab_id** | **str** | A unique id for all requests a user makes from a given tab, no matter how far apart. A new tab id is only generated when a user issues a request from a new tab. | [optional] 
**last_seen** | **datetime** | The last time the server saw this token. | [optional] 
**last_query** | **str** | The last query seen by the server. | [optional] 

## Example

```python
from openapi_client.models.session_info import SessionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInfo from a JSON string
session_info_instance = SessionInfo.from_json(json)
# print the JSON string representation of the object
print(SessionInfo.to_json())

# convert the object into a dict
session_info_dict = session_info_instance.to_dict()
# create an instance of SessionInfo from a dict
session_info_from_dict = SessionInfo.from_dict(session_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


