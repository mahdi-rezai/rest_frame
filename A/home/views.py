from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person,Question,Answer
from .serialiazers import PersonSerializers,QuestionSerializer,AnswerSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework import generics


class Home(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        person = Person.objects.all()
        ser_data = PersonSerializers(instance=person,many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)


class QuestionListView(APIView):
    throttle_scope = 'questions'
    def get(self,request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions,many=True)
        return Response(srz_data.data)


class QuestionCreateView(APIView):
    """
    THIS CREAT NEW QUESTION
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self,request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)



class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        question.delete()
        return Response({'messages':'question delete'},status=status.HTTP_200_OK)





