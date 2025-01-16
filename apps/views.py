import random
import uuid
from contextlib import redirect_stderr
from datetime import timedelta

import redis
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.dateformat import re_escaped
from django.views.generic import TemplateView, FormView
from drf_spectacular.utils import extend_schema
from redis import Redis
from rest_framework.views import APIView

from AllAuth.settings import EMAIL_HOST_USER
from apps.forms import ChangePasswordForm
from apps.serializers import ResetPasswordSerializer
from apps.tasks import send_email


# Create your views here.

# class TemplateTestView(TemplateView):
#     template_name = 'tmp.html'

@extend_schema(
        request=ResetPasswordSerializer,
        tags=['auth']
)
class ForgotPasswordApiView(APIView):
    def post(self , request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).exists()
        if not user:
            return JsonResponse({"message" : "Not Found Email"})

        confirm_key = str(uuid.uuid4())
        redis = Redis()
        redis.set(confirm_key , email.encode())
        redis.expire(email, timedelta(minutes=5))
        url = f"http://localhost:8000/api/v1/account/recovery/confirm/{confirm_key}"
        send_email(email, url)
        return JsonResponse({"message" : "Success send email"})


# class ConfirmKeyAPIView(APIView):
#     def get(self, request , confirm_key):
#         redis = Redis(decode_responses=True)
#         email = redis.get(confirm_key)
#         if email:
#             redis.delete(confirm_key)
#             return render(request, 'change-password.html' , context={"email" : email})
#
#         else:
#             return JsonResponse("Invalid Url")



class ChangePasswordFormView(FormView):
    template_name = 'change-password.html'
    form_class = ChangePasswordForm
    success_url = 'http://localhost:8000'


    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.filter(email=email)
        if not user.exists():
            messages.error(self.request , "Error data")
            return render(self.request, "change-password.html", context={"email": email})
        user.update(password=make_password(password))
        return super().form_valid(form)

    def form_invalid(self, form):
        email = form.cleaned_data.get("email")
        messages.error(self.request, list(form.errors.values())[0])
        return render(self.request , "change-password.html" , context={"email" : email})



"""
docker run --name rd -p 6379:6379 -d redis:alpine redis-server --save 60 1 --loglevel warning

"""