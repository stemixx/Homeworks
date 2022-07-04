def first_word(text: str) -> str:
    first_word = list()
    text_list = list(text)
    for i in text_list:
        if i != ' ':
            first_word.append(i)
        else:
            break
    return (''.join(first_word))


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"



