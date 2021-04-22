from django.shortcuts import render
from CRUD.models import Restaurant


def index(request):
    return render(request, "index.html")


def restOP(request):
    if request.method == "GET":
        button = request.GET["b1"]
        if button == "Insert":
            dish = request.GET["dish"]
            date_val = request.GET["date_stamp"]
            dish_type = request.GET["food"]
            cuisine = request.GET["opt_val"]
            try:
                seasonal = request.GET["info1"]
            except:
                seasonal = 0
            try:
                allergy = request.GET["info2"]
            except:
                allergy = 0
            try:
                advance = request.GET["info3"]
            except:
                advance = 0
            img = request.GET["img"]
            comm = request.GET["comment"]
            e = Restaurant.objects.create(
                dish_name=dish,
                date=date_val,
                dish_type=dish_type,
                cuisine=cuisine,
                seasonal=seasonal,
                allergens=allergy,
                advance=advance,
                img=img,
                comments=comm,
            )
            msg = "Record Saved"
            return render(request, "result.html", {"msg": msg})

        elif button == "Select":
            id = request.GET["id"]
            obj = Restaurant.objects.get(pk=id)
            return render(request, "result.html", {"obj": obj})

        elif button == "Update":
            id = request.GET["id"]
            dish = request.GET["dish"]
            date_val = request.GET["date_stamp"]
            dish_type = request.GET["food"]
            cuisine = request.GET["opt_val"]
            seasonal = request.GET["info1"]
            allergy = request.GET["info2"]
            advance = request.GET["info3"]
            img = request.FILES["img"]
            comm = request.GET["comment"]
            obj = Restaurant.objects.get(pk=id)
            obj.dish_name = dish
            obj.date = date_val
            obj.dish_type = dish_type
            obj.cuisine = cuisine
            obj.seasonal = seasonal
            obj.allergens = allergy
            obj.advance = advance
            obj.img = img
            obj.comments = comm
            obj.save()
            msg = "Updated"
            return render(request, "result.html", {"msg": msg})

        elif button == "Delete":
            id = request.GET["id"]
            obj = Restaurant.objects.get(pk=id)
            obj.delete()
            msg = "Deleted"
            return render(request, "result.html", {"msg": msg})
