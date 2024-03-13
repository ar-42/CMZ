import marshal
import zlib

file = input("file: ")

content = open(file, encoding='utf-8').read()

comp = compile(content, 'AnjingLo', 'exec')

enc = zlib.compress(marshal.dumps(comp))

with open('final.py', 'w') as f:
    f.write("import marshal,zlib\n")
    f.write(f"enc = {repr(enc)}\n")
    f.write("exec(marshal.loads(zlib.decompress(enc)))\n")
