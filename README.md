For dealing with the additional headache presented by the jumbling of the 'next-pointer' during tcache poisoning with newer versions of libc, mainly posting for my own future reference :)

# Obfuscation
```
def obfuscate(pos, ptr):
┊   pos >> 12 ^ ptr
```
Where pos is the address of the allocation and ptr is the address to be obfuscated.

# De-obfuscation
```
def deobfuscate(ptr):
┊   m = ptr >> 12 ^ ptr
┊   return m >> 24 ^ ptr
```
Where ptr is the pointer to be de-obfuscated.
