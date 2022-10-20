class JunDev:
    def __init__(self, name, age, experience, skills, program_language):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills
        self.program_language = program_language
    def __str__(self):
        return f'Имя-{self.name}\n' \
               f'Возраст-{self.age}\n' \
               f'Опыт-{self.experience}\n'\
               f'Умения-{self.skills}\n'\
               f'Язык программирования-{self.program_language}'
    def IT_sphere (self, sphere):
        return f'Область программирования-{sphere}'
    def Additional_Program_Language(self, language):
        if language == 'Python' or language == 'PHP' or language == 'HTML' or language == 'CSS':
            return f'Он/Она молодец! :)'
        elif language == 'QBasic':
            return f'Он/Она не молодец :('
        else:
            return f'Он/Она молодец и не молодец :!'
Programmer_1 = JunDev(name = 'Рустам', age = 17, experience = 'Нет' , skills = 'Базовые', program_language = 'C++')
print(Programmer_1)
print(Programmer_1.IT_sphere(str(input('В какой области программирования вы работаете? '))))
print(Programmer_1.Additional_Program_Language(str(input('Какой у него/нее дополнительный язык программирования? '))))
print('-'*50)
class MidDev(JunDev):
    def __init__(self, name, age, experience, skills, program_language, height , weight , hobby):
        super().__init__(name, age, experience, skills, program_language)
        self.height = height
        self.weight  = weight
        self.hobby = hobby
    def __str__(self):
        return super(MidDev, self).__str__()+f'\nРост-{self.height}\n' \
                                             f'Вес-{self.weight}\n' \
                                             f'Хобби-{self.hobby}'
    def Military (self, army):
        return f'Армия-{army}'
    def Additional_Program_Language(self, language):
        if language == 'Python' or language == 'PHP' or language == 'HTML' or language == 'CSS':
            return f'Он/Она молодец! :)'
        elif language == 'QBasic':
            return f'Он/Она не молодец :('
        else:
            return f'Он/Она молодец и не молодец :!'
Programmer_2 = MidDev (name = 'Адис', age = 18, experience = 'Да' , skills = 'На высоком уровне\n'
                       , program_language = 'C#',height = 172, weight = 50, hobby = 'Видеоигры')
print(Programmer_2)
print(Programmer_2.Military(str(input('Он был в армии ?'))))
print(Programmer_2.Additional_Program_Language(str(input('Какой у него/нее дополнительный язык программирования? '))))
print('-'*50)
class SenDev(MidDev):
    def __init__(self, name, age, experience, skills, program_language, height , weight , hobby , girlfriend , salary , freetime):
        super().__init__(name, age, experience, skills, program_language , height , weight , hobby)
        self.girlfriend = girlfriend
        self.salary  = salary
        self.freetime = freetime
    def __str__(self):
        return super(SenDev, self).__str__()+f'\nДевушка-{self.girlfriend}\n' \
                                             f'Зарплата-{self.salary}\n' \
                                             f'Свободное время-{self.freetime}'
    def Favorite_work (self, work):
        return f'Работа-{work}'

    def Additional_Program_Language(self, language):
        if language == 'Python' or language == 'PHP' or language == 'HTML' or language == 'CSS':
            return f'Он/Она молодец! :)'
        elif language == 'QBasic':
            return f'Он/Она не молодец :('
        else:
            return f'Он/Она молодец и не молодец :!'
Programmer_3 = SenDev (name = 'Улукбек', age = 17, experience = 'Огромный' , skills = 'На очень высоком уровне\n'
                       , program_language = 'python',height = 180, weight = 72, hobby = 'Рисование\n'
                       , girlfriend = 'Нет' , salary = '120000$/в год' , freetime = 'Очень мало , практически нет' )
print(Programmer_3)
print(Programmer_3.Favorite_work(str(input('Ему/ей нравится работа? '))))
print(Programmer_3.Additional_Program_Language(str(input('Какой у него/нее дополнительный язык программирования? '))))
print('-'*50)