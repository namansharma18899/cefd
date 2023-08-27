from itertools import permutations


class BWT:
    """
    BWT(burrows-wheeler theorem) is used for compression on small strings. We create all possible rotations of 
    the string and then sort them Lexicographically, we then take the last columns of each result (in LXC order) 
    and then we use the string for further processing. It gives a smooth string with similar characters residing 
    together.
    """
    def __init__(self) -> None:
        pass

    def transform(self, inputStr: str):
        rotations = []
        for index in range(0, len(inputStr)):
            newstr = inputStr[index:len(inputStr)] + inputStr[0:index]
            rotations.append(newstr)
        rotations = sorted(rotations)
        result = [each[-1] for each in rotations]
        return ''.join(result)
