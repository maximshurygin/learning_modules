from django.urls import path
from modules.apps import ModulesConfig

from modules.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView

app_name = ModulesConfig.name

urlpatterns = [
    path('', ModuleListAPIView.as_view(), name='module_list'),
    path('create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module_retrieve'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module_delete'),
]
