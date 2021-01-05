from encoding import encode
from decoding import decode


def test(path, msg):

    # encode(path, msg)

    txt = decode(path)
    for i in txt:
        print(i, end='')


if __name__ == '__main__':
    test('pictures\\senko_tail.png', msg='Senko\n' * 40)
