
# Drutex CRUD App Backend (API)

CRUD-app with different user-permissions for the code-review.

## Used Technologies

Python 3.9.6, Django 3.2, djangorestframework, postgreSQL, drf-nested-routers
Docker, Github-Actions for unittest-jobs, psycopg2 (db-connector)

## Applied principles
- TDD using Python unit testing framework
- DRY (don`t repeat yourself)

## API Reference

#
## Version: 0.0.0

### /login/

#### POST
##### Description:

Create auth token for user

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /myuser/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /notes/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /notes/{note_pk}/note-items/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### POST
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /notes/{note_pk}/note-items/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note item. | Yes | integer |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note item. | Yes | integer |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note item. | Yes | integer |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note item. | Yes | integer |
| note_pk | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /notes/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this note. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /schema/

#### GET
##### Description:

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| format | query |  | No | string |
| lang | query |  | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /todos/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /todos/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this task. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this task. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this task. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this task. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /users/

#### GET
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### POST
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /users/{id}/

#### GET
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### DELETE
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

### /users/{id}/userprofile/

#### GET
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### POST
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PUT
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### PATCH
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |

#### DELETE
##### Description:

Allows unauthenticated users to create
a new user, but requires authentication to retrieve, update, delete

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| tokenAuth | |


#### TODOs

```http
    GET & POST: /todos/
```
```http
    POST: /todos/
```
```http
    GET, PUT, DELETE: /todos/${id}
```

#### Users
```http
    GET & POST: /users/
```
```http
    GET, PUT, DELETE: /users/${id}
```
#### Users TODOs
```http
    GET & POST: /users/todos
```
```http
    GET, PUT, DELETE: /users/${id}/todos/${task_id}
```
#### Users Notes (List of what a user needs to do)
```http
    GET, POST: /users/${id}/notes
```
```http
    GET, PUT, DELETE: /users/${id}/notes/${note_id}
```
```http
    POST: /users/${id}/notes/${note_id}/note-items
```
```http
    PUT, DELETE: /users/${id}/note-items/${item_id}
```


#### necessary fields

## Task

 - user
 - title
 - description
 - completed
 - created_at
 - updated_at

## Notes

 - name
 - description
 - user
 - created_at
 - updated_at

 ## NoteItem

 - text
 - note
 - created_at
 - updated_at

 ## User

 - email (login)
 - password


 ### Authorization

 - /login with valid email and pw will provide token for frontend

 ### API docs

 - added OpenAPI swagger docs


 added
  - /users/ POST create new user (with email and password only, or including userprofile object) FINISHED -> NO AUTH token required
  - /user/{id}/ GET user by id FINISHED -> AUTH token required
  - /user/{id}/ PUT/PATCH/DELETE (update user) FINISHED -> password and auth token required

  explicit userprofile updates should be handled via /users/{id}/userprofile/

  - /users/{id}/userprofile/ GET POST PUT PATCH DELETE finished ( POST aswell possible via /users/ to make it possible to send one request from frontend for newly created users with optional userprofile-data)

