def geometric_progression(start, step, n):
    current_term = start
    for _ in range(n):
        yield current_term
        current_term *= step


start1, step1 = -2, -5
n1 = 6
progression1 = geometric_progression(start1, step1, n1)

print("Первая последовательность:")
for term in progression1:
    print(term)

start2, step2 = 10, 3
n2 = 6
progression2 = geometric_progression(start2, step2, n2)

print("Вторая последовательность:")
for term in progression2:
    print(term)
