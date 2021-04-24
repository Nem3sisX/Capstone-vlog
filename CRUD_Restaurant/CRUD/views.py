from django.shortcuts import render
from CRUD.models import Restaurant
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View


class index(TemplateView):
    template_name = "index.html"


class restOP(View):
    def post(self, request):
        button = request.POST["b1"]
        if button == "Insert":
            dish = request.POST["dish"]
            date_val = request.POST["date_stamp"]
            qty = request.POST["qty"]
            price = request.POST["price"]
            dish_type = request.POST["food"]
            cuisine = request.POST["opt_val"]
            try:
                seasonal = request.POST["info1"]
            except:
                seasonal = 0
            try:
                allergy = request.POST["info2"]
            except:
                allergy = 0
            try:
                advance = request.POST["info3"]
            except:
                advance = 0
            img = request.FILES["img"]
            comm = request.POST["comment"]
            e = Restaurant.objects.create(
                dish_name=dish,
                date=date_val,
                qty=qty,
                price=price,
                dish_type=dish_type,
                cuisine=cuisine,
                seasonal=seasonal,
                allergens=allergy,
                advance=advance,
                img=img,
                comments=comm,
            )
            return HttpResponse("<h1> Record Saved</h1>")

        elif button == "Select":
            id = request.POST["id"]
            obj = Restaurant.objects.get(pk=id)
            return render(request, "result.html", {"obj": obj})

        elif button == "Update":
            id = request.POST["id"]
            dish = request.POST["dish"]
            date_val = request.POST["date_stamp"]
            qty = request.POST["qty"]
            price = request.POST["price"]
            dish_type = request.POST["food"]
            cuisine = request.POST["opt_val"]
            try:
                seasonal = request.POST["info1"]
            except:
                seasonal = 0
            try:
                allergy = request.POST["info2"]
            except:
                allergy = 0
            try:
                advance = request.POST["info3"]
            except:
                advance = 0
            img = request.FILES["img"]
            comm = request.POST["comment"]
            obj = Restaurant.objects.get(pk=id)
            obj.dish_name = dish
            obj.date = date_val
            obj.qty = qty
            obj.price = qty
            obj.dish_type = dish_type
            obj.cuisine = cuisine
            obj.seasonal = seasonal
            obj.allergens = allergy
            obj.advance = advance
            obj.img = img
            obj.comments = comm
            obj.save()
            msg = "Updated"
            return HttpResponse("<h1> Record Updated </h1>")

        elif button == "Delete":
            id = request.POST["id"]
            obj = Restaurant.objects.get(pk=id)
            obj.delete()
            msg = "Deleted"
            return HttpResponse("<h1> Record Deleted</h1>")
