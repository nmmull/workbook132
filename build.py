import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

subs = [
  stdlib132.latex.matrix(
    stdlib132.random.int_matrix(1, 4)
  ),
  stdlib132.latex.matrix(
    stdlib132.random.int_matrix(4, 1)
  )
]

for i, sub in enumerate(subs):
    body = body.replace(f"<<{i}>>", sub)

with open('main.tex', 'w') as f:
    f.write(body)
