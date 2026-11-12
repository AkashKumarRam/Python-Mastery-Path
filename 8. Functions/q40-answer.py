'''
Write a function called discount_price that takes original_price
and discount_percent as parameters and print the final price after
discount.
'''

def discount_price(original_price,discount_percent):
    discount_amount = (discount_percent/100) * original_price
    final_price = original_price - discount_amount

    print(f"Final product price is = {final_price}")

discount_price(2000,50)