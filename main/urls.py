from django.urls import path,include
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

#Tugas 4
from main.views import register,login_user,logout_user,add_product,sell_product,remove_product

#Tugas 6
from main.views import get_product_json, add_product_ajax,del_product_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #Bonus Tugas 4
    path('add/', add_product, name='add_product'),
    path('remove/', sell_product, name='sell_product'),
    path('delete/', remove_product, name='remove_product'),
    #Tugas 6
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-product-ajax/', del_product_ajax, name='del_product_ajax')
]