from pprint import pprint

# bad assignment
bya = bytearray(10)
try:
    bya[2] = 10000
except ValueError as exc:
    pprint(exc)

bya[2] = 10
with open("file.bin", "wb") as outf:
    outf.write(bya)

with open("file.bin", "rb") as inf:
    readed = bytearray(inf.read())
    inf.seek(0)
    breaded = inf.read()

pprint(readed)
pprint(type(readed))
pprint(type(breaded))