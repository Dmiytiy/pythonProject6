# создайте словари со словами в каждом словаре должно быть 5 пар слов
words_easy = {'apple':'яблоко', 'strawberry':'клубника', 'orange':'аппельсин', 'banana':',банан', 'cherry':'вишня'}
words_medium = {'pen':'ручка', 'glue':'клей', 'paper':'бумага', 'ruler':'линейка', 'scissors':'ножницы'}
words_hard = {'biology':'биология', 'history':'история', 'physics':'физика', 'chemistry':'химия', 'economocs':'экономика'}

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
print('нажмите enter')
for word_en, word_ru in words.items():
    input()
    ...
    #print('нажмите enter')
    letter = len(word_ru)
    first_letter = word_ru[0]
    print(f'{word_en} - {letter} букв, первая буква{first_letter}' )

    user_answer = input().lower()
    if user_answer == word_ru:
        print(f'неверно{word_en}, правильно{word_ru}')
        anwser[word_en] = True
    else:
        print(f'неверно{word_en}, правильно{word_ru}')
        anwser[word_en] = False
#Для каждого слова вести ключ, длина слова, Первую букву


# Получите ответ и сравните