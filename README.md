# dm-borrower-frontend

The Borrower Frontend provides a service for a Borrower to view and sign their
mortgage deeds online.

## Contents
- [Usage](#usage)
- [Install The Requirements](#install-the-requirements)
- [Run The App](#run-the-app)
- [Run The Unit Tests](#run-the-unit-tests)
- [Acceptance Tests](#acceptance-tests)
- [Frontend] (#frontend)

## Usage
```
GET     /                               -- renders borrower landing page
GET     /health                         -- renders standard Gov UK template
GET     /searchdeed                     -- borrower views deed landing page
POST    /searchdeed/search              -- POST search for deed (deed reference is in the request body)
```

## Install the requirements

1. Clone the repo

2. Initialise the submodules

```
git submodule init
git submodule update
```

3. Install the requirements
```
pip install -r requirements.txt
```

Optional: export variable for deed-api
```
> export DEED_API_BASE_HOST=http://localhost:8000
```

> default is localhost:9030


## Run the app
```
python run.py runserver -host 0.0.0.0
```
> optional ```--port 9000``` where 9000 is the number of a port you can supply to start the server on.


## Run the Unit Tests

Install the requirements
```
pip install -r requirements_test.txt
```

Run unit tests and provide coverage report

```
source test.sh
```

## Acceptance tests

See, the following link for information on how to run the acceptance tests:-

[Acceptance Tests](https://github.com/LandRegistry/dm-acceptance-tests)

## Frontend

The templates and styles for the borrower frontend are built using a copy of the 
[Gov.UK Elements repo](https://github.com/alphagov/govuk_elements). 
The Elements repo uses the [Gov.UK frontend toolkit](https://github.com/alphagov/govuk_frontend_toolkit) which is 
included in this project as a git submodule. The frontend also uses 
the [Gov.UK Jinja2](https://github.com/alphagov/govuk_template) template which 
is downloaded into the /build directory before being copied into the 'live' /application/static/govuk_template folder.
The build directory in this project is intended as a staging area for the import and compilation of the 
government templates from source code (SASS). 
