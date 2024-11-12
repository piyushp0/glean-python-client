# openapi_client.ToolsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executeactiontool**](ToolsApi.md#executeactiontool) | **POST** /executeactiontool | Execute Action Tool


# **executeactiontool**
> ExecuteActionToolResponse executeactiontool(payload, timezone_offset=timezone_offset)

Execute Action Tool

Executes an Action tool with the specified parameters.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.execute_action_tool_request import ExecuteActionToolRequest
from openapi_client.models.execute_action_tool_response import ExecuteActionToolResponse
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
    api_instance = openapi_client.ToolsApi(api_client)
    payload = openapi_client.ExecuteActionToolRequest() # ExecuteActionToolRequest | Execute Action Tool request
    timezone_offset = 56 # int | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

    try:
        # Execute Action Tool
        api_response = api_instance.executeactiontool(payload, timezone_offset=timezone_offset)
        print("The response of ToolsApi->executeactiontool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->executeactiontool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ExecuteActionToolRequest**](ExecuteActionToolRequest.md)| Execute Action Tool request | 
 **timezone_offset** | **int**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**ExecuteActionToolResponse**](ExecuteActionToolResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

