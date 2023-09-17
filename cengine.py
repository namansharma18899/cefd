import subprocess
import argparse
import os
from compression.bwt import BWT
from compression.rle import RLE
from utils.utility import Logger

logger = Logger().get_logging_object(__name__)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-e", "--encode", action="store_true", help="Flag to Encode the string"
)
args = parser.parse_args()
encode = args.encode if args.encode else False
encoded_file_extension = ".enc"
decoded_file_extension = ".dec"


# TODO: ADD LOGS
def encode_string_buffer(string_buffer):
    bwt = BWT()
    logger.info("Encoding String")
    bwt = bwt.encode(string_buffer)
    rle_obj = RLE()
    compress_char_arr = rle_obj.encode(bwt)
    return compress_char_arr


def decode_string_buffer(string_buffer):
    rle_obj = RLE()
    logger.info("Decoding String")
    compress_char_arr = rle_obj.decode(string_buffer)
    bwt = BWT()
    bwt = bwt.decode(compress_char_arr)
    bwt = bwt[::-1][1:]
    return bwt


def write_file(file, buffer):
    """
    Note: This will make things slow, we can make write async & hold on to buffers upto a limit.
    """
    outF = open(file, "w")
    outF.write(buffer)


def handle_file(file):
    f = open(file, "rb")
    while True:
        str_buffer = f.read(1024).decode(encoding="utf-8")
        if not str_buffer:
            break
        if encode:
            resultant_file = encode_string_buffer(str_buffer)
        else:  # decode
            resultant_file = decode_string_buffer(str_buffer)
        res_file_extension = (
            encoded_file_extension if encode else decoded_file_extension
        )
        y = os.path.basename(file)
        y = y.split(".")
        newF = (
            file.split(os.path.basename(file))[0]
            + y[0]
            + res_file_extension
            + "."
            + y[1]
        )
        write_file(newF, resultant_file)
    f.close()


if __name__ == "__main__":
    enc_input_file = "/home/namansh/personal/projects/cefd/assets/temp.text"
    dec_input_file = "/home/namansh/personal/projects/cefd/assets/temp.enc.text"
    dec_output_file = "/home/namansh/personal/projects/cefd/assets/temp.dec.enc"
    encode= True 
    handle_file(file=enc_input_file)
    encode=False
    handle_file(file=dec_input_file)
    print(subprocess.run(f'md5sum {enc_input_file} {dec_output_file}', shell=True, check=True))
