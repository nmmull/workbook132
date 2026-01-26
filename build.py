import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

problems = [
]

for i, problem in enumerate(problems):
    body = body.replace(f"<<{i}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
