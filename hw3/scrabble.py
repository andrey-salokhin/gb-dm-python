#### 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 

dict1 = {
    1: 'A, E, I, O, U, L, N, S, T, R',
    2: 'D, G',
    3: 'B, C, M, P',
    4: 'F, H, V, W, Y',
    5: 'K',
    8: 'J, X',
    10: 'Q, Z',
}

word1 = 'notebook'
result = 0

for letter in word1.upper():
    for key, value in dict1.items():
        if (letter in value):
            result+=key
        continue
        

print(result)