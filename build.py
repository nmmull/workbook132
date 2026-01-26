import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

problems = [
    probgen.equiv_vector_eq(3, 3, 2356493351),
    probgen.equiv_vector_eq(2, 4, 1191322468),
]
# 1444954305
# 465354056

for i, problem in enumerate(problems):
    body = body.replace(f"<<{i}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
