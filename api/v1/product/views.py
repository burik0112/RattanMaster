from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from index.models import Product
from api.v1.product.serializers import ProductSerializer
from api.v1.product.services import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )
    queryset = Product.objects.all()

    # def get_object(self, pk=None):
    #     try:
    #         root = Product()
    #     except:
    #         raise NotFound("Object topilmadi")
    #     return root
    #
    # def get(self, requests, *args, **kwargs):
    #     if 'pk' in kwargs and kwargs['pk']:
    #         response = get_one(requests, kwargs['pk'])
    #     else:
    #         response = get_all(requests)
    #     return Response(response, status=HTTP_200_OK, content_type='application/json')

    # def post(self, requests, *args, **kwargs):
    #     model = Product
    #     data = requests.data
    #     serializer = self.serializer_class(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     root = serializer.create(serializer.data)
    #     root.image = data['qr_code']
    #     root.save()
    #     response = get_one(requests, root.id)
    #     return Response(response, status=HTTP_200_OK, content_type='application/json')

    # def put(self, requests, *args, **kwargs):
    #     data = requests.data
    #     root = self.get_object(pk=kwargs['pk'])
    #     serializer = self.get_serializer(data=data, instance=root, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     root = serializer.save()
    #     response = get_one(requests, root.id)
    #     return Response(response, status=HTTP_200_OK, content_type='application/json')

    # def delete(self, requests, *args, **kwargs):
    #     root = self.get_object(kwargs['pk'])
    #     root.delete()
    #     response = {'result': f'{root.inventar_number} was deleted'}
    #     return Response(response, status=HTTP_200_OK, content_type='application/json')


