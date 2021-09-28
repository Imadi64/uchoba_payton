def number_in_english(number):
    l1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
          9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 0: 'zero',
          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', }
    l2 = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
          8: 'eighty', 9: 'ninety'}
    if len(str(number)) == 3:
        sot = int((str(number))[0])
        des = int((str(number))[1])
        eden = int((str(number))[2])
    elif len(str(number)) == 2:
        des = int((str(number))[0])
        eden = int((str(number))[1])
    if len(str(number)) == 1:
        return l1.get(number)
    if len(str(number)) == 2 and des != 1 and eden != 0:
        return l2.get(des) + ' ' + l1.get(eden)
    if len(str(number)) == 2 and des == 1:
        return l1.get(number)
    if len(str(number)) == 2 and eden == 0:
        return l2.get(des)
    if len(str(number)) == 3 and eden == 0 and des != 0:
        return l1.get(sot) + ' hundred and ' + l2.get(des)
    if len(str(number)) == 3 and (des == 1 or des == 0) and eden != 0:
        return l1.get(sot) + ' hundred and ' + l1.get(int((str(number))[1] + (str(number))[2]))
    if len(str(number)) == 3 and des == 0 and eden == 0:
        return l1.get(sot) + ' hundred'
    if len(str(number)) == 3 and des != 0 and eden != 0:
        return l1.get(sot) + ' hundred and ' + l2.get(des) + ' ' + l1.get(eden)




print(number_in_english(720).lower())