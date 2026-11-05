# Question 1
bill = 2 * 500 + 2000
print("Total Bill:", bill)

# Question 2
recharge = 299
gst = recharge * 18 / 100
total = recharge + gst
print("GST:", gst)
print("Total:", total)

# Question 3
print(18 // 4 + 2)

# Question 4
print(18 % 5 * 2)

# Question 5
print(2 + 3 * 4 ** 2)

# Question 6
mobile = 25000
headphone = 3000
discount = 2500
premium = False

subtotal = 2 * mobile + headphone
after_discount = subtotal - discount
gst = after_discount * 18 / 100
final_amount = after_discount + gst

free_delivery = premium or final_amount >= 50000

print("Subtotal:", subtotal)
print("After Discount:", after_discount)
print("GST:", gst)
print("Final Amount:", final_amount)
print("Free Delivery:", free_delivery)