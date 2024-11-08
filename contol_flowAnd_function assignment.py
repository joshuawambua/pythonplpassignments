"""Create a function named calculate_discount(price,
 discount_percent) that calculates the final price after applying a discount. 
 The function should take the original price (price) and the discount percentage 
 (discount_percent) as parameters. If the discount is 20% or higher, apply the
   discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the
 original price of an item and the discount percentage. Print the 
 final price after applying the discount, or if no discount was applied, 
 print the original price."""


#Answer
def calculate_discount(price, discount_percent):
    #Calculating the final price after applying a discount if it's 20% or higher.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# INPUTS
#This block manages invalid input cases.
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculating the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Displaying the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
