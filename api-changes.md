### comments_presenter_action_toggle_private
```diff
/v1/comments/{threadId}/comment/{commentId}/toggle:
  post:
    operationId: commentsPresenterActionTogglePrivate
-   summary: Make a private comment public or vice versa
+   summary: Make a private comment public or vice versa [DEPRECATED]
-   description: Make a private comment public or vice versa
+   description: Make a private comment public or vice versa
[DEPRECATED]
    parameters:
    -
      name: threadId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: commentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    ...
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
+                 type: string
+                 pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                 example: 10000000-2000-4000-8000-160000000000
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
+                 type: string
+                 pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                 example: 10000000-2000-4000-8000-160000000000
```
### exercise_files_presenter_action_get_exercise_files
```diff
/v1/exercises/{id}/supplementary-files:
  get:
-   summary: Get list of all supplementary files for an exercise
+   summary: Get list of all exercise files for an exercise
-   description: Get list of all supplementary files for an exercise
+   description: Get list of all exercise files for an exercise
-   operationId: exerciseFilesPresenterActionGetSupplementaryFiles
+   operationId: exerciseFilesPresenterActionGetExerciseFiles
    ...
```
### exercise_files_presenter_action_upload_exercise_files
```diff
/v1/exercises/{id}/supplementary-files:
  post:
-   summary: Associate supplementary files with an exercise and upload them to remote file server
+   summary: Associate exercise files with an exercise and upload them to remote file server
-   description: Associate supplementary files with an exercise and upload them to remote file server
+   description: Associate exercise files with an exercise and upload them to remote file server
-   operationId: exerciseFilesPresenterActionUploadSupplementaryFiles
+   operationId: exerciseFilesPresenterActionUploadExerciseFiles
    ...
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              files:
                ...
-               description: Identifiers of supplementary files
+               description: Identifiers of exercise files
```
### exercise_files_presenter_action_delete_exercise_file
```diff
/v1/exercises/{id}/supplementary-files/{fileId}:
  delete:
-   summary: Delete supplementary exercise file with given id
+   summary: Delete exercise file with given id
-   description: Delete supplementary exercise file with given id
+   description: Delete exercise file with given id
-   operationId: exerciseFilesPresenterActionDeleteSupplementaryFile
+   operationId: exerciseFilesPresenterActionDeleteExerciseFile
    parameters:
    -
      name: fileId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    ...
```
### exercise_files_presenter_action_download_exercise_files_archive
```diff
/v1/exercises/{id}/supplementary-files/download-archive:
  get:
-   summary: Download archive containing all supplementary files for exercise.
+   summary: Download archive containing all files for exercise.
-   description: Download archive containing all supplementary files for exercise.
+   description: Download archive containing all files for exercise.
-   operationId: exerciseFilesPresenterActionDownloadSupplementaryFilesArchive
+   operationId: exerciseFilesPresenterActionDownloadExerciseFilesArchive
    ...
```
### exercise_files_presenter_action_get_attachment_files
```diff
/v1/exercises/{id}/attachment-files:
  get:
    operationId: exerciseFilesPresenterActionGetAttachmentFiles
-   summary: Get a list of all attachment files for an exercise
+   summary: Get a list of all attachment files for an exercise [DEPRECATED]
-   description: Get a list of all attachment files for an exercise
+   description: Get a list of all attachment files for an exercise
[DEPRECATED]: attachment files were unified with exercise files
+   deprecated: True
    ...
```
### exercise_files_presenter_action_upload_attachment_files
```diff
/v1/exercises/{id}/attachment-files:
  post:
    operationId: exerciseFilesPresenterActionUploadAttachmentFiles
-   summary: Associate attachment exercise files with an exercise
+   summary: Associate attachment exercise files with an exercise [DEPRECATED]
-   description: Associate attachment exercise files with an exercise
+   description: Associate attachment exercise files with an exercise
[DEPRECATED]: attachment files were unified with exercise files
+   deprecated: True
    ...
```
### exercise_files_presenter_action_delete_attachment_file
```diff
/v1/exercises/{id}/attachment-files/{fileId}:
  delete:
    operationId: exerciseFilesPresenterActionDeleteAttachmentFile
-   summary: Delete attachment exercise file with given id
+   summary: Delete attachment exercise file with given id [DEPRECATED]
-   description: Delete attachment exercise file with given id
+   description: Delete attachment exercise file with given id
[DEPRECATED]: attachment files were unified with exercise files
+   deprecated: True
    parameters:
    -
      name: fileId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    ...
```
### exercise_files_presenter_action_download_attachment_files_archive
```diff
/v1/exercises/{id}/attachment-files/download-archive:
  get:
    operationId: exerciseFilesPresenterActionDownloadAttachmentFilesArchive
-   summary: Download archive containing all attachment files for exercise.
+   summary: Download archive containing all attachment files for exercise. [DEPRECATED]
-   description: Download archive containing all attachment files for exercise.
+   description: Download archive containing all attachment files for exercise.
[DEPRECATED]: attachment files were unified with exercise files
+   deprecated: True
    ...
```
### exercises_config_presenter_action_get_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  get:
    operationId: exercisesConfigPresenterActionGetHardwareGroupLimits
-   summary: Get a description of resource limits for an exercise for given hwgroup.
+   summary: Get a description of resource limits for an exercise for given hwgroup. [DEPRECATED]
-   description: Get a description of resource limits for an exercise for given hwgroup.
+   description: Get a description of resource limits for an exercise for given hwgroup.
[DEPRECATED]
    parameters:
    -
      name: runtimeEnvironmentId
      ...
      schema:
        ...
