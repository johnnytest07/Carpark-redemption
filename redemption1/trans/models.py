from django.db import models

# Create your models here.

from typing import Any
from django.db import models
from datetime import datetime
from abc import ABC, abstractmethod

# Create your models here.

#Keeps track of how many couponns each store has
class types_of_coupons(models.Model):
    weekday_one_hour = models.IntegerField(default=0)
    weekday_two_hour = models.IntegerField(default=0)
    weekday_three_hour = models.IntegerField(default=0)
    weekend_one_hour = models.IntegerField(default=0)
    weekend_two_hour = models.IntegerField(default=0)
    weekend_three_hour = models.IntegerField(default=0)

    class Meta:
        abstract = True

class StockControl(types_of_coupons):
    storeID = models.AutoField(primary_key=True)
    active = models.BooleanField(default=False)

    class Meta:
        app_label = 'trans'

#TransactionHistory including all types of coupon ordered, total cost of the order, date they ordered, payment method they used
class TransactionHistory(types_of_coupons):     
    date_of_purchase = models.DateTimeField(default=datetime.now, blank=True, null=True)
    storeID = models.ForeignKey(StockControl, on_delete=models.CASCADE)
    price_of_order = models.FloatField(default=0)
    payment_method = models.CharField(max_length=200, blank=True)


#this part imports all the transaction data into the transaction hsitory
#I am how to put input variables into here 
#transaction should be a variable that can be inputted
    def enter_order(self,i1,i2,i3,i4,i5,i6,i7):
        transaction = TransactionHistory(
            date_of_purchase=datetime.now(),
            storeID_entered=i7,
            weekday_one_hour=i1,
            weekday_two_hour=i2,
            weekday_three_hour=i3,
            weekend_one_hour=i4,
            weekend_two_hour=i5,
            weekend_three_hour=i6,
            price_of_order=1,
            payment_method="",
        )
        transaction.save()

#storeID_entered is how we identify the store, they enter their ID and we use that to find their respective inventory in StockControl
#storeID_entered should be a variable where it can be changed when entered into the system

    def save_order(self):
        storeID_entered = StockControl.objects.get(pk=self.storeID)
        StockControl.weekday_one_hour += self.weekday_one_hour
        StockControl.weekday_two_hour += self.weekday_two_hour
        StockControl.weekday_three_hour += self.weekday_three_hour
        StockControl.weekend_one_hour += self.weekend_one_hour
        StockControl.weekend_two_hour += self.weekend_two_hour
        StockControl.weekend_three_hour += self.weekend_three_hour

#creation of coupons

    # def generating_coupons(self):
        types_list = [i1,i2,i3,i4,i5,i6]
        for i in range(len(types_list)):
            for _ in range(types_list[i]):
                new_object = CouponsTally(coupontype=i+1, storeID = storeID_entered)

#Keep track of all the tickets
#oct_number is octopus card number to keep track of how many coupons he used 
#for type(it shows the coupon type 1 - weekday 1 hr, 2 - weekday 2 hr, 3 - weekday 3 hr, 
#4 - weekend 1 hr, 5 - weekend 2 hr, 6 - weekend 3 hr)
#(default =0 but when activated with ocotopus card it will be replaced with user's octopus card)    
class CouponsTally(models.Model):
    couponID = models.AutoField(primary_key=True)
    coupontype = models.IntegerField(default=0)
    activation_date = models.DateField(blank=True,null=True)
    oct_number = models.CharField(default=0, max_length=200)
    storeID = models.ForeignKey(StockControl, on_delete=models.CASCADE)

