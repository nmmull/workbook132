import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

rref = stdlib132.random.rref(2, 3, seed=1722463322)
rref2 = stdlib132.random.rref(3, 5, seed=236229483)

problems = [
    (
        "input",
        stdlib132.latex.matrix(rref)
    ),
    (
        "input2",
        stdlib132.latex.matrix(rref2)
    ),
]

for (name, problem) in problems:
    body = body.replace(f"<<{name}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
