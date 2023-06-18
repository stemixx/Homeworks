# Написать функцию, на вход которой подаётся строка текста, а выводом должно быть первое слово строки

def first_word(text: str) -> str:
    first_word = list()
    text_list = list(text)
    for i in text_list:
        if i != ' ':
            first_word.append(i)
        else:
            break
    return (''.join(first_word))

def first_word2(text: str) -> str:
    return text.split(' ')[0]

if __name__ == "__main__":
    print(f'Example first_word("Hello world"):')
    print(first_word("Hello world"))
    print(f'Example first_word2("Hello world"):')
    print(first_word2("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"

    assert first_word2("Hello world") == "Hello"
    assert first_word2("a word") == "a"
    assert first_word2("hi") == "hi"


