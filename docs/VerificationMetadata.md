# VerificationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_verifier** | [**Person**](Person.md) |  | [optional] 
**last_verification_ts** | **int** | The unix timestamp of the verification (in seconds since epoch UTC). | [optional] 
**expiration_ts** | **int** | The unix timestamp of the verification expiration if applicable (in seconds since epoch UTC). | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**reminders** | [**List[Reminder]**](Reminder.md) | Info about all outstanding verification reminders for the document if exists. | [optional] 
**last_reminder** | [**Reminder**](Reminder.md) |  | [optional] 
**visitor_count** | [**List[CountInfo]**](CountInfo.md) | Number of visitors to the document during included time periods. | [optional] 
**candidate_verifiers** | [**List[Person]**](Person.md) | List of potential verifiers for the document e.g. old verifiers and/or users with view/edit permissions. | [optional] 

## Example

```python
from openapi_client.models.verification_metadata import VerificationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationMetadata from a JSON string
verification_metadata_instance = VerificationMetadata.from_json(json)
# print the JSON string representation of the object
print(VerificationMetadata.to_json())

# convert the object into a dict
verification_metadata_dict = verification_metadata_instance.to_dict()
# create an instance of VerificationMetadata from a dict
verification_metadata_from_dict = VerificationMetadata.from_dict(verification_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


