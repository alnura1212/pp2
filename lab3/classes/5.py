class Account:
    def __init__(self):
        self.owner=str(input("Имя: "))
        self.balance=0
    def deposit(self):
        self.amount=int(input("Введите сумму: "))
        self.balance+=self.amount
        print("Пополнение: ", self.balance, "\nДоступно:", self.balance)
    def widthdrawals(self):
        self.amount=int(input("Введите сумму для снятия: "))
        if self.amount<=self.balance:
            self.balance-=self.amount
            print("Вы успешно сняли сумму.")
            print ("Доступно:", self.balance)
        else:
            print("У вас недостаточно средств.")

p1=Account()
p1.deposit()
p1.widthdrawals()