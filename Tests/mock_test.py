import pytest


@pytest.fixture
class mockTest:
    def test_addition():
        assert 1 == 1

    def test_somethingelse():
        assert True, "this cant break"

print("THIS IS A MOCK TEST FOR PIPELINE PURPOSES")
