
def DAC(a, b, c):  # a = 10, b = 11, c = 12
    if b == 1:  # 종료조건
        print(a % c)
        return a % c  # return으로 왜 a % c 인가?

    if b % 2 == 0:
        # DAC(10,5) -> 이때 DAC로 들어가는가 안들어가는가? #들어간다(디버깅해봄)
        temp = DAC(a, b//2, c)
        print('temp:', temp)  # b//2를 하면 짝수면 그냥 하면 되고 홀수면 a하나가 날라간다.
        print('짝수일때', (temp*temp) % c)
        return temp * temp % c
    else:
        # DAC(10,5) -> 이때 DAC로 들어가는가 안들어가는가? #들어간다(디버깅해봄)
        temp = DAC(a, b//2, c)
        print('temp:', temp)  # b//2를 하면 짝수면 그냥 하면 되고 홀수면 a하나가 날라간다.
        print('홀수일때', (temp*temp) % c)
        return temp * temp * a % c


print(DAC(10, 11, 12))
