import cv2


def read_image(path):
    return cv2.imread(path)


def save_img(path, mat):
    cv2.imwrite(path, mat)


def merge_gen(*gen):
    """merge generators"""
    itr = [i.__iter__() for i in gen]

    while True:
        try:
            yield [next(i) for i in itr]
        except StopIteration:
            break


def num_to_bin_list(num):
    b = bin(num)[2:]
    v = [int(j) for j in b]
    while len(v) < 8:
        v = [0] + v
    assert len(v) == 8
    return v


def bin_list_to_num(v):
    s = ''.join([str(i) for i in v])
    return int(s, base=2)


def gen_group(size):
    """group elements of itr in a list of a certain size """
    def wrap(itr):
        v = []
        for i in itr:
            v += [i]
            if len(v) == size:
                yield v
                v = []
    return wrap


def gen_convert(new_type):
    """change type of yielded items to new_type"""
    def wrap(gen):
        for i in gen:
            yield new_type(i)
    return wrap


def flip_bit_of_integer(num, n):
    return num ^ 2 ** n


def gen_no_doubles(itr):
    store = set()
    for x in itr:
        h = hash(str(x))
        if h not in store:
            store.add(h)
            yield x


def gen_next_n(n):
    def wrap(itr):
        for i, x in enumerate(itr):
            if i == n:
                break
            yield x
    return wrap
