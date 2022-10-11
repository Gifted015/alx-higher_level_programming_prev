#!/usr/bin/python3
import os


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except BaseException as err:
        error = f"Exception: {err}"
        os.write(2, str.encode(error))
        return False
