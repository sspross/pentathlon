from django.contrib.auth import logout, login as auth_login
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, CreateView, RedirectView
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404

from event.models import Team, Event, Participation
from pentathlon.forms import ParticipationForm

class CreateTeamView(CreateView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

    def get_success_url(self):
        return '/team/%s/' % self.object.pk

class CreateParticipationView(CreateView):
    model = Participation
    form_class = ParticipationForm
    team = None

    def dispatch(self, request, *args, **kwargs):
        self.team = get_object_or_404(Team.objects.all(), pk=kwargs['pk'])
        return super(CreateParticipationView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class(team=self.team, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(CreateParticipationView, self).get_context_data(**kwargs)
        context['team'] = self.team
        return context

    def get_success_url(self):
        return '/team/%s/' % self.team.pk
