from unittest import TestCase


class TryTesting(TestCase):
    """
    Test  class for ensuring pipeline testing works

    ...

    Attributes
    ----------
    _

    Methods
    -------
    test_always_passes()
        basic assertTrue
    test_addition()
        test addition
    """

    def test_always_passes(self):
        self.assertTrue(True)

    def test_addition(self):
        a = 1
        b = 1
        self.assertEqual(a, b)


# THIS IS A MOCK TEST FOR PIPELINE PURPOSES
