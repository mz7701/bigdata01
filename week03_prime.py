number = int(input())
count =0

if number >= 2:

    for i in range(2, number):
        if number % i == 0:
            count = count + 1
        print(i, end=" ")

    if count == 2:
        print(f"{number}는(은) 소수입니다")
    else:
        print(f"{number}는(은) 소수가아닙니다")