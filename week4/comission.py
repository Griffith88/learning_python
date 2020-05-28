class Value:

    def __get__(self, obj, obj_type):
        return int(self.amount - self.amount * obj.commission)

    def __set__(self, obj, amount):
        self.amount = amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


# new_account = Account(0.1) # INIT
# new_account.amount = 100 # SET
#
# print(new_account.amount) # GET
