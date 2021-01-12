from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .models import Users,Booking,Payment
from django.contrib.auth.decorators import login_required
from .connectionform import ConnectionForm,AddressForm,DocumentForm
from .models import Address,Connection,Document
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import razorpay
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/user/login/')
def newconnection(request):

    try:
        status = Connection.objects.get(user=request.user)
        
    except:
        status = ''
        
    if request.method == 'POST':
        
        cf=ConnectionForm(request.POST)
        af=AddressForm(request.POST)
        df=DocumentForm(request.POST,request.FILES)
        relative=request.POST.get('relative')
        gender=request.POST.get('gender')
            
       
        if cf.is_valid() and af.is_valid() and df.is_valid():
            user = request.user
            # get Connection form data from user
            relative=cf.cleaned_data['relative']
            gender=cf.cleaned_data['gender']
            dob=cf.cleaned_data['dob']
            ffname=cf.cleaned_data['ffname']
            fmname=cf.cleaned_data['fmname']
            flname=cf.cleaned_data['flname']
            mfname=cf.cleaned_data['mfname']
            mmname=cf.cleaned_data['mmname']
            mlname=cf.cleaned_data['mlname']
            c_no=generate_customer_no()
            
            # get Address form data from user
            city=af.cleaned_data['city']
            district=af.cleaned_data['district']
            state=af.cleaned_data['state']
            pincode=af.cleaned_data['pincode']
            country=af.cleaned_data['country']
            address=af.cleaned_data['address']
            # fet document data from user
            aadhar_no=df.cleaned_data['aadhar_no']
            aadhar_image=df.cleaned_data['aadhar_image']
            rationcard_no=df.cleaned_data['rationcard_no']
            rationcard_image=df.cleaned_data['rationcard_image']
            try:
                con = Connection.objects.create(user=user,costomer_no=c_no,gender=gender,dob=dob,relative=relative,ffname=ffname,fmname=fmname,flname=flname,mfname=mfname,mmname=mmname,mlname=mlname)
                ad = Address.objects.create(user=user,city=city,district=district,state=state,pincode=pincode,country=country,address=address)
                doc = Document.objects.create(user=user,aadhar_no=aadhar_no,aadhar_image=aadhar_image,rationcard_no=rationcard_no,rationcard_image=rationcard_image)
                messages.success(request,'Your Connection Request send...!')
                af = AddressForm()
                cf=ConnectionForm()
                df=DocumentForm()
            except:
                messages.error(request,'Your Connection already Requested pending for Admin Aproval..!')
        # else:
        #     messages.error(request,'Your Connection Request send fail...!')
    else:
        gender=''
        relative=''
        cf=ConnectionForm()
        af=AddressForm()
        df=DocumentForm()
    
    return render(request,'user/connection.html',{'cform':cf,'aform':af,'dform':df,'relative':relative,'g':gender,'status':status})

def generate_customer_no():
    
    over=True
    while over:
        cust_no=uuid.uuid4().hex[:17].upper()
        try:
            Connection.objects.get(costomer_no=cust_no)
        except:
            over = False
    return cust_no
@login_required(login_url='/user/login/')
def cylinderbook(request):
    try:
        status = Connection.objects.get(user=request.user)
        mobile = Users.objects.get(user=request.user)
        
    except:
        status = ''
        mobile=''
    return render(request,'user/cylinderbook.html',{'status':status,'mobile':mobile})

@login_required(login_url='/user/login/')
def cylinderbookdetail(request):
   
    try:
        status=Connection.objects.get(user=request.user)
        mobile=Users.objects.get(user=request.user)
        address=Address.objects.get(user=request.user)
    except:
        status=''
    if request.method == 'POST':
        c_type=request.POST.get('cylinder_type')
        user=request.user
        book=Booking.objects.create(user=user,cylinder_type=c_type,price=500)
        order_amount = 50000
        order_currency = 'INR'
        notes = {'Shipping address': address.address+' '+address.district+' '+address.state+' '+address.pincode} 
        client= razorpay.Client(auth=('rzp_test_DObIl75MZtocjx','Hfxk6P8JiPbetBHwfEdMyhR9'))
        
        payment= client.order.create({'amount':order_amount, 'currency':order_currency,'notes':notes,'payment_capture':'1'})
        order_id=payment['id']
        order_status=payment['status']
        if order_status=='created':
            
            return render(request,'user/payment.html',{'product_id':"Gas Cylinder",'price':order_amount,'name':request.user.first_name,'phone':mobile.mobile,'email':request.user.email,'order_id':order_id})

    return render(request,'user/viewbookcylinder.html',{'status':status})

@login_required(login_url='/user/login/')
def cylinderbookhistory(request):
    
    user_booking=Booking.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_booking, 7)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'user/cylinderbookhistory.html',{'user_booking':users})

@login_required(login_url='/user/login/')
def cylindercancel(request,id):
    try:
        booking = Booking.objects.get(pk=id)
        if booking.status != 'delivered':
            booking.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect('/user/bookcylinderhistrory/')
@csrf_exempt
def success(request):
    print(request.POST['razorpay_payment_id'])
    print(request.POST['razorpay_order_id'])
   

    # Payment.objects.create(user=request.user,)
    messages.success(request,'Payment Success..')
    return HttpResponseRedirect('/user/bookcylinderhistrory')

