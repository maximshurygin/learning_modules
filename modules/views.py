from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.models import Module
from modules.paginators import ModulePaginator
from modules.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """Контроллер создания модуля"""
    serializer_class = ModuleSerializer


class ModuleListAPIView(generics.ListAPIView):
    """Контроллер просмотра списка модулей"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulePaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер просмотра модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """Контроллер обновления модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """Контроллер удаления модуля"""
    queryset = Module.objects.all()


class HomepageView(APIView):
    """Контроллер главной страницы"""

    def get(self, request):
        return Response({'message': 'Добро пожаловать на главную страницу!'},
                        status=status.HTTP_200_OK)
