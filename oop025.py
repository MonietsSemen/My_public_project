'''ввожу гнома и возможность улучшения артефактов,переход на следующий уровень автоматический'''
import random
from termcolor import colored
import math

class Monster:
    Result = [0, 0, 0,0] # 0- звание монстра 1- имя монстра 2- сила монстра 3- определение босса(для системы)
    monster_counter = 0 # переход на след уровень возможен только при убийстве мин. 5 монстров текущего уровня
    level_counter = 1  # счётчик уровней
    flag_boss = False
    boss_counter = 0
    def ran (self): # создание рандомного монстра
        Description = ["молодой ", "слабый ", "чахлый ", "старый ", "сильный ", "воскресший ", "древний ", "мрачный ","ужасный ", "непобедимый "]
        Name = ["троглодит", "скелет", "зомби", "призрак", "хоббит", "голем", "кентавр", "гарпия", "чёрт", "мурлок"]
        is_it_boss = random.randint (1,100)
        if (is_it_boss == 5):
            self.flag_boss = True
            self.gen_boss()
        else:
            self.flag_boss = False
            self.Result[2] = random.randint (1,9)
            self.Result[0] = Description[random.randint(self.Result[2]-1, self.Result[2])]
            self.Result[1] = Name[random.randint(0, 9)]
            return self.Result
    def gen_boss (self):
        name_boss = [" Тень пещер "," Торохтящая смерть "," Вонючий мясник "," Призрачный убийца "," Тихий ужас "," Обсидиановый кулак "," Жуткий громила "," Летящая стрела "," Ужас преисподни "," Морской чёрт"]
        name_rass = [" троглодит", " скелет", " зомби", " призрак", " хоббит", " голем", " кентавр", " гарпия", " чёрт", " мурлок"]
        boss_for_my_battle = [0,0,0,0]
        boss_for_my_battle[2] = my_hero.power * 3
        boss_for_my_battle[3]=1
        x= random.randint(0,9)
        flag=0
        while(flag==0):
            try:
                quantity_check_boss = sum((int(name_boss[i]) for i in range (0,int(len(name_boss)))))
            except ValueError:
                if (name_boss[x] != 0):
                    boss_for_my_battle[0]=name_rass[x]
                    boss_for_my_battle[1]=name_boss[x]
                    name_boss[x]=0
                    boss_monster.Result = boss_for_my_battle
                    flag = 1
                    return boss_monster.Result
                elif(quantity_check_boss == 0 ):
                    print ("Извините, но у нас закончились боссы((( сообщите администратору")

                else:
                    flag = 0
    def final_boss (self):
        final_boss.Result = [" Аватар бога Смерти "," Дорин сын Дрора ", 1200,1]

