def tip_calc():
    print('Welcome to the tip calculator.')
    total=float(input('What was the total bill?\n'))
    num_of_people=int(input('How many people to split the bill?\n'))
    percent_tip=1+int(input('What percentage tip would you like to give? 10,12,or 15?\n'))/100
    final = str(round((total/num_of_people)*percent_tip,2))
    print('Each person should pay: $'+ final)


tip_calc()
