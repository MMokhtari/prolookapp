from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from AuthAccount.models import Account
from AuthAccount.serializers import AccountSerializer
from rest_framework import status
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from subdomains.utils import reverse
# okay lets get thing started
# first im going to make my views based on classes ' like they call them class based views'
# exept for the workplace page


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
# the workplace page is alwayse rendered in html
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
def workplace(request, format=None):
    # The normal First page GET methode
    if request.method == 'GET':
        if request.user.is_authenticated():
            user = request.user
            company = user.company_set.all()
            print('user.username')
            print(user.username)
            content={
            'user':request.user.username,
            'auth':request.auth,
            'title':'Work Place'
            }
            # reverse('home', subdomain='api')
            return Response(content,template_name="./workplace/workplace_base.html")
        else:
        	#redirect to home page
            return redirect('/')
    elif request.method == 'POST':
        return HttpResponse("Hello, world. You're at workplace page")