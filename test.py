from SCons.Environment import Environment


flags = {
    'CFLAGS': ['1', '2', '3']
}
env = Environment()

# env['CFLAGS'] = ['0']
print(flags)
print(env.subst('${CFLAGS}'))
for i in range(10):
    env.MergeFlags(flags)
    print(flags)
    print(env.subst('${CFLAGS}'))
