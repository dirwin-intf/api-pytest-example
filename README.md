# api-pytest-example

Basic example harness running multistep API tests against the (deck of cards API)[https://deckofcardsapi.com]

Utilizes fixtures to set up data and paramaterize complex tests.

## Getting started

Requires: `python3`, `pip3`.

Recommended: `GNU Make`

From the project root:
1.  Run `make environment`
2.  Run `source ./env/bin/activate`
3.  Run `make install`

If you don't have `make` installed:

From the project root:
1. `python3 -m venv env`
2. `source ./env/bin/activate`
3. `pip3 install -r requirements.txt`

## Running tests

Run `pytest` to execute tests.
