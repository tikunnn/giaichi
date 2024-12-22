from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict

# from .forms import GiaichiForm
from .models import Giaichi, TKno, YTno, Phongban, Nhanvien


# Create your views here.

class GiaiChiCreateView(View):
    model = Giaichi
    template_name = "giaichi_form.html"

    def get(self, request, *args, **kwargs):
        nhanvien = Nhanvien.objects.filter(id=1).first()
        context = {"nhanvien": nhanvien}
        return render(request, "giaichi_form.html", context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        nhanvien_instance = Nhanvien.objects.get(tennv=data.get("tennv"))
        valid_fields = {
            "nhanvien": nhanvien_instance,
            "hinhthucthanhtoan": data.get("hinhthucthanhtoan"),
            "motathanhtoan": data.get("motathanhtoan"),
            "tiengiaichi": data.get("tiengiaichi"),
            "giaichithuoc": data.get("giaichithuoccongty"),
            "ghichu": data.get("ghichu"),
            "tkno": data.get("tkno"),
            "ytno": data.get("ytno"),
            "guiduyet": data.get("guiduyet"),
            "tieude": data.get("tieude"),
            "vat": data.get("vat"),
            "noidungmota": data.get("editor"),
        }
        obj = self.model.objects.create(**valid_fields)
        return JsonResponse(
            {
                "status": "Success",
                "message": f"{self.model.__name__} created",
                "data": model_to_dict(obj),
            }
        )


class GiaichiUpdateView(View):
    model = Giaichi
    template_name = "giaichi_form.html"

    def post(self, request, *args, **kwargs):
        data = request.POST
        obj_id = kwargs.get("pk")
        try:
            obj = self.model.objects.get(id=obj_id)
            if obj:
                nhanvien_instance = Nhanvien.objects.get(tennv=data.get("tennv"))

                obj.nhanvien = nhanvien_instance
                obj.hinhthucthanhtoan = data.get("hinhthucthanhtoan")
                obj.motathanhtoan = data.get("motathanhtoan")
                obj.tiengiaichi = data.get("tiengiaichi")
                obj.giaichithuoc = data.get("giaichithuoccongty")
                obj.ghichu = data.get("ghichu")
                obj.tkno = data.get("tkno")
                obj.ytno = data.get("ytno")
                obj.guiduyet = data.get("guiduyet")
                obj.tieude = data.get("tieude")
                obj.vat = data.get("vat")
                obj.noidungmota = data.get("editor")
                obj.save()

                return JsonResponse(
                    {
                        "status": "Success",
                        "message": f"{self.model.__name__} updated",
                        "data": model_to_dict(obj),
                    }
                )
            return JsonResponse(
                {
                    "status": "Failed",
                    "message": f"Not found Giaichi with id: {obj_id}",
                }
            )
        except self.model.DoesNotExist:
            return JsonResponse(
                {"status": "Error", "message": f"{self.model.__name__} not found"},
                status=404,
            )


class GiaichiDeleteView(View):
    model = Giaichi
    template_name = "giaichi_form.html"

    def post(self, request, *args, **kwargs):
        obj_id = kwargs.get("pk")
        try:
            obj = self.model.objects.get(id=obj_id)
            obj.delete()
            return JsonResponse(
                {"status": "Success", "message": f"{self.model.__name__} deleted"}
            )
        except self.model.DoesNotExist:
            return JsonResponse(
                {"status": "Error", "message": f"{self.model.__name__} not found"},
                status=404,
            )
