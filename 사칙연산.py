#20244043 김민주
print('20244043 김민주')

from random import randint, choice    #random모듈에서 randint함수와 choice함수를 사용      

operators = ['+', '-', '*', '/'] #사칙연산 리스트

num_1 = 0 #랜덤한 숫자를 저장할 변수 1
num_2 = 0 #랜덤한 숫자를 저장할 변수 2
sum = 0 #연산 값을 저장할 변수
g = 0 #정답을 입력받을 변수
score = 0 #점수를 저장할 변수

print('사칙연산게임 5개의 문제를 맞춰주세요')
print('한 문제 당 1점 입니다.')
print('모든 문제의 정답은 십에서 일의 자리만 입력해주세요')

for i in range(5): #루프를 5번 반복한다.
    num_1 = randint(1,10)  #randomo 함수를 사용하여 1~10의 숫자 중 랜덤으로 num_1에 할당
    num_2 = randint(1,10)  #randomo 함수를 사용하여 1~10의 숫자 중 랜덤으로 num_1에 할당
    op = choice(operators) #choice 함수를 사용하여 operators리스트에서 랜덤하게 부호를 선택해서 op에 할당

    g = input(str(num_1) + op + str(num_2) + '의 값을 구하시오')

    if op == '+':   #만약 op가 +인 경우
        sum = num_1 + num_2 #num_1 + num_2의 값을 sum에 저장
    elif op == '-':  #만약 op가 -인 경우
        sum = num_1 - num_2  #num_1 - num_2의 값을 sum에 저장
    elif op == '*':  #만약 op가 *인 경우
        sum = num_1 * num_2  #num_1 * num_2의 값을 sum에 저장
    else:   #위의 조건이 거짓인 경우
        sum = num_1 / num_2 #num_1 / num_2의 값을 sum에 저장

    if int(sum) == int(g): #만약 정수sum의 값이 정수g의 값과 같다면
        score = score + 1  #score + 1의 값을 score에 저장
        print('정답입니다. 현재 점수',score,"점")
    else:  #아닌 경우
        print('틀렸습니다. 현재 점수',score,"점")


print('당신의 점수는',score,'점')
if score == 5:  #만약 score가 5인 경우
    print('축하드립니다. 만점입니다.')
elif 5 > score >= 3: #만약 score가 5보다 작고 3보다 크거나 같은 경우
    print('대단합니다. 만점에 도전해보세요')
elif 2 >= score >= 1:  #만약 score가 2보다 작거나 같고 1보다 크거나 같은 경우
    print('아쉽네요. 다시 한 번 도전해보세요.')
else: #위의 조건이 거짓인 경우
    print('조금 더 분발해보세요')