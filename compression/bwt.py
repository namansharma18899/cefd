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
            input_buffer[index:] + input_buffer[:index]
            for index in range(len(input_buffer))
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


# inputfile = [x for x in "this is a real thing mate"]
# x = BWT()
# i, j = 0, 0
# temp = []
# while j <= len(inputfile):
#     if j == " ":
#         if j > 0 and inputfile[j - 1] != " ":
#             temp.append(x.encode(''.join(inputfile[i:j])))
#             i = j + 0
#         else:
#             temp.append(" ")
#     else:
#         try:
#             if j > 0 and inputfile[j - 1] == " ":
#                 i = j + 0
#         except Exception as e:
#             print(j)
#     j += 1

# print("temp", temp)
# enc = x.encode(inputfile)
# print('enc -> ', enc)
# dec = x.decode(enc)
# print('dec - ', dec[::-1][1:])
