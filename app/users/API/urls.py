from users.API.views import registration_view, login, AccountList, AccountDetails, AccountCreate,Profile
from django.urls import path
urlpatterns =[
    path('login/', login, name='login'),
    path('register/', registration_view, name='register'),
    #usersxd
    path('list/', AccountList.as_view(), name='account-list'),
    path('create/', AccountCreate.as_view(), name="account-create"),
    path('list/<int:pk>', AccountDetails.as_view(), name="account-delete"),


    #profile
    path('profile', Profile.as_view(), name="profile")
]