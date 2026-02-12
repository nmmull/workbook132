import sys
import re
import stdlib132

if len(sys.argv) != 2:
    print("usage: python3 build.py <filename>")
    exit(1)

filename = sys.argv[1]

text = None
with open(filename, 'r') as f:
    text = f.read()

if not text:
    print("error opening file")
    exit(1)

env = { 'stdlib132': stdlib132 }

def replace_match(m):
    code = m.group(1).strip()
    value = eval(code, env)
    return str(value)

pattern = re.compile(r'<<(.*?)>>', re.S)
text = pattern.sub(replace_match, text)

with open(filename, 'w') as f:
    f.write(text)
