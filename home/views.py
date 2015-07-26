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
from home.models import Visitor
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response
from django.template import RequestContext

# okay lets get thing started
# first im going to make my views based on classes ' like they call them class based views'
# exept for the home page


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
# the Home page is alwayse rendered in html
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
def home(request, format=None):
    # The normal First page GET methode
    if request.method == 'GET':
        if request.user.is_authenticated():
            # redirect to his working page
            return redirect('/WorkPlace/')
        else:
                # if is not authenticated that means a new user lets dance a littel with'm
                # get and save this vistitor meta data  for further proccessing
            metadata = get_visitor_meta(request,'HTTP_USER_AGENT','HTTP_X_FORWARDED_FOR','HTTP_REFERER')
            visitor = Visitor(user_agent=metadata['HTTP_USER_AGENT'], ip=metadata['HTTP_X_FORWARDED_FOR'], refer=metadata['HTTP_REFERER'])
            # verify the Meta info for an bad info injection
            try:
                visitor.full_clean()
            except ValidationError as e:
                return HttpResponse("What you are doing man,No monkey business here !")

            visitor.save()
            content = {
                 'user':request.user.username,
                'title': 'ProLookApp'
            }
            # give'm the home page (latter on will be based on filters
            # (lunguage,location,time ...))
            return Response(content, template_name='./home/home.html')
    elif request.method == 'POST':
        return HttpResponse("Hello, world. You're at Home page")


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            # redirect to his working page
            return redirect('/WorkPlace/')
            # return HttpResponse("Hello  "+request.user.username+" this is your woking page soon !<br\><a href='logout/'>Logout</a>")
        else:
            content = {
                        'user': request.user,
                        'auth': request.auth,
                        'title':'ProLookApp Log In'
                    }
            return Response({'content': content}, template_name='./home/login.html')
    elif request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.access_granted:
                auth_login(request, user)
                # Redirect to a success page.
                content = {
                    'user': request.user.username,
                    'auth': request.auth,
                    'status': 'OK_LOGIN'
                }
                # return redirect('/WorkPlace/')
                return Response(content)
                # return HttpResponse("You are going to be directed to your woking page soon ! ")
            else:
                # Return a 'disabled account' error message 'access granted for
                # some raison
                content = {
                    'status': 'ACCESS_NOT_GRANTED'
                }
                # return redirect('/WorkPlace/')
                return Response(content)
        else:
            # Return an 'invalid login' error message.
            content = {'status': 'INVALID_LOGIN'}
            return Response(content)


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def logout(request):
    auth_logout(request)
    content = {
        'user': request.user,  # `django.contrib.auth.User` instance.
        'auth': request.auth  # None
    }
    # return Response(content, status=status.HTTP_200_OK)
    return redirect('/')


@api_view(['GET', 'POST'])
# @authentication_classes((BasicAuthentication))
# @permission_classes((IsAuthenticatedOrReadOnly ,))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            # redirect to his working page
            return redirect('/WorkPlace/')
        else:
            content = {
                'user': request.user.username,  # `django.contrib.auth.User` instance.
                'auth': request.auth,
                'title':'ProLookApp Sign Up'  # None
            }
            # return redirect('/')
            return Response({'content': content}, template_name='./home/register.html')

    # if post then this user passed his info lets save them
    elif request.method == 'POST':
        # serializer = AccountSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     content={
        #         'created':serializer.data,
        #         'status':'VALID_INFO'
        #     }
        #     user = authenticate(username=serializer.data.username, password=serializer.data.password)
        #     auth_login(request, user)
        #     return Response(content)
            
        # content={'status':'INVALID_INFO'}    
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('', status=status.HTTP_400_BAD_REQUEST)


def get_visitor_meta(request, *args):
    dic = {}
    for meta in args:
        if meta == 'HTTP_X_FORWARDED_FOR':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            dic[meta] = ip
            print(meta+' '+ip)
        else:
            meta_text = request.META.get(meta)
            if meta_text:
                print(meta+' '+meta_text)
                dic[meta] = meta_text
            else:
                dic[meta] = 'None'
    return dic

def handler404(request):
    response = render_to_response('./home/soon.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response


# def handler500(request):
#     response = render_to_response('./home/500.html', {},context_instance=RequestContext(request))
#     response.status_code = 500
#     return response