import atheris
import sys


def TestOneInput(data):
    if (
        data
        == b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ):
        raise RuntimeError("Badness!")


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()