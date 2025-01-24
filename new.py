import math
price = 1000000
has_good_credit = input('You have a good credit. Answer True/False')
print(has_good_credit)
if has_good_credit == 'True' :
    down_payment = price * 0.1
    print('You have a good credit score')
else:
    down_payment = price * 0.2
    print('You do not have a good credit score')
print (f"Down Payment: ${int(down_payment)}")

