num = 0
while True:
    n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    if n in [1,2,3]:
        break
    else:
        print("잘못된 입력입니다. 1, 2, 3 중 하나를 입력해주세요.")