class Artefact:
        my_enter_artefact = [0, 0, 0, 0, 0]
        x=0

        def YesOrNot (self):
            lvl_factor = 0
            if(my_hero.power - monster.Result[2] >= 50):
                lvl_factor = 10000
            elif(my_hero.power - monster.Result[2] >= 10):
                lvl_factor = 100
            elif(my_hero.power - monster.Result[2] <= -30):
                lvl_factor = 5
            elif(my_hero.power - monster.Result[2] <= -100):
                lvl_factor = 1
            else:
                lvl_factor = 10
            x = random.randint(0, lvl_factor)  # определяет выпал-ли артефакт из монстра(вероятность 1 к 10)
            if (x==5):
                y = random.randint(0, 10)
                if (y == 5): #Запуск композитов
                    return self.composits()
                else:
                    return self.ran()

        def my_part_of_the_body(self):
            my_enter_artefact = input("Из убитого вами чудовища вам попался " + str(my_rez_artefact.my_enter_artefact[0]) + str(my_rez_artefact.my_enter_artefact[1]) + " c " + str(my_rez_artefact.my_enter_artefact[2]) + " единицами силы. Подобрать? (да/нет)")  # решение об одевании артефакта
            if (my_enter_artefact == "да"):  # выбор части тела
                if (my_rez_artefact.my_enter_artefact[3] == 1):
                    my_head_artefact.my_enter_artefact = my_rez_artefact.my_enter_artefact
                elif (my_rez_artefact.my_enter_artefact[3] == 2):
                    my_body_artefact.my_enter_artefact = my_rez_artefact.my_enter_artefact
                elif (my_rez_artefact.my_enter_artefact[3] == 3):
                    my_foot_artefact.my_enter_artefact = my_rez_artefact.my_enter_artefact
                elif (my_rez_artefact.my_enter_artefact[3] == 4):
                    my_weapon_artefact.my_enter_artefact = my_rez_artefact.my_enter_artefact
            elif (my_enter_artefact == "нет"):
                my_rez_artefact.my_enter_artefact = [0, 0, 0, 0, 0]
            else:
                print("Вы упустили свой шанс")

        def ran (self):
            Result = [0, 0, 0, 0,0]  # где 0 -описание качества артефакта, 1 - тип артефакта, 2 - сила артефакта,3 -  тип артефакта( для системы), 4 - доп системная инфа для сетовых наборов
            self.x = random.randint(0, 3)  # определяет тип артефакта
            Quality = ["Поломанный ","Гнилой ","Истлевший ","Ржавый ","Некачественный ","Треснутый ","Выщербленный "," Надколотый ","Старый ","Поношеный ","Низкопробный ","Хороший ","Добротный ","Новый ","Качественный ","Отличный ","Необычный ","Элитный ","Героический "]
            Had = ["Шлем ", "Каска ", "Забрало ", "Шишак ", "Маска ", "Подшлемник ", "Шляпа", "Колпак ", "Ведро ","Шапка "]
            Body = ["Кольчуга ", "Кирасса ", " Жилетка", "Куртка ", "Накидка ", "Броня ", "Рубашка ", "Панцирь ","Хитон ", "Балахон"]
            Foot = ["Ботинки ", "Поножи ", "Обувь ", "Сандали ", "Башмаки", "Чуни ", "Буцефалы ", "Туфли", "Берцы"," Тапки "]
            Weapon = ["Меч ", "Кинжал ", "Топор", "Шпага ", "Посох ", "Нож ", "Двуручник ", "Арбалет ", "Палаш ", "Лук"]
            Result[2] = random.randint(0, 20)   # рандомная сила артефакта
            if(Result[2]/Monster.level_counter == 20 ): # определяю качество артефакта
                Result[0] = Quality[-1]
            elif (Result[2]<= 19 and Result[2]>= 15  ):
                Result[0] = Quality[random.randint(16, 18)]
            elif (Result[2]<= 14 and Result[2]>= 10  ):
                Result[0] = Quality[random.randint(12, 15)]
            elif (Result[2]<= 9 and Result[2]>= 5  ):
                Result[0] = Quality[random.randint(8, 14)]
            elif (Result[2]<= 4 and Result[2]>= 0  ):
                Result[0] = Quality[random.randint(0, 7)]
            if (self.x==0):
                Result[1] = Had[random.randint(0, 9)] # определяю тип артефакта
                Result[3] = 1
            elif(self.x==1):
                Result[1] = Body[random.randint(0, 9)]
                Result[3] = 2
            elif (self.x == 2):
                Result[1] = Foot[random.randint(0, 9)]
                Result[3] = 3
            elif(self.x == 3):
                Result[1] = Weapon[random.randint(0, 9)]
                Result[3] = 4
            my_rez_artefact.my_enter_artefact = Result
            self.my_part_of_the_body()

        def composits (self):
            Result = [0, 0, 0, 0,0]  # где 0 -описание качества артефакта, 1 - тип артефакта, 2 - сила артефакта,3 -  тип артефакта( для системы), 4 - доп системная инфа для сетовых наборов
            y = random.randint(0, 2) # определяем семейство композита
            x = random.randint(0, 3)  # определяет тип артефакта
            name_my_composit = [" Небесной защиты ", " Дьявольского везения ", " Рокового выбора "]
            Had_composit =[" Шлем "," Маска "," Забрало "]
            Body_composit =[" Панцырь "," Мантия "," Кольчуга "]
            Foot_composit =[" Железные ботинки "," Кожаные ботинки "," Кольчужные ботинки "]
            Weapon_composit =[" Щит "," Кинжал "," Топор "]
            Power_composit =[35,40,32]
            Result[1] = name_my_composit[y]
            Result[2] = Power_composit[y]
            Result[4] = 1
            if (x == 0):
                Result[0] = Had_composit[y]  # определяю тип артефакта
                Result[3] = 1
            elif (x == 1):
                Result[0] = Body_composit[y]
                Result[3] = 2
            elif (x == 2):
                Result[0] = Foot_composit[y]
                Result[3] = 3
            elif (x == 3):
                Result[0] = Weapon_composit[y]
                Result[3] = 4
            my_rez_artefact.my_enter_artefact = Result
            self.my_part_of_the_body()

