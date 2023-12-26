# if
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# alfel printam impar
nr = 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

# if, else if, else
# cum ne saluta robotelul in f de ora?

# luam date de la tastatura
# ne asiguram ca sunt transformate din str in int
ora = int(input('Introdu ora'))
if ora < 0:
    print('ora negativa')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 21:
    print('buna seara')
elif ora <= 24:
    print('noapte buna')
else:
    print('ora mai mare de 24')
# CTRL + /



