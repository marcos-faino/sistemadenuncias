from django.contrib import admin
from .models import Denuncia


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', '_autor', 'criacao']
    exclude = ['autor']

    def _autor(self, instance):
        return instance.autor.get_full_name()

    def get_queryset(self, request):
        qs = super(DenunciaAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