class Hero :
    money = 0
    name = 0
    power = 5
    all_power = 0
    def my_power (self):
        x = my_head_artefact.my_enter_artefact[4] + my_body_artefact.my_enter_artefact[4] +my_foot_artefact.my_enter_artefact[4] + my_weapon_artefact.my_enter_artefact[4]
        if (x != 0):
            self.all_power = self.power+(my_head_artefact.my_enter_artefact[2]+my_body_artefact.my_enter_artefact[2]+my_foot_artefact.my_enter_artefact[2]+my_weapon_artefact.my_enter_artefact[2])*x
            return self.all_power
        else:
            self.all_power = self.power + my_head_artefact.my_enter_artefact[2] + my_body_artefact.my_enter_artefact[2] +my_foot_artefact.my_enter_artefact[2] + my_weapon_artefact.my_enter_artefact[2]
            return self.all_power

monster = Monster () # в игре сейчас один герой
boss_monster = Monster ()
final_boss = Monster ()
my_hero = Hero ()
my_rez_artefact = Artefact ()
my_head_artefact = Artefact ()
my_body_artefact = Artefact ()
my_foot_artefact = Artefact ()
my_weapon_artefact = Artefact ()

def GlobalProc (): # общий цикл игры
   attaking = 0
   while (attaking!="лагерь" and my_hero.power != 0):
        monster.ran() # создаю монстра
        my_hero.my_power() # пересчитываю показатели силы
        if (Monster.monster_counter == 5):
            Monster.monster_counter = 0
            Monster.level_counter += 1
            print(colored("Вы перешли на "+ str(Monster.level_counter) + " уровень!", 'green'))
        if (boss_monster.flag_boss==True):
            attaking = input(colored("Вы видите лучшего воина вида " + boss_monster.Result[0] + " это " + monster.Result[1] + "  атаковать?\n", 'white'))
        else:
            attaking = input (colored("Вы видите " + monster.Result[0] + " " + monster.Result[1] + "  атаковать?\n", 'red'))
        if (attaking == "да"):
           if (my_hero.all_power > monster.Result[2]*Monster.level_counter):
               my_hero.power += 1
               print (colored("Вы смогли убить монстра - "+ monster.Result[0] + " " + monster.Result[1] +" с силой в " + str(monster.Result[2]*Monster.level_counter) + " единиц!",'green') )
               Monster.monster_counter += 1
               if (boss_monster.flag_boss==True):
                   my_hero.money += 10
                   print ("Проходя мимо поверженного врага, ты замечаешь тусклые блики на земле, нагнувшись видишь 10 амулетов из тёмного металла с крупным рубином по центру. Не долго думая подобрал их. ")
               my_rez_artefact.YesOrNot()


           elif (my_hero.all_power <= monster.Result[2]*Monster.level_counter):
              print (colored("Вы были побеждены - " + monster.Result[0] + " " + monster.Result[1] +" с силой в " + str(monster.Result[2]*Monster.level_counter) + " единиц.", 'red') )
              my_hero.power -= 1
              if  ( Hero.power != 0):
                  print ("Сильно раненый вы вернулись в лагерь")
                  attaking = "лагерь"
        else :
            print (" Подумав вы решили лишний раз не нарываться на неизвестного монстра. ")

