from random import randrange, seed
from misc import *


def gen_random_coo(height, width, n_colors=3):
    """generate random coordinates"""
    while True:
        yield randrange(height), randrange(width), randrange(n_colors)


def message_bit_gen(msg: str):
    """convert message to bits"""
    for c in msg:
        for b in num_to_bin_list(ord(c)):
            yield b


def get_seed(mat, bits_in_byte=8):
    """use first bit of some bytes of mat to get a seed"""
    seed(0)
    s = ''
    height = len(mat)
    width = len(mat[0])
    for h, w, c in gen_next_n(height + width)(gen_random_coo(height, width)):
        s += str(mat[h][w][c] // (2**(bits_in_byte-1)))
    return s


def write_message(mat, gen_coo, gen_bin_msg):
    """modify mat by writing bits given by gen_bin_msg in coordinates specified by gen_coo"""
    for (h, w, c), target in merge_gen(gen_coo, gen_bin_msg):
        n = mat[h][w][c]
        n = n - n % 2 + target  # (n >> 2 << 2)+j
        mat[h][w][c] = n


def encode(path, msg, validation_byte='\n'):
    """use steganography to encode a message in an image"""
    msg = validation_byte + f'{len(msg)} ' + msg

    mat = read_image(path)
    height = len(mat)
    width = len(mat[0])

    seed(get_seed(mat))
    write_message(mat, gen_coo=gen_no_doubles(gen_random_coo(height, width)), gen_bin_msg=message_bit_gen(msg))

    save_img(path, mat)
