# ReCodEx Client Library



## Latest API Endpoint Changes
```diff
/v1/comments/{id}:
  get:
    ...
    operationId: commentsPresenterActionDefault
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: commentsPresenterActionAddComment
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
    parameters:
    -
      name: renameTo
      ...
      schema:
        ...
+       maxLength: 32
+       minLength: 1
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}:
  get:
    ...
    operationId: exercisesPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesPresenterActionUpdateDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: exercisesPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/validate:
  post:
    ...
    operationId: exercisesPresenterActionValidate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/fork:
  post:
    ...
    operationId: exercisesPresenterActionForkFrom
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/assignments:
  get:
    ...
    operationId: exercisesPresenterActionAssignments
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/hardware-groups:
  post:
    ...
    operationId: exercisesPresenterActionHardwareGroups
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/groups/{groupId}:
  post:
    ...
    operationId: exercisesPresenterActionAttachGroup
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: exercisesPresenterActionDetachGroup
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/tags/{name}:
  post:
    ...
    operationId: exercisesPresenterActionAddTag
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: name
      ...
      schema:
        ...
+       maxLength: 32
+       minLength: 1
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: exercisesPresenterActionRemoveTag
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/archived:
  post:
    ...
    operationId: exercisesPresenterActionSetArchived
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/author:
  post:
    ...
    operationId: exercisesPresenterActionSetAuthor
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/admins:
  post:
    ...
    operationId: exercisesPresenterActionSetAdmins
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/notification:
  post:
    ...
    operationId: exercisesPresenterActionSendNotification
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/supplementary-files:
  get:
    ...
    operationId: exerciseFilesPresenterActionGetSupplementaryFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exerciseFilesPresenterActionUploadSupplementaryFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/supplementary-files/{fileId}:
  delete:
    ...
    operationId: exerciseFilesPresenterActionDeleteSupplementaryFile
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/supplementary-files/download-archive:
  get:
    ...
    operationId: exerciseFilesPresenterActionDownloadSupplementaryFilesArchive
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/attachment-files:
  get:
    ...
    operationId: exerciseFilesPresenterActionGetAttachmentFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exerciseFilesPresenterActionUploadAttachmentFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/attachment-files/{fileId}:
  delete:
    ...
    operationId: exerciseFilesPresenterActionDeleteAttachmentFile
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/attachment-files/download-archive:
  get:
    ...
    operationId: exerciseFilesPresenterActionDownloadAttachmentFilesArchive
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/tests:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetTests
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionSetTests
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/environment-configs:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetEnvironmentConfigs
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionUpdateEnvironmentConfigs
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/config:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetConfiguration
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionSetConfiguration
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/config/variables:
  post:
    ...
    operationId: exercisesConfigPresenterActionGetVariablesForExerciseConfig
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetHardwareGroupLimits
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionSetHardwareGroupLimits
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: exercisesConfigPresenterActionRemoveHardwareGroupLimits
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercises/{id}/limits:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetLimits
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionSetLimits
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercises/{id}/score-config:
  get:
    ...
    operationId: exercisesConfigPresenterActionGetScoreConfig
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: exercisesConfigPresenterActionSetScoreConfig
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}:
  get:
    ...
    operationId: assignmentsPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: assignmentsPresenterActionUpdateDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: assignmentsPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/solutions:
  get:
    ...
    operationId: assignmentsPresenterActionSolutions
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/best-solutions:
  get:
    ...
    operationId: assignmentsPresenterActionBestSolutions
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/download-best-solutions:
  get:
    ...
    operationId: assignmentsPresenterActionDownloadBestSolutionsArchive
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/users/{userId}/solutions:
  get:
    ...
    operationId: assignmentsPresenterActionUserSolutions
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/users/{userId}/best-solution:
  get:
    ...
    operationId: assignmentsPresenterActionBestSolution
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/validate:
  post:
    ...
    operationId: assignmentsPresenterActionValidate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/sync-exercise:
  post:
    ...
    operationId: assignmentsPresenterActionSyncWithExercise
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/can-submit:
  get:
    ...
    operationId: submitPresenterActionCanSubmit
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/submit:
  post:
    ...
    operationId: submitPresenterActionSubmit
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/resubmit-all:
  get:
    ...
    operationId: submitPresenterActionResubmitAllAsyncJobStatus
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: submitPresenterActionResubmitAll
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/exercise-assignments/{id}/pre-submit:
  post:
    ...
    operationId: submitPresenterActionPreSubmit
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/exercise-assignments/{id}/async-jobs:
  get:
    ...
    operationId: asyncJobsPresenterActionAssignmentJobs
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}:
  get:
    ...
    operationId: groupsPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: groupsPresenterActionUpdateGroup
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
+                     type: string
+                     nullable: False
+                   permissionHints:
+                     description: 
+                     type: array
+                     nullable: False
+                     items:
+                       <empty object>
  delete:
    ...
    operationId: groupsPresenterActionRemoveGroup
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/subgroups:
  get:
    ...
    operationId: groupsPresenterActionSubgroups
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/organizational:
  post:
    ...
    operationId: groupsPresenterActionSetOrganizational
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/archived:
  post:
    ...
    operationId: groupsPresenterActionSetArchived
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/examPeriod:
  post:
    ...
    operationId: groupsPresenterActionSetExamPeriod
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: groupsPresenterActionRemoveExamPeriod
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/exam/{examId}:
  get:
    ...
    operationId: groupsPresenterActionGetExamLocks
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/relocate/{newParentId}:
  post:
    ...
    operationId: groupsPresenterActionRelocate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/students/stats:
  get:
    ...
    operationId: groupsPresenterActionStats
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/students/{userId}:
  get:
    ...
    operationId: groupsPresenterActionStudentsStats
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: groupsPresenterActionAddStudent
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: groupsPresenterActionRemoveStudent
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/students/{userId}/solutions:
  get:
    ...
    operationId: groupsPresenterActionStudentsSolutions
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/lock/{userId}:
  post:
    ...
    operationId: groupsPresenterActionLockStudent
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: groupsPresenterActionUnlockStudent
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/members:
  get:
    ...
    operationId: groupsPresenterActionMembers
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/members/{userId}:
  post:
    ...
    operationId: groupsPresenterActionAddMember
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: groupsPresenterActionRemoveMember
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/assignments:
  get:
    ...
    operationId: groupsPresenterActionAssignments
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/groups/{id}/shadow-assignments:
  get:
    ...
    operationId: groupsPresenterActionShadowAssignments
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/group-invitations/{id}:
  get:
    ...
    operationId: groupInvitationsPresenterActionDefault
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: groupInvitationsPresenterActionUpdate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    operationId: groupInvitationsPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/group-invitations/{id}/accept:
  post:
    ...
    operationId: groupInvitationsPresenterActionAccept
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/group-attributes/{id}:
  delete:
    ...
    operationId: groupExternalAttributesPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/instances/{id}:
  get:
    ...
    operationId: instancesPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: instancesPresenterActionUpdateInstance
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: instancesPresenterActionDeleteInstance
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/instances/{id}/licences:
  get:
    ...
    operationId: instancesPresenterActionLicences
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: instancesPresenterActionCreateLicence
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/reference-solutions/{id}/resubmit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionResubmit
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/reference-solutions/{id}/files:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSolution
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: assignmentSolutionsPresenterActionUpdateSolution
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: assignmentSolutionsPresenterActionDeleteSolution
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/bonus-points:
  post:
    ...
    operationId: assignmentSolutionsPresenterActionSetBonusPoints
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/submissions:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSubmissions
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/set-flag/{flag}:
  post:
    ...
    operationId: assignmentSolutionsPresenterActionSetFlag
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/resubmit:
  post:
    ...
    operationId: submitPresenterActionResubmit
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/files:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/download-solution:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionDownloadSolutionArchive
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/review:
  get:
    ...
    operationId: assignmentSolutionReviewsPresenterActionDefault
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionUpdate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: assignmentSolutionReviewsPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/review-comment:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionNewComment
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solutions/{id}/review-comment/{commentId}:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionEditComment
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: assignmentSolutionReviewsPresenterActionDeleteComment
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/assignment-solvers:
  get:
    ...
    operationId: assignmentSolversPresenterActionDefault
    parameters:
    -
      name: assignmentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/submission-failures/{id}:
  get:
    ...
    operationId: submissionFailuresPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/submission-failures/{id}/resolve:
  post:
    ...
    operationId: submissionFailuresPresenterActionResolve
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files/partial/{id}:
  put:
    ...
    operationId: uploadedFilesPresenterActionAppendPartial
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
+   requestBody:
+     content:
+       application/octet-stream:
+         schema:
+           type: string
+           format: binary
  post:
    ...
    operationId: uploadedFilesPresenterActionCompletePartial
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: uploadedFilesPresenterActionCancelPartial
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files:
  post:
    ...
    operationId: uploadedFilesPresenterActionUpload
    responses:
      200:
-       description: The data
+       description: Placeholder response
+   requestBody:
+     content:
+       multipart/form-data:
+         schema:
+           type: object
+           required:
+           -
+             file
+           properties:
+             file:
+               description: The whole file to be uploaded
+               type: string
+               format: binary
+               nullable: False
```
```diff
/v1/uploaded-files/supplementary-file/{id}/download:
  get:
    ...
    operationId: uploadedFilesPresenterActionDownloadSupplementaryFile
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files/{id}:
  get:
    ...
    operationId: uploadedFilesPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files/{id}/download:
  get:
    ...
    operationId: uploadedFilesPresenterActionDownload
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: entry
      ...
      schema:
        ...
+       minLength: 1
    -
      name: similarSolutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files/{id}/content:
  get:
    ...
    operationId: uploadedFilesPresenterActionContent
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: entry
      ...
      schema:
        ...
+       minLength: 1
    -
      name: similarSolutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/uploaded-files/{id}/digest:
  get:
    ...
    operationId: uploadedFilesPresenterActionDigest
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}:
  get:
    ...
    operationId: usersPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: usersPresenterActionUpdateProfile
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: usersPresenterActionDelete
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/invalidate-tokens:
  post:
    ...
    operationId: usersPresenterActionInvalidateTokens
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/groups:
  get:
    ...
    operationId: usersPresenterActionGroups
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/groups/all:
  get:
    ...
    operationId: usersPresenterActionAllGroups
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/instances:
  get:
    ...
    operationId: usersPresenterActionInstances
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/settings:
  post:
    ...
    operationId: usersPresenterActionUpdateSettings
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/ui-data:
  post:
    ...
    operationId: usersPresenterActionUpdateUiData
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/users/{id}/create-local:
  post:
    ...
    operationId: usersPresenterActionCreateLocalAccount
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/role:
  post:
    ...
    operationId: usersPresenterActionSetRole
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/external-login/{service}:
  post:
    ...
    operationId: usersPresenterActionUpdateExternalLogin
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: usersPresenterActionRemoveExternalLogin
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/calendar-tokens:
  get:
    ...
    operationId: userCalendarsPresenterActionUserCalendars
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: userCalendarsPresenterActionCreateCalendar
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/pending-reviews:
  get:
    ...
    operationId: assignmentSolutionReviewsPresenterActionPending
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/users/{id}/review-requests:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionReviewRequests
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/fork:
  post:
    ...
    operationId: pipelinesPresenterActionForkPipeline
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}:
  get:
    ...
    operationId: pipelinesPresenterActionGetPipeline
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: pipelinesPresenterActionUpdatePipeline
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: pipelinesPresenterActionRemovePipeline
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/runtime-environments:
  post:
    ...
    operationId: pipelinesPresenterActionUpdateRuntimeEnvironments
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/validate:
  post:
    ...
    operationId: pipelinesPresenterActionValidatePipeline
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/supplementary-files:
  get:
    ...
    operationId: pipelinesPresenterActionGetSupplementaryFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: pipelinesPresenterActionUploadSupplementaryFiles
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/supplementary-files/{fileId}:
  delete:
    ...
    operationId: pipelinesPresenterActionDeleteSupplementaryFile
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/pipelines/{id}/exercises:
  get:
    ...
    operationId: pipelinesPresenterActionGetPipelineExercises
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/shadow-assignments/{id}:
  get:
    ...
    operationId: shadowAssignmentsPresenterActionDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: shadowAssignmentsPresenterActionUpdateDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: shadowAssignmentsPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/shadow-assignments/{id}/validate:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionValidate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/shadow-assignments/{id}/create-points:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionCreatePoints
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/notifications/{id}:
  post:
    ...
    operationId: notificationsPresenterActionUpdate
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
  delete:
    ...
    operationId: notificationsPresenterActionRemove
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/async-jobs/{id}:
  get:
    ...
    operationId: asyncJobsPresenterActionDefault
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/async-jobs/{id}/abort:
  post:
    ...
    operationId: asyncJobsPresenterActionAbort
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/plagiarism:
  get:
    ...
    operationId: plagiarismPresenterActionListBatches
    parameters:
    -
      name: detectionTool
      ...
      schema:
        ...
+       maxLength: 255
+       minLength: 1
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: plagiarismPresenterActionCreateBatch
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/plagiarism/{id}:
  get:
    ...
    operationId: plagiarismPresenterActionBatchDetail
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: plagiarismPresenterActionUpdateBatch
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/plagiarism/{id}/{solutionId}:
  get:
    ...
    operationId: plagiarismPresenterActionGetSimilarities
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: plagiarismPresenterActionAddSimilarities
    parameters:
    -
      name: id
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```diff
/v1/extensions/{extId}/{instanceId}:
  get:
    ...
    operationId: extensionsPresenterActionUrl
    parameters:
    -
      name: locale
      ...
      schema:
        ...
