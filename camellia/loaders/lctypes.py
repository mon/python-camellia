from ctypes import create_string_buffer, CDLL

from .compile import compile_auto
from .compile import get_shared_library_path

def ctypes_auto_loader():
    compile_auto()
    return CDLL(get_shared_library_path())
