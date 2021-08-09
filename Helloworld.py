order_value =input("postage_rate: ")
postage_rate_1 = 3.95
postage_rate_2 = 4.95
postage_rate_3 = 0.00


order_value = float(order_value)

if (order_value <= 20.00):
    print("postage rate is: ", postage_rate_1)

elif  (order_value > 20.00 and order_value < 40):
    print("postage rate is: ", postage_rate_2)

elif (order_value > 40.00):
    print("postage rate is: ", postage_rate_3)

            

         