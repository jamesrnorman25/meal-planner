from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def new_recipe(request):
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        pass
    

    return render(request, "new_recipe.html")
