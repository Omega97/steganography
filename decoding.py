from random import seed
from encoding import get_seed, gen_no_doubles, gen_random_coo
from misc import read_image, gen_group, bin_list_to_num


def gen_bits(gen_coo, mat):
    for h, w, c in gen_coo:
        yield mat[h][w][c] % 2


def gen_bytes(gen_coo, mat):
    gen = gen_bits(gen_coo, mat)
    gen = gen_group(8)(gen)

    for v in gen:
        yield chr(bin_list_to_num(v))


def gen_message(gen_coo, mat, validation_byte='\n'):
    n = set([str(i) for i in range(10)])
    s = ''
    gen = gen_bytes(gen_coo, mat)

    for c in gen:
        if c == validation_byte:
            break
        else:
            return

    for c in gen:
        if c in n:
            s += c
        else:
            break
    if s:
        n = int(s)
        for i, c in enumerate(gen):
            if i == n:
                break
            yield c


def decode(path):
    mat = read_image(path)
    height = len(mat)
    width = len(mat[0])
    seed(get_seed(mat))
    gen_coo = gen_no_doubles(gen_random_coo(height, width))
    for i in gen_message(gen_coo, mat):
        yield i
