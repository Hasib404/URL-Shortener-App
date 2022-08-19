# URL Shortener App

* [Guidelines](#guidelines)
* [API Endpoints](#api-endpoints)
* [Error handling](#error-handling)
* [Install](#install)
* [Run tests locally](#run-tests-locally)

## Guidelines

This document provides guidelines and examples for URL Shortener APIs, encouraging consistency, maintainability, best practices across application. 


## API Endpoints

Below here shown the api endpoints.

### POST
`URL Shortener` [/url](#/url) <br/>

### GET
`URL Redirect and click counts` [/{url_key}](#/{url_key}) <br/>

___


#### POST /url
Post a long url and get a short URL key as response. URL validation is checked and an unique key is generated agains the given URL.

**Request**

```
{
  "url": "http://google.com"
}
```

**Successful Response**

```
{
  "data": {
    "shortener_id": "e62D5ZIKuI"
  },
  "code": 200,
  "message": "shortener object added successfully.",
  "error": false
}
```

**Request**
```
{
   "url": "http:/google.com"
}
```

**Error Response**
```
{
  "data": [],
  "code": 400,
  "message": "Invalid URL",
  "error": true
}
```
___

#### GET /{url_key}
Pass a generated shortener_id as parameter `url_key`. Based on the `url_key`, user will be redirected to the actual URL. Additionaly user's visit to the shortened_url will be counted.

**Successful Response**


`Will be redirected to the actual URl`


**Error Response**

```
{
  "Message": "No URL found to Redirect"
}
```
___
## Error handling

Used three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
* 200 - OK
* 400 - Bad Request
* 500 - Internal Server Error

___
## Install

A dockerfile for backend server added. A `docker-compose.yml` file consists of 2 services `backend` & `PostgreSQL` added.

To run, execute the following command:
   ```
   docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate
   ```
   (It will clean up existing containers and force to be recreated)
 
To test your API you can check `http://127.0.0.1:80/` on your browser.

___


## Run tests locally
Install dependencies:
1. Change DB_URL to following in settings.json file
    ```
    "DB_URL": "postgresql://username:password@localhost:5436/shortener"
    ```
2. Run docker-compose file
   ```
   docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate
   ```
1. Create a virtual env and activate it: 
    ```
    python3 -m venv env; source env/bin/activate
    ```
2. Install dependencies from server folder: 
    ```
    pip install -r requirements.txt
    ```
3. Run tests from server folder: 
    ```
    python -m pytest tests/ -v
    ```