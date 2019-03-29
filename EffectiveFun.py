from flask import Flask
class c1:

    def yell(text):
       print(text.upper())

    def whisper(text):
        print(text.lower())

    bark = yell

    def into(no):
        print(no*2)

    def greet(func):
        func('Hi,I am Python program')

    def get_speak_func(text,volume):#..............fun can capture local state
        def whisper():
            print(text.upper())
            print(volume)
            return text.upper()
        def yell():
            print(text.lower())
            return text.lower()
        if volume > 0.5:
            return yell
        else:
            return whisper

    get_speak_func('hello,world', 0.3)()
    greet(bark)
    greet(whisper)

    del yell
    print(bark.__name__)

    list(map(bark, ['hi', 'hello', 'hey']))
    list(map(into, [i for i in range(101, 111)]))
'''
    import random
    choices = list(range(10))
    random.shuffle(choices)
    print(choices.pop())
    while choices:
        if input('Want another random number?(n/N)').lower() == 'n':
            break
        print(choices.pop())
'''













