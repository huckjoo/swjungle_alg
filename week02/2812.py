N, K = map(int, input().split())  # 여기서 대문자의 의미는 변하지 않는 값을 의미한다.
li = list(input())
k, stack = K, []  # 여기서 k에 K를 넣어주는 것은 k를 바꾸고, 사용하겠다는 의미이다. -> 뭐가 틀렸는지 찾는데 한참걸림
for i in range(N):
    while k > 0 and stack and stack[-1] < li[i]:
        stack.pop()  # 보통 pop부터 먼저 적는 것 같다.
        k -= 1
    stack.append(li[i])
print(''.join(stack[:N-K]))
