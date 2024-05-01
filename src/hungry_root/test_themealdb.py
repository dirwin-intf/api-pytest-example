import requests
import json
import pytest

def get_data_from_response(response):
    return json.loads(response.text)

@pytest.fixture
def make_query_and_verify_response():
    api_url = 'https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772'  # Teriyaki Chicken Casserole
    return requests.get(api_url)

@pytest.fixture
def make_query_for_teriyaki_response():
    api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=Teriyaki'
    return requests.get(api_url)

@pytest.fixture
def make_query_for_chicken_response():
    api_url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=Chicken'
    return requests.get(api_url)

def test_lookup_returns_success(make_query_and_verify_response):
    response = make_query_and_verify_response
    assert response.status_code == 200

def test_lookup_returns_meals_array(make_query_and_verify_response):
    data = get_data_from_response(make_query_and_verify_response)
    meals = data['meals']
    assert type(meals) is list
    assert len(meals) == 1

def test_teriyaki_search_returns_52772(
    make_query_and_verify_response,
    make_query_for_teriyaki_response
    ):
    index_search_data = get_data_from_response(make_query_and_verify_response)
    name_search_data = get_data_from_response(make_query_for_teriyaki_response)
    index_meal = index_search_data['meals'][0]
    desired_teriyaki_meal = list(filter(
            lambda m: m['idMeal'] == '52772',
            name_search_data['meals']
            ))
    assert len(desired_teriyaki_meal) == 1
    assert desired_teriyaki_meal[0]['idMeal'] == index_meal['idMeal']

def test_chicken_query_returns_52772(
        make_query_for_chicken_response
        ):
    data = make_query_for_chicken_response.json()['meals']
    filtered = list(filter(lambda m: m['idMeal'] == '52772', data))
    assert len(filtered) == 1

