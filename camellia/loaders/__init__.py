try:
    from .lcython import cython_auto_loader as default_auto_loader
except ImportError:
    try:
        from .lcffi import cffi_auto_loader as default_auto_loader
    except ImportError:
        from .lctypes import ctypes_auto_loader as default_auto_loader

from .compile import get_shared_library_name

try:
    camlib = default_auto_loader()
except:
    raise
    print("Please install gcc and include camellia.c with this file, "
          "then run with sudo to compile!")
    raise ImportError(get_shared_library_name()+" not found. Please install "
                      "gcc and include camellia.c with this file, then run "
                      "with sudo to compile!")
