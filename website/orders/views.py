from django.http import JsonResponse, HttpResponse
from website.models import Order
from website.auth.decorators import supplier_required_ajax, customer_required_ajax


#@supplier_required_ajax
def order_accept(request, order):
    if order.supplier is not None:
        return JsonResponse({'success': False, 'error': 'Order has been accepted already'}, status=201)
    order.supplier = request.user.supplier
    order.status = Order.ACCEPTED
    order.save()
    return JsonResponse({'success': True, 'status_update': Order.STATUS_CHOICES[Order.ACCEPTED][1]}, status=201)


#@supplier_required_ajax
def order_shipping(request, order):
    if order.status is not Order.ACCEPTED:
        return JsonResponse({'success': False, 'error': 'Order can\'t be shiped'}, status=201)
    order.status = Order.SHIPPING
    order.save()
    return JsonResponse({'success': True, 'status_update': Order.STATUS_CHOICES[Order.SHIPPING][1]}, status=201)


#@supplier_required_ajax
def order_delivered(request, order):
    if order.status is not Order.SHIPPING:
        return JsonResponse({'success': False, 'error': 'Order is not shipping'}, status=201)
    order.status = Order.DELIVERED
    order.save()
    return JsonResponse({'success': True, 'status_update': Order.STATUS_CHOICES[Order.DELIVERED][1]}, status=201)


#@customer_required_ajax
def order_cancel(request, order):
    if order.status is Order.DECLINED:
        return JsonResponse({'success': False, 'error': 'Order declined already'}, status=201)
    order.status = Order.DECLINED
    order.save()
    return JsonResponse({'success': True, 'status_update': Order.STATUS_CHOICES[Order.DECLINED][1]}, status=201)


#@customer_required_ajax
def order_dispute(request, order):
    if order.status is Order.DISPUTE:
        return JsonResponse({'success': False, 'error': 'Dispute started already'}, status=201)
    if order.status is Order.DECLINED:
        return JsonResponse({'success': False, 'error': 'Can\'t dispute declined order'}, status=201)
    if order.status is not Order.DELIVERED:
        return JsonResponse({'success': False, 'error': 'Order not delivered yet'}, status=201)
    order.status = Order.DISPUTE
    order.save()
    return JsonResponse({'success': True, 'status_update': Order.STATUS_CHOICES[Order.DISPUTE][1]}, status=201)


# handle all order api requests
def order_handler(request, order_id, command):
    # check if deleverer is right
    if not request.method == 'POST':
        return JsonResponse({}, status = 400)
    try:
        order = Order.objects.get(id=order_id)
    except:
        return JsonResponse({"error":"Error occured", "description": str(e)}, status = 200)

    # if order.supplier is not request.user.supplier:
    #     return JsonResponse({"error": "Wrong supplier"}, status = 200)

    if command == 'accept':
        return order_accept(request, order)
    elif command == 'shipping':
        return order_shipping(request, order)
    elif command == 'delivered':
        return order_delivered(request, order)
    elif command == 'cancel':
        return order_cancel(request, order)
    elif command == 'dispute':
        return order_dispute(request, order)

    return JsonResponse({'error' : 'No such command'}, status = 400)
