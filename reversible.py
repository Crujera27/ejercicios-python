while True:
    num = int(input())
    if num == 0:
        break
    reversed_num = int(str(num)[::-1])
    result = num + reversed_num
    if all(int(digit) % 2 != 0 for digit in str(result)):
        print("SI")
    else:
        print("NO")