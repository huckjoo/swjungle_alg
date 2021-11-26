import sys
data = list(sys.stdin.readline().strip())
new = []
flag = 0  # 괄호 flag
temp = ''
for x in data:
    if x.isdigit():  # 숫자면
        temp += x
    else:  # 문자면
        new.append(str(int(temp)))
        temp = ''
        if x == '-' and flag == 0:
            new.append(x)
            new.append('(')
            flag = 1
        elif x == '-' and flag == 1:
            new.append(')')
            new.append(x)
            new.append('(')
            flag = 1
        elif x == '+':
            new.append(x)
if temp != '':
    new.append(str(int(temp)))
if flag == 1:  # 마지막 괄호닫기
    new.append(')')

ans = ''.join(new)
print(eval(ans))
