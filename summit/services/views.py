from django.shortcuts import render, redirect, get_object_or_404
from .models import Service

# Create your views here.

def services_index(request):
    services = Service.objects
    return render(request, 'services/services_index.html', {'services': services})


def service_detail(request, service_id, slug):
    service = get_object_or_404(Service, pk = service_id)
      # Redirect if the slug does not match
    if slug != service.slug():
        return redirect(service, permanent=True)
    return render(request, 'services/service_details.html', {
        'service': service,
    })
