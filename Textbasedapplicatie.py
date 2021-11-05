import random
import time
health = 4 
freepass = 0
def start():
    print(" ____  _____  ____  ____  _____ \n/ ___\/__ __\/  _ \/  __\/__ __\\\n|    \  / \  | / \||  \/|  / \  \n\___ |  | |  | |-|||    /  | |  \n\____/  \_/  \_/ \|\_/\_\  \_/  \n")
    time.sleep(1)
    print("Welkom bij mijn text based applicatie! \nIn dit programmatje probeer je te overleven in het mist van alle onveiligheid.\nKan jij overleven en het goeden leven vinden?\n")
    time.sleep(1)
    print("In dit verhaal is één mystryitem te vinden, hierdoor heb je toegang tot een veiliger pad.\nOok heb je 4 health en door de keuzes die je maakt gaat er health af of health bij!\n")
    print("Oke start!\n")
    time.sleep(1.5)
    vraag1()
def vraag1(): 
    print("Er is conflict gaande in je stad, de mensen gaan vechten met het leger en het land staat op het punt van een burgeroorlog.\nWil je MEEVECHTEN of VLUCHTEN of proberen te WERKEN?")
    v1 = input("==>")
    vraag1_0=v1.upper()
    if vraag1_0 == 'MEEVECHTEN':
        print("Je doet mee met het gevecht!\n")
        vraag15()
    elif vraag1_0 == 'VLUCHTEN':
        print("Je bent gevlucht!\n")
        vraag2()
    elif vraag1_0 == "WERKEN":
        print("Je gaat proberen te werken\n")
        vraag8()
    else:
        print("Dit is geen geldig antwoord!")
        vraag1()
def vraag2():
    print("Wil je vluchten met je GEZIN of VRIENDEN?")
    v2 = input("==>")
    vraag2_0=v2.upper()
    if vraag2_0 == 'GEZIN':
        print("Je gaat met je gezin, dit word een moeilijke opgave want ze zijn niet in optimale conditie.\n")
        vraag3()
    elif vraag2_0 == 'VRIENDEN':
        print("Je gaat met je vrienden alleen die zetten je op het verkeerde pad! -1 Health.\n")
        listofGlobals = globals()
        listofGlobals['health'] -=1
        print("Je hebt",health,"health")
        vraag15()
    else: 
        print("Dit is geen geldig antwoord!")
        vraag2()
def vraag3():
    print("Je gezin heeft honger dus je moet snel wat verzinnen, ga je eten STELEN of wacht je op HULP? ")
    v3 = input("==>")
    vraag3_0=v3.upper()
    if vraag3_0 == 'STELEN':
        print("Je hebt eten gestolen en daardoor verhonger je niet.\n")
        vraag7()
    elif vraag3_0 == 'HULP':
        print("Je hebt gewacht op hulp maar die komt er nooit je gezin gaat bijna dood aan de honger. -2 health.\n")
        listofGlobals = globals()
        listofGlobals['health'] -=2
        print("Je hebt",health,"health")
        vraag4()
    else: 
        print("Dit is geen geldig antwoord!")
        vraag3()
def vraag4():
    print("Je hebt gegeten, ga je meteen DOOR of ga je nog RUSTEN? ")
    v4 = input("==>")
    vraag4_0=v4.upper()
    if vraag4_0 == 'DOOR':
        print("Je gaat meeten verder lopen.\nHierdoor ben je wel sneller alleen verlies je wel wat health.\n")
        listofGlobals = globals()
        listofGlobals['health'] -=1
        print("Je hebt",health,"health")
        vraag6()
    elif vraag4_0 == 'RUSTEN': 
        print("Je hebt er voor gekozen om te rusten en daardoor krijg je extra health!\n")
        listofGlobals = globals()
        listofGlobals['health'] +=1
        print("Je hebt",health,"health")
        vraag5()
    else: 
        print("Dit is geen geldig antwoord!")
        vraag4()  
def vraag5():
    print("Je komt aan bij een haven ergens in Turkije, je moet gaan kiezen: LOPEND of per BOOT naar Europa?\n")
    v5 = input("==>")
    vraag5_0=v5.upper()
    if vraag5_0 == 'BOOT':
        print("Je bent per boot gegaan en zit op een lange reis naar Europa.\n")
    elif vraag5_0 == 'LOPEND':
        print("Je hebt er voor gekozen om toch lopend te gaan. -1 health\n")
        listofGlobals = globals()
        listofGlobals['health'] -=1
        print("Je hebt",health,"health")
        vraag6()
    else:
        print("Dit is geen geldig antwoord!")
        vraag5()
