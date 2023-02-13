from translate import Translator
translator = Translator(to_lang = "pt")



with open('testapp/test.txt', mode = 'r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)



with open('new_test.txt', mode = 'a') as my_file:
    my_file.write(translation)
