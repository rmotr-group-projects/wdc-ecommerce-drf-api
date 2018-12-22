<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Ecommerce DRF API

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) ecommerce
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

### Description

The main goal of this project is to practice all the concepts related with APIs and Django REST Framework.

We'll make use of the Ecommerce project that we've been working on, and implement all the endpoints related with the `Product` model.


### Your tasks

You'll be in charged of implementing an API using Django REST Framework.

For this task, views must be implemented inside `api/views.py`, serializers inside `api/serializers.py` and urls inside `api/urls.py`.

A couple of Product objects are already loaded in your database, so you can test the endpoints directly from the browser when you point to the proper URL.

The following endpoints must be supported:

##### LIST

- `GET /api/products/`

Example response:
```json
[
    {
        "id": 1,
        "name": "Nike Vapor",
        "sku": "44444444",
        "category": 4,
        "description": "",
        "price": "129.99",
        "created": "2018-12-22T17:01:08.683537Z",
        "featured": true
    },
    {
        "id": 2,
        "name": "Nike Cap",
        "sku": "33333333",
        "category": 2,
        "description": "",
        "price": "27.99",
        "created": "2018-12-22T17:01:08.684956Z",
        "featured": true
    }
]
```

##### DETAIL

- `GET /api/products/<product_id>`

Example response:
```json
{
    "id": 1,
    "name": "Nike Vapor",
    "sku": "44444444",
    "category": 4,
    "description": "",
    "price": "129.99",
    "created": "2018-12-22T17:01:08.683537Z",
    "featured": true
}
```

##### CREATE

- `POST /api/products/`

Example payload
```json
{
    "name": "New product",
    "category": 2,
    "sku": "11111111",
    "description": "New product description",
    "price": 39.99
}
```

##### FULL UPDATE

- `PUT /api/products/<product_id>`

Example payload
```json
{
    "name": "Updated name",
    "category": 1,
    "sku": "11111111",
    "description": "Updated description",
    "price": 39.99
}
```

##### PARTIAL UPDATE

- `PATCH /api/products/<product_id>`

Example payload
```json
{
    "name": "Updated name"
}
```

##### DELETE

- `DELETE /api/products/<product_id>`


### Tests

In order to check if your implementation is correct, a couple of tests that should pass are implemented inside `api/tests.py`. You can run them this way:

```
$ make test
```
