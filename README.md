
# Drutex CRUD App Backend (API)

CRUD-app with different user-permissions for the interview on the 26th of January 2023.



## Used Technologies

Python 3.9.6, Django 3.2, djangorestframework, mysqlclient, drf-nested-routers


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
 



