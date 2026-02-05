import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

subs = [
  probgen.gen_form_sol_mat_eq(
      rows=2,
      cols=2,
      rank=2,
      force_consistent=True,
  ),
]

for i, sub in enumerate(subs):
    body = body.replace(f"<<{i}>>", sub)

with open('main.tex', 'w') as f:
    f.write(body)
