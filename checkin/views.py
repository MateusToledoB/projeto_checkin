from django.shortcuts import render

def checkin(request):
    return render(request, 'checkin/checkin.html')
