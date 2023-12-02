from django.urls import path, include
from .views import *

urlpatterns = [
    #Product
    path('', list_products),
    path('crear/producto', create_product, name='create_product'),
    path('detalle/producto/<id>', detail_product, name='detail_product'),
    path('agregar/etiqueta/<id>', add_tag, name='add_tag'),
    path('quitar/etiqueta/<id>', remove_tag, name='remove_tag'),
    path('actualizar/producto/<id>', update_product, name='update_product'),
    path('eliminar/producto/<id>', delete_product, name='delete_product'),
    #Category
    path('categorias/', ListCategories.as_view()),
    path('crear/categoria', CreateCategory.as_view(), name='create_category'),
    path('actualizar/categoria/<pk>', UpdateCategory.as_view(), name='update_category'),
    path('eliminar/categoria/<id>', delete_category, name='delete_category'),
    #Sale
    path('ventas/', list_sales),
    path('procesar/venta', process_sale, name='process_sale'),
]