+       minLength: 1
    -
      name: hwGroupId
      ...
      schema:
        ...
+       minLength: 1
    ...
```
### exercises_config_presenter_action_remove_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  delete:
    operationId: exercisesConfigPresenterActionRemoveHardwareGroupLimits
-   summary: Remove resource limits of given hwgroup from an exercise.
+   summary: Remove resource limits of given hwgroup from an exercise. [DEPRECATED]
-   description: Remove resource limits of given hwgroup from an exercise.
+   description: Remove resource limits of given hwgroup from an exercise.
[DEPRECATED]
    parameters:
    -
      name: runtimeEnvironmentId
      ...
      schema:
        ...
+       minLength: 1
    -
      name: hwGroupId
      ...
      schema:
        ...
+       minLength: 1
    ...
```
### exercises_config_presenter_action_set_hardware_group_limits
```diff
/v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits:
  post:
    operationId: exercisesConfigPresenterActionSetHardwareGroupLimits
-   summary: Set resource limits for an exercise for given hwgroup.
+   summary: Set resource limits for an exercise for given hwgroup. [DEPRECATED]
-   description: Set resource limits for an exercise for given hwgroup.
+   description: Set resource limits for an exercise for given hwgroup.
[DEPRECATED]
    parameters:
    -
      name: runtimeEnvironmentId
      ...
      schema:
        ...
+       minLength: 1
    -
      name: hwGroupId
      ...
      schema:
        ...
+       minLength: 1
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
    ...
```
### assignments_presenter_action_detail
```diff
/v1/exercise-assignments/{id}:
  get:
    ...
```
### assignments_presenter_action_remove
```diff
/v1/exercise-assignments/{id}:
  delete:
    ...
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
            required:
            -
              version
            -
              isPublic
            -
              firstDeadline
            -
              maxPointsBeforeFirstDeadline
            -
              submissionsCountLimit
            -
              solutionFilesLimit
            -
              solutionSizeLimit
            -
              allowSecondDeadline
            -
              canViewLimitRatios
            -
              canViewMeasuredValues
            -
              canViewJudgeStdout
            -
              canViewJudgeStderr
            -
              maxPointsDeadlineInterpolation
            -
              isBonus
-           -
-             localizedTexts
+           -
+             localizedStudentHints
            properties:
              ...
-             localizedTexts:
-               description: A description of the assignment
-               type: array
-               nullable: False
-               items:
-                 <empty object>
              disabledRuntimeEnvironmentIds:
                ...
+               items:
+                 <empty object>
+             localizedStudentHints:
+               description: Additional localized hint texts for students (locale => hint text)
+               type: array
+               nullable: False
+               items:
+                 <empty object>
```
### submit_presenter_action_submit
```diff
/v1/exercise-assignments/{id}/submit:
  post:
    ...
    operationId: submitPresenterActionSubmit
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              userId:
                ...
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
              files:
                ...
-               type: string
+               type: array
+               items:
+                 type: string
+                 pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                 example: 10000000-2000-4000-8000-160000000000
```
### submit_presenter_action_pre_submit
```diff
/v1/exercise-assignments/{id}/pre-submit:
  post:
    ...
    operationId: submitPresenterActionPreSubmit
    parameters:
    -
      name: userId
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
-               description: 
+               description: Submitted files
-               nullable: False
+               nullable: True
+               items:
+                 type: string
+                 pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                 example: 10000000-2000-4000-8000-160000000000
```
### groups_presenter_action_subgroups
```diff
/v1/groups/{id}/subgroups:
  get:
    operationId: groupsPresenterActionSubgroups
-   summary: Get a list of subgroups of a group
+   summary: Get a list of subgroups of a group [DEPRECATED]
-   description: Get a list of subgroups of a group
+   description: Get a list of subgroups of a group
[DEPRECATED]: Subgroup list is part of group view.
+   deprecated: True
    ...
```
### groups_presenter_action_members
```diff
/v1/groups/{id}/members:
  get:
    operationId: groupsPresenterActionMembers
-   summary: Get a list of members of a group
+   summary: Get a list of members of a group [DEPRECATED]
-   description: Get a list of members of a group
+   description: Get a list of members of a group
[DEPRECATED]: Members are listed in group view.
+   deprecated: True
    ...
```
### uploaded_files_presenter_action_append_partial
```diff
/v1/uploaded-files/partial/{id}:
  put:
    ...
```
### uploaded_files_presenter_action_cancel_partial
```diff
/v1/uploaded-files/partial/{id}:
  delete:
    ...
```
### uploaded_files_presenter_action_complete_partial
```diff
/v1/uploaded-files/partial/{id}:
  post:
    operationId: uploadedFilesPresenterActionCompletePartial
-   summary: Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.
+   summary: Finalize partial upload and convert the partial file into UploadedFile entity. All data chunks are extracted from the store, assembled into one file, and that is moved back into the store.
-   description: Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.
+   description: Finalize partial upload and convert the partial file into UploadedFile entity. All data chunks are extracted from the store, assembled into one file, and that is moved back into the store.
    ...
```
### uploaded_files_presenter_action_download_exercise_file
```diff
/v1/uploaded-files/supplementary-file/{id}/download:
  get:
-   summary: Download supplementary file
+   summary: Download exercise file [DEPRECATED]
-   description: Download supplementary file
+   description: Download exercise file
[DEPRECATED]: use generic uploaded-file download endpoint instead
-   operationId: uploadedFilesPresenterActionDownloadSupplementaryFile
+   operationId: uploadedFilesPresenterActionDownloadExerciseFile
+   deprecated: True
    ...
```
### users_presenter_action_default
```diff
/v1/users:
  get:
    ...
```
### registration_presenter_action_create_account
```diff
/v1/users:
  post:
    ...
    operationId: registrationPresenterActionCreateAccount
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
              instanceId:
                ...
-               minLength: 1
-               example: text
+               example: 10000000-2000-4000-8000-160000000000
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### pipelines_presenter_action_get_exercise_files
```diff
/v1/pipelines/{id}/supplementary-files:
  get:
