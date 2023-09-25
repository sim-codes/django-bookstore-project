from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paystack_key'] = settings.PAYSTACK_TEST_KEY
        return context


def charge(request):

    perimission = Permission.objects.get(codename='special_status')
    u = request.user
    u.user_permissions.add(perimission)
    return render(request, 'orders/charge.html')