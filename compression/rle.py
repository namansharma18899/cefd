from utils.utility import print_progress_bar, timer, Logger

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
        logger.info("Encoding String")
        encoded = ""
        count = 1
        prev_char = text[0]
        index = 1
        total = len(text)
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
            print_progress_bar(iteration=index, total=total-1)
            index+=1
        encoded += str(count) + prev_char if count > 1 else prev_char
        print('\n')
        return encoded

    @timer
    def decode(self, encoded_text: str):
        logger.info("Decoding String")
        decoded = ""
        i = 0
        index = 1
        total = len(encoded_text)
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
            print_progress_bar(iteration=i+1, total=total)
        print('\n')
        return decoded