-   summary: Get list of all supplementary files for a pipeline
+   summary: Get list of all exercise files for a pipeline
-   description: Get list of all supplementary files for a pipeline
+   description: Get list of all exercise files for a pipeline
-   operationId: pipelinesPresenterActionGetSupplementaryFiles
+   operationId: pipelinesPresenterActionGetExerciseFiles
    ...
```
### pipelines_presenter_action_upload_exercise_files
```diff
/v1/pipelines/{id}/supplementary-files:
  post:
-   summary: Associate supplementary files with a pipeline and upload them to remote file server
+   summary: Associate exercise files with a pipeline and upload them to remote file server
-   description: Associate supplementary files with a pipeline and upload them to remote file server
+   description: Associate exercise files with a pipeline and upload them to remote file server
-   operationId: pipelinesPresenterActionUploadSupplementaryFiles
+   operationId: pipelinesPresenterActionUploadExerciseFiles
    ...
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              files:
                ...
-               description: Identifiers of supplementary files
+               description: Identifiers of exercise files
```
### pipelines_presenter_action_delete_exercise_file
```diff
/v1/pipelines/{id}/supplementary-files/{fileId}:
  delete:
-   summary: Delete supplementary pipeline file with given id
+   summary: Delete exercise file with given id
-   description: Delete supplementary pipeline file with given id
+   description: Delete exercise file with given id
-   operationId: pipelinesPresenterActionDeleteSupplementaryFile
+   operationId: pipelinesPresenterActionDeleteExerciseFile
    parameters:
    -
      name: fileId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    ...
```
### sis_presenter_action_get_terms
```diff
/v1/extensions/sis/terms/:
  get:
    operationId: sisPresenterActionGetTerms
-   summary: Get a list of all registered SIS terms
+   summary: Get a list of all registered SIS terms [DEPRECATED]
-   description: Get a list of all registered SIS terms
+   description: Get a list of all registered SIS terms
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_register_term
```diff
/v1/extensions/sis/terms/:
  post:
    operationId: sisPresenterActionRegisterTerm
-   summary: Register a new term
+   summary: Register a new term [DEPRECATED]
-   description: Register a new term
+   description: Register a new term
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_delete_term
```diff
/v1/extensions/sis/terms/{id}:
  delete:
    operationId: sisPresenterActionDeleteTerm
-   summary: Delete a term
+   summary: Delete a term [DEPRECATED]
-   description: Delete a term
+   description: Delete a term
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_edit_term
```diff
/v1/extensions/sis/terms/{id}:
  post:
    operationId: sisPresenterActionEditTerm
-   summary: Set details of a term
+   summary: Set details of a term [DEPRECATED]
-   description: Set details of a term
+   description: Set details of a term
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_subscribed_courses
```diff
/v1/extensions/sis/users/{userId}/subscribed-groups/{year}/{term}/as-student:
  get:
    operationId: sisPresenterActionSubscribedCourses
-   summary: Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
+   summary: Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names. [DEPRECATED]
-   description: Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
+   description: Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_supervised_courses
```diff
/v1/extensions/sis/users/{userId}/supervised-courses/{year}/{term}:
  get:
    operationId: sisPresenterActionSupervisedCourses
-   summary: Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
+   summary: Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names. [DEPRECATED]
-   description: Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
+   description: Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_possible_parents
```diff
/v1/extensions/sis/remote-courses/{courseId}/possible-parents:
  get:
    operationId: sisPresenterActionPossibleParents
-   summary: Find groups that can be chosen as parents of a group created from given SIS group by current user
+   summary: Find groups that can be chosen as parents of a group created from given SIS group by current user [DEPRECATED]
-   description: Find groups that can be chosen as parents of a group created from given SIS group by current user
+   description: Find groups that can be chosen as parents of a group created from given SIS group by current user
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_create_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/create:
  post:
    operationId: sisPresenterActionCreateGroup
-   summary: Create a new group based on a SIS group
+   summary: Create a new group based on a SIS group [DEPRECATED]
-   description: Create a new group based on a SIS group
+   description: Create a new group based on a SIS group
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_bind_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/bind:
  post:
    operationId: sisPresenterActionBindGroup
-   summary: Bind an existing local group to a SIS group
+   summary: Bind an existing local group to a SIS group [DEPRECATED]
-   description: Bind an existing local group to a SIS group
+   description: Bind an existing local group to a SIS group
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### sis_presenter_action_unbind_group
```diff
/v1/extensions/sis/remote-courses/{courseId}/bindings/{groupId}:
  delete:
    operationId: sisPresenterActionUnbindGroup
-   summary: Delete a binding between a local group and a SIS group
+   summary: Delete a binding between a local group and a SIS group [DEPRECATED]
-   description: Delete a binding between a local group and a SIS group
+   description: Delete a binding between a local group and a SIS group
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### shadow_assignments_presenter_action_create
```diff
/v1/shadow-assignments:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionCreate
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              groupId:
                ...
-               nullable: True
+               nullable: False
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
```
### shadow_assignments_presenter_action_create_points
```diff
/v1/shadow-assignments/{id}/create-points:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionCreatePoints
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              userId:
                ...
