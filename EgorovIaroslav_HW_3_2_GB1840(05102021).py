# * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
dict = {'one':'один', 'two':'два','three':'три','four':'четыре', 'five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять' }
def num_translate_adv(word):
    if word[0] == word[0].upper():
        word = word.lower()
        return dict[word].capitalize()
    else:
        return dict[word]
print(num_translate_adv('one'))
print(num_translate_adv('One'))