from collections import deque
n = int(input())
cards = deque()
for x in range(1, n+1):
    cards.append(x)

while len(cards) > 1:
    cards.popleft()
    return_card = cards.popleft()
    cards.append(return_card)

print(cards[0])
