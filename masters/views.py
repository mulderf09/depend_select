from django.shortcuts import render
from .models import SubCategory, Category
from django.http import HttpResponse
import json

def get_subcategory(request):
    id = request.GET.get('id', '1')
    print(f"id: {id}")
    desc = {'desc':'Ricky Baratan'}
    result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
    result.append(desc)
    return HttpResponse(json.dumps(result), content_type="application/json")