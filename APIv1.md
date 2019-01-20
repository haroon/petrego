# Pet Registry
----
## Description

This document descibes the REST API of the The PetRego pet registry service.

PetRego maintain a list of owners, their pets, and attributes. With this service
they provide API to query information about following:

- The owner's name
- The pet's name
- The type of animal

----
## Version

This document describes the version 1 of the PetRego API.

----

## Usage

All *GET* responses will have the form

```json
{
    "data": "List of result sets"
}
```

All *POST* and *PUT* responses will have one of two forms depending on if the operation was successful or if an error occurred.

**Error:**
```Relevant HTTP Error Code```

**Success:**


- ```HTTP Success Code```
- ```json
{
    "links": {
        "href": API end point,
        "rel": Relation,
        "type": METHOD
    }
}
```

----

## API Reference

### Add a new animal

**Description**

Record a new animal and food it eats.

**Definition**

`POST /animalfoods/<animal>/<food>/`

**Arguments**

- `"animal":string` The name of animal
- `"food":string` The food it eats

**Response**

- `201` on success
```json
{
    "links": [
        {
            "href": "animalfoods/<animal>/",
            "rel": "animalfoods.search",
            "type": "GET"
        },        
        {
            "href": "animalfoods/<animal>/<food>",
            "rel": "animalfoods.update",
            "type": "PUT"
        }
    ]
}```
- `422` if animal already exists

### Update an existing animal

**Description**

Update the food for an existing animal.

**Definition**

`PUT /animalfoods/<animal>/<food>/`

**Arguments**

- `"animal":string` The name of animal
- `"food":string` The food it eats

**Response**

- `201` on success
- ```json
{
    "links": {
        "href": "animalfoods/<animal>/",
        "rel": "animalfoods.search",
        "type": "GET"
    }
}
```
- `422` if an error occurred.

### Get animal food

**Description**

Get the food an animal eats.

**Definition**

`GET /animalfoods/<animal>/`

**Arguments**

- `"animal":string` The name of animal

**Response**

- `200` on success
- ```json
{
    "data": [
        {
            "animal": <animal>,
            "food": <food>
        }
    ]
}
```

### Get all animals

**Description**

Get a list of all animal.

**Definition**

`GET /animals/`

**Response**

- `200` on success
- ```json
{
    "data": [
        {
            "name": <animal>
        }
    ]
}
```

### Add a new owner

**Description**

Record a new owner's details.

**Definition**

`POST /owners/<first_name>/<last_name>/`

**Arguments**

- `"first_name":string` The first name of the owner
- `"last_name":string` The last name of the owner

**Response**

- `201` on success
```json
{
    "links": [
        {
            "href": "owners/",
            "rel": "owners.all",
            "type": "GET"
        }
    ]
}```
- `422` if error occurred.

### Get all owners

**Description**

Get a list of all owners.

**Definition**

`GET /owners/`

**Response**

- `200` on success
- ```json
{
    "data": [
        {
          "first_name": <first_name>,
          "last_name": <last_name>
        }
    ]
}
```

### Add a new pet

**Description**

Add a new pet for an owner.

**Definition**

`POST /pets/<pet_name>/<pet_type>/<first_name>/<last_name>/`

**Arguments**

- `"pet_name":string` The  name of the pet
- `"pet_type":string` The animal type of the pet
- `"first_name":string` The first name of the owner
- `"last_name":string` The last name of the owner

**Response**

- `201` on success
```json
{
    "links": [
        {
          "href": "pets/<first_name>/<last_name>/",
          "rel": "pets.get",
          "type": "GET"
        }
    ]
}```
- `422` if error occurred.

### Get all pets of an owner

**Description**

Get a list of all pets of an owner.

**Definition**

`GET /pets/<first_name>/<last_name>/`

**Arguments**

- `"first_name":string` The first name of the owner
- `"last_name":string` The last name of the owner

**Response**

- `200` on success
- ```json
{
    "data": [
        {
          "first_name": <first_name>,
          "last_name": <last_name>,
          "pet_name": <pet_name>,
          "pet_type": <pet_type>
        }
    ]
}
```


### Delete a pet

**Description**

Delete a pet from an owner's pets list.

**Definition**

`DELETE /pets/<pet_name>/<first_name>/<last_name>/`

**Arguments**

- `"pet_name":string` The  name of the pet
- `"last_name":string` The last name of the owner
- `"last_name":string` The last name of the owner

**Response**

- `202` on success
- ```json
{
    "links": [
        {
            "href": "pets/<first_name>/<last_name>/",
            "rel": "pets.get",
            "type": "GET"
        }
    ]
}
```
