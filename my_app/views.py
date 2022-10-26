from django.shortcuts import render
from datetime import date
from my_app.models import Member
from django.http import HttpResponse

def members(request):
    members = Member.objects.all()

    context_dict = {"members": members}
    
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/member_list.html",
        
    )
    

