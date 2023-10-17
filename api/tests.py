from django.test import TestCase

# Create your tests here.


class MyMockTest(TestCase):
    def test_addition(self):
        self.assertEqual(1, 1)

    def test_something_else(self):
        self.assertTrue(True, "this can't break")


print("THIS IS A MOCK TEST FOR PIPELINE PURPOSES")
