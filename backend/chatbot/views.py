from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from chatbot.models_data import DbUploader


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    print('############ 1 ##########')
    DbUploader().insert_data()
    return JsonResponse({'Chatbot Data Upload': 'SUCCESS'})
