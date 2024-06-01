import UserInput

from datetime import datetime
from datetime import date
from rich.panel import Panel as pane
from rich.text import Text as text
from rich.table import Table as tab
from rich.columns import Columns as col
from rich import print


def mainWindow():
    date_ = str(date.today())
    print(pane.fit("Выберите операцию\n\n"
               "1 Добавление товара\n"
               "2 Просмотр корзины\n"
               "3 Очистка корзины\n"
               "4 Пробить чек\n"
               "5 Завершить работу\n",
               title = "Касса", subtitle = date_))


def totalPrice(products=[]):
    total = 0
    if len(products) != 0:
        for i in range(len(products)):
            total += products[i][1] * products[i][2]
    return total


def showCart(products):
    cart = tab(title="ВАША КОРЗИНА")
    cart.add_column("Наименование", justify="left")
    cart.add_column("Количество", justify="left")
    cart.add_column("Стоимость", justify="left")
    if len(products) == 0:
        print(pane.fit("ВАША КОРЗИНА ПУСТА!", title = "ВАША КОРЗИНА"))
    else:
        for i in range(len(products)):
            cart.add_row(products[i][0],
                         str(products[i][1]),
                         f"{products[i][2]*products[0][1]:.2f}" + '$')
    print(cart)
    print(pane.fit("Общая стоимость вашей корзины равна " + f"{totalPrice(products):.2f}" + '$'))


def showCheck(user_kassa, prod):
    byer = UserInput.userName("Введите имя покупателя")
    check_title = ("\nДобро пожаловать!\n"
                   "Вас Обслуживает кассир:\n"
                   "")+user_kassa+("\n"
                    "Адрес нашего магазина:\n"
                    "Чита, ул. Строителей, 1А/2")
    check_title += "\n\n####################\n\n"
    for i in range(len(prod)):
        check_title += f"{prod[i][0]} {prod[i][1]}x{prod[i][2]:.2f}$\n"
    check_title += f"ИТОГО ПО ЧЕКУ {totalPrice(prod):.2f}$"
    check_title += (f"\n\n####################\n\n"
                    f"Покупатель {byer}\n\n"
                    f"Дата {date.today()}\n"
                    f"Время {datetime.now().strftime("%H:%M:%S")}\n"
                    f"\n####################\n\n"
                    f"Приходите еще!\n")
    print(pane.fit(check_title, title = "Чек"))

