
"I love Python"

hoku = "I listen, owl voices everywhere\
       all creatures singing Python-on-on\
        yellow snake moves through hole, over into my net !"

Python = list(filter(lambda x: x in list("I love Python!"), list(zip(*list(filter(lambda a: a != '', hoku.split(' ')))))[0]))
Python.insert(1,' ')
Python.insert(6,' ')

print("".join(Python))

print(list(zip(*list(filter(lambda a: a != '', hoku.split(' ')))))[0])