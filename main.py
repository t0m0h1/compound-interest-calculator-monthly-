#monthly AER total calculator

#principal:
P = float(input("Enter amount: "))

#rate 
# must be entered as .0(number), e.g. 3% AER = .03

r = float(input("Enter AER: "))


#compounding periods will be 12 months 

n = 12


#total years will be 1 initially

t = 1


#calculate amount

calc = P*(pow((1+r/n), n*t))

def calc_amount():
    print(calc)


calc_amount()