-               example: text
+               example: 10000000-2000-4000-8000-160000000000
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
              ...
```
### worker_files_presenter_action_download_exercise_file
```diff
/v1/worker-files/supplementary-file/{hash}:
  get:
-   summary: Sends over an exercise supplementary file (a data file required by the tests).
+   summary: Sends over an exercise file (a data file required by the tests).
-   description: Sends over an exercise supplementary file (a data file required by the tests).
+   description: Sends over an exercise file (a data file required by the tests).
-   operationId: workerFilesPresenterActionDownloadSupplementaryFile
+   operationId: workerFilesPresenterActionDownloadExerciseFile
    parameters:
    -
      name: hash
      ...
-     description: identification of the supplementary file
+     description: identification of the exercise file
    ...
```
### exercise_files_presenter_action_get_exercise_files
```diff
+/v1/exercises/{id}/files:
+ get:
+   summary: Get list of all exercise files for an exercise
+   description: Get list of all exercise files for an exercise
+   operationId: exerciseFilesPresenterActionGetExerciseFiles
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_upload_exercise_files
```diff
+/v1/exercises/{id}/files:
+ post:
+   summary: Associate exercise files with an exercise and upload them to remote file server
+   description: Associate exercise files with an exercise and upload them to remote file server
+   operationId: exerciseFilesPresenterActionUploadExerciseFiles
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             files
+           properties:
+             files:
+               description: Identifiers of exercise files
+               type: string
+               nullable: True
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_delete_exercise_file
```diff
+/v1/exercises/{id}/files/{fileId}:
+ delete:
+   summary: Delete exercise file with given id
+   description: Delete exercise file with given id
+   operationId: exerciseFilesPresenterActionDeleteExerciseFile
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   -
+     name: fileId
+     in: path
+     description: identification of file
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_download_exercise_files_archive
```diff
+/v1/exercises/{id}/files/download-archive:
+ get:
+   summary: Download archive containing all files for exercise.
+   description: Download archive containing all files for exercise.
+   operationId: exerciseFilesPresenterActionDownloadExerciseFilesArchive
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_get_file_links
```diff
+/v1/exercises/{id}/file-links:
+ get:
+   summary: Retrieve a list of all exercise-file links for given exercise.
+   description: Retrieve a list of all exercise-file links for given exercise.
+   operationId: exerciseFilesPresenterActionGetFileLinks
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_create_file_link
```diff
+/v1/exercises/{id}/file-links:
+ post:
+   summary: Create a new exercise-file link for given exercise.
+   description: Create a new exercise-file link for given exercise.
+   operationId: exerciseFilesPresenterActionCreateFileLink
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             exerciseFileId
+           -
+             key
+           properties:
+             exerciseFileId:
+               description: Target file the link will point to
+               type: string
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
+               nullable: False
+             key:
+               description: Internal user-selected identifier of the exercise file link within the exercise
+               type: string
+               pattern: ^[-a-zA-Z0-9_]+$
+               example: text
+               nullable: False
+               maxLength: 16
+               minLength: 1
+             requiredRole:
+               description: Minimal required user role to access the file (null = non-logged-in users)
+               type: string
+               example: text
+               nullable: True
+               maxLength: 255
+               minLength: 1
+             saveName:
+               description: File name override (the file will be downloaded under this name instead of the original name)
+               type: string
+               example: text
+               nullable: True
+               maxLength: 255
+               minLength: 1
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_delete_file_link
```diff
+/v1/exercises/{id}/file-links/{linkId}:
+ delete:
+   summary: Delete a specific exercise-file link.
+   description: Delete a specific exercise-file link.
+   operationId: exerciseFilesPresenterActionDeleteFileLink
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   -
+     name: linkId
+     in: path
+     description: of the exercise file link
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### exercise_files_presenter_action_update_file_link
```diff
+/v1/exercises/{id}/file-links/{linkId}:
+ post:
+   summary: Update a specific exercise-file link. Missing arguments are not changed.
+   description: Update a specific exercise-file link. Missing arguments are not changed.
+   operationId: exerciseFilesPresenterActionUpdateFileLink
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   -
+     name: linkId
+     in: path
+     description: of the exercise file link
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           properties:
+             key:
+               description: Internal user-selected identifier of the exercise file link within the exercise
+               type: string
+               pattern: ^[-a-zA-Z0-9_]+$
+               example: text
+               nullable: False
+               maxLength: 16
+               minLength: 1
+             requiredRole:
+               description: Minimal required user role to access the file (null = non-logged-in users)
+               type: string
+               example: text
+               nullable: True
+               maxLength: 255
+               minLength: 1
+             saveName:
+               description: File name override (the file will be downloaded under this name instead of the original name)
+               type: string
+               example: text
+               nullable: True
+               maxLength: 255
+               minLength: 1
+   responses:
+     200:
+       description: Placeholder response
```
### uploaded_files_presenter_action_download_exercise_file_link_by_key
```diff
+/v1/exercises/{id}/file-download/{linkKey}:
+ get:
+   summary: Download a specific exercise-file via its link key. Unlike `downloadFileLink`, the key is selected by the user and does not have to change (when the link or the file is updated). On the other hand, it always retrieves the latest version of the file.
+   description: Download a specific exercise-file via its link key. Unlike `downloadFileLink`, the key is selected by the user and does not have to change (when the link or the file is updated). On the other hand, it always retrieves the latest version of the file.
+   operationId: uploadedFilesPresenterActionDownloadExerciseFileLinkByKey
+   parameters:
+   -
+     name: id
+     in: path
+     description: of exercise
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   -
+     name: linkKey
+     in: path
+     description: Internal user-selected identifier of the exercise file link within the exercise
+     required: True
+     schema:
+       type: string
+       nullable: False
+       maxLength: 16
+       minLength: 1
+   responses:
+     200:
+       description: Placeholder response
```
### assignments_presenter_action_update_localized_texts
```diff
+/v1/exercise-assignments/{id}/localized-texts:
+ post:
+   summary: Update (only) the localized texts of an assignment. This is a separate operations since the texts are taken over from the exercise. Updating them is an override of the exercise specification and needs to be handled carefully.
+   description: Update (only) the localized texts of an assignment. This is a separate operations since the texts are taken over from the exercise. Updating them is an override of the exercise specification and needs to be handled carefully.
+   operationId: assignmentsPresenterActionUpdateLocalizedTexts
+   parameters:
+   -
+     name: id
+     in: path
+     description: Identifier of the updated assignment
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             version
+           -
+             localizedTexts
+           properties:
+             version:
+               description: Version of the edited assignment
+               type: integer
+               example: 0
+               nullable: False
+             localizedTexts:
+               description: Localized texts with exercise/assignment specification
+               type: array
+               nullable: False
+               items:
+                 <empty object>
+   responses:
+     200:
+       description: Placeholder response
```
### groups_presenter_action_set_exam
```diff
+/v1/groups/{id}/exam:
+ post:
+   summary: Change the group 'exam' indicator. If denotes that the group should be listed in exam groups instead of regular groups and the assignments should have 'isExam' flag set by default.
+   description: Change the group 'exam' indicator. If denotes that the group should be listed in exam groups instead of regular groups and the assignments should have 'isExam' flag set by default.
+   operationId: groupsPresenterActionSetExam
+   parameters:
+   -
+     name: id
+     in: path
+     description: An identifier of the updated group
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             value
+           properties:
+             value:
+               description: The value of the flag
+               type: boolean
+               example: true
+               nullable: False
+   responses:
+     200:
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
+                 description: Whether the request was processed successfully.
+                 type: boolean
+                 example: true
+                 nullable: False
+               code:
+                 description: HTTP response code.
+                 type: integer
+                 example: 0
+                 nullable: False
+               payload:
+                 description: The payload of the response.
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
+                         description: IDs of all group supervisors
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       observers:
+                         description: IDs of all group observers
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       students:
+                         description: IDs of the students of this group
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       instanceId:
+                         description: ID of an instance in which the group belongs
+                         type: string
+                         pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                         example: 10000000-2000-4000-8000-160000000000
+                         nullable: False
+                       hasValidLicence:
+                         description: Whether the instance where the group belongs has a valid license
+                         type: boolean
+                         example: true
+                         nullable: False
+                       assignments:
+                         description: IDs of all group assignments
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       shadowAssignments:
+                         description: IDs of all group shadow assignments
+                         type: array
+                         nullable: False
+                         items:
+                           type: string
+                           pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+                           example: 10000000-2000-4000-8000-160000000000
+                       publicStats:
+                         description: Whether the student's results are visible to other students
+                         type: boolean
+                         example: true
+                         nullable: False
+                       detaining:
+                         description: Whether the group detains the students (so they can be released only by the teacher)
+                         type: boolean
+                         example: true
+                         nullable: False
+                       threshold:
+                         description: A relative number of points a student must receive from assignments to fulfill the requirements of the group
+                         type: number
+                         example: 0.1
+                         nullable: False
+                       pointsLimit:
+                         description: A minimal number of points that a student must receive to fulfill the group's requirements
+                         type: integer
+                         example: 0
+                         nullable: False
+                       bindings:
+                         description: Entities bound to the group
+                         type: array
+                         nullable: False
+                         items:
+                           <empty object>
+                       examBegin:
+                         description: The time when the exam starts if there is an exam scheduled
+                         type: integer
+                         example: 1740135333
+                         nullable: False
+                       examEnd:
+                         description: The time when the exam ends if there is an exam scheduled
+                         type: integer
+                         example: 1740135333
+                         nullable: False
+                       examLockStrict:
+                         description: Whether the scheduled exam requires a strict access lock
+                         type: boolean
+                         example: true
+                         nullable: False
+                       exams:
+                         description: All past exams (with at least one student locked)
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
### uploaded_files_presenter_action_download_exercise_file_by_link
```diff
+/v1/uploaded-files/link/{id}:
+ get:
+   summary: Download a specific exercise-file via its link. This endpoint is deliberately placed in UploadedFilesPresenter so it works for non-logged-in users as well.
+   description: Download a specific exercise-file via its link. This endpoint is deliberately placed in UploadedFilesPresenter so it works for non-logged-in users as well.
+   operationId: uploadedFilesPresenterActionDownloadExerciseFileByLink
+   parameters:
+   -
+     name: id
+     in: path
+     description: of the exercise file link entity
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### users_presenter_action_find_by_external_login
```diff
+/v1/users/external-login/{service}/{externalId}:
+ get:
+   summary: Get details of a user identified via external login.
+   description: Get details of a user identified via external login.
+   operationId: usersPresenterActionFindByExternalLogin
+   parameters:
+   -
+     name: service
+     in: path
+     description: External authentication service name
+     required: True
+     schema:
+       type: string
+       nullable: False
+       minLength: 1
+   -
+     name: externalId
+     in: path
+     description: External user identifier
+     required: True
+     schema:
+       type: string
+       nullable: False
+       minLength: 1
+   responses:
+     200:
+       description: Placeholder response
```
### users_presenter_action_set_allowed
```diff
+/v1/users/{id}/allowed:
+ post:
+   summary: Set 'isAllowed' flag of the given user. The flag determines whether a user may perform any operation of the API.
+   description: Set 'isAllowed' flag of the given user. The flag determines whether a user may perform any operation of the API.
+   operationId: usersPresenterActionSetAllowed
+   parameters:
+   -
+     name: id
+     in: path
+     description: Identifier of the user
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             isAllowed
+           properties:
+             isAllowed:
+               description: Whether the user is allowed (active) or not.
+               type: boolean
+               example: true
+               nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### pipelines_presenter_action_get_exercise_files
```diff
+/v1/pipelines/{id}/exercise-files:
+ get:
+   summary: Get list of all exercise files for a pipeline
+   description: Get list of all exercise files for a pipeline
+   operationId: pipelinesPresenterActionGetExerciseFiles
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of pipeline
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### pipelines_presenter_action_upload_exercise_files
```diff
+/v1/pipelines/{id}/exercise-files:
+ post:
+   summary: Associate exercise files with a pipeline and upload them to remote file server
+   description: Associate exercise files with a pipeline and upload them to remote file server
+   operationId: pipelinesPresenterActionUploadExerciseFiles
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of pipeline
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           required:
+           -
+             files
+           properties:
+             files:
+               description: Identifiers of exercise files
+               type: string
+               nullable: True
+   responses:
+     200:
+       description: Placeholder response
```
### pipelines_presenter_action_delete_exercise_file
```diff
+/v1/pipelines/{id}/exercise-files/{fileId}:
+ delete:
+   summary: Delete exercise file with given id
+   description: Delete exercise file with given id
+   operationId: pipelinesPresenterActionDeleteExerciseFile
+   parameters:
+   -
+     name: id
+     in: path
+     description: identification of pipeline
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   -
+     name: fileId
+     in: path
+     description: identification of file
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### worker_files_presenter_action_download_exercise_file
```diff
+/v1/worker-files/exercise-file/{hash}:
+ get:
+   summary: Sends over an exercise file (a data file required by the tests).
+   description: Sends over an exercise file (a data file required by the tests).
+   operationId: workerFilesPresenterActionDownloadExerciseFile
+   parameters:
+   -
+     name: hash
+     in: path
+     description: identification of the exercise file
+     required: True
+     schema:
+       type: string
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### security_presenter_action_check
```diff
/v1/security/check:
  post:
    operationId: securityPresenterActionCheck
+   summary: A preflight test whether given URL (and HTTP method) would be allowed by internal ACL checks (for the current user).
+   description: A preflight test whether given URL (and HTTP method) would be allowed by internal ACL checks (for the current user).
    ...
```
### login_presenter_action_default
```diff
/v1/login:
  post:
    ...
    operationId: loginPresenterActionDefault
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
+             expiration:
+               description: Token expiration in seconds (not greater than the default)
+               type: integer
+               example: 0
+               nullable: False
```
### login_presenter_action_take_over
```diff
/v1/login/takeover/{userId}:
  post:
    ...
    operationId: loginPresenterActionTakeOver
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### login_presenter_action_external
```diff
/v1/login/{authenticatorName}:
  post:
    ...
    operationId: loginPresenterActionExternal
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              ...
+             expiration:
+               description: Token expiration in seconds (not greater than the default)
+               type: integer
+               example: 0
+               nullable: False
```
### comments_presenter_action_set_private
```diff
/v1/comments/{threadId}/comment/{commentId}/private:
  post:
    ...
    operationId: commentsPresenterActionSetPrivate
    parameters:
    -
      name: threadId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: commentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### comments_presenter_action_delete
