################
# With if as code you are goin to write more.
################

from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

def square(n):
    return n * n

if __name__ === "__main__"
    main()

