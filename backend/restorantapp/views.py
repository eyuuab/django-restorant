from restorantapp.models import Menu, Order, UserModel
from django.http import JsonResponse
from django.utils import timezone

# Renamed the view function to avoid naming conflict with the Menu model
def userHandler(request):
    print("function called")
    if request.method == 'POST':
        userEmail = request.POST.get('email')
        userPassword = request.POST.get('password')
        userBalance = request.POST.get('balance')

        newUser = UserModel(
            email=userEmail,
            password=userPassword,
            balance=userBalance
        )
        newUser.save()
        return JsonResponse({'message':'user successfuly created'})
    
    elif request.method == 'GET':
        userId = request.GET.get('userId')
        try:
            user = UserModel.objects.filter(id=userId)
            return JsonResponse({"userEmail":user.email,'userBalance':user.balance})
        except:
            return JsonResponse({"Error":"User not found"}, status= 404)
 
    else:
        return JsonResponse({'Error':'User Not Created'})

def menuHandler(request):
    if request.method == 'POST':
        menu_name = request.POST.get('name')
        item_price = request.POST.get('price')

        menu_object = Menu(
            name=menu_name,
            price=item_price,
            created=timezone.now(),
            updated=timezone.now()
        )

        menu_object.save()
        return JsonResponse({"message": "Menu item stored"}, status=200)
    else:
        return JsonResponse({}, status=404)
    
def order(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')  # Corrected field name to match the form
        quantity = request.POST.get('quantity')

        try:
            ordered_item = Menu.objects.get(id=menu_id)
            total_price = ordered_item.price * int(quantity)
            return JsonResponse({'total_price': total_price}, status=200)
        except Menu.DoesNotExist:
            return JsonResponse({'error': 'Menu item not found'}, status=404)
    else:
        return JsonResponse({}, status=405)  # Method not allowed

def payment(request):
    if request.method == 'POST':
        paymentAmount = request.POST.get('payment_amount')

        balance = UserModel.balance
        balance -= int(paymentAmount)

        balanceUPT = UserModel(
            balance = balance
        )

        balanceUPT.save()

        return JsonResponse({"Paid:{paymentAmount}, 'balance':{balance}"})
    else:
        return JsonResponse({'Error':"Not Successful"})
