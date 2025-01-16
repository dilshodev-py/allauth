from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from apps.schema import schema
from apps.views import ForgotPasswordApiView, ChangePasswordFormView

urlpatterns = [
    path("forgot-password" , ForgotPasswordApiView.as_view()),
    # path("account/recovery/confirm/<str:confirm_key>" , ConfirmKeyAPIView.as_view()),
    path("account/password/change/" , ChangePasswordFormView.as_view() , name="change_password"),
    # path("", TemplateTestView.as_view()),
    path(r"graphql", csrf_exempt(GraphQLView.as_view(graphiql=True ,  schema=schema))),

]
