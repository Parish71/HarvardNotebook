#
# Assert -> Linear expressior to use inside a fuction for assert a value
# Assertion ERROR just implicit that the expect value of the analisys is not the expected
#
#
#
########################################
# Ex1:
def main ():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
########################################


