def calculate_years(principal, interest, tax, desired):
    year = 0
    if principal == desired:
        return year
    else:
        while principal < desired:
            some = (principal * interest) - (principal * interest * tax)
            principal += some
            year += 1
        return year


a = calculate_years(1000, 0.05, 0.18, 1100)
print(a)
