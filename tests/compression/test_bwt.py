import unittest
from compression.bwt import BWT


class TestBWTCompression(unittest.TestCase):

    def setUp(self) -> None:
        self.bwt = BWT()
        self.test_input = 'DOGWOOD'
        self.test_output = 'DO$OODWG'

    def test_bwt_encode(self):
        """
        Test that it can transform the string
        """
        result = self.bwt.encode(self.test_input)
        self.assertEqual(result, self.test_output)

    def test_bwt_decode(self):
        """
        Test that it can decode previously encoded string
        """
        result = self.bwt.decode(self.test_output)
        self.assertEqual(result[::-1][1:], self.test_input)

if __name__ == '__main__':
    unittest.main()
    