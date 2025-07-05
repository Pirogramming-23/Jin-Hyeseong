from random import randint

num = 0
gameOver = False
winPlayer = False

def brGame(player):
    global num, gameOver, winPlayer
    if player == "player":
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
    else:
        n = randint(1,3)

    for i in range(n):
        num+=1
        print("{0} {1}".format(player, num))
        if num == 31:
            gameOver=True
            if player == "computer":
                winPlayer = True
            break


while(not gameOver):
    brGame("computer")
    if(gameOver): break
    brGame("player")


if(winPlayer): print("player win!")
else: print("computer win!")