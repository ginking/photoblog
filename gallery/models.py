#-*- coding: utf-8 -*-
from django.db.models import *
from datetime import date
from thumbs import ImageWithThumbsField

class Albums(Model):
    name = CharField(max_length=30, blank=True, null=True, editable=True, help_text=u"альбом", verbose_name=u"название альбома")
    about = TextField(blank=True, null=True, editable=True, help_text=u"о альбоме", verbose_name=u"информация о альбоме")
    photo = ForeignKey('Photos', verbose_name=u"фотография альбома", null=True, blank=True)
    created = DateTimeField(auto_now=True, auto_now_add=True, editable=False, verbose_name=u"дата создания")
    last_edit = DateTimeField(auto_now=True, auto_now_add=True, editable=False, verbose_name=u"дата последнего редактировния")
    hidden = BooleanField(editable=True, default=False, verbose_name=u"скрытый альбом")

    def __unicode__(self, *args, **kwargs):
        return self.name

    class Meta:
        verbose_name = u'альбом'
        verbose_name_plural = u'альбомы'

class Photos(Model):
    name = CharField(max_length=30, blank=True, null=True, editable=True, help_text=u"название", verbose_name=u"название фотографии")
    album = ForeignKey(Albums, verbose_name=u"альбом")
    image = ImageWithThumbsField(upload_to='photos/', blank=False, null=False, sizes=((160, 120),(312,398)))
    content = TextField(blank=True, null=True, editable=True, help_text=u"описание")
    created = DateTimeField(auto_now=True, auto_now_add=True, editable=False, verbose_name=u"дата создания")
    like = IntegerField(blank=True, null=True, default=0, editable=True, verbose_name=u"понравилось")
    not_like = IntegerField(blank=True, null=True, default=0, editable=True, verbose_name=u"не понравилось")

    def save(self):
        for field in self._meta.fields:
            if 'image' in field.name: field.upload_to = 'photos/%s/' % (date.today().strftime("%Y-%m-%d"))
        super(Photos, self).save()

    def __unicode__(self, *args, **kwargs):
        return self.name

    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
