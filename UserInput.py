from rich.prompt import Confirm as conf
from rich.prompt import IntPrompt as i_prompt
from rich.prompt import FloatPrompt as f_prompt
from rich.prompt import Prompt as s_prompt


def choiceItem():
    return i_prompt.ask("Введите номер операции (1-5)")


def userName(name):
    return s_prompt.ask(name)


def confirmChoice(str_ask):
    return conf.ask(str_ask, show_choices=False)

def addProduct():
    product = s_prompt.ask("Что вы хотите добавить?")
    amount = i_prompt.ask("Уточните количество этого товара?")
    coast = f_prompt.ask("Уточните стоимость товара?")
    return [product, amount, coast]