```diff
/v1/comments/{threadId}/comment/{commentId}:
  delete:
    ...
    operationId: commentsPresenterActionDelete
    parameters:
    -
      name: threadId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    -
      name: commentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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
```
### exercises_presenter_action_create
```diff
/v1/exercises:
  post:
    ...
    operationId: exercisesPresenterActionCreate
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              groupId:
                ...
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
```
### exercises_presenter_action_authors
```diff
/v1/exercises/authors:
  get:
    ...
    operationId: exercisesPresenterActionAuthors
    parameters:
    -
      name: instanceId
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
```
### exercises_presenter_action_fork_from
```diff
/v1/exercises/{id}/fork:
  post:
    ...
    operationId: exercisesPresenterActionForkFrom
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              groupId:
                ...
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
```
### exercises_presenter_action_detach_group
```diff
/v1/exercises/{id}/groups/{groupId}:
  delete:
    ...
    operationId: exercisesPresenterActionDetachGroup
    parameters:
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### exercises_presenter_action_attach_group
```diff
/v1/exercises/{id}/groups/{groupId}:
  post:
    ...
    operationId: exercisesPresenterActionAttachGroup
    parameters:
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignments_presenter_action_create
```diff
/v1/exercise-assignments:
  post:
    ...
    operationId: assignmentsPresenterActionCreate
    requestBody:
      content:
        application/json:
          schema:
            ...
            properties:
              exerciseId:
                ...
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
              groupId:
                ...
+               pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+               example: 10000000-2000-4000-8000-160000000000
```
### assignments_presenter_action_user_solutions
```diff
/v1/exercise-assignments/{id}/users/{userId}/solutions:
  get:
    ...
    operationId: assignmentsPresenterActionUserSolutions
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignments_presenter_action_best_solution
```diff
/v1/exercise-assignments/{id}/users/{userId}/best-solution:
  get:
    ...
    operationId: assignmentsPresenterActionBestSolution
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignments_presenter_action_sync_with_exercise
```diff
/v1/exercise-assignments/{id}/sync-exercise:
  post:
    ...
    operationId: assignmentsPresenterActionSyncWithExercise
+   requestBody:
+     content:
+       application/json:
+         schema:
+           type: object
+           properties:
+             syncOptions:
+               description: List of options what to synchronize (if missing, everything is synchronized)
+               type: array
+               nullable: False
+               items:
+                 type: string
+                 pattern: ^(configurationType|exerciseConfig|exerciseEnvironmentConfigs|exerciseTests|files|fileLinks|hardwareGroups|limits|localizedTexts|mergeJudgeLogs|runtimeEnvironments|scoreConfig)$
+                 example: text
+                 maxLength: 32
+                 minLength: 1
```
### submit_presenter_action_can_submit
```diff
/v1/exercise-assignments/{id}/can-submit:
  get:
    ...
    operationId: submitPresenterActionCanSubmit
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_relocate
```diff
/v1/groups/{id}/relocate/{newParentId}:
  post:
    ...
    operationId: groupsPresenterActionRelocate
    parameters:
    -
      name: newParentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_students_stats
