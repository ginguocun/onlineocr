# Online Ocr

This is an open source online OCR service built by the Django framework.

## 1. Requirements

### 1.1. Run directly

- python 3.8

- tesseract 4.1.x

#### 1.1.1. install Tesseract

[https://github.com/tesseract-ocr/tessdoc/blob/master/Home.md](https://github.com/tesseract-ocr/tessdoc/blob/master/Home.md)

##### macOS

A macOS wrapper for the Tesseract API is also available at [Tesseract macOS](https://github.com/scott0123/Tesseract-macOS).

**MacPorts**

To install Tesseract run this command:

```sh
sudo port install tesseract
```

To install any language data, run:

```sh
sudo port install tesseract-<langcode>
```

List of available langcodes can be found on [MacPorts tesseract page](https://www.macports.org/ports.php?by=name&substr=tesseract-).

**Homebrew**

To install Tesseract run this command:

```sh
brew install tesseract
```

The tesseract directory can then be found using `brew info tesseract`, e.g. `/usr/local/Cellar/tesseract/3.05.02/share/tessdata/`.

##### Linux

Tesseract is available directly from many Linux distributions. The package is generally called **'tesseract'** or **'tesseract-ocr'** - search your distribution's repositories to find it. Thus you can install Tesseract 4.x and its developer tools on Ubuntu 18.x bionic by simply running:

```sh
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

### 1.2. Run by Docker 

Docker Engine

## 2. What's included

Within the download, you'll find the following directories and files. You'll see something like this:

```
├────.gitattributes
├────.gitignore
├────app/
│    ├────__init__.py
│    ├────admin.py
│    ├────apps.py
│    ├────migrations/
│    │    ├────0001_initial.py
│    │    ├────0002_auto_20200505_0909.py
│    │    └────__init__.py
│    ├────models.py
│    ├────ocr.py
│    ├────serializers.py
│    ├────urls_api.py
│    └────views.py
├────db/
│    └────__init__.py
├────dockerfile_base
├────dockerfile_product
├────manage.py
├────media/
│    └────test/
├────nginx.conf
├────onlineocr/
│    ├────__init__.py
│    ├────asgi.py
│    ├────settings.py
│    ├────urls.py
│    └────wsgi.py
├────README.md
├────requirements.txt
├────sources.list
├────start.sh
├────static/
├────templates/
├────uwsgi/
├────uwsgi.ini
└────uwsgi_params

```

## 3. Run directly

Before run it you need first install Tesseract.

### 3.1. Clone the project

```sh
git clone https://github.com/ginguocun/onlineocr.git
cd onlineocr
```

### 3.2. Create the virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3.3. Install the reqirements

```sh
pip install -r requirements.txt
```

### 3.4. Migrate the database

```sh
python3 manage.py migrate
```

### 3.5. Runserver

Start development server at http://127.0.0.1:9999/

```sh
python3 manage.py runserver 127.0.0.1:9999
```

## 4. Run through docker

### 4.1. Build the basic docker image

```sh
git clone https://github.com/ginguocun/onlineocr.git
cd onlineocr
sudo docker build --rm -t onlineocr:base -f dockerfile_base .
```

### 4.2. Build the product docker image

```sh
sudo docker build --rm -t onlineocr:latest -f dockerfile_product .
```

### 4.3. Runserver by docker run

Start development server at http://127.0.0.1:9999/

```sh
sudo docker run -it -p 9999:80 onlineocr:latest /bin/bash
```

## 5. API documents

The online API documents is at http://127.0.0.1:9999/docs/

The main APIs are listed below:

- /api/ocr/
- /api/history/
- /api/register/
- /api/token_obtain_pair/ 
- /api/token_refresh/

### 5.1. /api/ocr/

POST `/api/ocr/`

This is an API which can take an uploaded image(jpg, png) and find any letters in it.

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter            | Description                                    |
| :------------------- | :--------------------------------------------- |
| `image` **required** | A image file, the size should be less than 2Mb |

### 5.2. /api/history/

GET `/api/history/`

This is an API used to obtain the historical upload records.

#### Query Parameters

The following parameters can be included as part of a URL query string.

| Parameter  | Description                                    |
| :--------- | :--------------------------------------------- |
| `page`     | A page number within the paginated result set. |
| `search`   | A search term.                                 |
| `ordering` | Which field to use when ordering the results.  |

### 5.3. /api/register/

POST `/api/register/`

This is an API for user registration.

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter               | Description                                                  |
| :---------------------- | :----------------------------------------------------------- |
| `username` **required** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |
| `email`                 |                                                              |
| `password` **required** |                                                              |

### 5.4. /api/token_obtain_pair/

POST `/api/token_obtain_pair/`

Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter               | Description |
| :---------------------- | :---------- |
| `username` **required** |             |
| `password` **required** |             |

### 5.5. /api/token_refresh/

POST `/api/token_refresh/`

Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter              | Description |
| :--------------------- | :---------- |
| `refresh` **required** |             |

