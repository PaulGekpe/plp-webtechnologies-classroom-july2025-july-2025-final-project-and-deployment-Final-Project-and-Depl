def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is less than 20%, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"Final price: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")