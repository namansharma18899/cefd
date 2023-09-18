from utils.utility import timer, Logger

logger = Logger().get_logging_object(__name__)


class RLE:
    """
    RLE(Run-Length Encoding is a way of lossless compression where we compress the main string by
    frequently occurring  characters in a substring with the notation of CX where C is the character which
    is repeating and X represents it's frequency)
    """

    def __init__(self) -> None:
        pass

    @timer
    def encode(self, text):
        encoded = ""
        count = 1
        prev_char = text[0]
        for char in text[1:]:
            if char == prev_char:
                count += 1
            else:
                if count == 1:
                    encoded += prev_char
                else:
                    encoded += str(count) + prev_char
                count = 1
                prev_char = char
        encoded += str(count) + prev_char if count > 1 else prev_char
        return encoded

    @timer
    def decode(self, encoded_text: str):
        logger.info("encoded -> {} as".format(encoded_text))
        decoded = ""
        i = 0
        while i < len(encoded_text):
            if encoded_text[i].isdigit():
                decoded += encoded_text[i + 1] * int(encoded_text[i])
                i += 2
            else:
                decoded += encoded_text[i]
                i += 1
        return decoded
