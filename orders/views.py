from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from authentication.models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class OrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'msg':'hello order'},status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self,request):
        orders = self.get_queryset()
        serializer = self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        # import pdb ; pdb.set_trace()
        data = request.data 
        user = request.user 
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid(): 
            serializer.save(customer = user) 
            return Response(data=serializer.data,status=status.HTTP_201_CREATED) 
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class OrderDetailView(generics.GenericAPIView):

    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,order_id):
        order= get_object_or_404(Order,id=order_id) 
        serializer = self.serializer_class(instance=order) 
        return Response(serializer.data,status=status.HTTP_200_OK) 

    def put(self,request,order_id):
        data=request.data
        order = get_object_or_404(Order,id=order_id)
        serializer =self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,order_id):
        # order = get_object_or_404(Order,id=order_id) yo dui ma j lekhe ni hunxa
        order = Order.objects.filter(id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateOrderStatusView(generics.GenericAPIView):
    serializer_class = OrderStatusSerializer

    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        data = request.data
        serializer = self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserOrderView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer 
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        orders=Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders,many=True) 
        return Response(data=serializer.data,status=status.HTTP_200_OK) 

# class UserOrderDetail(generics.GenericAPIView):
#     serializer_class = OrderDetailSerializer 

#     def get(self,request,user_id,order_id): 
#         user = User.objects.get(id=user_id) 
#         order=Order.objects.all().filter(customer=user).filter(id=order_id) 
#         serializer = self.serializer_class(instance=order,many=True) 
#         return Response(data=serializer.data,status=status.HTTP_200_OK) 