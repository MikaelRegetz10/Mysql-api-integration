# Flask Consumables API

## Introduction

This project is a Flask-based API for managing consumable items. The API allows you to retrieve, add, and delete consumables. It interacts with a database through queries defined in the models.queries module. This structure was utilized as a study reference in a repository for developing RESTful APIs integrated with databases.
## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Get All Consumables](#get-all-consumables)
  - [Add a Consumable](#add-a-consumable)
  - [Get a Consumable by ID](#get-a-consumable-by-id)
  - [Delete a Consumable by ID](#delete-a-consumable-by-id)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone <https://github.com/MikaelRegetz10/Mysql-api-integration.git>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database and configure the `models.queries` module as needed.

## Usage
To run the API, use the following command:
```sh
python app.py
```

The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Get All Consumables
- **Endpoint:** `/consumables`
- **Method:** `GET`
- **Response:**
  - **200:** List of consumables
  - **500:** Internal Server Error

### Add a Consumable
- **Endpoint:** `/consumables/add`
- **Method:** `POST`
- **Request Parameters:**
  - `name`: Name of the consumable (string)
  - `buy`: Buy price (float)
  - `sell`: Sell price (float)
  - `type`: Type of the consumable (must be one of `Poções`, `Mágicos`, `Alquímicos`)
  - `link`: Link to the consumable details (string)
- **Response:**
  - **201:** Consumable added successfully
  - **400:** Invalid type
  - **500:** Internal Server Error

### Get a Consumable by ID
- **Endpoint:** `/consumables/<int:id>`
- **Method:** `GET`
- **Response:**
  - **200:** Consumable details
  - **404:** Not Found
  - **500:** Internal Server Error

### Delete a Consumable by ID
- **Endpoint:** `/consumables/delete/<int:id>`
- **Method:** `DELETE`
- **Response:**
  - **204:** Consumable deleted successfully
  - **404:** Not Found
  - **500:** Internal Server Error

## Features
- Retrieve all consumables
- Add new consumables
- Get consumable details by ID
- Delete consumable by ID

## Dependencies
- Flask
- models.queries module

Ensure all dependencies are listed in the `requirements.txt` file.

## Configuration
The following configuration can be adjusted in the `app.py` file:
- Debug mode: `app.run(debug=True)`

## Examples
Here are some examples of how to use the API:

### Get All Consumables
```sh
curl http://127.0.0.1:5000/consumables
```

### Add a Consumable
```sh
curl -X POST -F "name=Health Potion" -F "buy=10" -F "sell=15" -F "type=Poções" -F "link=http://example.com/health_potion" http://127.0.0.1:5000/consumables/add
```

### Get a Consumable by ID
```sh
curl http://127.0.0.1:5000/consumables/1
```

### Delete a Consumable by ID
```sh
curl -X DELETE http://127.0.0.1:5000/consumables/delete/1
```

## Contributors
- Mikael de Oliveira Regetz

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
