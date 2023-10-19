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






from math import floor

working_total = 127

used_bills = {
    1: 0,
    5: 0,
    10: 0,
    20: 0,
    50: 0,
    100: 0
}

used_bills[100] = floor(working_total / 100)
working_total = working_total % 100

used_bills[50] = floor(working_total / 50)
working_total = working_total % 50

used_bills[20] = floor(working_total / 20)
working_total = working_total % 20

used_bills[10] = floor(working_total / 10)
working_total = working_total % 10

used_bills[5] = floor(working_total / 5)
working_total = working_total % 5

used_bills[1] = floor(working_total / 1)
working_total = working_total % 1


print(used_bills)




working_total = 127

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
    used_bills[bill_types[0]] = floor(working_total / bill_types[0])
    working_total = working_total % bill_types[0]
    del bill_types[0]

print(used_bills)