def bank(years, money):
    sus = money + money / 100 * 10
    sum = years * sus
    print(sum)


bank(9, 10000)
