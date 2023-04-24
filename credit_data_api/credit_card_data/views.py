from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CreditCard
from .serializers import CreditCardSerializer

# Create your views here.


#get all Credit Cards
@api_view(['GET'])
def getCreditCards(request):
    creditcard = CreditCard.objects.all()
    serializer = CreditCardSerializer(creditcard, many=True)
    return Response(serializer.data)

#get Credit Card
@api_view(['GET'])
def getUser(request, pk):
    creditcard = CreditCard.objects.get(id=pk)
    serializer = CreditCardSerializer(creditcard, many=False)
    return Response(serializer.data)

#add Credit Card
@api_view(['POST'])
def addUser(request):
    serializer = CreditCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update Credit Cards
@api_view(['PUT'])
def updateUser(request,pk):
    creditcard = CreditCard.objects.get(id=pk)
    serializer = CreditCardSerializer(instance=creditcard, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#delete Credit Cards
@api_view(['DELETE'])
def deleteUser(request, pk):
    creditcard = CreditCard.objects.get(id=pk)
    creditcard.delete()

    return Response('Item successfully deleted:')