def menu () :
    lager =0
    while (lager != "в"):
        print("\nВы находитесь в своём временном лагере.\n Здесь вы можете:\n - просмотреть свой инвентарь и глянуть свои характеристики (Введите `и`)\n - перейти на следующий уровень(введите `ап`)\n - для выхода из лагеря введитете `в`. \n ")
        print(" - захотел зайти на чашку чая к Гному? введи `гном`")
        lager = input (" - Если-же тебе приелся этот Мир, тогда введи ( `пока` ), но учти любой твой выход из Мира означает твою окончательную смерть в нём.\n")
        if (lager == "и"):
            my_hero.my_power()
            print ("Жизненная сила : " + str(my_hero.power) + " ед. "+ "/ Общий показатель силы : " + str(my_hero.all_power) + " ед.    " "Ты убил " + str(boss_monster.boss_counter) + " из 10 боссов \n")
            print ("Надетые артефакты:\n"+ " Голова - " + str (my_head_artefact.my_enter_artefact[0]) +" "+ str (my_head_artefact.my_enter_artefact[1]) +" "+ str (my_head_artefact.my_enter_artefact[2]) )
            print(" Тело - " + str(my_body_artefact.my_enter_artefact[0]) + " " + str(my_body_artefact.my_enter_artefact[1]) + " " + str(my_body_artefact.my_enter_artefact[2]))
            print(" Руки - " + str(my_weapon_artefact.my_enter_artefact[0]) + " " + str(my_weapon_artefact.my_enter_artefact[1]) + " " + str(my_weapon_artefact.my_enter_artefact[2]))
            print(" Ноги - " + str(my_foot_artefact.my_enter_artefact[0]) + " " + str(my_foot_artefact.my_enter_artefact[1]) + " " + str(my_foot_artefact.my_enter_artefact[2]))
        elif (lager == "ап"):
            if ((Monster.monster_counter/Monster.level_counter) >= 5):
                Monster.level_counter += 1
                print (" Поздравляю, вы перешли на " + str(Monster.level_counter) +" уровень!")
            else:
                print (str(my_hero.name)+", на твоём счету недостаточно черепов местных обитателей.")
        elif (lager == "пока"):
            print ("Удачи тебе "+ str(my_hero.name)+ "...")
            my_hero.power = 0
            lager = "в"
        elif (lager == "гном"):
            if(monster.level_counter != 100):
                print("Привет " + str(my_hero.name) + "! Как успехи в новом Мире? ")
                dialog_with_gnom = input(" По какому вопросу зашел?\nВарианты комманд")
                if(dialog_with_gnom == "чаю попить" or dialog_with_gnom == "чай попить" or dialog_with_gnom == "чай поганять" or dialog_with_gnom == "попить чая" or dialog_with_gnom == "выпить чаю" ):
                    print(" Ну тогда держи и слушай историю. - он протянул вам чашку, полную гарячего и ароматного чая....(истории доделать) ")
                elif(dialog_with_gnom == "правила"):
                    print("\nВсе вы, герои, изначально появляетесь в нашем мире одинаково сильными - с 5-ю условными единицами жизненной энергии. И только от тебя зависит каким ты станешь в дальнейшем. Знай что за каждого убитого монстра Мир даст тебе одну единицу жизненной энергии, а за поражение отнимет столько-же. Будь внимателен и следи за показателями жизненной энергии. ")
                    print("\nТут тебе придётся сражаться, сражаться с монстрами и чудовищами населяющими большую часть Мира. Видов монстров множество, но для себя запомни : в момент когда ты посмотришь на монстра, Мир сообщит тебе кто это, но умолчит о его силе, дав лишь подсказку охарактеризовав чудовище по своему усмотрению...  ")
                    print("\nЕсли ты хочешь оставить свой след в истории тебе придётся достигнуть вершины - сотого уровня, а иначе - ты канешь в лету.")
                    print("\nНа каждом уровне тебе придётся сразиться с не менее как 5-ю противниками, и лишь доказав своё превосходство, этот мир дарует тебе новую ступень, новые возможности, НОВЫЙ УРОВЕНЬ!\n")
                    print("\nКогда-же ты победишь в бою, будь внимателен - из обитателей этих мест, временами, выпадают весьма интересные вещички. Но учти, себе ты можешь оставить, только, один предмет каждого вида, так-что делай выбор обдумано! ")
                elif(dialog_with_gnom == "улучшение"):
                    dialog_with_gnom = input("Да я могу улучшить твоё снаряжение... Но есть-ли у тебя, чем заплатить за эту услугу? Меня интересуют тёмные амулеты, ты... уже встречал их? ")
                    if (dialog_with_gnom == "да" and my_hero.money != 0):
                        dialog_with_gnom = input("Отлично! Я вижу у тебя " +str(my_hero.money) + " тёмных амулетов. Я готов за один такой амулет улучшить практически любой твой предмет, скажем... на 10 %. Все... кроме сетовых, их я улучшить не могу.\nЧто ты хочешь улучшить? (Введи часть тела на которую одет интересующий тебя артефакт)")
                        if (dialog_with_gnom == "голова"):
                            if(my_head_artefact.my_enter_artefact[2] != 0 and my_head_artefact.my_enter_artefact[3] != 0):
                                my_head_artefact.my_enter_artefact[2] = int(my_head_artefact.my_enter_artefact[2]*1.1)
                            else:
                                print(" Извини, ну у тебя нет нужного артефакта(")
                        elif (dialog_with_gnom == "тело"):
                            if (my_body_artefact.my_enter_artefact[2] != 0 and my_body_artefact.my_enter_artefact[3] != 0):
                                my_body_artefact.my_enter_artefact[2] = int(my_body_artefact.my_enter_artefact[2] * 1.1)
                            else:
                                print(" Извини, ну у тебя нет нужного артефакта(")
                        elif (dialog_with_gnom == "ноги"):
                            if (my_foot_artefact.my_enter_artefact[2] != 0 and my_foot_artefact.my_enter_artefact[3] != 0):
                                my_foot_artefact.my_enter_artefact[2] = int(my_foot_artefact.my_enter_artefact[2] * 1.1)
                            else:
                                print(" Извини, ну у тебя нет нужного артефакта(")
                        elif (dialog_with_gnom == "руки"):
                            if (my_weapon_artefact.my_enter_artefact[2] != 0 and my_weapon_artefact.my_enter_artefact[3] != 0):
                                my_weapon_artefact.my_enter_artefact[2] = int(my_weapon_artefact.my_enter_artefact[2] * 1.1)
                            else:
                                print(" Извини, ну у тебя нет нужного артефакта(")
                    elif(dialog_with_gnom == "да" and my_hero.money == 0):
                        print (colored("Эээ нет старого Дорина так просто не обманешь. Приходи когда твои слова будут отвечать действительности.", 'red'))
                    else:
                        print("Нуу, нет так, нет.")
