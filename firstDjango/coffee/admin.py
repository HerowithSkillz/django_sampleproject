from django.contrib import admin
from .models import CoffeeVariety, CoffeeReview, Store, CoffeeCertification

# Register your models here.
class CoffeeReviewInline(admin.TabularInline):
    model = CoffeeReview
    extra = 2

class CoffeeVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CoffeeReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('coffee_varieties',)

class CoffeeCertificationAdmin(admin.ModelAdmin):
    list_display = ('coffee', 'certification_number') 


admin.site.register(CoffeeVariety, CoffeeVarietyAdmin)
admin.site.register(CoffeeReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(CoffeeCertification, CoffeeCertificationAdmin)
