print('Hello, Python!')

print('Привет, Python!\n'
      'Hello, Python!\n'
      'Bonjour Python!\n'
      'Hej, Python!\n'
      'Hola, Python!')

print('Привет')
print('Python')

print('(\\___/)')
print('(=\'.\'=)')
print('(\")_(\")')

print('Привет, Python!\n''Hello, Python!\n''Bonjour Python!\n''Hej, Python!\n''Hola, Python!')

print('Как Вас зовут?')
s = input()
print('Здравствуйте, ' + s)

print('Как Вас зовут?')
s = input()
print('Здравствуйте, ' + s)
print('Что Вам нравится? ')
k = input()
print('Отлично! ' + k + '  - хорошее увлечение.')


print('Login: ')
login = input()
print('Password: ')
password = input()
print('New password: ')
np = input()
print('User {0} has changed the password to {1}'.format(login, np))

pl = ['Ace Of Base - All That She Wants',
      'No Doubt - Dont Speak',
      'Bad Boys Blue - You\'re A Woman',
      'E-Type - Angels Crying',
      'Haddaway - What Is Love']

for song in reversed(pl):
      print(song, end='\n')

nr = input()
nrus = input()
neng = input()
tdrus = input()
tdeng = input()
print('Заканчивается посадка на рейс {0} {1} до {2} '.format(nr, nrus, tdrus))
print('This is the final boarding call for {0} flight {1} to {2}'.format(neng, nr, tdeng))