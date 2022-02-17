from django.shortcuts import render
from .models import PassSave


def manager(request):
    if request.method == "POST":
        title = request.POST.get("title")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = PassSave(title=title, email=email, password=password)
        data.save()
    data = PassSave.objects.all()
    query = request.GET.get("query")
    if query:
        query = PassSave.objects.filter(title__contains=query)
    query_data = query
    return render(request, 'index.html', {"data":data,
                                        "query_data":query_data})