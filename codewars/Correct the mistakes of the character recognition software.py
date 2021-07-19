def correct(s):
    new = ""
    for i in s:
        if i == "5":
            new += "S"
        elif i == "1":
            new += "I"
        elif i == "0":
            new += "O"
        else: new += i

    return new

print(correct("PAR15000115555501"))