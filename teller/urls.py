from django.urls import path
from teller.views import (
   add_teller_view,
   detail_teller_view,
   edit_teller_view,
)

app_name = 'teller'

urlpatterns = [
    path('addteller/', add_teller_view, name="addteller"),
    path('<slug>/', detail_teller_view, name="detailteller"),
    path('<slug>/edit', edit_teller_view, name="editteller"),

]