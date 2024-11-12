# openapi_client.CalendarApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getevents**](CalendarApi.md#getevents) | **POST** /getevents | Read events


# **getevents**
> GetEventsResponse getevents(payload, x_scio_actas=x_scio_actas)

Read events

Read detailed information about the given event ids.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_events_request import GetEventsRequest
from openapi_client.models.get_events_response import GetEventsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://domain-be.glean.com/rest/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://domain-be.glean.com/rest/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarApi(api_client)
    payload = openapi_client.GetEventsRequest() # GetEventsRequest | GetEvents request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read events
        api_response = api_instance.getevents(payload, x_scio_actas=x_scio_actas)
        print("The response of CalendarApi->getevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->getevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetEventsRequest**](GetEventsRequest.md)| GetEvents request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetEventsResponse**](GetEventsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

