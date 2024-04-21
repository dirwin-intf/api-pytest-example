# api-pytest-example

Basic example harness running multistep API tests against the (deck of cards API)[https://deckofcardsapi.com]

Utilizes fixtures to set up data and paramaterize complex tests.

## Dependencies
Required: `python3`, `pip3`.

Recommended: `GNU Make`

## Getting started
From the project root (without `make`):
1. `python3 -m venv env`
2. `source ./env/bin/activate`
3. `pip3 install -r requirements.txt`

From the project root (with `make`):
1. `make environment`
2. `source ./env/bin/activate`
3. `make install`

## Running tests
`pytest` to execute tests.
