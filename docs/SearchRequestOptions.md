# SearchRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_filter** | **str** | Filter results to a single datasource name (e.g. gmail, slack). All results are returned if missing. | [optional] 
**datasources_filter** | **List[str]** | Filter results to one or more datasources (e.g. gmail, slack). All results are returned if missing. | [optional] 
**query_overrides_facet_filters** | **bool** | If true, the operators in the query are taken to override any operators in facetFilters in the case of conflict. This is used to correctly set rewrittenFacetFilters and rewrittenQuery. | [optional] 
**facet_filters** | [**List[FacetFilter]**](FacetFilter.md) | A list of filters for the query. An AND is assumed between different facetFilters. For example, owner Sumeet and type Spreadsheet shows documents that are by Sumeet AND are Spreadsheets. | [optional] 
**facet_filter_sets** | [**List[FacetFilterSet]**](FacetFilterSet.md) | A list of facet filter sets that will be OR&#39;ed together. SearchRequestOptions where both facetFilterSets and facetFilters set are considered as bad request. Callers should set only one of these fields. | [optional] 
**facet_bucket_filter** | [**FacetBucketFilter**](FacetBucketFilter.md) |  | [optional] 
**facet_bucket_size** | **int** | The maximum number of FacetBuckets to return in each FacetResult. | 
**default_facets** | **List[str]** | Facets for which FacetResults should be fetched and that don&#39;t apply to a particular datasource. If specified, these values will replace the standard default facets (last_updated_at, from, etc.). The requested facets will be returned alongside datasource-specific facets if searching a single datasource. | [optional] 
**auth_tokens** | [**List[AuthToken]**](AuthToken.md) | Auth tokens which may be used for non-indexed, federated results (e.g. Gmail). | [optional] 
**fetch_all_datasource_counts** | **bool** | Hints that the QE should return result counts (via the datasource facet result) for all supported datasources, rather than just those specified in the datasource[s]Filter | [optional] 
**response_hints** | **List[str]** | Array of hints containing which fields should be populated in the response. | [optional] 
**timezone_offset** | **int** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**disable_spellcheck** | **bool** | Whether or not to disable spellcheck. | [optional] 
**disable_query_autocorrect** | **bool** | Disables automatic adjustment of the input query for spelling corrections or other reasons. | [optional] 
**return_llm_content_over_snippets** | **bool** | [beta] Enables expanded content to be returned for LLM usage. The size of content per result returned should be modified using maxSnippetSize. Server may return less or more than what is specified in maxSnippetSize. For more details, https://docs.google.com/document/d/1CTOLSxWWT9WDEnHVLoCUaxbGYyXYP8kctPRF-RluSQY/edit. Requires sufficient permissions. | [optional] 
**inclusions** | [**RestrictionFilters**](RestrictionFilters.md) |  | [optional] 
**exclusions** | [**RestrictionFilters**](RestrictionFilters.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_request_options import SearchRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestOptions from a JSON string
search_request_options_instance = SearchRequestOptions.from_json(json)
# print the JSON string representation of the object
print(SearchRequestOptions.to_json())

# convert the object into a dict
search_request_options_dict = search_request_options_instance.to_dict()
# create an instance of SearchRequestOptions from a dict
search_request_options_from_dict = SearchRequestOptions.from_dict(search_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


