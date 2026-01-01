from stdlib132 import probgen

with open('main-template.tex', 'r') as f:
    body = f.read()

problems = [
    (
        "determineCoefficientAugmentedMatrix2",
        probgen.determine_coefficient_augmented_matrix(
            num_eqs=2,
            num_vars=2,
            seed=2009837464,
        )
    ),
    (
        "determineCoefficientAugmentedMatrix1",
        probgen.determine_coefficient_augmented_matrix(
            num_eqs=3,
            num_vars=3,
            seed=3209557267,
        )
    ),
    (
        "determineCoefficientAugmentedMatrix3",
        probgen.determine_coefficient_augmented_matrix(
            num_eqs=4,
            num_vars=5,
            seed=2878334791,
        )
    ),
    (
        "determineUniqueSolutionLinearSystem1",
        probgen.determine_unique_solution_linear_system(
            num_eqs=2,
            seed=3094789175,
        )
    ),
    (
        "determineUniqueSolutionLinearSystem2",
        probgen.determine_unique_solution_linear_system(
            num_eqs=3,
            seed=425464091,
        )
    ),
    (
        "determineUniqueSolutionLinearSystem3",
        probgen.determine_unique_solution_linear_system(
            num_eqs=3,
            seed=2573908387,
        )
    ),
    (
        "determineUniqueSolutionLinearSystem4",
        probgen.determine_unique_solution_linear_system(
            num_eqs=4,
            seed=4148622710,
        )
    ),
]

for (name, problem) in problems:
    body = body.replace(f"<<{name}>>", problem)

with open('main.tex', 'w') as f:
    f.write(body)
