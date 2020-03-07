from django.shortcuts import render, HttpResponse

# Create your views here.


# function to render html template.
def get_todo_list(request):
    return render(request, "todo_list.html")
