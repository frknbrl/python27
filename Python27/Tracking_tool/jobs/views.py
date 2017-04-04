from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'jobs/post_list.html', {})
	
def index(request):
    return render(request, 'jobs/index.html', {})

def yeni2(request):
    return render(request, 'jobs/yeni2.html', {})