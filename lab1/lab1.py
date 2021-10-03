# calcultator.py
def sum(m,n):
	result = m
	if n < 0:
		for i in range(abs(n)):
			result -= i
	else:
		for i in range(n):
			result += 1
	return result
        
def divide(m,n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0 # uno dei due e' positivo?
    n = abs(n)
    m = abs(m)

    while (m - n >= 0):
        m -= n
        result += 1

    result = -result if negativeResult else result # <result> e' uguale a <-result> se <negativeResult> e' uguale a 1, altrimenti rimane invariato
    return result