+       maxLength: 2
+       minLength: 2
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
  post:
    ...
    operationId: exercisesPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/groups:
  get:
    ...
    operationId: groupsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
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
```diff
/v1/groups/{groupId}/invitations:
  get:
    ...
    operationId: groupInvitationsPresenterActionList
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: groupInvitationsPresenterActionCreate
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/instances:
  get:
    ...
    operationId: instancesPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: instancesPresenterActionCreateInstance
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/instances/licences/{licenceId}:
  post:
    ...
    operationId: instancesPresenterActionUpdateLicence
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: instancesPresenterActionDeleteLicence
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/reference-solutions/{solutionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDetail
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionUpdate
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteReferenceSolution
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/reference-solutions/submission/{submissionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/assignment-solutions/submission/{submissionId}:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: assignmentSolutionsPresenterActionDeleteSubmission
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
  post:
    ...
    operationId: registrationPresenterActionCreateAccount
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/users/ical/{id}:
  get:
    ...
    operationId: userCalendarsPresenterActionDefault
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: userCalendarsPresenterActionExpireCalendar
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
  post:
    ...
    operationId: pipelinesPresenterActionCreatePipeline
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/extensions/sis/status/:
  get:
    operationId: sisPresenterActionStatus
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/extensions/sis/terms/:
  get:
    ...
    operationId: sisPresenterActionGetTerms
    responses:
      200:
-       description: The data
+       description: Placeholder response
  post:
    ...
    operationId: sisPresenterActionRegisterTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
```diff
/v1/extensions/sis/terms/{id}:
  post:
    ...
    operationId: sisPresenterActionEditTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: sisPresenterActionDeleteTerm
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
```diff
/v1/shadow-assignments/points/{pointsId}:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionUpdatePoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
  delete:
    ...
    operationId: shadowAssignmentsPresenterActionRemovePoints
    responses:
      200:
-       description: The data
+       description: Placeholder response
```
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
