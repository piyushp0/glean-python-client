# DocumentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** |  | [optional] 
**datasource_instance** | **str** | The datasource instance from which the document was extracted. | [optional] 
**object_type** | **str** | The type of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**container** | **str** | The name of the container (higher level parent, not direct parent) of the result. Interpretation is specific to each datasource (e.g. Channels for Slack, Project for Jira). cf. parentId | [optional] 
**container_id** | **str** | The Glean Document ID of the container. Uniquely identifies the container. | [optional] 
**super_container_id** | **str** | The Glean Document ID of the super container. Super container represents a broader abstraction that contains many containers. For example, whereas container might refer to a folder, super container would refer to a drive. | [optional] 
**parent_id** | **str** | The id of the direct parent of the result. Interpretation is specific to each datasource (e.g. parent issue for Jira). cf. container | [optional] 
**mime_type** | **str** |  | [optional] 
**document_id** | **str** | The index-wide unique identifier. | [optional] 
**logging_id** | **str** | A unique identifier used to represent the document in any logging or feedback requests in place of documentId. | [optional] 
**document_id_hash** | **str** | Hash of the Glean Document ID. | [optional] 
**create_time** | **datetime** |  | [optional] 
**update_time** | **datetime** |  | [optional] 
**author** | [**Person**](Person.md) |  | [optional] 
**owner** | [**Person**](Person.md) |  | [optional] 
**mentioned_people** | [**List[Person]**](Person.md) | A list of people mentioned in the document. | [optional] 
**visibility** | [**DocumentVisibility**](DocumentVisibility.md) |  | [optional] 
**components** | **List[str]** | A list of components this result is associated with. Interpretation is specific to each datasource. (e.g. for Jira issues, these are [components](https://confluence.atlassian.com/jirasoftwarecloud/organizing-work-with-components-764478279.html).) | [optional] 
**status** | **str** | The status or disposition of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue status such as Done, In Progress or Will Not Fix). | [optional] 
**status_category** | **str** | The status category of the result. Meant to be more general than status. Interpretation is specific to each datasource. | [optional] 
**pins** | [**List[PinDocument]**](PinDocument.md) | A list of stars associated with this result.  \&quot;Pin\&quot; is an older name. | [optional] 
**priority** | **str** | The document priority. Interpretation is datasource specific. | [optional] 
**assigned_to** | [**Person**](Person.md) |  | [optional] 
**updated_by** | [**Person**](Person.md) |  | [optional] 
**labels** | **List[str]** | A list of tags for the document. Interpretation is datasource specific. | [optional] 
**collections** | [**List[Collection]**](Collection.md) | A list of collections that the document belongs to. | [optional] 
**datasource_id** | **str** | The user-visible datasource specific id (e.g. Salesforce case number for example, GitHub PR number). | [optional] 
**interactions** | [**DocumentInteractions**](DocumentInteractions.md) |  | [optional] 
**verification** | [**Verification**](Verification.md) |  | [optional] 
**viewer_info** | [**ViewerInfo**](ViewerInfo.md) |  | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**visit_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**shortcuts** | [**List[Shortcut]**](Shortcut.md) | A list of shortcuts of which destination URL is for the document. | [optional] 
**path** | **str** | For file datasources like onedrive/github etc this has the path to the file | [optional] 
**custom_data** | [**Dict[str, CustomDataValue]**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 
**document_category** | **str** | The document&#39;s document_category(.proto). | [optional] 
**contact_person** | [**Person**](Person.md) |  | [optional] 
**thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**index_status** | [**IndexStatus**](IndexStatus.md) |  | [optional] 
**ancestors** | [**List[Document]**](Document.md) | A list of documents that are ancestors of this document in the hierarchy of the document&#39;s datasource, for example parent folders or containers. Ancestors can be of different types and some may not be indexed. Higher level ancestors appear earlier in the list. | [optional] 

## Example

```python
from openapi_client.models.document_metadata import DocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetadata from a JSON string
document_metadata_instance = DocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(DocumentMetadata.to_json())

# convert the object into a dict
document_metadata_dict = document_metadata_instance.to_dict()
# create an instance of DocumentMetadata from a dict
document_metadata_from_dict = DocumentMetadata.from_dict(document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


