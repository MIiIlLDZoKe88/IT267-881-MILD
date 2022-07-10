class Juicemachine:
    menu_type = "JuiceOrder"
    total = 0

    def __init__(self,customer_name:str,menu:str,num = 1,size = 'R',size = 'L') -> None:
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,
        }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price += 1
        elif self.size == 'L':
            self.price += 5
        else:
            self.price
        
        juicemachine.total = self.price * self.num
        
    def display_order(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} ({self.num}{self.size} * ${self.price} => ${Juicemachine.total}'

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    order1 = juicemachine("WJ",1,"L")
    order2 = juicemachine("OJ",1,"R")
    order3 = juicemachine("PJ",1,"L")
    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())
    
