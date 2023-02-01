

def is_valid_month(month: str) -> bool:
    pp = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    realmonths = []
    for i in range(len(pp)):
        lowercasemonths = pp[i].lower()
        realmonths.append(lowercasemonths)
    
    lowercasemonth = month.lower()

    if lowercasemonth in lowercasemonths:
        return True
    else:
        return False


print(is_valid_month("DeCember"))