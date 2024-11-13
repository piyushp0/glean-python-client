# AdminAlertEmailTemplateProperties

Non-specific fields of an admin alert email template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_type** | **str** | Banner type to display for this alert | [optional] 
**banner_text** | **str** | Text to display for the alert banner | [optional] 
**alert_description** | **str** | Text for what happened section of an admin alert. | [optional] 
**relevance_description** | **str** | Text for why this matters section of an admin alert. | [optional] 
**resolution_steps_description** | **str** | Text for to do section before actual steps. | [optional] 
**resolution_steps** | [**List[ResolutionStep]**](ResolutionStep.md) | Steps to take to resolve an alert which are optionally mapped to a link for instructions (e.g. help doc) | [optional] 
**help_link** | **str** | Help link for the alert that the admin can reference | [optional] 

## Example

```python
from openapi_client.models.admin_alert_email_template_properties import AdminAlertEmailTemplateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AdminAlertEmailTemplateProperties from a JSON string
admin_alert_email_template_properties_instance = AdminAlertEmailTemplateProperties.from_json(json)
# print the JSON string representation of the object
print(AdminAlertEmailTemplateProperties.to_json())

# convert the object into a dict
admin_alert_email_template_properties_dict = admin_alert_email_template_properties_instance.to_dict()
# create an instance of AdminAlertEmailTemplateProperties from a dict
admin_alert_email_template_properties_from_dict = AdminAlertEmailTemplateProperties.from_dict(admin_alert_email_template_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


