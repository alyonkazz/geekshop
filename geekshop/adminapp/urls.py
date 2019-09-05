from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # re_path(r'^', adminapp.index, name='index'),
    path('', adminapp.ShopUsersListView.as_view(), name='index'),
    path('shopuser/create/', adminapp.shopuser_create, name='create'),
    path('shopuser/update/<int:pk>/', adminapp.shopuser_update, name='update'),
    path('shopuser/delete/<int:pk>/', adminapp.shopuser_delete, name='delete'),
    path('shopuser/restore/<int:pk>/', adminapp.shopuser_restore, name='restore'),

    path('productcategory/list/', adminapp.productcategory_list,
            name='productcategory_list'),
    # re_path(r'^productcategory/create/', adminapp.productcategory_create,
    #         name='productcategory_create'),
    path('productcategory/create/', adminapp.ProductCategoryCreateView.as_view(),
            name='productcategory_create'),
    # re_path(r'^productcategory/update/<int:pk>/', adminapp.productcategory_update,
    #         name='productcategory_update'),
    path('productcategory/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(),
            name='productcategory_update'),
    # re_path(r'^productcategory/delete/<int:pk>/', adminapp.productcategory_delete,
    #         name='productcategory_delete'),
    path('productcategory/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(),
            name='productcategory_delete'),
    path('productcategory/products/<int:pk>/', adminapp.productcategory_products,
            name='productcategory_products'),

    path('product/create/<int:pk>/', adminapp.product_create,
            name='product_create'),
    path('product/update/<int:pk>/', adminapp.product_update,
            name='product_update'),
    # re_path(r'^product/read/<int:pk>/', adminapp.product_read,
    #         name='product_read'),
    path('product/read/<int:pk>/', adminapp.ProductDetailView.as_view(),
            name='product_read'),
    path('product/delete/<int:pk>/', adminapp.product_delete,
            name='product_delete'),
]
