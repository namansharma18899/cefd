from itertools import permutations


class BWT:
    """
    BWT(burrows-wheeler theorem) is used for compression on small strings.
    One of the key features of BWT is its ability to group together similar characters in a string,
    which is a key factor in achieving efficient compression
    """

    def __init__(self) -> None:
        pass

    def transform(self, inputStr: str):
        rotations = []
        for index in range(0, len(inputStr)):
            newstr = inputStr[index : len(inputStr)] + inputStr[0:index]
            rotations.append(newstr)
        rotations = sorted(rotations)
        result = [each[-1] for each in rotations]
        print(result)
        return "".join(result)
