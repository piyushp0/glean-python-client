# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-friendly display name. | 
**profile_url** | **str** | Link to internal company company profile. | [optional] 
**website_urls** | **List[str]** | Link to company&#39;s associated websites. | [optional] 
**logo_url** | **str** | The URL of the company&#39;s logo. Public, Glean-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**location** | **str** | User facing string representing the company&#39;s location. | [optional] 
**phone** | **str** | Phone number as a number string. | [optional] 
**fax** | **str** | Fax number as a number string. | [optional] 
**industry** | **str** | User facing string representing the company&#39;s industry. | [optional] 
**annual_revenue** | **float** | Average company&#39;s annual revenue for reference. | [optional] 
**number_of_employees** | **int** | Average company&#39;s number of employees for reference. | [optional] 
**stock_symbol** | **str** | Company&#39;s stock symbol if company is public. | [optional] 
**founded_date** | **date** | The date when the company was founded. | [optional] 
**about** | **str** | User facing description of company. | [optional] 

## Example

```python
from openapi_client.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


