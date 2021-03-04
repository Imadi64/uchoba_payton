def number_in_english(number):
    a = ""
    sivri = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
             5: "five", 6: "six", 7: "seven", 8: "eight",
             9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
             13: "thetin", 14: "fourtin",
             15: "fifteen", 16: "sixtin", 17: "seventin", 18: "eighteen",
             19: "nineteen", 20: "twenty", 30: "theten",
             40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy",
             80: "eighty", 90: "ninety", 100: "hundred and"}
    if number <= 20:
        a = sivri[number]
    if 20 < number < 100:
        if number % 10 == 0:
            a = sivri[(number // 10) * 10]
        else:
            a = sivri[(number // 10) * 10] + " " + sivri[number % 10]
    if number >= 100:
        if 1 <= number % 100 < 20:
            a = sivri[number // 100] + " " + sivri[100] + " " + sivri[
                number % 100]
        elif number % 100 == 0:
            a = sivri[number // 100] + " hundred"
        elif number % 10 == 0:
            a = sivri[number // 100] + " " + sivri[number // 10]
        elif 20 <= number % 100 <= 99:
            a = sivri[number // 100] + " " + sivri[100] + " " + sivri[
                (number % 100 // 10) * 10] + " " + sivri[number % 10]
    return a



print(number_in_english(720).lower())