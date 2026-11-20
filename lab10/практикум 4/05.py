rank = ["6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

a = input()
n = int(input())

for i in range(n):
    card1 = input().split()
    card2 = input().split()
    
    # card1[0] - достоинство, card1[1] - масть
    
    if card1[1] == card2[1]:
        if rank.index(card2[0]) > rank.index(card1[0]):
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        if card2[1] == a:
            print(1, end=" ")
        else:
            print(0, end=" ")