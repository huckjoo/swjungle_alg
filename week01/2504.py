s = input()


def is_check(s):    # 올바른 괄호열인지 확인하는 함수 >> pop시키기 때문에 무조건 순서를 지키게 되어있음
    stack = []
    flag = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])  # 그냥 집어넣는다.

        else:    # ) ] 일 때,
            if s[i] == ')':
                if stack and stack[-1] == '(': 
                    stack.pop()
                else:
                    flag = False

            else:    # ] 일 때
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False

    if not stack and flag: #stack이 다 꺼내지고, flag도 true이면,
        return True
    return False


def calc_value(s):    # 괄호의 값을 계산하는 함수
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        else:    # ) ]
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2 #pop하고 2를 넣어주는 대신 그냥 스택 가장 위에있는 놈을 2로 바꿔준다.
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '(':
                            stack[-1] = temp * 2
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()

            else:    # ]
                if stack[-1] == '[':
                    stack[-1] = 3
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '[':
                            stack[-1] = temp * 3
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)


if is_check(s):
    print(calc_value(s))
else:
    print(0)
