import subprocess
import hashlib
from utils.utility import create_cefd_banner, get_compression_ratio, print_colored
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
    # bwt = BWT()
    # bwt = bwt.encode(string_buffer)
    rle_obj = RLE()
    compress_char_arr = rle_obj.encode(string_buffer)
    return compress_char_arr


def decode_string_buffer(string_buffer):
    rle_obj = RLE()
    compress_char_arr = rle_obj.decode(string_buffer)
    # bwt = BWT()
    # bwt = bwt.decode(compress_char_arr)
    # bwt = compress_char_arr[::-1][1:]
    return compress_char_arr


def write_file(file, buffer):
    """
    Note: This will make things slow, we can make write async & hold on to buffers upto a limit.
    """
    outF = open(file, "w")
    outF.write(buffer)


def get_resultant_file(original_file, transform):
    res_file_extension = encoded_file_extension if transform else decoded_file_extension
    y = os.path.basename(original_file)
    y = y.split(".")
    return (
        original_file.split(os.path.basename(original_file))[0]
        + y[0]
        + res_file_extension
        + "."
        + y[1]
    )


def handle_file(file: str, transform: bool):
    f = open(file, "rb")
    result_file_loc = get_resultant_file(file, transform)
    while True:
        str_buffer = f.read().decode(
            encoding="utf-8"
        )  # for good performance batch it, ex: read(1024)
        if not str_buffer:
            break
        if transform:
            result_buffer = encode_string_buffer(str_buffer)
        else:  # decode
            result_buffer = decode_string_buffer(str_buffer)
        write_file(result_file_loc, result_buffer)
    f.close()

def find_md5sum(f):
    return hashlib.md5(open(f,'rb').read()).hexdigest()
class Colors:
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    purple = "purple"
    cyan = "cyan"


if __name__ == "__main__":
    print(create_cefd_banner())
    enc_input_file = "/home/namansh/personal/projects/cefd/assets/temp.text"
    dec_input_file = "/home/namansh/personal/projects/cefd/assets/temp.enc.text"
    dec_output_file = "/home/namansh/personal/projects/cefd/assets/temp.dec.enc"
    print("Compressing data:")
    clrs = Colors()
    print(
        f"Original Size: {print_colored(text=os.path.getsize(enc_input_file), color=clrs.blue)} bytes"
    )
    handle_file(file=enc_input_file, transform=True)
    handle_file(file=dec_input_file, transform=False)
    print(
        f"Compressed Size: {print_colored(text=os.path.getsize(dec_input_file),  color=clrs.yellow)} bytes"
    )
    print(
        f"Compressed Ratio: {print_colored(text=get_compression_ratio(enc_input_file, dec_input_file ),  color=clrs.green)}"
    )
    if find_md5sum(enc_input_file) == find_md5sum(dec_output_file):
        print(f'md5 matched ✅ \n Original: {print_colored(text=find_md5sum(enc_input_file),color=clrs.green)}\n Decrypted: {print_colored(text=find_md5sum(enc_input_file),color=clrs.green)}')
    else:
        print(f'md5sum mismatch ❌ \n Original: {print_colored(text=find_md5sum(enc_input_file),color=clrs.green)}\n Decrypted: {print_colored(text=find_md5sum(enc_input_file),color=clrs.red)}')