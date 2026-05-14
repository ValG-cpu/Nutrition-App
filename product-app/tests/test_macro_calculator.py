import pytest
from macro_calculator import calculate_macros
from sample_data import sample_data


def test_calculate_macros():
    food_items = [
        {"name": "chicken_breast", "quantity": 1},
        {"name": "rice", "quantity": 1},
        {"name": "broccoli", "quantity": 1}
    ]
    
    expected_macros = {
        "calories": 165 + 205 + 55,
        "protein": 31 + 4 + 3.7,
        "carbs": 0 + 45 + 11,
        "fats": 3.6 + 0.4 + 0.6
    }
    
    assert calculate_macros(food_items, sample_data) == expected_macros


def test_calculate_macros_empty():
    food_items = []
    expected_macros = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    
    assert calculate_macros(food_items, sample_data) == expected_macros


def test_calculate_macros_unknown_food():
    food_items = [{"name": "unknown_food", "quantity": 1}]
    expected_macros = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    
    assert calculate_macros(food_items, sample_data) == expected_macros