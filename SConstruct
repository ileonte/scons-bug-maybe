from SCons.Environment import Environment
from SCons.Variables import Variables, BoolVariable
from SCons.Script import Help, Exit
from typing import Dict, List, Union, AnyStr, Any
from copy import deepcopy
from random import shuffle


def compare_dicts(d1: Dict[str, Any], d2: Dict[str, Any]) -> bool:
    for k1 in d1.keys():
        if k1 not in d2:
            return False
    for k2 in d2.keys():
        if k2 not in d1:
            return False
    for k in d1.keys():
        if d1[k] != d2[k]:
            return False
    return True


def add_program(env: Environment, ident: int, flags: Any, src: Any):
    prog_env = env.Clone()

    prog_flags = deepcopy(flags)
    assert(compare_dicts(flags, prog_flags))

    prog_env.MergeFlags(flags)
    if not compare_dicts(flags, prog_flags):
        print(f'prog{ident} = {flags}')

    obj = prog_env.Object(
        target=f'#build_dir/prog{ident}',
        source=src)
    prog_env.Program(
        target=f'#build_dir/prog{ident}',
        source=obj)


def add_library(env: Environment, ident: int, flags: Any, src: Any):
    lib_env = env.Clone()

    lib_flags = deepcopy(flags)
    assert(compare_dicts(flags, lib_flags))

    lib_env.MergeFlags(flags)
    if not compare_dicts(flags, lib_flags):
        print(f'lib{ident}  = {flags}')

    obj = lib_env.SharedObject(
        target=f'#build_dir/lib{ident}',
        source=lib_src)
    lib_env.SharedLibrary(
        target=f'#build_dir/lib{ident}',
        source=obj)


global_flags = {
    'CFLAGS': ['-pipe', '-pthread', '-g'],
    'CXXFLAGS': ['${CFLAGS}', '-std=c++11'],
    'LINKFLAGS': ['-rdynamic', '-pthread'],
    'CPPDEFINES': ['DEF1=1', 'DEF2=2'],
}

global_env = Environment()

prog_src = global_env.Textfile(
    target='#src/prog.cpp',
    source=['int main() { return 0; }'])
lib_src = global_env.Textfile(
    target='#src/lib.cpp',
    source=['extern "C" int get_secret() { return 42; }']
)

idents: List[int] = [i for i in range(5)]
shuffle(idents)  # comment this to work-around the issue
print(f'Target add order: {idents}')

for i in idents:
    add_program(global_env, i, global_flags, prog_src)
    if i % 2 == 0:
        add_library(global_env, i, global_flags, lib_src)
