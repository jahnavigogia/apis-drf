from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class AgentListCreateView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({}, status=status.HTTP_201_CREATED)


class AgentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignResultListCreateView(generics.ListCreateAPIView):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer


class CampaignResultRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
