from django.contrib import admin
from .models import Users,Connection,Address,Document,Booking,Payment


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=['user','mobile']
    search_fields = ['mobile']


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display=['costomer_no','user','gender','dob','status']
    search_fields = ['costomer_no', 'dob','status']

@admin.register(Address)
class UsersAdmin(admin.ModelAdmin):
    list_display=['user','city','state','country','pincode','address']
    search_fields = ['city','state','country','pincode','address']

@admin.register(Document)
class UsersAdmin(admin.ModelAdmin):
    list_display=['user','aadhar_no','aadhar_image','rationcard_no','rationcard_image']
    search_fields = ['rationcard_no','aadhar_no']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['user','cylinder_type','price','status','book_date']
    search_fields = ['status','book_date']
@admin.register(Payment)
class BookingAdmin(admin.ModelAdmin):
    list_display=['user','payment_type','amount','transaction_date','cylinder_type']
    search_fields = ['transaction_date','cylinder_type']