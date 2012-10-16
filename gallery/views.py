# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response as render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from gallery.models import *
from django.shortcuts import redirect

def main(request, *args, **kwargs):
    photos = Photos.objects.all()
    dic = {'photo': photos[0], 'photos': photos}
    dic['img_urls'] = ",".join(["%s: '%s'" % (i.id, i.image.url_312x398) for i in Photos.objects.order_by('id')])
    dic['imgs_id'] = [i['id'] for i in Photos.objects.order_by('id').values('id')].__str__()
    return render('base.html', dic)

def browser(request, *args, **kwargs):
    dic = {'photos': Photos.objects.all()}
    return render('browser.html', dic)

def photo(request, img_id, *args, **kwargs):
    try: photo = Photos.objects.get(id=img_id)
    except: return redirect('/gallery/')
    ids = list(Photos.objects.values_list("id", flat=True))
    current_idx = ids.index(photo.id)
    prev_page = Photos.objects.get(id=ids[current_idx-1])
    try: next_page = Photos.objects.get(id=ids[current_idx+1])
    except: next_page = Photos.objects.get(id=ids[0])
    dic = {'photo': photo, 'photos': Photos.objects.all()}
    dic['img_urls'] = ",".join(["%s: '%s'" % (i.id, i.image.url_312x398) for i in Photos.objects.order_by('id')])
    dic['imgs_id'] = [i['id'] for i in Photos.objects.order_by('id').values('id')].__str__()
    return render('base.html', dic)

def title_by_id(request, img_id, *args, **kwargs):
    try:
        photo = Photos.objects.get(id=img_id)
        title = photo.name
    except: title = ''
    return HttpResponse(title, mimetype="text/plain")

def content_by_id(request, img_id, *args, **kwargs):
    try:
        photo = Photos.objects.get(id=img_id)
        content = photo.content
    except: content = ''
    return HttpResponse(content, mimetype="text/plain")
