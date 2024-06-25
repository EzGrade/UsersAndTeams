from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from team_management.models import Team, UserProfile
from team_management.serializers import UserSerializer, TeamSerializer


class GetUserView(APIView):
    def get(self, request, pk: int):
        user = UserProfile.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: UserSerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetTeamView(APIView):
    def get(self, request, pk: int):
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)


class TeamView(APIView):

    @swagger_auto_schema(
        request_body=TeamSerializer,
        responses={
            201: TeamSerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        request_body=TeamSerializer,
        responses={
            201: TeamSerializer,
            400: 'Bad Request'
        }
    )
    def put(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team_pk = request.data.pop('pk')
            team = Team.objects.get(pk=team_pk)
            updated_team = serializer.update(team, request.data)
            serializer = TeamSerializer(updated_team)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
