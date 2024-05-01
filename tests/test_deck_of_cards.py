import pytest
import requests
import json
from types import SimpleNamespace

base_url = "https://deckofcardsapi.com/api/"
def get_response_data(response):
    return json.loads(
        response.text,
    )

@pytest.fixture
def create_response():
    endpoint = "deck/new"
    response = requests.get(url = base_url + endpoint)
    return response

@pytest.fixture
def shuffle_response(create_response):
    setup_data = get_response_data(create_response)
    endpoint = "deck/{}/shuffle".format(setup_data['deck_id'])
    response = requests.get(url = base_url + endpoint)
    return response

def test_create_a_deck(create_response):
    other_data = json.loads(create_response.text)
    data = get_response_data(create_response)
    assert create_response.status_code == 200
    assert data['success'] == True
    assert data['shuffled'] == False
    assert data['remaining'] == 52

def test_shuffle_a_deck(create_response, shuffle_response):
    create_data = get_response_data(create_response)
    shuffle_data = get_response_data(shuffle_response)
    assert shuffle_response.status_code == 200
    assert shuffle_data['deck_id'] == create_data['deck_id']
    assert shuffle_data['success'] == True
    assert shuffle_data['shuffled'] == True
    assert shuffle_data['remaining'] == 52

@pytest.mark.parametrize("cards_to_draw", [5, 10, 20])
def test_draw_cards_from_a_deck(create_response, shuffle_response, cards_to_draw):
    setup_data = get_response_data(create_response)
    endpoint = "deck/{deck_id}/draw/?count={cards_to_draw}".format(
        deck_id=setup_data['deck_id'],
        cards_to_draw=cards_to_draw
    )
    response = requests.get(url = base_url + endpoint)
    data = get_response_data(response)
    assert response.status_code == 200
    assert data['deck_id'] == setup_data['deck_id']
    assert data['success'] == True
    assert data['remaining'] == 52 - cards_to_draw
    assert isinstance(data['cards'], list)
    assert len(data['cards']) == cards_to_draw
    for card in data['cards']:
        matching_cards = list(filter(
            lambda x: x['code'] == card['code'],
            data['cards']
        ))
        assert len(matching_cards) == 1
