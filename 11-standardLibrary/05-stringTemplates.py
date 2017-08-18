from string import Template
t = Template('${subject}logy is my favourite subject')

for everySub in ['bio', 'zoo', 'physio', 'psycho']:
    string = t.substitute(subject = everySub)
    print string