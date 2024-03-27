
#!/usr/bin/env python3
# class TestCashRegister:
#     '''CashRegister in cash_register.py'''

#     cash_register = CashRegister()
#     cash_register_with_discount = CashRegister(20)

#     def reset_register_totals(self):
#       self.cash_register.total = 0
#       self.cash_register_with_discount.total = 0

#     def test_discount_attribute(self):
#         '''takes one optional argument, a discount, on initialization.'''
#         assert(self.cash_register.discount == 0)
#         assert(self.cash_register_with_discount.discount == 20)

#     def test_total_attribute(self):
#         '''sets an instance variable total to zero on initialization.'''
#         assert(self.cash_register.total == 0)
#         assert(self.cash_register_with_discount.total == 0)

#     def test_items_attribute(self):
#         '''sets an instance variable items to empty list on initialization.'''
#         assert(self.cash_register.items == [])
#         assert(self.cash_register_with_discount.items == [])

#     def test_add_item(self):
#         '''accepts a title and a price and increases the total.'''
#         self.cash_register.add_item("eggs", 0.98)
#         assert(self.cash_register.total == 0.98)
#         # self.reset_total(self.cash_register)
#         self.reset_register_totals()

#     def test_add_item_optional_quantity(self):
#         '''also accepts an optional quantity.'''
#         self.cash_register.add_item("book", 5.00, 3)
#         assert(self.cash_register.total == 15.00)
#         # self.cash_register.total = 0
#         self.reset_register_totals()

#     def test_add_item_with_multiple_items(self):
#         '''doesn"t forget about the previous total'''
#         self.cash_register.add_item("Lucky Charms", 4.5)
#         assert(self.cash_register.total == 4.5)
#         self.cash_register.add_item("Ritz Crackers", 5.0)
#         assert(self.cash_register.total == 9.5)
#         self.cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
#         assert(self.cash_register.total == 14.5)
#         self.reset_register_totals()

#     def test_apply_discount(self):
#         '''applies the discount to the total price.'''
#         self.cash_register_with_discount.add_item("macbook air", 1000)
#         self.cash_register_with_discount.apply_discount()   
#         assert(self.cash_register_with_discount.total == 800)
#         # self.cash_register_with_discount.total = 0
#         self.reset_register_totals()

#     def test_apply_discount_success_message(self):
#         '''prints success message with updated total'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         self.cash_register_with_discount.add_item("macbook air", 1000)
#         self.cash_register_with_discount.apply_discount()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "After the discount, the total comes to $800.\n")
#         self.reset_register_totals()

#     def test_apply_discount_reduces_total(self):
#         '''reduces the total'''
#         self.cash_register_with_discount.add_item("macbook air", 1000)
#         self.cash_register_with_discount.apply_discount()
#         assert(self.cash_register_with_discount.total == 800)
#         self.reset_register_totals()

#     def test_apply_discount_when_no_discount(self):
#         '''prints a string error message that there is no discount to apply'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         self.cash_register.apply_discount()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "There is no discount to apply.\n")
#         self.reset_register_totals()

#     def test_items_list_without_multiples(self):
#         '''returns an array containing all items that have been added'''
#         new_register = CashRegister()
#         new_register.add_item("eggs", 1.99)
#         new_register.add_item("tomato", 1.76)
#         assert(new_register.items == ["eggs", "tomato"])

#     def test_items_list_with_multiples(self):
#         '''returns an array containing all items that have been added, including multiples'''
#         new_register = CashRegister()
#         new_register.add_item("eggs", 1.99, 2)
#         new_register.add_item("tomato", 1.76, 3)
#         assert(new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"])

#     def test_void_last_transaction(self):
#       '''subtracts the last item from the total'''
#       self.cash_register.add_item("apple", 0.99)
#       self.cash_register.add_item("tomato", 1.76)
#       self.cash_register.void_last_transaction()
#       assert(self.cash_register.total == 0.99)
#       self.reset_register_totals()

#     def test_void_last_transaction_with_multiples(self):
#       '''returns the total to 0.0 if all items have been removed'''
#       self.cash_register.add_item("tomato", 1.76, 2)
#       self.cash_register.void_last_transaction() 
#       assert(self.cash_register.total == 0.0)
#       self.reset_register_totals()
   
class CashRegister:
   
    def __init__(self,discount=0,total=0) :        
        self.discount=0
        self.total=0 
        self.discount+=discount  
        self.total+=total       
        self.items=[] 
        self.totals=[]   
       
   
    def add_item(self,title,price,option=1,):         
       self.discount=price*0.2 
       self.total+=(price*option)
       #self.total-self.discount
       self.totals.append(self.total)
    #    self.discount=discount
      # total=(price*option)-discount 
      # CashRegister(discount,total)       
       self.items.append(title*option)         
            
    
    def apply_discount(self):        
        self.total=float(self.total-self.discount)
        self.total=self.total
        if self.total>0 :
            #self.discount=CashRegister.discount
            print(f"After the discount, the total comes to ${self.total}.")
        else:print("There is no discount to apply.")

    def item_list_without_multiples(self):
        total3=[]
        for a in range(len(self.items)):
            for b in range(a+1,len(self.items)):
             if self.items[a] not in self.items[b]:
                total3.append(self.items[a])
        return total3    
    def item_list_with_multiples(self):
       # return self.items
        total4=[]
        for a in range(len(self.items)):
            total4.append(self.items[a])
        return total4
        
        
        # return self.items
    
    def void_last_transaction(self):        
        rem=self.totals.pop(len(self.totals))
        return self.total-rem
        
     

