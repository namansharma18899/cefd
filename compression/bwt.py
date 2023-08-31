from utils.utility import Logger

logger = Logger().get_logging_object(__name__)


class BWT:
    """
    BWT(burrows-wheeler theorem) is used for compression on small strings.
    One of the key features of BWT is its ability to group together similar characters in a string,
    which is a key factor in achieving efficient compression
    """

    def __init__(self) -> None:
        pass

    def encode(self, input_buffer: str):
        input_buffer += "$"
        rotations = [
            input_buffer[index:] + input_buffer[:index] for index in range(len(input_buffer))
        ]
        rotations.sort()
        result = [each[-1] for each in rotations]
        logger.debug("Encoded Text")
        return "".join(result)

    def decode(self, encoded_text):
        table = sorted([(c, i) for i, c in enumerate(encoded_text)])
        index = 0
        for ind, _ in enumerate(table):
            if table[ind][0] == "$":
                index = ind
                break
        decoded_text = ""
        for _ in range(len(encoded_text)):
            decoded_text = table[index][0] + decoded_text
            index = table[index][1]

        return decoded_text
