from unittest import TestCase



class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_addition(self):
        a = 1
        b = 1
        self.assertEqual(a, b)


print("THIS IS A MOCK TEST FOR PIPELINE PURPOSES")
