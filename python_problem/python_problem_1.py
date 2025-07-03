num = 0

while True:
    user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    # 정수인지 확인
    if not user_input.isdigit():
        print("정수를 입력하세요")
        continue

    n = int(user_input)

    # 1, 2, 3 중 하나인지 확인
    if n not in [1,2,3]:
        print("1,2,3 중 하나를 입력하세요")
        continue
    break

for i in range(n):
    num+=1
    print("playerA : {0}".format(num))
