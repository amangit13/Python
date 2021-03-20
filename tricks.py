#conditional asignment
cond = True
x = 1 if cond else 0
print (x)

# formating
x = 1_000_000
print (f"total {x:,}")

# generators
names = ['hello1','hello2', 'hello3']
for i, name in enumerate(names):
    print (name, i)

cities = ['seattle', 'chicago', 'madison']

for name,city in zip(names, cities):
    print(f'name {name} from {city}')

# unpacking
a,b = (1,2)
print (a, b)
a,b,*c = (1,2,3,4,5,6,7)
print(a,b,c)

#class dynamic attributes
class Person():
    pass

p = Person()
p.firstname = "hello"

print (p.firstname)
del(p)
p = Person()
setattr(p, "firstname", "name value")
print(p.firstname)

# dictionary & using a generator
dic = {'IL':'Chicago','WA':'Seattle'}
for state, city in dic.items():
    print (state, city)


# multi line statemens & dictionary, itteration
dic = {'city1':'Seattle',
       'city2':'Chicago',
       'city3':'Madison',
       'city4':'Milwaukee'}

print (dic['city1'])
for key in dic:
    print (key, dic.get(key))
