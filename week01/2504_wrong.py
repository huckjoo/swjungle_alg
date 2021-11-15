# 틀린 코드
def sol(data):
    stack = []
    for p in data:
        if p == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    return 0
                elif top == '(':
                    if t == 0:
                        stack.append(2)
                        break
                    else:
                        stack.append(t*2)
                        break
                else:  # top이 숫자일때
                    t += top
        elif p == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    return 0
                elif top == '[':
                    if t == 0:
                        stack.append(3)
                        break
                    else:
                        stack.append(t*3)
                        break
                else:
                    t += top
        else:
            stack.append(p)
    return stack


data = input()
res = sol(data)

if res == 0:
    res = []
print(0 if '(' in res or '[' in res else sum(res))
