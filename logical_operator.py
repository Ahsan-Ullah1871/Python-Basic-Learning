has_high_income= False
has_good_credit_card = True
has_criminal_record = False

#AND operator
if has_high_income and has_good_credit_card:
     print("And: I give you money")

#Or
if has_high_income or has_good_credit_card:
     print("Or: I give you money")

# NOT
if has_high_income and not has_criminal_record:
     print("NOT: I give you money")
