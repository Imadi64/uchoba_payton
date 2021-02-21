translated_text = []


def split(s):
    return [char for char in s]


def translate(text):
    global translated_text
    glasnie_bykvi = ["а", "А", "у", "У", "Е", "е", "О", "о", "Э",
                     "э", "Я", "я", "И", "и", "Ю", "ю", "Ё", "Ё", ",",
                     ".", "\"\"", "?", "!", "-", "...", ":", ";", "(", ")", "\'"]
    text = split(text)
    for i in text:
        if not i in glasnie_bykvi:
            del text[i]


print(translated_text)

translate("орулбсюатврэвляртке")
