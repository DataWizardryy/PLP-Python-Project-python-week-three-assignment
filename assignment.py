# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        # Calculate the discount amount and subtract it from the original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))

# Get the discount percentage from the user
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Display the result
if final_price < price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
