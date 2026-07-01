


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Project,
    Task,
    Comment,
    Attachment,
    TaskHistory
)

from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer,
    AttachmentSerializer,
    TaskHistorySerializer
)


class CreateProject(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)


class CreateTask(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class UpdateStatus(APIView):
    def patch(self, request, pk):
        task = Task.objects.get(id=pk)

        old_status = task.status
        new_status = request.data["status"]

        task.status = new_status
        task.save()

        TaskHistory.objects.create(
            task=task,
            action=f"Status changed from {old_status} to {new_status}"
        )

        return Response({
            "message": "Status Updated Successfully"
        })


class AddComment(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)


class UploadAttachment(APIView):
    def post(self, request):
        serializer = AttachmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class TaskHistoryList(APIView):
    def get(self, request):
        history = TaskHistory.objects.all().order_by("-changed_at")
        serializer = TaskHistorySerializer(history, many=True)
        return Response(serializer.data)