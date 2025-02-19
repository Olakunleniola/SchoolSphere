from django.shortcuts import render, get_object_or_404, redirect
from apps.school.models import School

# Create your views here.
def dashboard(request):
    if request.subdomain:
        print(request.subdomain)
        # Assume the subdomain middleware has set request.subdomain
        school = get_object_or_404(School, slug=request.subdomain)
        return render(request, 'dashboard.html', {'school': school})
    return redirect('home')