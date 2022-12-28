from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from django.core.files import File
from rest_framework import viewsets, generics, mixins
from .serializers import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .utils import predict
from django.conf import settings
from rest_framework.response import Response
import os

class ImageUploadViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):

        # data = request.FILES

        # image = data['image']
        # print("----------------------------------->")
        # print(type(image))
        # print(image.name)
        # print("----------##########---------------------->")

        # # url = settings.MEDIA_URL + < upload_to > + request.FILES['file'].name


        data = request.FILES['image'] # or self.files['image'] in your form
        n = f"tmp.{data.name.split('.')[-1]}"
        
        path = default_storage.save(n, ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        texte = predict.predict(tmp_file)


        td = Traduction.objects.create(
            texte = texte,
            image = data
        )

        td.save()
        return Response(data=TraductionSerializer(td).data, status=200)