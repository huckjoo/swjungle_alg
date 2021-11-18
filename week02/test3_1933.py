import sys
import heapq
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append([a[0], a[2], a[1]])  # 건물의 왼쪽좌표, 오른쪽좌표, 높이 순으로 arr에 저장
arr.sort()  # 왼쪽좌표 순으로 sort()
heap = []   # 현재 최대 height를 확인하기 위해서 heap구조를 사용, heap에 저장되어있다는 것은 어떤걸 의미하는가?
ans = []    # 나중에 출력될 답들을 미리 저장해놓는 공간
i = 0
n = len(arr)  # n은 arr의 길이
while i < n or heap:  # i가 n보다 작거나(arr의 모든것을 훑었거나) heap이 존재한다면, 실행
    # heap이 비었을 때 혹은 최대 높이의 오른쪽 좌표가 arr[i]의 왼쪽 좌표보다 클 때 heappush > 겹쳐있으므로 현재 어떤것이 가장큰지 heap에서 확인해야함
    if not heap or i < n and arr[i][0] <= -heap[0][1]:
        temp = arr[i][0]  # temp에 현재 arr 왼쪽좌표를 저장해놓는다.
        # i < n이고 현재 arr 왼쪽좌표가 temp일때(처음에는 무조건 실행, i가 증가하면 넘어감(값이 같지 않는 한))
        while i < n and arr[i][0] == temp:
            # heap에는 높이,오른쪽좌표가 maxheap형태로 넣어진다.
            heapq.heappush(heap, (-arr[i][2], -arr[i][1]))
            i += 1
    # arr[i]의 왼쪽좌표가 heap[0]의 오른쪽 좌표보다 클 때
    else:
        # temp에는 현재 최대높이건물의 오른쪽좌표가 들어간다. 왜? 얘보다 작거나 같으면 heappop해주려고
        temp = -heap[0][1]
        # heap이 존재하고 while문이 돌 동안 그 전의 heap들의 건물의 오른쪽좌표가 temp보다 작거나 같다면 다 빼준다.
        while heap and -heap[0][1] <= temp:
            heapq.heappop(heap)
    if heap:
        height = -heap[0][0]      # heap이 있다면 최대높이건물의 높이를 저장한다.
    else:
        height = 0                # heap이 없다면 height를 0으로 놓는다.
    # height와 방금 저장한 ans와 다르다면! ans = [[1,11]]
    if not ans or height != ans[-1][1]:
        # ans에 temp(왼쪽이든 오른쪽이든 변화하는 값),height를 저장한다.
        ans.append([temp, height])
for a in ans:
    print(*a, end=' ')
