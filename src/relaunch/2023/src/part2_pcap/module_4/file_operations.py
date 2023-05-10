from pprint import pprint

FILENAME = "testfile.txt"
print("Creating file...")
try:
    with open(FILENAME, "w") as f:
        print("some content", file=f)
        print("some other content", file=f)
except Exception as exc:
    print(ecx)

print("Reading created file...")
try:
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        pprint(lines)
except Exception as exc:
    print(exc)

print("Truncating file...")
try:
    with open(FILENAME, "w") as f:
        if f.readable():
            lines = f.readlines()
            pprint(lines)
except Exception as exc:
    print(exc)

print("Recreating file...")
try:
    with open(FILENAME, "r+") as f:
        print("Actual content", f.readlines())
        print("Writing new content...")
        print("new content", file=f)
        print("Reading the new file...")
    with(open(FILENAME, "r")) as f:
        print(f.readlines())
except Exception as exc:
    print(exc)

print("Appending new content...")
try:
    with open(FILENAME, "a+") as f:
        print("brand new content", file=f)
    with open(FILENAME, "r") as f:
        print("New content:", f.readlines())
except Exception as exc:
    print(exc)

