# API for extracting Employee risk of leaving company level from a trained ML model

1 - High risk, please take preventative measures

0 - Low risk, no additional measures required

## Creating virtual env

`python3 -m venv venv`

`pip3 install -r requirements.txt`

`source venv/bin/activate`

## Running the endpoint service from the console

`uvicorn main:app --reload`

The endpoint will be available on http://127.0.0.1:8000/

## Accessing the API endpoint

You can access the API endpont and get the response using requests or any other library

`requests.post(url='http://127.0.0.1:8000/', json=request_json)`

## Testing the API

To run the test cases with unittest package execute

`python3 tests/test.py`