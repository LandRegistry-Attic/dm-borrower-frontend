# dm-borrower-frontend

The Borrower Frontend provides a website for Borrower to view and sign their
mortgage deeds online.

## Contents
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Acceptance Tests](#acceptance-tests)

## Usage
```
GET     /health                         -- renders standard Gov UK template
GET     /searchdeed                     -- borrower views deed landing page
POST    /searchdeed/search              -- form POST the response is a html page which will display the deed or an error page
```

Install the requirements
```
pip install -r requirements.txt
pip install -r requirements_test.txt
```

Optional: export variable for deed-api
```
export DEED_API_BASE_HOST=http://localhost:8000
```

> default is localhost:9030

Run the unit tests
```
source tests.sh
```

Run the app
```
python run.py runserver --host 0.0.0.0
```
> optional ```--port 9000``` where 9000 is the number of a port you can supply to start the server on.

## Acceptance Tests

### Running the Tests

All of the acceptance tests are contained within the acceptance-tests folder with the feature files under the features folder and the step-definitions under the steps folder.

If you would like to run all of the acceptance tests then navigate into the acceptance-tests folder and run the following command:

'./test.sh'

### Running Rubocop

Rubocop is ruby gem that will check any ruby code in the repository against the ruby style guide and then provide a report of any offenses.

In order to run Rubocop on the acceptance test code then navigate into the acceptance test folder and run the command:

' ./run_linting.sh'

If you wish to amend what cops are used, what files are ignored when running Rubocop then you will need to put this in the rubocop.yml file.
