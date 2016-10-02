from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CodeCompileSerializer
from .models import CodeCompile


class CompileView(generics.ListCreateAPIView):
    serializer_class = CodeCompileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CodeCompile.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.validated_data['user'] = current_user
        serializer.save()
