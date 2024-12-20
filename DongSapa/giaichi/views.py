from django.shortcuts import get_object_or_404, render, redirect
from .forms import GiaichiForm
from .models import Giaichi, TKno, YTno, Phongban

# Create your views here.


def giaichi_form(request):
    if request.method == 'POST':
        form = GiaichiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GiaichiForm()

    return render(request, 'giaichi_form.html', {'form': form})


def giaichi_form_view(request, giaichi_id):
    giaichi = Giaichi.objects.filter(username=request.user).first()
    nhanvien = giaichi.nhanvien
    tknos = TKno.objects.all()
    ytnos = YTno.objects.all()
    phongban_list = Phongban.objects.all()

    context = {
        'giaichi': giaichi,
        'nhanvien': nhanvien,
        'tknos': tknos,
        'ytnos': ytnos,
    }

    context = {
        'phongban_list': phongban_list,
        'giaichi': giaichi,
    }
    return render(request, 'giaichi_form.html', context)


def phongban_view(request):
    phongban_list = Phongban.objects.all()
    return render(request, 'giaichi_form.html', {'phongban_list': phongban_list})
