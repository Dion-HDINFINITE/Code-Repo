import fractions

u = int(input("variable of what number : "))
un = int(input("Last variable : "))
a = float(fractions.Fraction(input("First number : ")))
r = float(fractions.Fraction(input("Ratio : ")))

outcome = 0
for n in range(u, un+1):
    syllables = a*(r**(n-1))
    outcome = outcome + syllables
    print(syllables)

print('The sum of all variables (Sn) = ', outcome)