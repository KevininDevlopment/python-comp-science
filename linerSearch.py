lis = [1, 2, 3, 4, 5, 6]


for i in lis:
    i += 1
    print(i)
    if i == 3:
        print("found the number " + str([i]))
        print("Breaking from this fudging loop")
        break
    else:
        print("number not found")
