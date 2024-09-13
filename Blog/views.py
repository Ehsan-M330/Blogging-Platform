from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreatePostSerializer, UpdatePostSerializer, GetPostSerializer
from rest_framework import status
from .models import Post

# Create your views here.


@api_view(["POST", "GET"])
def create_post(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = GetPostSerializer(posts, many=True)  # Serialize all posts
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )  # Return all posts with 200 OK status

    elif request.method == "POST":
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # Return created post with 201 Created status
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # Return errors with 400 Bad Request status


@api_view(["PUT", "DELETE"])
def update_post(request, id: int):
    try:
        # Assuming `Post` is your model and you want to update an existing post
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = UpdatePostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )  # Success status code
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # Validation error status code

    elif request.method == "DELETE":
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )  # No content status code after deletion
