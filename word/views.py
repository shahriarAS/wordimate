from django.shortcuts import render, redirect
from django.http import HttpResponse
from word.models import Word
from word.forms import AddForm
from django.contrib import messages

def Home(request):
	if request.GET.get("q"):
		q = request.GET.get("q")
		all_word = Word.objects.filter(main_word__contains=q)
		temp = "Search"
	else:
		all_word = Word.objects.all()
		temp = "List"
		q = None

	return render(request, "index.html", {"all_word":all_word, "temp":temp, "q":q})

def AddNew(request):
	form = AddForm(request.GET)
	if form.is_valid():
		cd = form.cleaned_data
		try:
			Word.objects.get(main_word = cd["main_word"])
			return HttpResponse("Already Added")
		except:
			new_word = Word.objects.create(main_word = cd["main_word"], mean_word = cd["mean_word"])
			new_word.save()
			messages.success(request, "Successfully Added A Word!!")
			return redirect("Home")

	return render(request, "add.html", {"form":form})