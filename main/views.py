from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product
from .permisssions import ProductPermission
from .serializers import ProductSerializer, ProductDetailsSerializer, CreateProductSerializer, UpdateProductSerializer

# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)
#
#
# class ProductsList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)

# class ProductsList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetails(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailsSerializer
#
#
# class CreateProduct(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = CreateProductSerializer
#     permission_classes = [ProductPermission, ]
#
#
# class UpdateProduct(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = UpdateProductSerializer
#     permission_classes = [ProductPermission, ]
#
#
# class DeleteProduct(DestroyAPIView):
#     queryset = Product.objects.all()
# CreateAPIView
# class MyView(CreateMixin, ListMixin, GenericAPIView):
#     def post(self):
#         ...
#     def get(self):
#         ...


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filterset_class = ProductFilter

    # pagination_class = MyPaginationClass
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     params = self.request.query_params
    #     print(params)
    #     # queryset = queryset.filter(**params)
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [ProductPermission, ]
        return [permission() for permission in permissions]

    # def create(self, request, *args, **kwargs):
    #     ...

# class ModelViewSet(CreateModelMixin, ListModelMixin,
#                    RetrieveModelMixin, ...,
#                    GenericViewSet)

# class ProductViewSet(CreateMixin, ListMixin, UpdateMixin, GenericViewSet)
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ProductSerializer
    #     return ProductDetailsSerializer
    #
    # def get_serializer_context(self):
    #     return {'action': self.action}


    # {"id": 1, "title": "...", "description": "...",
    #  "price": 29.19, "image": "http://....", "category": {"name": "...", "slug": "..."}}
    # obj -> {} -> '{}'
    #
    # '{}' -> {} -> obj

    # 'GET', 'POST', 'PATCH', 'PUT', 'DELETE'

    # /products/ "GET" - получение листинга
    # /products/<id>/ "GET" - получение деталей продукта
    # /products/ "POST" - создание продукта
    # /products/<id>/ "PUT/PATCH" - изменение
    # /products/<id>/ "DELETE" - удаление

    # CRUD(Create, Retrieve, Update, Delete)

# {'id': 1, "title": "Adidas Predator", "description": "Brand new cleats"}
# /products/1/ - PUT "{'title': 'Adidas Predator Accelerator'}" -> {'title': 'Adidas Predator Accelerator'}
# /product/1/ - PATCH "{'title': 'Adidas Predator Accelerator'}" -> {'id': 1, "title": "Adidas Predator Accelerator", "description": "Brand new cleats"}
#
# Product() -> {'id': 1, 'title': 'Adidas Originals', ....}

# 'create', 'list', 'retrieve', 'update', 'partial_update', 'destroy'

# TODO: пагинация
# TODO: фильтрация
# TODO: поиск
# TODO: управление правами доступа
# TODO: корзина
# TODO: оформление заказа