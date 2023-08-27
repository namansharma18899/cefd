#todo: 
"""
read the data in chunks, don't read the whole file in memory..
"""

import os
from compression.bwt import BWT
from compression.rle import RLE


def compress_string(string_buffer):
    bwt = BWT()
    bwt = bwt.transform(string_buffer)
    compressed_string = RLE()
    compress_char_arr = compressed_string.compress(list(bwt))
    return ''.join(compress_char_arr)

def write_file(file, buffer):
    """
    this will make things slow, we can make write async & hold on to buffers upto a limit
    """
    outF = open(file, 'w')
    outF.write(buffer)

def compress_file(file):
    f = open(file, 'rb')
    while True:
        str_buffer = f.read(1024).decode(encoding='utf-8')
        if not str_buffer:
            break
        cmp_output = compress_string(str_buffer)
        y = os.path.basename(file)
        y = y.split('.')
        newF = file.split(os.path.basename(file))[0] +  y[0] + '.cmp' + '.' + y[1]
        write_file(newF, cmp_output)
    f.close()


if __name__=="__main__":
    compress_file('/home/namansh/personal/projects/cefd/temp.text')