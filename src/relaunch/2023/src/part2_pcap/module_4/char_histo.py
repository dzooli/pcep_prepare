from pprint import pprint
from time import perf_counter, perf_counter_ns

inf_name = input("Enter the filename: ")
chars = None
try:
    with open(inf_name, "rb") as inf:
        chars = inf.read()
except FileNotFoundError:
    print("File not found")
    exit()
except IOError as exc:
    pprint(exc)
    exit()

# with bytearray
print("\nCounting with bytearray indexes...")
hist = bytearray(26)
start_time = perf_counter_ns()
for char in chars:
    ch = chr(char).lower()
    try:
        hist[ord(ch) - 97] += 1
    except IndexError:
        continue
end_time = perf_counter_ns()
i = 0
for counts in hist:
    if counts:
        print(f"{chr(i+97)} -> {int(counts)}")
    i += 1
print(f"Counting time: {(end_time-start_time)}ns")

# with dict
print("\nCounting with dictionary keys...")
hist = {chr(k).lower(): 0 for k in range(97, 123)}
start_time = perf_counter_ns()
for char in chars:
    ch = chr(char).lower()
    try:
        hist[ch] += 1
    except KeyError:
        continue
end_time = perf_counter_ns()
result = {ch: co for ch, co in hist.items() if co > 0}
for ch,co in result.items():
    print(f"{ch} -> {co}")
print(f"Counting time: {(end_time-start_time)}ns")
