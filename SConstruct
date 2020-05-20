from SCons.Script import Environment
from typing import Dict, List, Union, AnyStr, Any
from copy import deepcopy
from random import shuffle, randint


global_env = Environment()
prog_src = global_env.Textfile(
    target='#src/prog.cpp',
    source=['int main() { return 0; }'])
lib_src = global_env.Textfile(
    target='#src/lib.cpp',
    source=['extern "C" int get_secret() { return 42; }']
)


build_flags: Dict[str, Union[str, List[str]]] = {
    'CFLAGS': [
        '-pipe',
        '-Wall',
        '-Wextra',
        '-Wno-unused-result',
        '-Wno-unused-local-typedefs',
        '-fno-omit-frame-pointer',
        '-Wno-missing-field-initializers',
        '-pthread',
        '-ggdb',
    ],
    'CXXFLAGS': [
        '${CFLAGS}', '-std=c++11'
    ],
    'LINKFLAGS': [
        '-rdynamic',
        '-pthread',
        '-Wl,--as-needed',
        '-Wl,--build-id=sha1',
    ],
    'LIBPATH': ['.'],
    'CPPPATH': ['#include'],
    'CPPDEFINES': [
        '__STDC_FORMAT_MACROS=1',
        'FMT_HEADER_ONLY=1',
    ],
    'RPATH': ['.']
}


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


class Binary:
    env: Environment

    def __init__(self, env: Environment):
        self.env = env.Clone()


class Program(Binary):
    def __init__(self, env: Environment):
        super().__init__(env)


class Library(Binary):
    def __init__(self, env: Environment):
        super().__init__(env)


class Builder:
    env: Environment
    targets: List[Binary]
    flags: Dict[str, Union[str, List[str]]]

    def __init__(self, env: Environment):
        self.env = env.Clone()
        self.targets = []
        self.flags = deepcopy(build_flags)

    def add_program(self, ident: int):
        prog = Program(self.env)

        prog_flags = deepcopy(self.flags)
        assert(compare_dicts(self.flags, prog_flags))

        prog.env.MergeFlags(self.flags)
        if not compare_dicts(self.flags, prog_flags):
            print(f'>>> ({id(prog.env)}) self.flags = {self.flags}')

        obj = prog.env.Object(
            target=f'#build_dir/prog{ident}',
            source=prog_src)
        prog.env.Program(
            target=f'#build_dir/prog{ident}',
            source=obj)

        self.targets.append(prog)

    def add_library(self, ident: int):
        lib = Library(self.env)

        lib_flags = deepcopy(self.flags)
        assert(compare_dicts(self.flags, lib_flags))

        lib.env.MergeFlags(self.flags)
        if not compare_dicts(self.flags, lib_flags):
            print(f'>>> ({id(lib.env)}) self.flags = {self.flags}')

        obj = lib.env.SharedObject(
            target=f'#build_dir/lib{ident}',
            source=lib_src)
        lib.env.SharedLibrary(
            target=f'#build_dir/lib{ident}',
            source=obj)

        self.targets.append(lib)


idents: List[int] = [i for i in range(5)]
shuffle(idents)

builder = Builder(global_env)
for i in idents:
    builder.add_program(i)
    if randint(0, 100) % 2 == 0:
        builder.add_library(i)
