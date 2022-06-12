from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.serializers import ShopSerializer, MenuSerializer
from order.models import Shop, Menu, Order, Orderfood


@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list': order_list})


@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order_item = Order.objects.get(pk=request.POST['order_id'])
        shop = order_item.shop
        order_item.estimated_time = int(request.POST['estimated_time'])
        order_item.save()
        return render(request, 'boss/success.html', {'shop': int(shop)})
    else:
        return HttpResponse(status=404)
