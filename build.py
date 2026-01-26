import stdlib132
from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

problems = [
    probgen.gen_form_sol_vec_eq(3, 4, 2295471575),
    probgen.gen_form_sol_vec_eq(2, 4, 3131868451),

]

for i, problem in enumerate(problems):
    body = body.replace(f"<<{i}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
