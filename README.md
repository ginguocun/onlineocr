# Online Ocr

This is an open source online OCR service built by the Django framework.



[TOC]



## Requirements

### Run directly

- python 3.8

- tesseract 4.1.x

#### install Tesseract

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

### Run by Docker 

Docker Engine

## What's included

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
├────dockerfile_base
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
├────static/
├────templates/
└────uwsgi_params

```

## Run directly



### Clone the project

```sh
git clone https://github.com/ginguocun/onlineocr.git
cd onlineocr
```

### Create the virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### Install the reqirements

```sh
pip install -r requirements.txt
```

### Migrate the database

```sh
python3 manage.py migrate
```

### Runserver

```sh
python3 manage.py runserver 127.0.0.1:9999
```

## Run through docker

### Build the basic docker image

```sh
git clone https://github.com/ginguocun/onlineocr.git
cd onlineocr
sudo docker build --rm -t onlineocr:base -f dockerfile_base .
```

### Build the product docker image

```sh
sudo docker build --rm -t onlineocr:latest -f dockerfile_product .
```

### Run server by docker

```sh
sudo docker run -it -p 9001:80 onlineocr:test /bin/bash
```