def vraag6():
    print("Je bent aan het lopen wil je de gevaarlijke KORTE weg of de langzame LANGE weg? ")
    v6 = input("==>")
    vraag6_0=v6.upper()
    if vraag6_0 == 'KORTE':
        print("Je hebt voor de korte weg gekozen.\n")
        vraag13()
    elif vraag6_0 == 'LANGE':
        print("Je hebt voor de LANGE weg gekozen\n")
        vraag12()
    else:
        print("Dit is geen geldig antwoord!")
        vraag6()
def vraag7():
    print("je hebt toch eten nodig hoe wil je dit verhelpen.\nWil je een kleine JOB doen, BEDELEN of VERLAAT je je gezin?")
    v7 = input("==>")
    vraag7_0=v7.upper()
    if vraag7_0 == 'JOB':
        print("Je gaat opzoek naar een job!\n")
        vraag8()
    elif vraag7_0 == 'BEDELEN':
        print("Je gaat opzoek naar een goede plek om te bedelen.\n ")
        vraag9()
    elif vraag7_0 == 'VERLAAT':
        print("Je verlaat je familie omdat je niet meer voor ze kan zorgen!\n")
        vraag15()
    else:
        print("Dit is geen geldig antwoord!")
        vraag7()
def vraag8():
    print("Je hebt werk gevonden maar wil je dit LEGAAL doen of ZWART doen?")
    v8 = input("==>")
    vraag8_0=v8.upper()
    if vraag8_0 == "legaal":
        print("Je soliciteerd bij het legalen bedrijf.\nOke je bent aangenomen bij een winkel +1 health.\n")
        vraag22()
    elif vraag8_0 == 'ZWART':
        print("Je wilt gaan zwart werken want daar verdien je meer.\n")
        vraag10()
    else:
        print("Dit is geen geldig antwoord!")
        vraag8()
def vraag9():
    print("Waar ga je bedelen? OPSTRAAT of voor een WINKEL?  ")
    v9 = input("==>")
    vraag9_0=v9.upper()
    if vraag9_0 == 'OPSTRAAT':
        print("Je wilt opstraat bedelen alleen haalt de politie je daar weg dus moet je met je gezin snel naar de haven in Turkije.\n")
        vraag5()
    elif vraag9_0 == 'WINKEL':
        print("Je gaat voor een winkel bedelen alleen de eigenaar heeft medeleiden met je, dus neemt hij je aan.\n")
        vraag22()
    else:
        print("Dit is geen geldig antwoord!")
        vraag9()
def vraag10():
    print("Er word gevraagd of je bij een rebbel groep wilt aansluiten ga je WEL mee of NIET mee? ")
    v10 = input("==>")
    vraag10_0=v10.upper()
    if vraag10_0 == 'WEL':
        print("Je gaat wel meedoen met de rebbellen groep!\n")
        vraag17()
    elif vraag10_0 == 'NIET':
        print("Je gaat niet meedoen met je rebbelen groep en je komt weer terug bij je gezin. Hierbij verlies je wel 2 health!\n")
        listofGlobals = globals()
        listofGlobals['health'] -=2
        print("Je hebt",health,"health")
        vraag5()
    else:
        print("Dit is geen geldig antwoord!")
        vraag10()
def vraag11():
    print("Er valt iemand het water in wil je diegene HELPEN of LATEN gaan? ")
    v11 = input("==>")
    vraag11_0=v11.upper()
    if vraag11_0 == 'HELPEN':
        print("Je hebt diegene geholpen maar daardoor ben je wel nat geworden -2 health!\n")
        listofGlobals = globals()
        listofGlobals['health'] -=2
        print("Je hebt",health,"health")
        vraag19()
    elif vraag11_0 == 'LATEN':
        print("Je hebt hem laten gaan daardoor word je niet nat, +1 Health!\n")
        listofGlobals = globals()
        listofGlobals['health'] +=1
        print("Je hebt",health,"health")
        vraag13()
    else:
        print("Dit is geen geldig antwoord!")
        vraag11()
def vraag12():
    print("Je krijgt het koud en daardoor raak je bijna onderkoeld SHELTER of DOORLOPEN?  ")
    listofGlobals = globals()
    listofGlobals['health'] -=2
    v12 = input("==>")
    vraag12_0=v12.upper()
    if vraag12_0 == 'SHELTER':
        print("Je hebt shelter gezocht en hierdoor kan je veilig door lopen naar de bestemming!\n")
        nederland()
    elif vraag12_0 == 'DOOLOPEN':
        print("Je wilt doorlopen maar hierdoor kom je wel bij een vluchtelingenkamp uit!\n")
        vluchtelingenkamp()
    else:
        print("Dit is geen geldig antwoord!")
        vraag12()
