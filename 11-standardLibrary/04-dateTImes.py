from datetime import date

<<<<<<< HEAD
print(date.today())

now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1988, 6, 2)
age = now - birthday
print(age.days)
=======
print (date.today())

now = date.today()
print (now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1988, 6, 2)
age = now - birthday
print (age.days)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
