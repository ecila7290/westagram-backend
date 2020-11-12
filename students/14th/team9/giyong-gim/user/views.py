import json
import re
import bcrypt
import jwt

from django.db.models import Q
from django.http      import JsonResponse
from django.views     import View

import my_settings
from .models          import User
from core.utils       import (validate_email,
                              validate_password,
                              validate_phone_number)

class Register(View):

    def post(self, request):
        data = json.loads(request.body)
#        def validate_email(email):
#            return bool(re.search('^[a-zA-Z0-9+-_.]+@[a-zA-Z]+\.[a-z.]+$', email))
#        def validate_password(password):
#            return len(password) > 5
#        def validate_phone_number(phone_number):
#            return bool(re.search('^[0-9]{3}-[0-9]{3,4}-[0-9]{4}$', phone_number))
#        if validate_email(data['email']) == False:
#            return JsonResponse({'message':'INVALID_MAIL'}, status = 400)
#        if validate_password(data['password']) == False:
#            return JsonResponse({'message':'INVALID_PASSWORD'}, status = 400)
#        if validate_phone_number(data['phone_number']) == False:
#            return JsonResponse({'meesage':'INVALID_PHONE_NUMBER'}, status = 400)
#        if data['username'] == data['password']:
#            return JsonResponse({'message':'INVALID_INPUT'}, status=400)

        if not validate_email(data['email']):
            return JsonResponse({'message':'INVALID_MAIL'}, status = 400)
        if not validate_password(data['password']):
            return JsonResponse({'message':'INVALID_PASSWORD'}, status = 400)
        if not validate_phone_number(data['phone_number']):
            return JsonResponse({'message':'INVALID_PHONE_NUMBER'}, status = 400)
        try:
            if User.objects.filter(Q(username= data['username']) | Q(email = data['email']) | Q(phone_number = data['phone_number'])):
                return JsonResponse({'message': 'USER ALREADY EXIST'}, status = 400)

 #            if User.objects.filter(username = data['username']).exists():
 #                return JsonResponse({'message':'username already exists!'}, status = 400)
 #            elif User.objects.filter(email = data['email']).exists():
 #                return JsonResponse({'message':'email already exists!'}, status = 400)
 #            elif User.objects.filter(phone_number = data['phone_number']).exists():
 #                return JsonResponse({'message':'phone_number already exists!'})

            password        = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cryped_password = hashed_password.decode('utf-8')

            User.objects.create(
                username = data['username'],
                email = data['email'],
                password=cryped_password,
                phone_number = data['phone_number'])
            return JsonResponse({'message':'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'meesge':'KEY_ERROR'}, status =400)

class LogIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.filter(Q(username = data['key']) | Q(email = data['key']) | Q(phone_number = data['key']))

 #            if User.objects.filter(username = data['key']).exists():
 #                user = User.objects.get(username = data['key'])
 #            elif User.objects.filter(email = data['key']).exists():
 #                user = User.objects.get(email = data['key'])
 #            elif User.objects.filter(phone_number = data['key']).exists():
 #                user = User.objects.get(phone_number = data['key'])

            # decryped user password and compare with database
            if bcrypt.checkpw(data['password'].encode('utf-8'), user[0].password.encode('utf-8')):
                # if Ture, issue JWT token
                secret       = my_settings.SECRET_KEY
                token        = jwt.encode({'id' : user[0].id}, secret, my_settings.ALGORITHM)
                access_token = token.decode('utf-8')
                return JsonResponse({'access_token':access_token}, status = 200)
            return JsonResponse({'meesage':'INVALID_PASSWORD'}, status = 400)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)
        except UnboundLocalError:
            return JsonResponse({'message':'INVALID_USER'}, status = 400)
