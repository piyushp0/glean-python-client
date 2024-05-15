# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. | 
**domains** | **List[str]** | Link to company&#39;s associated website domains. | [optional] 
**company** | [**Company**](Company.md) |  | 
**document_counts** | **Dict[str, int]** | A map of {string, int} pairs representing counts of each document type associated with this customer. | [optional] 
**poc** | [**List[Person]**](Person.md) | A list of POC for company. | [optional] 
**metadata** | [**CustomerMetadata**](CustomerMetadata.md) |  | [optional] 
**merged_customers** | [**List[Customer]**](Customer.md) | A list of Customers. | [optional] 
**start_date** | **date** | The date when the interaction with customer started. | [optional] 
**contract_annual_revenue** | **float** | Average contract annual revenue with that customer. | [optional] 
**notes** | **str** | User facing (potentially generated) notes about company. | [optional] 

## Example

```python
from openapi_client.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


