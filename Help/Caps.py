# import fileinput

# text_to_caps = ""

# for line in fileinput.input():
#     text_to_caps += line.upper()

# print(text_to_caps)


import sys

# text = sys.stdin.read()
# print(text.upper())

ask = input()
print(ask.upper())
while ask:
    try:
        ask = input()
        print(ask.upper())
    except EOFError:
        print("FINISH")
        sys.exit()
