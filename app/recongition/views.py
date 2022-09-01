from django.shortcuts import render
# from app.recongition import serializers
from recongition.facedetect import facedetect
from recongition.forms import recognitions_Form
from PIL import Image
import numpy as np
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
# 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action,api_view
from rest_framework import mixins
from recongition.models import *
from recongition.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.parsers import FormParser, MultiPartParser

FACEDECTER = facedetect()
# Create your views here.

class CreateViewSet(mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
        pass

class recognitionViewSet(viewsets.GenericViewSet):
    queryset = face.objects.all()
    serializer_class = faceSerializer
    # permission_classes = [IsAuthenticated,]
    parser_classes = (FormParser, MultiPartParser)

    # @swagger_auto_schema(
    #     operation_summary='我是 POST 的摘要',
    #     operation_description='我是 POST 的說明',
    #     manual_parameters=[
    #        openapi.Parameter(
    #            name='image',
    #            in_=openapi.IN_FORM,
    #            description='Image',
    #            type=openapi.TYPE_FILE
    #        ),
    #    ]
    # )

    @action(detail = False, methods = ['post'],name ='face')
    def face(self,request,*args,**kwargs):
        # return self.create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # print(serializer.data)
        
        form = recognitions_Form(request.POST,request.FILES)
        # print(request.POST)
        print(form.is_valid())
        # print(request)
        # print(request.POST)
        # print(request.FILES)
        # print(form.is_valid())
        # if form.is_valid():
            # form.save()
        # print(request.FILES)
        # print(form.cleaned_data)
        img = request.FILES['img']
        # img = form.cleaned_data['img']
        # print(img)
        img = Image.open(img)
        img = np.array(img)
        # print(img)
        # img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            # return HttpResponse('something error')
            print("error")
        faces = FACEDECTER.recognition(img)
        # print(faces)
        # facelist, boxes =  face.DetectFace(img)
        # feature = face.GetFeture(facelist=facelist)
        # if feature is None:
        #     return HttpResponse("can not get face")
        # print(faces)
        # resaults = list()
        # for face in faces:
        #     resault = dict()
        #     resault['bbox'] = face['bbox']
        #     resault['kps'] = face['kps']
        #     resault['embedding'] = face['embedding']
        #     resaults.append(resault)
        # print(resaults)
        # data = {
        #     'data':faces
        #     # 'boxes':boxes.tolist(),
        #     # 'feature':feature.tolist()
        # }
        print(faces)
        return Response(faces,status = 201)
    # if request.methods == 'POST':
            

    #     return render(request,'recognition.html',{'form':form})
    
    # def create(self,request, *args, **kwargs):
    #     print("123")


    # def post(self, request, *args, **kwargs):
    #     print("123")
    #     return self.create(request, *args, **kwargs)
    # def create(self,request,*args,**kwargs):
    #     print('123')
    #     serializer = self.get_serializer(data=request.data)
    #     super().create(request,*args,**kwargs)

# class test_views(generics.GenericAPIView):

#     def post(self, request, *args, **krgs):
#         pass

# class UsersView(generics.GenericAPIView):
#     serializer_class = faceSerializer
#     @swagger_auto_schema(
#         operation_summary='我是 GET 的摘要',
#         operation_description='我是 GET 的說明',
#     )
#     def get(self, request, *args, **krgs):
#         pass
#     @swagger_auto_schema(
#         operation_summary='我是 POST 的摘要',
#         operation_description='我是 POST 的說明',
#     )
#     def post(self, request, *args, **krgs):
#         pass