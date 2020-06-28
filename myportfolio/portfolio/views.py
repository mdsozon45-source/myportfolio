from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class IndexView(View):

	def get(self, request):
		context = {}
		return render(request, 'index.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'index.html', context)