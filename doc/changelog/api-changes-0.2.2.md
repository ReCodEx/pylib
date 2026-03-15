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
+     style: deepObject
```
