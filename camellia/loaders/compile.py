import os
import sys
import platform

__version__ = "0.1"

d = dict(
    linux='.so',
    freebsd='.so',
    openbsd='.so',
    netbsd='.so',
    unix='.so',  # ???
    darwin='.so',
    win32='.dll',
    cygwin='.dll',
)

d['Pocket PC'] = '.dll'

try:
    __file__
except NameError:
    __file__ == "."

def get_shared_library_name():
    plat = sys.platform.replace('linux2', 'linux').replace('linux3', 'linux')

    base = "camellia-{}-{}-{}"+d.get(plat, '.shared')

    proc = platform.machine() if platform.machine else "unknown"
    arch = platform.architecture()[1]

    return base.format(__version__, plat, proc)

def get_shared_library_path():
    return OUT

ADD = "./" if not os.path.dirname(__file__) else ""

IN = os.path.join(os.path.dirname(__file__), "camellia.c")
OUT = os.path.join(os.path.dirname(__file__), get_shared_library_name())

ucc = os.environ.get('CC', 'cc')

acc = ["cc", "gcc", "clang", "tcc"]

if ucc in acc:
    i = acc.index(ucc)
    acc.pop(i)
else:
    acc = [UCC] + acc
#CMD = "%s %s -shared -fPIC -O3 -o%s" % (GCC, IN, OUT)

def try_compiler(cc, inf, outf):
    cmd = "%s %s -shared -fPIC -O3 -o%s" % (cc, inf, outf)
    print (cmd)
    try:
        assert not os.system(cmd)
    except:
        print("Compiler %s failed! Not existend or no permission?" % cc)
        return 1
    else:
        return 0

def compile_auto():

    if not os.path.exists(OUT) and sys.platform != "win32":  # win32 is precompiled
        for cc in acc:
            print("Compiling camellia with %s..." % cc)
            if not try_compiler(cc, IN, OUT):
                break
            
        else:
            raise Exception("Please install gcc, clang or tcc and include "
                            "\"camellia.c\" with this file, then run with "
                            "sudo to compile!")
        print("Done!")
