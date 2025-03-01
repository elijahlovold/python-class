import pytest

from personal.dict import key_in_nested_dict, create_character, level_up, display_stats

def test_key_in_nested_dict():
    nested = {"a": {"b": {"c": 3}}, "m": 23}
    assert key_in_nested_dict(nested, "m") is True
    assert key_in_nested_dict(nested, "c") is True
    assert key_in_nested_dict(nested, "x") is False


@pytest.fixture
def default_character():
    return create_character("Alderan", "Warrior", "Human", 10, 8, 6, 1)

def test_create_character(default_character):
    assert default_character["name"] == "Alderan"
    assert default_character["class"] == "Warrior"
    assert default_character["race"] == "Human"
    assert default_character["strength"] == 10
    assert default_character["agility"] == 8
    assert default_character["intelligence"] == 6
    assert default_character["level"] == 1

def test_level_up(default_character):
    updated_character = level_up(default_character)
    assert updated_character["level"] == 2
    assert updated_character["strength"] == 12
    assert updated_character["agility"] == 9
    assert updated_character["intelligence"] == 7

def test_display_stats(default_character, capsys):
    display_stats(default_character)
    captured = capsys.readouterr()
    assert "Name: Alderan" in captured.out
    assert "Class: Warrior" in captured.out
    assert "Race: Human" in captured.out
    assert "Strength: 10" in captured.out
    assert "Agility: 8" in captured.out
    assert "Intelligence: 6" in captured.out
    assert "Level: 1" in captured.out
