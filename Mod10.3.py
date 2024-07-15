from threading import Thread
from threading import Lock

class BankAccount():

    def __init__(self, balance: int):
        super().__init__()
        self.__balance = balance
        self.__lock = Lock()

    def depositing(self, depo: int):
        self.__lock.acquire()
        self.__balance += depo
        print(f"Внесено: {depo}, баланс счета: {self.__balance}")
        self.__lock.release()

    def withdraw(self, cash: int):
        self.__lock.acquire()
        self.__balance -= cash
        print(f"Снято наличных: {cash}, баланс счета: {self.__balance}")
        self.__lock.release()

def deposit(account, summ):
    for i in range(100):
        account.depositing(summ)

def withdrawing(account, summ):
    for i in range(100):
        account.withdraw(summ)

bank = BankAccount(100000)
depo = Thread(target=deposit, args=(bank, 100))
withdraw = Thread(target=withdrawing, args=(bank, 150))

depo.start()
withdraw.start()
depo.join()
withdraw.join()
