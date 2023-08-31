import unittest

from compression.bwt import BWT
from compression.rle import RLE


class TestLossLessCmp(unittest.TestCase):
    def setUp(self) -> None:
        self.bwt = BWT()
        self.rle = RLE()
        self.input = "this is a good day to be in"

    def test_compression(self):
        str_buffer = self.bwt.encode(self.input)
        compressed = self.rle.encode(str_buffer)
        rle_decoded = self.rle.decode(compressed)
        result = self.bwt.decode(rle_decoded)[::-1][1:]
        self.assertEqual(result, self.input)
