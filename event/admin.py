from django.contrib import admin

from equipment.models import GiantSlalomEquipment, JumpEquipment
from event.models import Event, Participation, Player, Team


class GiantSlalomEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'multiplier',)
    search_fields = ('name', 'multiplier',)


admin.site.register(GiantSlalomEquipment, GiantSlalomEquipmentAdmin)


class JumpEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'multiplier',)
    search_fields = ('name', 'multiplier',)


admin.site.register(JumpEquipment, JumpEquipmentAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'birthdate', 'email')
    search_fields = ('firstname', 'lastname', 'gender', 'birthdate', 'email')
    list_filter = ('gender',)


admin.site.register(Player, PlayerAdmin)


class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'event',)
    search_fields = ('name',)
    list_filter = ('event',)
    inlines = (ParticipationInline,)


admin.site.register(Team, TeamAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date',)
    search_fields = ('name', 'start_date',)


admin.site.register(Event, EventAdmin)




