kilometers = 12.25
miles = 7.38
factor_m2k = 1.60934

miles_to_kilometers = miles * factor_m2k
kilometers_to_miles = kilometers / factor_m2k

print(miles, 'miles is', round(miles_to_kilometers, 2), 'kilometers')
print(kilometers, 'kilometers is', round(kilometers_to_miles, 2), 'miles')
