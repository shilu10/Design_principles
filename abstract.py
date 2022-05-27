# imports.
from abc import ABC, abstractmethod

# ClassLine is a online shopping website, where we can buy and able to process it
# for checkout.
# there are three kinds of payment options -> Debit Card, Credit Card, COD(Cash On Delivery)

class PaymentMethod(ABC) :
    @abstractmethod 
    def pay(self, inr) :
        pass 

class DebitCard(PaymentMethod) :
    def pay(self, inr) :
        return "Success paying using debit card!!!"

class COD(PaymentMethod) :
    def pay(self, inr) : 
        return "Confirm paying usinf COD" 

class CreditCard :
    def pay(self, inr) :
        return "Success paying using Credit Card!!!"

class ClassLine :

    def __init__(self) :
        pass 
    
    def payment_processing(self, inr : int, payment_method) :
        try :
            return payment_method.pay(inr)

        except :
            return "Fails"


    def select_payment(self) :
        debit_card = DebitCard()
        credit_card = CreditCard()
        cod = COD()

        payment_method = input("Enter Payment Option! option1 : debit_card, option2 : credit_card, option3 : cod = ")
        inr = 100

        if payment_method == "cod" :
            payment_method = cod 
        
        elif payment_method == "debit_card" :
            payment_method = debit_card

        print(self.payment_processing(100, payment_method))


classline = ClassLine()

classline.select_payment()








