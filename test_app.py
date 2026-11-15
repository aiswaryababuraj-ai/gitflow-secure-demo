def test_add_tax():
    from app import add_tax
    assert add_tax(100, 0.10) == 110