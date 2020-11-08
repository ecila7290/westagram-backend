import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Post, User, Comment

class PostView(View):

    def get(self, request, *args, **kwargs):
        try:
            qs = Post.objects.all()
            post_dict = [{'author': post.author.username,
                          'title': post.title,
                          'content': post.content,
                          'image': post.image,
                          'post_created': str(post.post_created),
                          'id': post.id} for post in qs]
            context  = {'result': post_dict}
            return JsonResponse(context,  status = 200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

    def post(self, request):
        try:
            data = json.loads(request.body)
            if 'content' in data:
                Post.objects.create(author = User.objects.get(id=data['id']), title = data['title'], content = ['content'], image = data['image'])
                return JsonResponse({'message': 'POST HAS BEEN CREATED SUCCESSFULLY!'}, status = 201)
            Post.objects.create(author = User.objects.get(id=data['id']), title = data['title'], image = data['image'])
            return JsonResponse({'message': 'Post has been created successfully!'}, status = 201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)


    def put(self, request):
        try:
            data = json.loads(request.body)
            obj = Post.objects.get(id=data['id'])
            if 'title' in data:
                obj.title = data['title']
            if 'content' in data:
                obj.content = data['content']
            if 'image' in data:
                obj.image = data['image']
            obj.save()
            return JsonResponse({'message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

    def delete(self, request):
        try:
            data = json.loads(request.body)
            if Post.objects.filter(id = data['id']).exists():
               q = Post.objects.get(id = data['id'])
               q.delete()
               return JsonResponse({'message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)


class CommentView(View):

    def get(self, request):
        try:
            data = json.loads(request.body)
            if 'post_id' in data:
                qs = Comment.objects.filter(post_id = data['post_id'])
                context = [{'feed_id': cmt.post_id.id,
                            'author': cmt.author.username,
                            'content': cmt.content,
                            'created_time': cmt.comment_created} for cmt in qs]
                return JsonResponse({'result':context}, status = 200)
        except KeyError:
            JsonResponse({'message':'nope'}, status = 400)

    def post(self, request):
        try:
            data = json.loads(request.body)
            Comment.objects.create(author = User.objects.get(id=data['user_id']), post_id = Post.objects.get(id = data['post_id']), content = data['content'])
            return JsonResponse({'meesage':'SUCCESS'}, status = 200)
        except KeyError:
            JsonResponse({'message':'KEY_ERROR'}, status = 400)

    def put(self, request):
        try:
            data = json.loads(request.body)
            if Comment.objects.filter(id=data['id']).exists():
                q = Comment.objects.get(id=data['id'])
                q.content = data['content']
                q.save()
                return JsonResponse({'message':'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'meesage':'KEY_ERROR'}, status = 400)
    def delete(self, request):
        try:
            data = json.loads(request.body)
            if Comment.objects.filter(id=data['id']).exists():
                q = Comment.objects.get(id=data['id'])
                q.delete()
                return JsonResponse({'message':'cmt, success'}, status = 200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 200)
