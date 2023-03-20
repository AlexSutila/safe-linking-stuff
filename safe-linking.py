
def obfuscate(pos, ptr):
    pos >> 12 ^ ptr

def deobfuscate(ptr):
    m = ptr >> 12 ^ ptr
    return m >> 24 ^ ptr

