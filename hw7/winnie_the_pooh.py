#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 

def winnie_the_pooh_rythm(string: str, is_extended: bool = True) -> None:
    vowels = set("аяуюоеёэиы");
    result_letter_list = list()
    vowels_counter_list = list()
    for line in string.replace('-', '').split():
        current_line_result = {}
        current_vowels_counter = 0
        for letter in line:
            if letter in vowels:
                if letter in current_line_result:
                    current_line_result[letter] = current_line_result[letter] + 1
                else:
                    current_line_result[letter] = 1
                current_vowels_counter += 1
        result_letter_list.append(current_line_result)
        if current_vowels_counter: vowels_counter_list.append(current_vowels_counter)
    return [len(set(vowels_counter_list)) == 1, result_letter_list] if is_extended else len(set(vowels_counter_list)) == 1
        

print(winnie_the_pooh_rythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
print(winnie_the_pooh_rythm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(winnie_the_pooh_rythm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
print(winnie_the_pooh_rythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(winnie_the_pooh_rythm("Пам-парам-пурум Пум-пурум-карам"))