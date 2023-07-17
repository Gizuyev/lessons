"""
#Task 1
data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
print(data.replace('е','3'))

#Task 2
a = 'паралелепипед'
b = input()
print(a.split(b))

#Task 3
text = 'Я Торфин'
text2 = 'сын Торса'
print(text.lower(), text2.upper())

#Task4
c = '123'
print(c.isdigit())

#Task 5
d = 'Свобода - это фантом, там нету тепла для меня без тебя'
print(len(d))

#Task 6
name, age, cinema = input('Ваше имя'), input('Ваш возраст'), input('Фильм')
print(cinema,'это очень захватывающий фильм')

#Task 7
t1 = 'Goggle Collab all the time'
print(t1.replace('a',' |'))

#Task 8
t2 = "Мы больше не летаем и это не наши сны, И тот остров необитаем и в нем нет весны. И мы не производим больше искры на свет, И как бы есть, но как будто бы нас нет."
print(t2.title())

#Task 9
x, y = input(), input()
z = y +' '+ x
z = len(z.split()) * 7 ** 5
print(z)
a = len(str(z))
print(z%(10**(a-1))//(10**(a-2)))

#Task 10
phone = '8 700 736 9090'
phone = phone.replace('8','+7').replace(' ', '')
print(phone)

#Task 11
wrd, wrd1 = input(), input()
wrd = wrd.startswith()
wrd1 = wrd1.startswith()
"""
#Task 12
user_age = input('How old are you? ')
my_age = input("Сколько вам лет? ")
print(int(my_age) * 2 - 4)

