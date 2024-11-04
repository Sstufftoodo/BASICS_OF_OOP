# encapsulation : It describes the idea of wrapping data and the
#                 methods that work on data within one unit. This
#                 puts restriction on accessing variables and methods
#                 directly and can prevent the accidental modification
#                 of a certain data.``
#                 There are 2 types of encanpsulation, which is private
#                 member ( __ ) and protected members ( _ )
#
# protected     : members of the class that cannot be accessed 
#                 outside the class but can be accessed from 
#                 within the class and its subclasses
# 
# private       : private members are only accessible within 
#                 the class where they are declared.

class Payment:
    def __init__(self, price):
        self.__finalprice = price + price * 0.5

    def get_finalprice(self):
        return self.__finalprice
    
    def set_finalprice(self, discount):
        self.__finalprice = self.__finalprice - self.__calculate_discount
    
    def __calculate_discount(self, discount):
        return self.__finalprice * (discount/100)

payment = Payment(10)
payment.set_finalprice(5)
payment.__calculate_discount(50)
print(payment.get_finalprice())