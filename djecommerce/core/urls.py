from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('userprofile', view=UserProfile.as_view()),
    path('orderitem', view=OrderItem.as_view()),
    path('item', view=Item.as_view()),
    path('payment', view=Payment.as_view()),
    path('address', view=Address.as_view()),
    path('refund', view=Refund.as_view()),
    path('orders', view=Orders.as_view()),
]