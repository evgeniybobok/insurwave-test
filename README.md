# API for extracting Employee risk of leaving company level from a trained ML model

1 - High risk, please take preventative measures
0 - Low risk, no additional measures required

## Creating virtual env

`python3 -m venv venv`

`pip3 install -r requirements.txt`

`source venv/bin/activate`

## Running the endpoint service from the console

`uvicorn main:app --reload`

## Testing the API

To run the test cases with unittest package execute
`python3 tests/test.py`