def vraag13():
    print("Je komt uit bij een vluchtelingen kamp wil je BLIJVEN of ONTSNAPPEN? ") 
    v13 = input("==>")
    vraag13_0=v13.upper()
    if vraag13_0 == 'BLIJVEN':
        print("Je blijft wat jammer nou!\n")
        vluchtelingenkamp()
    elif vraag13_0 == 'ONTSNAPPEN':
        print("Je hebt geprobeert de ontsnappen!\n")
        vraag14()
    else:
        print("Dit is geen geldig antwoord!")
        vraag13()
def vraag14():
    print("Wil je je GEZIN meebrengen of in je EENTJE? ") 
    v14 = input("==>")
    vraag14_0=v14.upper()
    if vraag14_0 == 'GEZIN':
        print("Je neemt je gezin mee om te ontsnappen.\n")
        vraag20()
    elif vraag14_0 == 'EENTJE':
        print("Je probeerde in je eentje te ontsnapen hierdoor heb je kans op 1/3 om het te halen of niet\n")
        ja_ofnee = random.randint(1, 3)
        if ja_ofnee == 3:
            print("Je hebt het gehaald")
            nederland()
        else: 
            dood()
    else:
        print("Dit is geen geldig antwoord!")
        vraag14()
def vraag15():
    print("Er is een opstootje in Damaskus wil je MEEVECHTEN of VLUCHTEN") 
    v15 = input("==>")
    vraag15_0=v15.upper()
    if vraag15_0 == 'MEEVECHTEN':
        print("Je behoort nu tot de rebellengroep. Je hebt nu ook toegang tot een freepass. En door je positie in het verleden word je kanidaat voor leider!\n")
        listofGlobals = globals()
        listofGlobals['freepass'] +=1
        vraag16()
    elif vraag15_0 == 'VLUCHTEN':
        print("Je hebt proberen te vluchten want hier wou je echt niet aan meedoen. Alleen het loop niet echt goed af want je bent:\n")
        dood()
    else:
        print("Dit is geen geldig antwoord!")
        vraag15()
def vraag16():
    print("Wil je daar aan meedoen? Ja of Nee?") 
    v16 = input("==>")
    vraag16_0=v16.upper()
    if vraag16_0 == 'JA':
        print("Je gaat meedoen voor leiderschap!\n")
        vraag17()
    elif vraag16_0 == 'NEE':
        print("Je wilt hier niet aan medoen dus kom je terug bij je gezin!\n")
        vraag5()
    else:
        print("Dit is geen geldig antwoord!")
        vraag16()
def vraag17():
    print("Er word gekozen door andere leden. Je hebt een kans op 1 op 5 ") 
    ja_ofnee1 = random.randint(1, 5)
    if ja_ofnee1 == 3:
            print("Je bent leider geworden!\n")
            rebbelen()
    else:
        print("Je bent geen leider geworden nu moet je gezin wegsmokkelen want dat is veiliger.\n") 
        vraag18()
def vraag18():
    print("Wil je VEILIGE mensen smokkel of GEEN sagfe smokkel?")
    v18 = input("==>")
    vraag18_0=v18.upper()
    if vraag18_0 == 'VEILIGE':
        print("Je hebt gekozen voor de veilige kant en je moest daar voor een freepass hebben daar word nu voor gekeken!\n")
        if freepass == 1:
            vraag13()
        else:
            print("Je hebt geen freepass daardoor krijg je -3 health en ga je de unsafe kant op! maar..\n")
        nederland()
    elif vraag18_0 == 'GEEN':
        print("Je haalt je gezin over om meetegaan voor de niet safe manier maar..\n")
        nederland()
    else:
        print("Dit is geen geldig antwoord!")
        vraag18()
def vraag19():
    print("Je komt bij om DOOR te gaan of om TERUG tegaan.")
    v19 = input("==>")
    vraag19_0=v19.upper()
    if vraag19_0 == 'DOOR':
        print("Je wilt doorgaan daardoor kom je aan in:\n")
        nederland()
    elif vraag19_0 == 'TERUG':
        print("Je wou terug gaan alleen dit liep fataal af daarom ben je nu:\n")
        dood()
    else:
        print("Dit is geen geldig antwoord!")
        vraag19()
def vraag20():
    print("Wil je eten SPAREN of gewoon ETEN")
    v20 = input("==>")
    vraag20_0=v20.upper()
    if vraag20_0 == 'SPAREN':
        print("Je hebt het eten gespaard.\n")
        vraag21()
    elif vraag20_0 == 'ETEN':
        print("Je hebt het gewoon gegeten. -1 health!\n")
        listofGlobals = globals()
        listofGlobals['health'] -=1
        print("Je hebt",health,"health")
        vraag19()
    else:
        print("Dit is geen geldig antwoord!")
        vraag20()
