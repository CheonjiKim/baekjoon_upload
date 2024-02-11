A, B = map(str, input().split())
rev_A = A[2] + A[1] + A[0]
rev_B = B[2] + B[1] + B[0]
rev_A = int(rev_A)
rev_B = int(rev_B)
print(rev_A if (rev_A > rev_B) else rev_B)
