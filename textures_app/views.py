from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from textures_app.services import generate512x512


class GeneratedImagesViewSet(ViewSet):
    def create(self, request):
        prompt = request.POST.get("prompt")
        negative_prompt = request.POST.get("negative_prompt")
        seed = request.POST.get("seed")
        num_samples = request.POST.get("num_samples")

        images = generate512x512(prompt=prompt, negative_prompt=negative_prompt, seed=seed, num_samples=num_samples)
        return Response()
