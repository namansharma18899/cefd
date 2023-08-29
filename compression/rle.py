from utility import timer


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
                encoded += str(count) + prev_char
                count = 1
                prev_char = char
        encoded += str(count) + prev_char
        return encoded

    @timer
    def decode(self, encoded_text):
        decoded = ""
        i = 0
        print("encoddc -> ", encoded_text)
        while i < len(encoded_text):
            count = int(encoded_text[i])
            char = encoded_text[i + 1]
            decoded += char * count
            i += 2
        return decoded
