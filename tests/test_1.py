import pytest
from yamlenc.yamlenc import YamlENC

CONFIG_GOOD = {
    "DEFAULT": {"classes": []},
    "classes_only": {"classes": ["classname"]},
    "environment_only": {"environment": "environment"},
    "^xyzzy$": {"environment": "xyzzy"}
}

CONFIG_BAD = {
    "^+bad_regular_expression$": {"environment": "bad_regular_expression"}
}

CONFIG_MISSING = {
    "regress": {"xyzzy": None}
}


def test_good():
    _ = YamlENC([CONFIG_GOOD])

def test_bad():
    with pytest.raises(Exception):
        _ = YamlENC([CONFIG_BAD])

def test_missing():
    with pytest.raises(ValueError):
        _ = YamlENC([CONFIG_MISSING])
