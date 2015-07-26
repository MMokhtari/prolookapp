# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# class JSONResponse(HttpResponse):

#     """
#     An HttpResponse that renders its content into JSON.
#     """

#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application / json'
#         super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# @api_view(['GET', 'POST']) # for function
class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self,request,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        #return JSONResponse(serializer.data)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JSONResponse(serializer.data, status=201)
        # return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self,request, pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    def put(self,request, pk,format=None):
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(snippet, data=data)
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, pk,format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
