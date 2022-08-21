
# Django adventure

Úlohou bolo vytvoriť vhodné modely, rozparsovať JSON request a poskytnúť vhodné endpointy pre získanie dát.


## Acknowledgements

*test_data.json* som považoval za valídny vstup a tiež aj objekty tohoto json súboru za valídne. *id atribút* som u objektov nepovažoval za *primary_key*. 
Využitá je základná *sqllite db* ktorá je súčasťou django framework, použitie Postgres by možno umožnilo krajšie ukladanie pomocou *ListField* a nie *JsonField*.
Kód som písal na **Windows 10, Python 3.10.2** + venv -> docker, napriek tomu, som kvôli čitateľnosti ponechal *if statements* a nie *Match - Case* (zabijanie mravca Glock-om).


## API Reference

#### Import items

```bash
  POST http://127.0.0.1:8000/import
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Json Content` | `json` |  JSON formated data  |

Use for data importing.

#### Get items

```bash
  GET http://127.0.0.1:8000/detail/{name}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Desired Object name |

Returns all instances for specific Object name.

#### Get item

```bash
  GET http://127.0.0.1:8000/detail/{name}/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required**. Desired Object name |
| `id`      | `int` | **Required**. id for specific object instance |

Returns specific instance of Object.
## Run Locally

Clone the project

```bash
  git clone https://github.com/Ad4mk0/adventurous-django
```

Go to the project directory

```bash
  cd adventurous-django
```
The easiest and cleaniest way is just to,
use docker:
```bash
  docker-compose up
```

or:
```bash
# make sure you have approppriate Python version
pip install -r requirements.txt
python manage.py makemigrations whys
python manage.py migrate
python manage.py runserver
# server is now running on localhost
```


## Usage/Examples
Lets say we called:
```bash
POST http://127.0.0.1:8000/import
```
on:
```json
[
  {
    "AttributeValue": {
      "id": 1,
      "hodnota": "modrá"
    }
  },
  {
    "AttributeValue": {
      "id": 2,
      "hodnota": "zelená"
    }
  },
  {
    "AttributeName": {
      "id": 3,
      "zobrazit": true
    }
  }
]
```
These objects should be stored.

Now, if we call:
```bash
GET http://127.0.0.1:8000/detail/AttributeValue/
```
it would get us a following response:

```json
[
  {
    "AttributeValue": {
      "id": 1,
      "hodnota": "modrá"
    }
  },
  {
    "AttributeValue": {
      "id": 2,
      "hodnota": "zelená"
    }
  }
]
```
If we go further:
```bash
GET http://127.0.0.1:8000/detail/AttributeValue/2
```
the response is:

```json
[  
  {
    "AttributeValue": {
      "id": 2,
      "hodnota": "zelená"
    }
  }
]
```

[*Adam 2022*](https://github.com/Ad4mk0)
