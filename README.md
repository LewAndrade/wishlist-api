# Wishlist API

This is a REST API to a Wishlist application made using Flask and MongoDB.

## Install

    docker-compose build

## Run the app

    docker-compose up -d

# REST API

The API is hosted at `http://localhost:5000/api/v1`.

## User SignUp

For Creating a new User account.

### Request

#### URL: `POST /auth/signup`

```json
{
  "email": "<string>",
  "password": "<string --min-length:6>"
}
```
###### _body_

### Response

```json
{
  "id": "<user_id>"
}
```
###### _body_

## User Login

By sending a User's correct credentials you receive an `JWT bearer token`.

### Request:

#### URL: `POST /auth/signup`

```json
{
  "email": "<string>",
  "password": "<string min-length:6>"
}
```
###### _body_

### Response

```json
{
  "token": "<jwt-bearer-token>"
}
```
###### _body_

---
> ## Authentication required endpoints
> All request on the API besides User Signup and User Login requires the user to be logged in.\
> To do so, use the `JWT bearer token` retrieved at User Login as the Authentication method for the requests.|
---

## Get Wishlist

Get the Wishlist of the current user.

### Request:

#### URL: `GET /wishlist`

### Response

```json
[
  {
    "_id": {
      "$oid": "<wish_id>"
    },
    "name": "<string>",
    "description": "<string>",
    "url": "<string>",
    "image": "<string>",
    "added_by": {
      "$oid": "<user_id>"
    }
  }
]
```
###### _body_

## Get Random Wish

Get a random wish from the User's Wishlist.

### Request:

#### URL: `GET /wishlist/random`

### Response

```json
{
  "_id": {
    "$oid": "<wish_id>"
  },
  "name": "<string>",
  "description": "<string>",
  "url": "<string>",
  "image": "<string>",
  "added_by": {
    "$oid": "<user_id>"
  }
}
```
###### _body_

## Get Wish

Get a single wish from the user's Wishlist.

### Request:

#### URL: `GET /wishlist/<wish_id>`

### Response

```json
{
  "_id": {
    "$oid": "<wish_id>"
  },
  "name": "<string>",
  "description": "<string>",
  "url": "<string>",
  "image": "<string>",
  "added_by": {
    "$oid": "<user_id>"
  }
}
```
###### _body_



## Update Wish

Update a wish from the User's Wishlist.

### Request:

#### URL: `PUT /wishlist/<wish_id>`

```json
{
  "name": "<string:optional>",
  "description": "<string:optional>",
  "url": "<string:optional>",
  "image": "<string:optional>"
}
```
###### _body_

### Response

```json
"Wish updated"
```

###### _body_

## Delete Wishlist

Update a wish from the User's Wishlist.

### Request:

#### URL: `DELETE /wishlist`
### Response

```json
"Wish deleted"
```
###### _body_
