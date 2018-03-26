import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index.lambda_handler(None, None)
        print(len(result))
        self.assertEqual(len(result),6)
        

if __name__ == '__main__':
    unittest.main()
