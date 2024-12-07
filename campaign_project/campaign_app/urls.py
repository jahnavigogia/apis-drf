from django.urls import path
from . import views

urlpatterns = [
    path('agents/', views.AgentListCreateView.as_view(), name='agent-list-create'),
    path('agents/<int:pk>/', views.AgentRetrieveUpdateDeleteView.as_view(), name='agent-detail'),
    path('campaigns/', views.CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('campaigns/<int:pk>/', views.CampaignRetrieveUpdateDeleteView.as_view(), name='campaign-detail'),
    path('campaign-results/', views.CampaignResultListCreateView.as_view(), name='campaign-result-list-create'),
    path('campaign-results/<int:pk>/', views.CampaignResultRetrieveUpdateDeleteView.as_view(), name='campaign-result-detail'),
]