```diff
/v1/groups/{id}/students/{userId}:
  get:
    ...
    operationId: groupsPresenterActionStudentsStats
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_remove_student
```diff
/v1/groups/{id}/students/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionRemoveStudent
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
        ...
        content:
          application/json:
            schema:
              ...
              properties:
                ...
                payload:
                  ...
                  properties:
                    ...
                    localizedTexts:
                      ...
+                     items:
+                       <empty object>
                    privateData:
                      ...
                      properties:
                        ...
                        bindings:
                          ...
+                         items:
+                           <empty object>
                        exams:
                          ...
+                         items:
+                           <empty object>
                    permissionHints:
                      ...
+                     items:
+                       <empty object>
```
### groups_presenter_action_add_student
```diff
/v1/groups/{id}/students/{userId}:
  post:
    ...
    operationId: groupsPresenterActionAddStudent
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
        ...
        content:
          application/json:
            schema:
              ...
              properties:
                ...
                payload:
                  ...
                  properties:
                    ...
                    localizedTexts:
                      ...
+                     items:
+                       <empty object>
                    privateData:
                      ...
                      properties:
                        ...
                        bindings:
                          ...
+                         items:
+                           <empty object>
                        exams:
                          ...
+                         items:
+                           <empty object>
                    permissionHints:
                      ...
