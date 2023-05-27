# Folio Manager Project

This is a folio manager project

## Setup

To install all the necessary items, install `pipenv` and then use it to install the dependencies:

```bash
pip install pipenv
pipenv install
```

To start the server for development, run the following in a terminal:

```bash
pipenv run uvicorn server:app --host 0.0.0.0 --port 5050
```
