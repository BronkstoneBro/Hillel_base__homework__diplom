def progress(start, step, n):
    sequence = []
    for _ in range(n):
        sequence.append(start)
        start *= step
    return sequence


start1, step1, n1 = -2, -5, 6
start2, step2, n2 = 10, 3, 5

sequence_1 = progress(start1, step1, n1)
sequence_2 = progress(start2, step2, n2)

print("Послідовність 1:", sequence_1)
print("Послідовність 2:", sequence_2)
