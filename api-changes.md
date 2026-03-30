### exercise_files_presenter_action_upload_exercise_files
```diff
-/v1/exercises/{id}/supplementary-files:
- post:
-   summary: Associate exercise files with an exercise and upload them to remote file server
-   description: Associate exercise files with an exercise and upload them to remote file server
-   operationId: exerciseFilesPresenterActionUploadExerciseFiles
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   requestBody:
-     content:
-       application/json:
-         schema:
-           type: object
-           required:
-           -
-             files
-           properties:
-             files:
-               description: Identifiers of exercise files
-               type: string
-               nullable: True
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_get_exercise_files
```diff
-/v1/exercises/{id}/supplementary-files:
- get:
-   summary: Get list of all exercise files for an exercise
-   description: Get list of all exercise files for an exercise
-   operationId: exerciseFilesPresenterActionGetExerciseFiles
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_delete_exercise_file
```diff
-/v1/exercises/{id}/supplementary-files/{fileId}:
- delete:
-   summary: Delete exercise file with given id
-   description: Delete exercise file with given id
-   operationId: exerciseFilesPresenterActionDeleteExerciseFile
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   -
-     name: fileId
-     in: path
-     description: identification of file
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_download_exercise_files_archive
```diff
-/v1/exercises/{id}/supplementary-files/download-archive:
- get:
-   summary: Download archive containing all files for exercise.
-   description: Download archive containing all files for exercise.
-   operationId: exerciseFilesPresenterActionDownloadExerciseFilesArchive
-   parameters:
-   -
-     name: id
-     in: path
-     description: of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_upload_attachment_files
```diff
-/v1/exercises/{id}/attachment-files:
- post:
-   summary: Associate attachment exercise files with an exercise [DEPRECATED]
-   description: Associate attachment exercise files with an exercise
[DEPRECATED]: attachment files were unified with exercise files
-   operationId: exerciseFilesPresenterActionUploadAttachmentFiles
-   deprecated: True
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   requestBody:
-     content:
-       application/json:
-         schema:
-           type: object
-           required:
-           -
-             files
-           properties:
-             files:
-               description: Identifiers of attachment files
-               type: string
-               nullable: True
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_get_attachment_files
```diff
-/v1/exercises/{id}/attachment-files:
- get:
-   summary: Get a list of all attachment files for an exercise [DEPRECATED]
-   description: Get a list of all attachment files for an exercise
[DEPRECATED]: attachment files were unified with exercise files
-   operationId: exerciseFilesPresenterActionGetAttachmentFiles
-   deprecated: True
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_delete_attachment_file
```diff
-/v1/exercises/{id}/attachment-files/{fileId}:
- delete:
-   summary: Delete attachment exercise file with given id [DEPRECATED]
-   description: Delete attachment exercise file with given id
[DEPRECATED]: attachment files were unified with exercise files
-   operationId: exerciseFilesPresenterActionDeleteAttachmentFile
-   deprecated: True
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   -
-     name: fileId
-     in: path
-     description: identification of file
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### exercise_files_presenter_action_download_attachment_files_archive
```diff
-/v1/exercises/{id}/attachment-files/download-archive:
- get:
-   summary: Download archive containing all attachment files for exercise. [DEPRECATED]
-   description: Download archive containing all attachment files for exercise.
[DEPRECATED]: attachment files were unified with exercise files
-   operationId: exerciseFilesPresenterActionDownloadAttachmentFilesArchive
-   deprecated: True
-   parameters:
-   -
-     name: id
-     in: path
-     description: of exercise
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### uploaded_files_presenter_action_download_exercise_file
```diff
-/v1/uploaded-files/supplementary-file/{id}/download:
- get:
-   summary: Download exercise file [DEPRECATED]
-   description: Download exercise file
[DEPRECATED]: use generic uploaded-file download endpoint instead
-   operationId: uploadedFilesPresenterActionDownloadExerciseFile
-   deprecated: True
-   parameters:
-   -
-     name: id
-     in: path
-     description: Identifier of the file
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### pipelines_presenter_action_upload_exercise_files
```diff
-/v1/pipelines/{id}/supplementary-files:
- post:
-   summary: Associate exercise files with a pipeline and upload them to remote file server
-   description: Associate exercise files with a pipeline and upload them to remote file server
-   operationId: pipelinesPresenterActionUploadExerciseFiles
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of pipeline
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   requestBody:
-     content:
-       application/json:
-         schema:
-           type: object
-           required:
-           -
-             files
-           properties:
-             files:
-               description: Identifiers of exercise files
-               type: string
-               nullable: True
-   responses:
-     200:
-       description: Placeholder response
```
### pipelines_presenter_action_get_exercise_files
```diff
-/v1/pipelines/{id}/supplementary-files:
- get:
-   summary: Get list of all exercise files for a pipeline
-   description: Get list of all exercise files for a pipeline
-   operationId: pipelinesPresenterActionGetExerciseFiles
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of pipeline
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### pipelines_presenter_action_delete_exercise_file
```diff
-/v1/pipelines/{id}/supplementary-files/{fileId}:
- delete:
-   summary: Delete exercise file with given id
-   description: Delete exercise file with given id
-   operationId: pipelinesPresenterActionDeleteExerciseFile
-   parameters:
-   -
-     name: id
-     in: path
-     description: identification of pipeline
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   -
-     name: fileId
-     in: path
-     description: identification of file
-     required: True
-     schema:
-       type: string
-       pattern: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
### worker_files_presenter_action_download_exercise_file
```diff
-/v1/worker-files/supplementary-file/{hash}:
- get:
-   summary: Sends over an exercise file (a data file required by the tests).
-   description: Sends over an exercise file (a data file required by the tests).
-   operationId: workerFilesPresenterActionDownloadExerciseFile
-   parameters:
-   -
-     name: hash
-     in: path
-     description: identification of the exercise file
-     required: True
-     schema:
-       type: string
-       nullable: False
-   responses:
-     200:
-       description: Placeholder response
```
