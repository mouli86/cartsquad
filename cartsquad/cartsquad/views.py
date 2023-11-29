from django.shortcuts import render, redirect

def index(request):
	#To capture search query 
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    return render(request, 'homepage.html')

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)


