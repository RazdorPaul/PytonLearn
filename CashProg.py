import Tables
import UserInput

from rich import print


shop_cash = []
cashier = UserInput.userName("Введите ваше имя")
while True:
    Tables.mainWindow()
    item_ = UserInput.choiceItem()
    if item_ == 1:
        shop_cash.append(UserInput.addProduct())
        while True:
            if UserInput.confirmChoice("Желаете добавить еще? (y-да/n-нет)") == False:
                break
            else:
                shop_cash.append(UserInput.addProduct())
    elif item_ == 2:
        Tables.showCart(shop_cash)
        input("Для возврата нажмите ENTER")
    elif item_ == 3:
        if UserInput.confirmChoice("Вы действительно хотите очистить корзину? (y-да/n-нет)") == True:
            shop_cash.clear()
    elif item_ == 4:
        if len(shop_cash) == 0:
            print("Вывод чека невозможен, корзина пуста")
            continue
        Tables.showCheck(cashier, shop_cash)
        input("Для возврата нажмите ENTER")
    elif item_ == 5:
        if UserInput.confirmChoice("Вы действительно желаете выйти (y=да/n=нет)?"):
            break
        else:
            continue
