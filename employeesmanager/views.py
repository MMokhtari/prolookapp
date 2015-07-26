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
from rest_framework import status
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
# Create your views here.


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
# the Home page is alwayse rendered in html
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
def employeesmanager(request, format=None):
    # The normal First page GET methode
    if request.method == 'GET':
        if not request.user.is_authenticated():
            # redirect to his working page
            return redirect('/login/')
        else:
            # okay we verify that this user is admin 
            user = request.user
            if user.is_admin:
                try:
                    company = user.company()[0];
                except Exception:
                    company = "no company yet"
               
                content = {
                     'user':request.user,
                    'title': 'Company Manager',
                    'company':company,
                }
                return Response(content, template_name='./employeesmanager/employeesmanager_base.html')
            else:
                # kick his ass
                return redirect('/WorkPlace/')
    elif request.method == 'POST':
        return HttpResponse("Hello, world. You're at Home page")