def vraag21():
    print("Wil je door blijven LOPEN of RUST pakken")
    v21 = input("==>")
    vraag21_0=v21.upper()
    if vraag21_0 == 'LOPEN':
        print("Je gaat doorlopen en daardoor kom je uit bij de:\n")
        rebbelen()
    elif vraag21_0 == 'RUST':
        print("Je pakt je rust alleen komen de autoriteiten er achter waar je zit daardoor kom je bij het:\n")
        vluchtelingenkamp()
    else:
        print("Dit is geen geldig antwoord!")
        vraag21()
def vraag22():
    print("Je kan jezelf laten betalen voor een ticket naar nederland wil je BETALEN of GEWOON gaan. ")
    v22 = input("==>")
    vraag22_0=v22.upper()
    if vraag22_0 == 'BETALEN':
        print("Je wilt jezelf een ticket naar Nederland laten betalen alleen de autoriteiten komen er acher dat het vals geld is dus je word weggezet naar een haven!\n ")
        vraag5()
    elif vraag22_0 == 'GEWOON':
        print("Je gaat gewoon zonder naatedenke en door je gehaast checken de autoriteiten het geld niet en ze denken dat het echt is daardoor kom je veilig aan in:\n")
        nederland()
    else:
        print("Dit is geen geldig antwoord!")
        vraag22()
def dood():
    if health <= 0:
        dood()
        listofGlobals = globals()
        listofGlobals['health'] +=1
    print("_____   ____   ____  _____  \n|  __ \ / __ \ / __ \|  __ \ \n| |  | | |  | | |  | | |  | |\n| |  | | |  | | |  | | |  | |\n| |__| | |__| | |__| | |__| |\n|_____/ \____/ \____/|_____/\n ")
    print("Je bent helaas dood gegaan!\nwil je nog een keer spelen? y/n?")
    opnieuw = input("==>")
    if opnieuw == 'y':
        start()
    else:
        exit
def nederland():
    print(" _   _ ______ _____  ______ _____  _               _   _ _____  \n| \ | |  ____|  __ \|  ____|  __ \| |        /\   | \ | |  __ \ \n|  \| | |__  | |  | | |__  | |__) | |       /  \  |  \| | |  | |\n| . ` |  __| | |  | |  __| |  _  /| |      / /\ \ | . ` | |  | |\n| |\  | |____| |__| | |____| | \ \| |____ / ____ \| |\  | |__| |\n|_| \_|______|_____/|______|_|  \_\______/_/    \_\_| \_|_____/ \n")
    print("Je bent aangekomen in Nederland je hebt je vrijheid gevonden en je pakt je leven opnieuw op.\nWil je nog een keer spelen? y/n?")
    opnieuw = input("==>")
    if opnieuw == 'y':
        start()
    else:
        exit 
def rebbelen():
    print("_____  ______ ____  ______ _      _      ______ _   _  \n|  __ \|  ____|  _ \|  ____| |    | |    |  ____| \ | | \n| |__) | |__  | |_) | |__  | |    | |    | |__  |  \| | \n|  _  /|  __| |  _ <|  __| | |    | |    |  __| | . ` | \n| | \ \| |____| |_) | |____| |____| |____| |____| |\  | \n|_|  \_\______|____/|______|______|______|______|_| \_|\n ")
    print("Je blijft bij de rebbelgroep misschien word of ben je wel leider?\nWil je nog een keer spelen y/n?")
    opnieuw = input("==>")
    if opnieuw == 'y':
        start()
    else:
        exit 
def vluchtelingenkamp():
    print("__      ___     _    _  _____ _______ _    _ ______ _      _____ _   _  _____ ______ _   _ _  __          __  __ _____  \n\ \    / / |   | |  | |/ ____|__   __| |  | |  ____| |    |_   _| \ | |/ ____|  ____| \ | | |/ /    /\   |  \/  |  __ \ \n\ \  / /| |   | |  | | |       | |  | |__| | |__  | |      | | |  \| | |  __| |__  |  \| | ' /    /  \  | \  / | |__) |\n\ \/ / | |   | |  | | |       | |  |  __  |  __| | |      | | | . ` | | |_ |  __| | . ` |  <    / /\ \ | |\/| |  ___/ \n\  /  | |___| |__| | |____   | |  | |  | | |____| |____ _| |_| |\  | |__| | |____| |\  | . \  / ____ \| |  | | |     \n\/   |______\____/ \_____|  |_|  |_|  |_|______|______|_____|_| \_|\_____|______|_| \_|_|\_\/_/    \_\_|  |_|_|\n")
    print("Je bent blijfen hangen in een vlucthelingenkamp, je hoop dat je nog verder kan gaan naar Europa!\n Wil je nog een keer spelen y/n?")
    opnieuw = input("==>")
    if opnieuw == 'y':
        start()
    else:
        exit 
start()
