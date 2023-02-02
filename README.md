
# Drutex CRUD App Backend (API)

CRUD-app with different user-permissions for the code-review.



## Used Technologies

Python 3.9.6, Django 3.2, djangorestframework, postgreSQL, drf-nested-routers
Docker, Github-Actions for unittest-jobs, psycopg2 (db-connector)

## Applied principles
- TDD using Python unit testing framework
- DRY (don`t repeat yourself)

## API Reference
JSON returns 
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
 



