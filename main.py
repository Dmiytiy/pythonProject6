# создайте словари со словами в каждом словаре должно быть 5 пар слов
words_easy = {'apple':'яблоко', 'strawberry':'клубника', 'orange':'аппельсин', 'banana':',банан', 'cherry':'вишня',}
words_medium = {'pen':'ручка', 'glue':'клей', 'paper':'бумага', 'ruler':'линейка', 'scissors':'ножницы',}
words_hard = {'biology':'биология', 'history':'история', 'physics':'физика', 'chemistry':'химия', 'economocs':'экономика',}

#создайте словарь levels - это уровни
levels = {
    0:'нулевой',
    1:'так себе',
    2:'можно лучше ',
    3:'нормально',
    4:'хорошо',
    5:'отлично'
}
# создайте словарь answers, в нем будут хранится правильные и неправильные ответы
answers = {}

#получите у пользователя уровень сложности

print('ведите уровень:easy,medium,hard')
user_answer = input().lower()
#создайте словарь word и положите в него один из словарей (easy/medium/hard) в заваисимости от выбранной сложности


if user_answer == 'easy':
    words = words_easy
    print('выбран лёгий уровень, мы подберём 5 слов переведите их ')
elif user_answer == 'medium':
    words = words_medium
    print('выбран средний уровень, мы подберём 5 слов переведите их ')
elif user_answer == 'hard':
    words = words_hard
    print('выбран сложный уровень, мы подберём 5 слов переведите их ')
#шаг2
#Запустите цикл по пяти словам из словаря word. Понадобится ключ и значение

for word_en, word_ru in words.items():
    print('нажмите enter')
    input()
    ...
    # Для каждого слова вести ключ, длина слова, Первую букву
    letter = len(word_ru)
    first_letter = word_ru[0]
    print(f'{word_en} - {letter} букв, первая буква {first_letter}...' )

    # Получите ответ и сравните
    user_answer = input().lower()
    if user_answer == word_ru:
        print(f'верно {word_en}, это {word_ru}')
        answers[word_en] = True
    else:
        print(f'неверно {word_en}, это {word_ru}')
        answers[word_en] = False

correct_words = []
incorrect_words = []

for word_en, is_correct in answers.items():
    if is_correct:
        correct_words.append(word_en)
    else:
        incorrect_words.append(word_en)
print('правильно отмечаны слова')
print('/n'.join(correct_words))
print('неправильно отмечаны слова')
print('/n'.join(incorrect_words))

correct_count = len(correct_words)
user_level = levels[correct_count]

print()
print('Ваш ранг ')
print(f'{user_level}')