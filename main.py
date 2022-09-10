words = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


# def combinations(a):
#     combinations = []
#     for letter in words[a[0]]:
#         for second_letter in words[a[1]]:
#             combinations.append(letter+second_letter)
#     print(combinations)


# v = 0
#
# def combinations(a):
#     global v
#     univer_combinations = []
#     combinati = []
#     number_len = len(a)
#     for _ in range(number_len):
#         for letter in words[a[0]]:
#             v += 1
#             combinations(a)
#             combinati.append(letter)
#     print(len(combinati))


# v = 1
# combination = []
#
#
# def combinations(a):
#     global v
#     global combination
#     for letter in words[a[0]]:
#         for second_letter in words[a[v]]:
#             combination.append(letter+second_letter)
#     if v == len(a)-1:
#         print(combination)
#         return
#     v += 1
#     combinations(a)
#
#
# combinations('23')

# def combination(date):
#     def make_combination(numbers):
#         for number in numbers:
#             for i in words[number]:
#                 print('')
#
#
# combination('23')


# def combat(numbers):
#     v = 1
#     combination = []
#     def combinations(a):
#         # global v
#         # global combination
#         for letter in words[a[0]]:
#             for second_letter in words[a[v]]:
#                 combination.append(letter+second_letter)
#         if v == len(a)-1:
#             print(combination)
#             return
#         v += 1
#         combinations(a)


# combinations('23')

# def ssss():
#     combinations = []
#     for i, l in zip(['s', 'd', 'f'], ['1', '2', '3']):
#         combinations.append(i + l)
#     print(combinations)
#
#
# ssss()

# НЕ СТАЛ УДАЛЯТЬ ВАРИАНТЫ СВЕРХУ ДЛЯ ОТСЛЕЖИВАНИЕ МОЕЙ ЛОГИКИ

def combinations(numbers):
    def make_combinations(numbers, word, res):
        if numbers == '':
            res.append(word)
            return
        for letter in words[numbers[0]]:
            word += letter
            make_combinations(numbers[1:], word, res)
            word = word[:-1]
    res = []
    make_combinations(numbers, '', res)
    print(res)


combinations('23')