+                     items:
+                       <empty object>
```
### groups_presenter_action_students_solutions
```diff
/v1/groups/{id}/students/{userId}/solutions:
  get:
    ...
    operationId: groupsPresenterActionStudentsSolutions
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_unlock_student
```diff
/v1/groups/{id}/lock/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionUnlockStudent
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_lock_student
```diff
/v1/groups/{id}/lock/{userId}:
  post:
    ...
    operationId: groupsPresenterActionLockStudent
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### groups_presenter_action_remove_member
```diff
/v1/groups/{id}/members/{userId}:
  delete:
    ...
    operationId: groupsPresenterActionRemoveMember
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
        ...
        content:
          application/json:
            schema:
              ...
              properties:
                ...
                payload:
                  ...
                  properties:
                    ...
                    localizedTexts:
                      ...
+                     items:
+                       <empty object>
                    privateData:
                      ...
                      properties:
                        ...
                        bindings:
                          ...
+                         items:
+                           <empty object>
                        exams:
                          ...
+                         items:
+                           <empty object>
                    permissionHints:
                      ...
+                     items:
+                       <empty object>
```
### groups_presenter_action_add_member
```diff
/v1/groups/{id}/members/{userId}:
  post:
    ...
    operationId: groupsPresenterActionAddMember
    parameters:
    -
      name: userId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
    responses:
      200:
        ...
        content:
          application/json:
            schema:
              ...
              properties:
                ...
                payload:
                  ...
                  properties:
                    ...
                    localizedTexts:
                      ...
+                     items:
+                       <empty object>
                    privateData:
                      ...
                      properties:
                        ...
                        bindings:
                          ...
+                         items:
+                           <empty object>
                        exams:
                          ...
+                         items:
+                           <empty object>
                    permissionHints:
                      ...
+                     items:
+                       <empty object>
```
### group_invitations_presenter_action_list
```diff
/v1/groups/{groupId}/invitations:
  get:
    ...
    operationId: groupInvitationsPresenterActionList
    parameters:
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### group_invitations_presenter_action_create
```diff
/v1/groups/{groupId}/invitations:
  post:
    ...
    operationId: groupInvitationsPresenterActionCreate
    parameters:
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### group_invitations_presenter_action_default
```diff
/v1/group-invitations/{id}:
  get:
    ...
```
### group_invitations_presenter_action_remove
```diff
/v1/group-invitations/{id}:
  delete:
    operationId: groupInvitationsPresenterActionRemove
+   summary: Remove the invitation.
+   description: Remove the invitation.
    ...
```
### group_invitations_presenter_action_update
```diff
/v1/group-invitations/{id}:
  post:
    ...
```
### group_external_attributes_presenter_action_get
```diff
/v1/group-attributes/{groupId}:
+ get:
+   summary: Get all external attributes for a group. This endpoint is meant to be used by webapp to display the attributes.
+   description: Get all external attributes for a group. This endpoint is meant to be used by webapp to display the attributes.
+   operationId: groupExternalAttributesPresenterActionGet
+   parameters:
+   -
+     name: groupId
+     in: path
+     description: 
+     required: True
+     schema:
+       type: string
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
+       nullable: False
+   responses:
+     200:
+       description: Placeholder response
```
### group_external_attributes_presenter_action_remove
```diff
/v1/group-attributes/{groupId}:
  delete:
    ...
```
### group_external_attributes_presenter_action_add
```diff
/v1/group-attributes/{groupId}:
  post:
    ...
```
### instances_presenter_action_delete_licence
```diff
/v1/instances/licences/{licenceId}:
  delete:
    ...
    operationId: instancesPresenterActionDeleteLicence
    parameters:
    -
      name: licenceId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### instances_presenter_action_update_licence
```diff
/v1/instances/licences/{licenceId}:
  post:
    ...
    operationId: instancesPresenterActionUpdateLicence
    parameters:
    -
      name: licenceId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_solutions
