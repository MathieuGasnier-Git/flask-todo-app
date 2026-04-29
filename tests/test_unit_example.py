from app import validate_item


def test_validate_item_valid():
    assert validate_item("hello") == "hello"


def test_validate_item_strips_whitespace():
    assert validate_item("  hello  ") == "hello"


def test_validate_item_empty_string():
    assert validate_item("") is None


def test_validate_item_whitespace_only():
    assert validate_item("   ") is None


def test_validate_item_none():
    assert validate_item(None) is None
