from smpc.poly import evaluate_polynomial, lagrange_interpolation
from smpc.random import generate_random
from smpc.smpc import Party


parties = [Party(15), Party(20), Party(30)]


p = Party(65)

n = 4
k = 2
shares = p.shares(n, k)

print(shares)
x0 = shares[0]
x2 = shares[2]
x4 = shares[3]

print(x0, x2)
x_1 = lagrange_interpolation(0, k=2, j=x0[0], nodes=(x0[0], x2[0], x4[0]))
x_2 = lagrange_interpolation(0, k=2, j=x2[0], nodes=(x0[0], x2[0], x4[0]))
x_3 = lagrange_interpolation(0, k=2, j=x4[0], nodes=(x0[0], x2[0], x4[0]))


print(x0[1]*x_1 + x2[1]*x_2 + x4[1]*x_3)


# x_1 = lagrange_interpolation(0, 3, 1)
#x_2 = lagrange_interpolation(0, 3, 2)
#x_3 = lagrange_interpolation(0, 3, 3)
#
#
#print('Shares', shares)
#print(x_1)
#print('Sum', x_1 * shares[0])
#print(x_2)
#print('Sum', x_2 * shares[1])
#print(x_3)
#print('Sum', x_3 * shares[2])
#
#print(x_1 + x_2 + x_3)