```diff
/v1/reference-solutions/exercise/{exerciseId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSolutions
    parameters:
    -
      name: exerciseId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_pre_submit
```diff
/v1/reference-solutions/exercise/{exerciseId}/pre-submit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionPreSubmit
    parameters:
    -
      name: exerciseId
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
```
### reference_exercise_solutions_presenter_action_submit
```diff
/v1/reference-solutions/exercise/{exerciseId}/submit:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmit
    parameters:
    -
      name: exerciseId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_resubmit_all
```diff
/v1/reference-solutions/exercise/{exerciseId}/resubmit-all:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionResubmitAll
    parameters:
    -
      name: exerciseId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_detail
```diff
/v1/reference-solutions/{solutionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDetail
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_delete_reference_solution
```diff
/v1/reference-solutions/{solutionId}:
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteReferenceSolution
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_update
```diff
/v1/reference-solutions/{solutionId}:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionUpdate
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_submissions
```diff
/v1/reference-solutions/{solutionId}/submissions:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmissions
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_download_solution_archive
```diff
/v1/reference-solutions/{solutionId}/download-solution:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDownloadSolutionArchive
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_set_visibility
```diff
/v1/reference-solutions/{solutionId}/visibility:
  post:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSetVisibility
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_submission
```diff
/v1/reference-solutions/submission/{submissionId}:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionSubmission
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_delete_submission
```diff
/v1/reference-solutions/submission/{submissionId}:
  delete:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDeleteSubmission
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_download_result_archive
```diff
/v1/reference-solutions/submission/{submissionId}/download-result:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionDownloadResultArchive
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### reference_exercise_solutions_presenter_action_evaluation_score_config
```diff
/v1/reference-solutions/submission/{submissionId}/score-config:
  get:
    ...
    operationId: referenceExerciseSolutionsPresenterActionEvaluationScoreConfig
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solutions_presenter_action_submission
```diff
/v1/assignment-solutions/submission/{submissionId}:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionSubmission
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solutions_presenter_action_delete_submission
```diff
/v1/assignment-solutions/submission/{submissionId}:
  delete:
    ...
    operationId: assignmentSolutionsPresenterActionDeleteSubmission
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solutions_presenter_action_download_result_archive
```diff
/v1/assignment-solutions/submission/{submissionId}/download-result:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionDownloadResultArchive
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solutions_presenter_action_evaluation_score_config
```diff
/v1/assignment-solutions/submission/{submissionId}/score-config:
  get:
    ...
    operationId: assignmentSolutionsPresenterActionEvaluationScoreConfig
    parameters:
    -
      name: submissionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solution_reviews_presenter_action_delete_comment
```diff
/v1/assignment-solutions/{id}/review-comment/{commentId}:
  delete:
    ...
    operationId: assignmentSolutionReviewsPresenterActionDeleteComment
    parameters:
    -
      name: commentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### assignment_solution_reviews_presenter_action_edit_comment
```diff
/v1/assignment-solutions/{id}/review-comment/{commentId}:
  post:
    ...
    operationId: assignmentSolutionReviewsPresenterActionEditComment
    parameters:
    -
      name: commentId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### sis_presenter_action_status
```diff
/v1/extensions/sis/status/:
  get:
    operationId: sisPresenterActionStatus
+   summary: Check SIS status for the current user. [DEPRECATED]
+   description: Check SIS status for the current user.
[DEPRECATED]: Use the new SIS extension instead
+   deprecated: True
    ...
```
### emails_presenter_action_send_to_group_members
```diff
/v1/emails/groups/{groupId}:
  post:
    ...
    operationId: emailsPresenterActionSendToGroupMembers
    parameters:
    -
      name: groupId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### shadow_assignments_presenter_action_remove_points
```diff
/v1/shadow-assignments/points/{pointsId}:
  delete:
    ...
    operationId: shadowAssignmentsPresenterActionRemovePoints
    parameters:
    -
      name: pointsId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### shadow_assignments_presenter_action_update_points
```diff
/v1/shadow-assignments/points/{pointsId}:
  post:
    ...
    operationId: shadowAssignmentsPresenterActionUpdatePoints
    parameters:
    -
      name: pointsId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### plagiarism_presenter_action_get_similarities
```diff
/v1/plagiarism/{id}/{solutionId}:
  get:
    ...
    operationId: plagiarismPresenterActionGetSimilarities
    parameters:
    -
      name: solutionId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
### plagiarism_presenter_action_add_similarities
```diff
/v1/plagiarism/{id}/{solutionId}:
  post:
    ...
    operationId: plagiarismPresenterActionAddSimilarities
    parameters:
    -
      name: solutionId
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
```
### extensions_presenter_action_url
```diff
/v1/extensions/{extId}/{instanceId}:
  get:
    ...
    operationId: extensionsPresenterActionUrl
    parameters:
    -
      name: instanceId
      ...
      schema:
        ...
+       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
