# ReCodEx Client Library

A client API library for the [ReCodEx](https://recodex.mff.cuni.cz/) system.
This library can be used in custom scripts and command-line interfaces for fine-grained interactions with the system.

## Installation

The recommended way to install the library is via `pip`. Python 3.11 is recommended, but other versions may also work:

```bash
PIP_EXTRA_INDEX_URL="https://test.pypi.org/simple/" pip install recodex_cli_lib_eceltov
```

### Installation from Source

For developers or those who prefer to install directly from the source code, follow these steps:

```bash
# make sure to run these commands from the root of the repository
./commands/initRepo.sh
source venv/bin/activate
```

This will install the library in interactive mode, meaning that changes made to the source afterwards will be automatically reflected in the installation.

The script will clone the `swagger-api/swagger-codegen` repository, install it, generate code from an OpenAPI Specification file, and setup a Python `venv` environment.
Note that this process may take several minutes.

## Usage

### Creating Client Instance

The Client class is the primary interface with the library and can be created in multiple ways.
Some methods also create local sessions that store the URL and authorization token of the server.

```python
# URL of the API server
api_url = "http://localhost:4000"

# JWT token used for authentication
api_token = "eyJhbGciOi..."

username = "user"
password = "pwd"

# creating client without a session
client = Client(api_token, api_url)

# creating client and a session
client = client_factory.get_client(api_url, username, password, verbose=True)

# creating session
client_factory.create_session_from_credentials(api_url, username, password, verbose=True)
client_factory.create_session_from_token(api_url, api_token, verbose=True)

# creating client from session 
client = client_factory.get_client_from_session()

# removing the session
client_factory.remove_session()
```

### Calling Endpoints

There are two methods for calling an endpoint that differ on how the it is specified.
- `send_request` accepts string names of the presenter and action.
- `send_request_by_callback` accepts a generated callback.

Request parameters are passed with the `path_params`, `query_params`, `body`, and `files` function parameters as name-value pairs.
Generated model instances can also be passed to the `body` parameter. 

```python
# DefaultApi can be used as an enumeration of all endpoint callbacks
from recodex_cli_lib.generated.swagger_client import DefaultApi
# generated models are imported one by one
from recodex_cli_lib.generated.swagger_client.models.id_organizational_body import IdOrganizationalBody

# specify endpoint with string identifiers
response = client.send_request("groups", "set_organizational", path_params={"id": "154b..."}, body={"value": True})

# specify endpoint with a callback
response = client.send_request_by_callback(
  DefaultApi.groups_presenter_action_set_organizational, 
  path_params={"id": "154b..."},
  # body can also be specified with a generated model class
  body=IdOrganizationalBody(value=True)
)
```

The methods return a `ClientResponse` object that contains the status, headers, and the actual data.
The data can be retrieved in multiple ways.

```python
# binary response data
binary_data = response.data_binary

# stringified response data
utf8_string = response.data

# data parsed into a dictionary
dictionary_data = response.get_parsed_data()
if dictionary_data is None:
  raise Exception("Data is not in JSON format.")

# formatted data (useful for printing in the CLI)
formatted_json_string = response.get_json_string()
formatted_yaml_string = response.get_json_string()
```

### Utility Functions

In case you want to manually create api tokens, the Client contains methods for this purpose. 

```python
new_token = client.get_login_token(username, password)
refresh_token = client.get_refresh_token()
```

To upload a file, you can use the `upload` utility function that automatically sends the file in chunks.

```python
from recodex_cli_lib.helpers.file_upload_helper import upload
file_id = upload(client, "file.txt", verbose=True)
```

# Development

## Commands

The `commands` folder contains four utility commands:
- `initRepo.sh` is used for initial setup of the repository after download; it is described in the installation section.
- `replaceGenerated.sh` generates code from a new OAS and replaces the old one. It also appends an update log to this README. Make sure to change the `recodexSwaggerDocsPath` variable to point to the path of the new OAS before you run the command.
- `runTestsLocally` installs the library in interactive mode and runs all tests in the `tests` folder.
- `uploadPackage.sh` packages the library and uploads it to PyPI. This action requires a PyPI token and rights to modify the package.

## Repository Structure

### Library Code

The `src/recodex_cli_lib` contains all code of the library.

The `client.py` contains the main `Client` class that links all parts together.
It uses the `SwaggerValidator` (`client_components/swagger_validator.py`) class to validate requests against their schema and the `EndpointResolver` (`client_components/endpoint_resolver.py`) to translate endpoint identifiers to the generated API functions.

It uses the generated `ApiClient` and `DefaultApi` classes to interface the generated part of the library, which is contained in the `generated` folder.
The folder is not part of the repository and needs to be manually generated.

The `aliases.yaml` file contains all aliases for endpoints. These aliases can be used instead of the default presenter and action identifiers.
The aliases are parsed and managed by the `AliasContainer` (`client_components/alias_container.py`) class.

### Repository Utilities

During code regeneration, the `src/swaggerDiffchecker.py` script is used to find differences between the old and new OAS and writes a summary to this README file.

### Testing

Testing relies on a mock ReCodEx API server implemented in flask that exposes a few endpoints, which are implemented in the `tests/mockEndpoints` folder.
The files are then linked to the server in the `tests/mock_server.py` script.

The actual tests are implemented in dedicated classes in the `tests/testClasses` folder.
They derive from the `test_class_base.py` which uses the full login process to connect to the mock server.

The tests are automatically run in GitHub CI/CD, where code is generated from the `tests/swagger.yaml` file.
This file should be updated regularly to make sure the tests reflect the latest state.


## Latest API Endpoint Changes
### security_presenter_action_check
```diff
/v1/security/check:
  post:
    operationId: securityPresenterActionCheck
    ...
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### login_presenter_action_default
```diff
/v1/login:
  post:
    ...
    operationId: loginPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### login_presenter_action_refresh
```diff
/v1/login/refresh:
  post:
    ...
    operationId: loginPresenterActionRefresh
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### login_presenter_action_issue_restricted_token
```diff
/v1/login/issue-restricted-token:
  post:
    ...
    operationId: loginPresenterActionIssueRestrictedToken
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              scopes:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### login_presenter_action_take_over
```diff
/v1/login/takeover/{userId}:
  post:
    ...
    operationId: loginPresenterActionTakeOver
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### login_presenter_action_external
```diff
/v1/login/{authenticatorName}:
  post:
    ...
    operationId: loginPresenterActionExternal
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### broker_presenter_action_stats
```diff
/v1/broker/stats:
  get:
    ...
    operationId: brokerPresenterActionStats
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### broker_presenter_action_freeze
```diff
/v1/broker/freeze:
  post:
    ...
    operationId: brokerPresenterActionFreeze
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### broker_presenter_action_unfreeze
```diff
/v1/broker/unfreeze:
  post:
    ...
    operationId: brokerPresenterActionUnfreeze
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### broker_reports_presenter_action_error
```diff
/v1/broker-reports/error:
  post:
    ...
    operationId: brokerReportsPresenterActionError
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### broker_reports_presenter_action_job_status
```diff
/v1/broker-reports/job-status/{jobId}:
  post:
    ...
    operationId: brokerReportsPresenterActionJobStatus
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### comments_presenter_action_default
```diff
/v1/comments/{id}:
  get:
    ...
    operationId: commentsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### comments_presenter_action_add_comment
```diff
/v1/comments/{id}:
  post:
    ...
    operationId: commentsPresenterActionAddComment
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### comments_presenter_action_toggle_private
```diff
/v1/comments/{threadId}/comment/{commentId}/toggle:
  post:
    ...
    operationId: commentsPresenterActionTogglePrivate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### comments_presenter_action_set_private
```diff
/v1/comments/{threadId}/comment/{commentId}/private:
  post:
    ...
    operationId: commentsPresenterActionSetPrivate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### comments_presenter_action_delete
```diff
/v1/comments/{threadId}/comment/{commentId}:
  delete:
    ...
    operationId: commentsPresenterActionDelete
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_default
```diff
/v1/exercises:
  get:
    ...
    operationId: exercisesPresenterActionDefault
    parameters:
    -
      name: filters
      ...
      schema:
        ...
+       items:
+         <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_create
```diff
/v1/exercises:
  post:
    ...
    operationId: exercisesPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_list_by_ids
```diff
/v1/exercises/list:
  post:
    ...
    operationId: exercisesPresenterActionListByIds
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ids:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_authors
```diff
/v1/exercises/authors:
  get:
    ...
    operationId: exercisesPresenterActionAuthors
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_all_tags
```diff
/v1/exercises/tags:
  get:
    ...
    operationId: exercisesPresenterActionAllTags
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_tags_stats
```diff
/v1/exercises/tags-stats:
  get:
    ...
    operationId: exercisesPresenterActionTagsStats
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_tags_update_global
```diff
/v1/exercises/tags/{tag}:
  post:
    ...
    operationId: exercisesPresenterActionTagsUpdateGlobal
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_remove
```diff
/v1/exercises/{id}:
  delete:
    ...
    operationId: exercisesPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_detail
```diff
/v1/exercises/{id}:
  get:
    ...
    operationId: exercisesPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_update_detail
```diff
/v1/exercises/{id}:
  post:
    ...
    operationId: exercisesPresenterActionUpdateDetail
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_validate
```diff
/v1/exercises/{id}/validate:
  post:
    ...
    operationId: exercisesPresenterActionValidate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_fork_from
```diff
/v1/exercises/{id}/fork:
  post:
    ...
    operationId: exercisesPresenterActionForkFrom
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_assignments
```diff
/v1/exercises/{id}/assignments:
  get:
    ...
    operationId: exercisesPresenterActionAssignments
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_hardware_groups
```diff
/v1/exercises/{id}/hardware-groups:
  post:
    ...
    operationId: exercisesPresenterActionHardwareGroups
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              hwGroups:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_detach_group
```diff
/v1/exercises/{id}/groups/{groupId}:
  delete:
    ...
    operationId: exercisesPresenterActionDetachGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_attach_group
```diff
/v1/exercises/{id}/groups/{groupId}:
  post:
    ...
    operationId: exercisesPresenterActionAttachGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_remove_tag
```diff
/v1/exercises/{id}/tags/{name}:
  delete:
    ...
    operationId: exercisesPresenterActionRemoveTag
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_add_tag
```diff
/v1/exercises/{id}/tags/{name}:
  post:
    ...
    operationId: exercisesPresenterActionAddTag
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_set_archived
```diff
/v1/exercises/{id}/archived:
  post:
    ...
    operationId: exercisesPresenterActionSetArchived
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_set_author
```diff
/v1/exercises/{id}/author:
  post:
    ...
    operationId: exercisesPresenterActionSetAuthor
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_set_admins
```diff
/v1/exercises/{id}/admins:
  post:
    ...
    operationId: exercisesPresenterActionSetAdmins
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              admins:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_presenter_action_send_notification
```diff
/v1/exercises/{id}/notification:
  post:
    ...
    operationId: exercisesPresenterActionSendNotification
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_get_supplementary_files
```diff
/v1/exercises/{id}/supplementary-files:
  get:
    ...
    operationId: exerciseFilesPresenterActionGetSupplementaryFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_upload_supplementary_files
```diff
/v1/exercises/{id}/supplementary-files:
  post:
    ...
    operationId: exerciseFilesPresenterActionUploadSupplementaryFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_delete_supplementary_file
```diff
/v1/exercises/{id}/supplementary-files/{fileId}:
  delete:
    ...
    operationId: exerciseFilesPresenterActionDeleteSupplementaryFile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_download_supplementary_files_archive
```diff
/v1/exercises/{id}/supplementary-files/download-archive:
  get:
    ...
    operationId: exerciseFilesPresenterActionDownloadSupplementaryFilesArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_get_attachment_files
```diff
/v1/exercises/{id}/attachment-files:
  get:
    ...
    operationId: exerciseFilesPresenterActionGetAttachmentFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_upload_attachment_files
```diff
/v1/exercises/{id}/attachment-files:
  post:
    ...
    operationId: exerciseFilesPresenterActionUploadAttachmentFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_delete_attachment_file
```diff
/v1/exercises/{id}/attachment-files/{fileId}:
  delete:
    ...
    operationId: exerciseFilesPresenterActionDeleteAttachmentFile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercise_files_presenter_action_download_attachment_files_archive
```diff
/v1/exercises/{id}/attachment-files/download-archive:
  get:
    ...
    operationId: exerciseFilesPresenterActionDownloadAttachmentFilesArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_tests
```diff
/v1/exercises/{id}/tests:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetTests
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_set_tests
```diff
/v1/exercises/{id}/tests:
  post:
    ...
    operationId: exercisesConfigPresenterActionSetTests
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              tests:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_environment_configs
```diff
/v1/exercises/{id}/environment-configs:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetEnvironmentConfigs
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_update_environment_configs
```diff
/v1/exercises/{id}/environment-configs:
  post:
    ...
    operationId: exercisesConfigPresenterActionUpdateEnvironmentConfigs
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              environmentConfigs:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_configuration
```diff
/v1/exercises/{id}/config:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetConfiguration
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_set_configuration
```diff
/v1/exercises/{id}/config:
  post:
    ...
    operationId: exercisesConfigPresenterActionSetConfiguration
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              config:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_variables_for_exercise_config
```diff
/v1/exercises/{id}/config/variables:
  post:
    ...
    operationId: exercisesConfigPresenterActionGetVariablesForExerciseConfig
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              pipelinesIds:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_remove_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  delete:
    ...
    operationId: exercisesConfigPresenterActionRemoveHardwareGroupLimits
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetHardwareGroupLimits
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_set_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  post:
    ...
    operationId: exercisesConfigPresenterActionSetHardwareGroupLimits
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              limits:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_limits
```diff
/v1/exercises/{id}/limits:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetLimits
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_set_limits
```diff
/v1/exercises/{id}/limits:
  post:
    ...
    operationId: exercisesConfigPresenterActionSetLimits
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              limits:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_get_score_config
```diff
/v1/exercises/{id}/score-config:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetScoreConfig
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### exercises_config_presenter_action_set_score_config
```diff
/v1/exercises/{id}/score-config:
  post:
    ...
    operationId: exercisesConfigPresenterActionSetScoreConfig
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_create
```diff
/v1/exercise-assignments:
  post:
    ...
    operationId: assignmentsPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_remove
```diff
/v1/exercise-assignments/{id}:
  delete:
    ...
    operationId: assignmentsPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_detail
```diff
/v1/exercise-assignments/{id}:
  get:
    ...
    operationId: assignmentsPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_update_detail
```diff
/v1/exercise-assignments/{id}:
  post:
    ...
    operationId: assignmentsPresenterActionUpdateDetail
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
              disabledRuntimeEnvironmentIds:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_solutions
```diff
/v1/exercise-assignments/{id}/solutions:
  get:
    ...
    operationId: assignmentsPresenterActionSolutions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_best_solutions
```diff
/v1/exercise-assignments/{id}/best-solutions:
  get:
    ...
    operationId: assignmentsPresenterActionBestSolutions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_download_best_solutions_archive
```diff
/v1/exercise-assignments/{id}/download-best-solutions:
  get:
    ...
    operationId: assignmentsPresenterActionDownloadBestSolutionsArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_user_solutions
```diff
/v1/exercise-assignments/{id}/users/{userId}/solutions:
  get:
    ...
    operationId: assignmentsPresenterActionUserSolutions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_best_solution
```diff
/v1/exercise-assignments/{id}/users/{userId}/best-solution:
  get:
    ...
    operationId: assignmentsPresenterActionBestSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_validate
```diff
/v1/exercise-assignments/{id}/validate:
  post:
    ...
    operationId: assignmentsPresenterActionValidate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignments_presenter_action_sync_with_exercise
```diff
/v1/exercise-assignments/{id}/sync-exercise:
  post:
    ...
    operationId: assignmentsPresenterActionSyncWithExercise
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_can_submit
```diff
/v1/exercise-assignments/{id}/can-submit:
  get:
    ...
    operationId: submitPresenterActionCanSubmit
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_submit
```diff
/v1/exercise-assignments/{id}/submit:
  post:
    ...
    operationId: submitPresenterActionSubmit
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_resubmit_all_async_job_status
```diff
/v1/exercise-assignments/{id}/resubmit-all:
  get:
    ...
    operationId: submitPresenterActionResubmitAllAsyncJobStatus
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_resubmit_all
```diff
/v1/exercise-assignments/{id}/resubmit-all:
  post:
    ...
    operationId: submitPresenterActionResubmitAll
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_pre_submit
```diff
/v1/exercise-assignments/{id}/pre-submit:
  post:
    ...
    operationId: submitPresenterActionPreSubmit
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              files:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### async_jobs_presenter_action_assignment_jobs
```diff
/v1/exercise-assignments/{id}/async-jobs:
  get:
    ...
    operationId: asyncJobsPresenterActionAssignmentJobs
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_default
```diff
/v1/groups:
  get:
    ...
    operationId: groupsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_add_group
```diff
/v1/groups:
  post:
    ...
    operationId: groupsPresenterActionAddGroup
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_validate_add_group_data
```diff
/v1/groups/validate-add-group-data:
  post:
    ...
    operationId: groupsPresenterActionValidateAddGroupData
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_remove_group
```diff
/v1/groups/{id}:
  delete:
    ...
    operationId: groupsPresenterActionRemoveGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_detail
```diff
/v1/groups/{id}:
  get:
    ...
    operationId: groupsPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_update_group
```diff
/v1/groups/{id}:
  post:
    ...
    operationId: groupsPresenterActionUpdateGroup
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Response data
+       content:
+         application/json:
+           schema:
+             type: object
+             required:
+             -
+               success
+             -
+               code
+             -
+               payload
+             properties:
+               success:
+                 description: 
+                 type: boolean
+                 example: true
+                 nullable: False
+               code:
+                 description: 
+                 type: integer
+                 example: 0
+                 nullable: False
+               payload:
+                 description: 
+                 type: object
+                 nullable: False
+                 properties:
+                   id:
+                     description: An identifier of the group
+                     type: string
+                     pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                     example: 10000000-2000-4000-8000-160000000000
+                     nullable: False
+                   externalId:
+                     description: An informative, human readable identifier of the group
+                     type: string
+                     example: text
+                     nullable: True
+                   organizational:
+                     description: Whether the group is organizational (no assignments nor students).
+                     type: boolean
+                     example: true
+                     nullable: False
+                   exam:
+                     description: Whether the group is an exam group.
+                     type: boolean
+                     example: true
+                     nullable: False
+                   archived:
+                     description: Whether the group is archived
+                     type: boolean
+                     example: true
+                     nullable: False
+                   public:
+                     description: Should the group be visible to all student?
+                     type: boolean
+                     example: true
+                     nullable: False
+                   directlyArchived:
+                     description: Whether the group was explicitly marked as archived
+                     type: boolean
+                     example: true
+                     nullable: False
+                   localizedTexts:
+                     description: Localized names and descriptions
+                     type: array
+                     nullable: False
+                     items:
+                       <empty object>
+                   primaryAdminsIds:
+                     description: IDs of users which are explicitly listed as direct admins of this group
+                     type: array
+                     nullable: False
+                     items:
+                       type: string
+                       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                       example: 10000000-2000-4000-8000-160000000000
+                   parentGroupId:
+                     description: Identifier of the parent group (absent for a top-level group)
+                     type: string
+                     pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                     example: 10000000-2000-4000-8000-160000000000
+                     nullable: False
+                   parentGroupsIds:
+                     description: Identifications of groups in descending order.
+                     type: array
+                     nullable: False
+                     items:
+                       type: string
+                       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                       example: 10000000-2000-4000-8000-160000000000
+                   childGroups:
+                     description: Identifications of child groups.
+                     type: array
+                     nullable: False
+                     items:
+                       type: string
+                       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                       example: 10000000-2000-4000-8000-160000000000
+                   privateData:
+                     description: 
+                     type: object
+                     nullable: False
+                     properties:
+                       admins:
+                         description: IDs of all users that have admin privileges to this group (including inherited)
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       supervisors:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       observers:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       students:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       instanceId:
+                         description: 
+                         type: string
+                         pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                         example: 10000000-2000-4000-8000-160000000000
+                         nullable: False
+                       hasValidLicence:
+                         description: 
+                         type: boolean
+                         example: true
+                         nullable: False
+                       assignments:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       shadowAssignments:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       publicStats:
+                         description: 
+                         type: boolean
+                         example: true
+                         nullable: False
+                       detaining:
+                         description: 
+                         type: boolean
+                         example: true
+                         nullable: False
+                       threshold:
+                         description: 
+                         type: number
+                         example: 0.1
+                         nullable: False
+                       pointsLimit:
+                         description: 
+                         type: integer
+                         example: 0
+                         nullable: False
+                       bindings:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           <empty object>
+                       examBegin:
+                         description: 
+                         type: integer
+                         example: 1740135333
+                         nullable: False
+                       examEnd:
+                         description: 
+                         type: integer
+                         example: 1740135333
+                         nullable: False
+                       examLockStrict:
+                         description: 
+                         type: boolean
+                         example: true
+                         nullable: False
+                       exams:
+                         description: 
+                         type: array
+                         nullable: False
+                         items:
+                           <empty object>
+                   permissionHints:
+                     description: 
+                     type: array
+                     nullable: False
+                     items:
+                       <empty object>
```
### groups_presenter_action_subgroups
```diff
/v1/groups/{id}/subgroups:
  get:
    ...
    operationId: groupsPresenterActionSubgroups
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_set_organizational
```diff
/v1/groups/{id}/organizational:
  post:
    ...
    operationId: groupsPresenterActionSetOrganizational
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_set_archived
```diff
/v1/groups/{id}/archived:
  post:
    ...
    operationId: groupsPresenterActionSetArchived
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_remove_exam_period
```diff
/v1/groups/{id}/examPeriod:
  delete:
    ...
    operationId: groupsPresenterActionRemoveExamPeriod
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_set_exam_period
```diff
/v1/groups/{id}/examPeriod:
  post:
    ...
    operationId: groupsPresenterActionSetExamPeriod
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_get_exam_locks
```diff
/v1/groups/{id}/exam/{examId}:
  get:
    ...
    operationId: groupsPresenterActionGetExamLocks
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_relocate
```diff
/v1/groups/{id}/relocate/{newParentId}:
  post:
    ...
    operationId: groupsPresenterActionRelocate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_stats
```diff
/v1/groups/{id}/students/stats:
  get:
    ...
    operationId: groupsPresenterActionStats
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_remove_student
```diff
/v1/groups/{id}/students/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionRemoveStudent
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_students_stats
```diff
/v1/groups/{id}/students/{userId}:
  get:
    ...
    operationId: groupsPresenterActionStudentsStats
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_add_student
```diff
/v1/groups/{id}/students/{userId}:
  post:
    ...
    operationId: groupsPresenterActionAddStudent
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_students_solutions
```diff
/v1/groups/{id}/students/{userId}/solutions:
  get:
    ...
    operationId: groupsPresenterActionStudentsSolutions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_unlock_student
```diff
/v1/groups/{id}/lock/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionUnlockStudent
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_lock_student
```diff
/v1/groups/{id}/lock/{userId}:
  post:
    ...
    operationId: groupsPresenterActionLockStudent
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_members
```diff
/v1/groups/{id}/members:
  get:
    ...
    operationId: groupsPresenterActionMembers
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_remove_member
```diff
/v1/groups/{id}/members/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionRemoveMember
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_add_member
```diff
/v1/groups/{id}/members/{userId}:
  post:
    ...
    operationId: groupsPresenterActionAddMember
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_assignments
```diff
/v1/groups/{id}/assignments:
  get:
    ...
    operationId: groupsPresenterActionAssignments
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### groups_presenter_action_shadow_assignments
```diff
/v1/groups/{id}/shadow-assignments:
  get:
    ...
    operationId: groupsPresenterActionShadowAssignments
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_list
```diff
/v1/groups/{groupId}/invitations:
  get:
    ...
    operationId: groupInvitationsPresenterActionList
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_create
```diff
/v1/groups/{groupId}/invitations:
  post:
    ...
    operationId: groupInvitationsPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_remove
```diff
/v1/group-invitations/{id}:
  delete:
    operationId: groupInvitationsPresenterActionRemove
    ...
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_default
```diff
/v1/group-invitations/{id}:
  get:
    ...
    operationId: groupInvitationsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_update
```diff
/v1/group-invitations/{id}:
  post:
    ...
    operationId: groupInvitationsPresenterActionUpdate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_invitations_presenter_action_accept
```diff
/v1/group-invitations/{id}/accept:
  post:
    ...
    operationId: groupInvitationsPresenterActionAccept
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_external_attributes_presenter_action_default
```diff
/v1/group-attributes:
  get:
    ...
    operationId: groupExternalAttributesPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_external_attributes_presenter_action_add
```diff
/v1/group-attributes/{groupId}:
  post:
    ...
    operationId: groupExternalAttributesPresenterActionAdd
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### group_external_attributes_presenter_action_remove
```diff
/v1/group-attributes/{id}:
  delete:
    ...
    operationId: groupExternalAttributesPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_default
```diff
/v1/instances:
  get:
    ...
    operationId: instancesPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_create_instance
```diff
/v1/instances:
  post:
    ...
    operationId: instancesPresenterActionCreateInstance
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_delete_instance
```diff
/v1/instances/{id}:
  delete:
    ...
    operationId: instancesPresenterActionDeleteInstance
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_detail
```diff
/v1/instances/{id}:
  get:
    ...
    operationId: instancesPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_update_instance
```diff
/v1/instances/{id}:
  post:
    ...
    operationId: instancesPresenterActionUpdateInstance
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_licences
```diff
/v1/instances/{id}/licences:
  get:
    ...
    operationId: instancesPresenterActionLicences
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_create_licence
```diff
/v1/instances/{id}/licences:
  post:
    ...
    operationId: instancesPresenterActionCreateLicence
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_delete_licence
```diff
/v1/instances/licences/{licenceId}:
  delete:
    ...
    operationId: instancesPresenterActionDeleteLicence
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### instances_presenter_action_update_licence
```diff
/v1/instances/licences/{licenceId}:
  post:
    ...
    operationId: instancesPresenterActionUpdateLicence
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_solutions
```diff
/v1/reference-solutions/exercise/{exerciseId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSolutions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_pre_submit
```diff
/v1/reference-solutions/exercise/{exerciseId}/pre-submit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionPreSubmit
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              files:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_submit
```diff
/v1/reference-solutions/exercise/{exerciseId}/submit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmit
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_resubmit_all
```diff
/v1/reference-solutions/exercise/{exerciseId}/resubmit-all:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionResubmitAll
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_delete_reference_solution
```diff
/v1/reference-solutions/{solutionId}:
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteReferenceSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_detail
```diff
/v1/reference-solutions/{solutionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_update
```diff
/v1/reference-solutions/{solutionId}:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionUpdate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_resubmit
```diff
/v1/reference-solutions/{id}/resubmit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionResubmit
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_submissions
```diff
/v1/reference-solutions/{solutionId}/submissions:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmissions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_files
```diff
/v1/reference-solutions/{id}/files:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_download_solution_archive
```diff
/v1/reference-solutions/{solutionId}/download-solution:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDownloadSolutionArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_set_visibility
```diff
/v1/reference-solutions/{solutionId}/visibility:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSetVisibility
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_delete_submission
```diff
/v1/reference-solutions/submission/{submissionId}:
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_submission
```diff
/v1/reference-solutions/submission/{submissionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_download_result_archive
```diff
/v1/reference-solutions/submission/{submissionId}/download-result:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDownloadResultArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### reference_exercise_solutions_presenter_action_evaluation_score_config
```diff
/v1/reference-solutions/submission/{submissionId}/score-config:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionEvaluationScoreConfig
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_delete_solution
```diff
/v1/assignment-solutions/{id}:
  delete:
    ...
    operationId: assignmentSolutionsPresenterActionDeleteSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_solution
```diff
/v1/assignment-solutions/{id}:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_update_solution
```diff
/v1/assignment-solutions/{id}:
  post:
    ...
    operationId: assignmentSolutionsPresenterActionUpdateSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_set_bonus_points
```diff
/v1/assignment-solutions/{id}/bonus-points:
  post:
    ...
    operationId: assignmentSolutionsPresenterActionSetBonusPoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_submissions
```diff
/v1/assignment-solutions/{id}/submissions:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSubmissions
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_set_flag
```diff
/v1/assignment-solutions/{id}/set-flag/{flag}:
  post:
    ...
    operationId: assignmentSolutionsPresenterActionSetFlag
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submit_presenter_action_resubmit
```diff
/v1/assignment-solutions/{id}/resubmit:
  post:
    ...
    operationId: submitPresenterActionResubmit
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_files
```diff
/v1/assignment-solutions/{id}/files:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_download_solution_archive
```diff
/v1/assignment-solutions/{id}/download-solution:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionDownloadSolutionArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_delete_submission
```diff
/v1/assignment-solutions/submission/{submissionId}:
  delete:
    ...
    operationId: assignmentSolutionsPresenterActionDeleteSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_submission
```diff
/v1/assignment-solutions/submission/{submissionId}:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_download_result_archive
```diff
/v1/assignment-solutions/submission/{submissionId}/download-result:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionDownloadResultArchive
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_evaluation_score_config
```diff
/v1/assignment-solutions/submission/{submissionId}/score-config:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionEvaluationScoreConfig
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_remove
```diff
/v1/assignment-solutions/{id}/review:
  delete:
    ...
    operationId: assignmentSolutionReviewsPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_default
```diff
/v1/assignment-solutions/{id}/review:
  get:
    ...
    operationId: assignmentSolutionReviewsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_update
```diff
/v1/assignment-solutions/{id}/review:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionUpdate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_new_comment
```diff
/v1/assignment-solutions/{id}/review-comment:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionNewComment
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_delete_comment
```diff
/v1/assignment-solutions/{id}/review-comment/{commentId}:
  delete:
    ...
    operationId: assignmentSolutionReviewsPresenterActionDeleteComment
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_edit_comment
```diff
/v1/assignment-solutions/{id}/review-comment/{commentId}:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionEditComment
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solvers_presenter_action_default
```diff
/v1/assignment-solvers:
  get:
    ...
    operationId: assignmentSolversPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submission_failures_presenter_action_default
```diff
/v1/submission-failures:
  get:
    ...
    operationId: submissionFailuresPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submission_failures_presenter_action_unresolved
```diff
/v1/submission-failures/unresolved:
  get:
    ...
    operationId: submissionFailuresPresenterActionUnresolved
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submission_failures_presenter_action_detail
```diff
/v1/submission-failures/{id}:
  get:
    ...
    operationId: submissionFailuresPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### submission_failures_presenter_action_resolve
```diff
/v1/submission-failures/{id}/resolve:
  post:
    ...
    operationId: submissionFailuresPresenterActionResolve
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_start_partial
```diff
/v1/uploaded-files/partial:
  post:
    ...
    operationId: uploadedFilesPresenterActionStartPartial
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_cancel_partial
```diff
/v1/uploaded-files/partial/{id}:
  delete:
    ...
    operationId: uploadedFilesPresenterActionCancelPartial
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_complete_partial
```diff
/v1/uploaded-files/partial/{id}:
  post:
    ...
    operationId: uploadedFilesPresenterActionCompletePartial
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_append_partial
```diff
/v1/uploaded-files/partial/{id}:
  put:
    ...
    operationId: uploadedFilesPresenterActionAppendPartial
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_upload
```diff
/v1/uploaded-files:
  post:
    ...
    operationId: uploadedFilesPresenterActionUpload
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_download_supplementary_file
```diff
/v1/uploaded-files/supplementary-file/{id}/download:
  get:
    ...
    operationId: uploadedFilesPresenterActionDownloadSupplementaryFile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_detail
```diff
/v1/uploaded-files/{id}:
  get:
    ...
    operationId: uploadedFilesPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_download
```diff
/v1/uploaded-files/{id}/download:
  get:
    ...
    operationId: uploadedFilesPresenterActionDownload
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_content
```diff
/v1/uploaded-files/{id}/content:
  get:
    ...
    operationId: uploadedFilesPresenterActionContent
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### uploaded_files_presenter_action_digest
```diff
/v1/uploaded-files/{id}/digest:
  get:
    ...
    operationId: uploadedFilesPresenterActionDigest
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_default
```diff
/v1/users:
  get:
    ...
    operationId: usersPresenterActionDefault
    parameters:
    -
      name: filters
      ...
      schema:
        ...
+       items:
+         <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### registration_presenter_action_create_account
```diff
/v1/users:
  post:
    ...
    operationId: registrationPresenterActionCreateAccount
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### registration_presenter_action_validate_registration_data
```diff
/v1/users/validate-registration-data:
  post:
    ...
    operationId: registrationPresenterActionValidateRegistrationData
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_list_by_ids
```diff
/v1/users/list:
  post:
    ...
    operationId: usersPresenterActionListByIds
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ids:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### user_calendars_presenter_action_expire_calendar
```diff
/v1/users/ical/{id}:
  delete:
    ...
    operationId: userCalendarsPresenterActionExpireCalendar
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### user_calendars_presenter_action_default
```diff
/v1/users/ical/{id}:
  get:
    ...
    operationId: userCalendarsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### registration_presenter_action_create_invitation
```diff
/v1/users/invite:
  post:
    ...
    operationId: registrationPresenterActionCreateInvitation
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              groups:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### registration_presenter_action_accept_invitation
```diff
/v1/users/accept-invitation:
  post:
    ...
    operationId: registrationPresenterActionAcceptInvitation
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_delete
```diff
/v1/users/{id}:
  delete:
    ...
    operationId: usersPresenterActionDelete
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_detail
```diff
/v1/users/{id}:
  get:
    ...
    operationId: usersPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_update_profile
```diff
/v1/users/{id}:
  post:
    ...
    operationId: usersPresenterActionUpdateProfile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_invalidate_tokens
```diff
/v1/users/{id}/invalidate-tokens:
  post:
    ...
    operationId: usersPresenterActionInvalidateTokens
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_groups
```diff
/v1/users/{id}/groups:
  get:
    ...
    operationId: usersPresenterActionGroups
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_all_groups
```diff
/v1/users/{id}/groups/all:
  get:
    ...
    operationId: usersPresenterActionAllGroups
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_instances
```diff
/v1/users/{id}/instances:
  get:
    ...
    operationId: usersPresenterActionInstances
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_update_settings
```diff
/v1/users/{id}/settings:
  post:
    ...
    operationId: usersPresenterActionUpdateSettings
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_update_ui_data
```diff
/v1/users/{id}/ui-data:
  post:
    ...
    operationId: usersPresenterActionUpdateUiData
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              uiData:
                ...
+               items:
+                 <empty object>
              ...
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_create_local_account
```diff
/v1/users/{id}/create-local:
  post:
    ...
    operationId: usersPresenterActionCreateLocalAccount
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_set_role
```diff
/v1/users/{id}/role:
  post:
    ...
    operationId: usersPresenterActionSetRole
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_remove_external_login
```diff
/v1/users/{id}/external-login/{service}:
  delete:
    ...
    operationId: usersPresenterActionRemoveExternalLogin
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### users_presenter_action_update_external_login
```diff
/v1/users/{id}/external-login/{service}:
  post:
    ...
    operationId: usersPresenterActionUpdateExternalLogin
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### user_calendars_presenter_action_user_calendars
```diff
/v1/users/{id}/calendar-tokens:
  get:
    ...
    operationId: userCalendarsPresenterActionUserCalendars
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### user_calendars_presenter_action_create_calendar
```diff
/v1/users/{id}/calendar-tokens:
  post:
    ...
    operationId: userCalendarsPresenterActionCreateCalendar
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solution_reviews_presenter_action_pending
```diff
/v1/users/{id}/pending-reviews:
  get:
    ...
    operationId: assignmentSolutionReviewsPresenterActionPending
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### assignment_solutions_presenter_action_review_requests
```diff
/v1/users/{id}/review-requests:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionReviewRequests
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### email_verification_presenter_action_email_verification
```diff
/v1/email-verification/verify:
  post:
    ...
    operationId: emailVerificationPresenterActionEmailVerification
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### email_verification_presenter_action_resend_verification_email
```diff
/v1/email-verification/resend:
  post:
    ...
    operationId: emailVerificationPresenterActionResendVerificationEmail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### forgotten_password_presenter_action_default
```diff
/v1/forgotten-password:
  post:
    ...
    operationId: forgottenPasswordPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### forgotten_password_presenter_action_change
```diff
/v1/forgotten-password/change:
  post:
    ...
    operationId: forgottenPasswordPresenterActionChange
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### forgotten_password_presenter_action_validate_password_strength
```diff
/v1/forgotten-password/validate-password-strength:
  post:
    ...
    operationId: forgottenPasswordPresenterActionValidatePasswordStrength
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### runtime_environments_presenter_action_default
```diff
/v1/runtime-environments:
  get:
    ...
    operationId: runtimeEnvironmentsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### hardware_groups_presenter_action_default
```diff
/v1/hardware-groups:
  get:
    ...
    operationId: hardwareGroupsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_default
```diff
/v1/pipelines:
  get:
    ...
    operationId: pipelinesPresenterActionDefault
    parameters:
    -
      name: filters
      ...
      schema:
        ...
+       items:
+         <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_create_pipeline
```diff
/v1/pipelines:
  post:
    ...
    operationId: pipelinesPresenterActionCreatePipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_get_default_boxes
```diff
/v1/pipelines/boxes:
  get:
    ...
    operationId: pipelinesPresenterActionGetDefaultBoxes
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_fork_pipeline
```diff
/v1/pipelines/{id}/fork:
  post:
    ...
    operationId: pipelinesPresenterActionForkPipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_remove_pipeline
```diff
/v1/pipelines/{id}:
  delete:
    ...
    operationId: pipelinesPresenterActionRemovePipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_get_pipeline
```diff
/v1/pipelines/{id}:
  get:
    ...
    operationId: pipelinesPresenterActionGetPipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_update_pipeline
```diff
/v1/pipelines/{id}:
  post:
    ...
    operationId: pipelinesPresenterActionUpdatePipeline
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              parameters:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_update_runtime_environments
```diff
/v1/pipelines/{id}/runtime-environments:
  post:
    ...
    operationId: pipelinesPresenterActionUpdateRuntimeEnvironments
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_validate_pipeline
```diff
/v1/pipelines/{id}/validate:
  post:
    ...
    operationId: pipelinesPresenterActionValidatePipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_get_supplementary_files
```diff
/v1/pipelines/{id}/supplementary-files:
  get:
    ...
    operationId: pipelinesPresenterActionGetSupplementaryFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_upload_supplementary_files
```diff
/v1/pipelines/{id}/supplementary-files:
  post:
    ...
    operationId: pipelinesPresenterActionUploadSupplementaryFiles
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_delete_supplementary_file
```diff
/v1/pipelines/{id}/supplementary-files/{fileId}:
  delete:
    ...
    operationId: pipelinesPresenterActionDeleteSupplementaryFile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### pipelines_presenter_action_get_pipeline_exercises
```diff
/v1/pipelines/{id}/exercises:
  get:
    ...
    operationId: pipelinesPresenterActionGetPipelineExercises
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_status
```diff
/v1/extensions/sis/status/:
  get:
    operationId: sisPresenterActionStatus
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_get_terms
```diff
/v1/extensions/sis/terms/:
  get:
    ...
    operationId: sisPresenterActionGetTerms
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_register_term
```diff
/v1/extensions/sis/terms/:
  post:
    ...
    operationId: sisPresenterActionRegisterTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_delete_term
```diff
/v1/extensions/sis/terms/{id}:
  delete:
    ...
    operationId: sisPresenterActionDeleteTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_edit_term
```diff
/v1/extensions/sis/terms/{id}:
  post:
    ...
    operationId: sisPresenterActionEditTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_subscribed_courses
```diff
/v1/extensions/sis/users/{userId}/subscribed-groups/{year}/{term}/as-student:
  get:
    ...
    operationId: sisPresenterActionSubscribedCourses
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_supervised_courses
```diff
/v1/extensions/sis/users/{userId}/supervised-courses/{year}/{term}:
  get:
    ...
    operationId: sisPresenterActionSupervisedCourses
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_possible_parents
```diff
/v1/extensions/sis/remote-courses/{courseId}/possible-parents:
  get:
    ...
    operationId: sisPresenterActionPossibleParents
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_create_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/create:
  post:
    ...
    operationId: sisPresenterActionCreateGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_bind_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/bind:
  post:
    ...
    operationId: sisPresenterActionBindGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### sis_presenter_action_unbind_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/bindings/{groupId}:
  delete:
    ...
    operationId: sisPresenterActionUnbindGroup
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### emails_presenter_action_default
```diff
/v1/emails:
  post:
    ...
    operationId: emailsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### emails_presenter_action_send_to_supervisors
```diff
/v1/emails/supervisors:
  post:
    ...
    operationId: emailsPresenterActionSendToSupervisors
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### emails_presenter_action_send_to_regular_users
```diff
/v1/emails/regular-users:
  post:
    ...
    operationId: emailsPresenterActionSendToRegularUsers
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### emails_presenter_action_send_to_group_members
```diff
/v1/emails/groups/{groupId}:
  post:
    ...
    operationId: emailsPresenterActionSendToGroupMembers
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_remove
```diff
/v1/shadow-assignments/{id}:
  delete:
    ...
    operationId: shadowAssignmentsPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_detail
```diff
/v1/shadow-assignments/{id}:
  get:
    ...
    operationId: shadowAssignmentsPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_update_detail
```diff
/v1/shadow-assignments/{id}:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionUpdateDetail
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_create
```diff
/v1/shadow-assignments:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_validate
```diff
/v1/shadow-assignments/{id}/validate:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionValidate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_create_points
```diff
/v1/shadow-assignments/{id}/create-points:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionCreatePoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_remove_points
```diff
/v1/shadow-assignments/points/{pointsId}:
  delete:
    ...
    operationId: shadowAssignmentsPresenterActionRemovePoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### shadow_assignments_presenter_action_update_points
```diff
/v1/shadow-assignments/points/{pointsId}:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionUpdatePoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### notifications_presenter_action_default
```diff
/v1/notifications:
  get:
    ...
    operationId: notificationsPresenterActionDefault
    parameters:
    -
      name: groupsIds
      ...
      schema:
        ...
+       items:
+         <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### notifications_presenter_action_create
```diff
/v1/notifications:
  post:
    ...
    operationId: notificationsPresenterActionCreate
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              groupsIds:
                ...
+               items:
+                 <empty object>
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### notifications_presenter_action_all
```diff
/v1/notifications/all:
  get:
    ...
    operationId: notificationsPresenterActionAll
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### notifications_presenter_action_remove
```diff
/v1/notifications/{id}:
  delete:
    ...
    operationId: notificationsPresenterActionRemove
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### notifications_presenter_action_update
```diff
/v1/notifications/{id}:
  post:
    ...
    operationId: notificationsPresenterActionUpdate
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              groupsIds:
                ...
+               items:
+                 <empty object>
              ...
              localizedTexts:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### worker_files_presenter_action_download_supplementary_file
```diff
/v1/worker-files/supplementary-file/{hash}:
  get:
    ...
    operationId: workerFilesPresenterActionDownloadSupplementaryFile
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### async_jobs_presenter_action_default
```diff
/v1/async-jobs/{id}:
  get:
    ...
    operationId: asyncJobsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### async_jobs_presenter_action_list
```diff
/v1/async-jobs:
  get:
    ...
    operationId: asyncJobsPresenterActionList
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### async_jobs_presenter_action_abort
```diff
/v1/async-jobs/{id}/abort:
  post:
    ...
    operationId: asyncJobsPresenterActionAbort
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### async_jobs_presenter_action_ping
```diff
/v1/async-jobs/ping:
  post:
    ...
    operationId: asyncJobsPresenterActionPing
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_list_batches
```diff
/v1/plagiarism:
  get:
    ...
    operationId: plagiarismPresenterActionListBatches
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_create_batch
```diff
/v1/plagiarism:
  post:
    ...
    operationId: plagiarismPresenterActionCreateBatch
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_batch_detail
```diff
/v1/plagiarism/{id}:
  get:
    ...
    operationId: plagiarismPresenterActionBatchDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_update_batch
```diff
/v1/plagiarism/{id}:
  post:
    ...
    operationId: plagiarismPresenterActionUpdateBatch
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_get_similarities
```diff
/v1/plagiarism/{id}/{solutionId}:
  get:
    ...
    operationId: plagiarismPresenterActionGetSimilarities
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### plagiarism_presenter_action_add_similarities
```diff
/v1/plagiarism/{id}/{solutionId}:
  post:
    ...
    operationId: plagiarismPresenterActionAddSimilarities
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              files:
                ...
+               items:
+                 <empty object>
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### extensions_presenter_action_url
```diff
/v1/extensions/{extId}/{instanceId}:
  get:
    ...
    operationId: extensionsPresenterActionUrl
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
### extensions_presenter_action_token
```diff
/v1/extensions/{extId}:
  post:
    ...
    operationId: extensionsPresenterActionToken
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
