import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

problems = [
    probgen.compute_lin_comb_vec(2, 2, 720840271),
    probgen.compute_lin_comb_vec(3, 3, 2553921248),
]

for i, problem in enumerate(problems):
    body = body.replace(f"<<{i}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
