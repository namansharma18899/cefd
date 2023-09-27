from utils.suffix_tree import SuffixTree


def compress_buffer(string_buffer: str):
    string_buffer+='$'
    tree = SuffixTree(string_buffer)
    return tree.get_repeated_substrings()



dc = compress_buffer('KAKANENENELIOLELIONE$')
dc = [k for k, v in sorted(dc.items(), key=lambda item: item[1]) if v > 3]
print(dc)


#TODO: Need to brainstorm a little on how to put a text replacement among them