print (" - Ну здравствуй путник. Знаю, ты ожидал увидеть трактат нашего мира и вступительные слова. Но вместо этого тебя встречаю я. \n Перед вами у костра сидел добродушный седой гном и потягивал ароматный чай. \n - Я просто люблю поболтать. Но не беспокойся, я не отниму у тебя много времени. ")
you_hero_dialog = input ("Ну так что, Пообщаемся? Выбор(да/нет)\n")
if (you_hero_dialog == "нет"):
    print ("Удачи тебе странник, быть может свидимся...")
elif(you_hero_dialog == "да"):
    print (" - Ну здорово, значит старику будет с кем поболтать. Для начала я хотел бы представиться.\n Я Дорин сын Дрора, смотрящий за этим миром, если что-то тебя волнует ты всегда можешь обратиться ко мне во пременном лагере.")
    my_hero.name = input (" А ты?... Как я к тебе могу обращаться?\n")
    if (my_hero.name == "Семми"): #панель админа
        my_hero.power = 100
        exit = 0
        while (exit==0):
            admin_command = input ("Введи команду...")
            if (admin_command == "арт"):
                my_rez_artefact.ran()
            elif(admin_command == "ко"):
                my_rez_artefact.composits()
            elif(admin_command== "бос"):
                boss_monster.gen_boss()
            elif(admin_command == "глобалка"):
                GlobalProc()
            elif(admin_command == "меню"):
                menu()
            elif (admin_command=="пока"):
                exit = 1

    else:
        you_hero_dialog = input ("- Ну что же," + str(my_hero.name)+" ты новый герой нашего мира. Хочу немного рассказать о нём:\nОн, совсем ещё молод и возможно отличается от вашего. Но и в нём есть некоторые правила...\nНаш мир - это история. Поэтому ты не можешь поменять её ход, если однажды ошибся, однако, наш создатель знает что все могут ошибаться и потому он даёт тебе возможность писать свою историю, покуда, у тебя хватит сил...\nБудем называть это - Жизненной силой, она является и твоей силой для противостоянию злу, и запасом твоей жизненной энергии. " )
        you_hero_dialog = input ("\nВсе вы, герои, изначально появляетесь в нашем мире одинаково сильными - с 5-ю условными единицами жизненной энергии. И только от тебя зависит каким ты станешь в дальнейшем. Знай что за каждого убитого монстра Мир даст тебе одну единицу жизненной энергии, а за поражение отнимет столько-же. Будь внимателен и следи за показателями жизненной энергии. ")
        you_hero_dialog = input ("\nТут тебе придётся сражаться, сражаться с монстрами и чудовищами населяющими большую часть Мира. Видов монстров множество, но для себя запомни : в момент когда ты посмотришь на монстра, Мир сообщит тебе кто это, но умолчит о его силе, дав лишь подсказку охарактеризовав чудовище по своему усмотрению...  ")
        you_hero_dialog = input ("\nЕсли ты хочешь оставить свой след в истории тебе придётся достигнуть вершины - сотого уровня, а иначе - ты канешь в лету.")
        you_hero_dialog = input ("\nНа каждом уровне тебе придётся сразиться с не менее как 5-ю противниками, и лишь доказав своё превосходство, этот мир дарует тебе новую ступень, новые возможности, НОВЫЙ УРОВЕНЬ!\n")
        you_hero_dialog = input ("\nКогда-же ты победишь в бою, будь внимателен - из обитателей этих мест, временами, выпадают весьма интересные вещички. Но учти, себе ты можешь оставить, только, один предмет каждого вида, так-что делай выбор обдумано! ")
        you_hero_dialog = input ("\nБерегись!\n")
    while (my_hero.power > 0):
        GlobalProc ()
        if  ( my_hero.power != 0):
            menu ()
print ("Увы, но вы погибли окончательной смертью, вас будут помнить...")
