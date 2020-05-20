from SCons.Environment import Environment
from copy import deepcopy
from random import shuffle


def add_program(env, ident, flags, src):
    prog_env = env.Clone()
    prog_env.MergeFlags(flags)
    obj = prog_env.Object(
        target='#build_dir/prog{}'.format(ident),
        source=src)
    prog_env.Program(
        target='#build_dir/prog{}'.format(ident),
        source=obj)


def add_library(env, ident, flags, src):
    lib_env = env.Clone()
    lib_env.MergeFlags(flags)
    obj = lib_env.SharedObject(
        target='#build_dir/lib{}'.format(ident),
        source=lib_src)
    lib_env.SharedLibrary(
        target='#build_dir/lib{}'.format(ident),
        source=obj)


flags = {
    'CFLAGS': ['-pipe', '-pthread', '-g'],
    'CXXFLAGS': ['${CFLAGS}', '-std=c++11'],
    'LINKFLAGS': ['-rdynamic', '-pthread'],
    'CPPDEFINES': ['DEF1=1', 'DEF2=2'],
}

env = Environment(tools=['default', 'textfile'])
prog_src = env.Textfile(
    target='#src/prog.cpp',
    source=['int main() { return 0; }'])
lib_src = env.Textfile(
    target='#src/lib.cpp',
    source=['extern "C" int get_secret() { return 42; }']
)

idents = [i for i in range(3)]
shuffle(idents)
print('Target add order: {}'.format(idents))

print('original -> {}'.format(flags))
for ident in idents:
    # replace `flags` with `deepcopy(flags)` to work-around the problem
    add_program(env, ident, flags, prog_src)
    print('prog{}    -> {}'.format(ident, flags))
    if ident % 2 == 0:
        # replace `flags` with `deepcopy(flags)` to work-around the problem
        add_library(env, ident, flags, lib_src)
        print('lib{}     -> {}'.format(ident, flags))
