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
        logger.info(f"encoded -> {encoded_text} as")
        decoded = ""
        i = 0
        while i < len(encoded_text):
            if encoded_text[i].isdigit():
                temp=0
                while(encoded_text[i].isdigit()):
                    temp= temp*10+int(encoded_text[i])
                    i+=1
                decoded += encoded_text[i] * temp 
                i+=1
            else:
                decoded += encoded_text[i]
                i += 1
        return decoded
