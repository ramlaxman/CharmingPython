from string import Template
t = Template('${subject}logy is my favourite subject')

for everySub in ['bio', 'zoo', 'physio', 'psycho']:
    string = t.substitute(subject = everySub)
<<<<<<< HEAD
    print(string)
=======
    print (string)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
