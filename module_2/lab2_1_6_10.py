# test data
# input: 1
# output: 0.6000000000000001
# input: 10
# output: 0.09901951566867294
# input 100
# output: 0.009999000199950014
# input: -5
# output: -0.19258202567760344

x = float(input('Enter x: '))
outp = 1/(x+(1/(x+(1/(x+(1/x))))))
print(outp)
