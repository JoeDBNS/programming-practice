# Highest Bill Returns
# -----------------------------------------
# Enter total number of dollars desired and the program will return that total
# using the fewest number of individual dollar bills.



def ReturnFewestBillAmounts(working_total):
    bill_types = [100, 50, 20, 10, 5, 1]

    used_bills = {
        1: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0
    }

    while working_total > 0:
        if working_total >= bill_types[0]:
            working_total -= bill_types[0]
            used_bills[bill_types[0]] += 1
        else:
            del bill_types[0]
    
    return used_bills



print( ReturnFewestBillAmounts(127) )
print( ReturnFewestBillAmounts(43) )
print( ReturnFewestBillAmounts(999) )
print( ReturnFewestBillAmounts(2) )