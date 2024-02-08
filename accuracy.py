import numpy as np
from numpy.polynomial.chebyshev import chebfit, chebval, chebinterpolate

def calculate_rmse(func, poly, domain):
	# Calculate the RMSE between the function and polynomial values at domain points
	poly_values = chebval(domain, poly)
	func_values = np.sign(domain)

	rmse = np.sqrt(np.mean((func_values - poly_values) ** 2))
	return rmse

def calculate_error(poly, domain):

	poly_values = chebval(domain, poly)
	func_values = np.sign(domain)

	err = np.absolute(poly_values - func_values)
	acc = np.ones_like(err) - err
	# print(err[0], err[1], err[2], err[3])
	# print(acc[0], acc[1], acc[2], acc[3])
	# print(poly_values[0], poly_values[1], poly_values[2], poly_values[3])

	errors = 0

	for i in range(len(acc)):
		if acc[i] < 0.8:
			acc[i] = 0
			errors += 1

	summary = np.average(acc)
	return summary, errors


'''
(sum * 10)/ (4096)
'''
# существующие
# подходы
# и
# ограничения
#
# Вводная - почему это важно
#
# Пример текущих работ, как считать sign на ckks
# Результат Чебышева
# Результаты нашего виннера

