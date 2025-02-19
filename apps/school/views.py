from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from apps.account.models import User
from django.contrib.auth.hashers import make_password
from .forms import SchoolSignupForm
from .models import School


# Create your views here.
def HomepageView(request):
    # if request.subdomain:
    #     return render(request, 'dashboard.html')
    return render(request, 'homepage.html')


def RegisterView(request):
    if request.method == "POST":
        form = SchoolSignupForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the school without the admin yet.
            school = form.save(commit=False)
            school.save()
            print(school.slug)
            # Create the admin user for this school.
            admin_email = form.cleaned_data.get('admin_email')
            admin_password = form.cleaned_data.get('admin_password')
            # Use the school's slug as the username
            admin_user = User.objects.create(
                username=school.slug,
                email=admin_email,
                name=school.name,
                password=make_password(admin_password),
                role = 'admin',
                is_staff=True, 
                is_superuser=False
            )
            school.admin = admin_user
            school.save()

            # Redirect to the school’s subdomain.
            # Assuming your subdomain URL is constructed as: https://<school_slug>.schoolsphere.com/dashboard/
            subdomain_url = f"http://{school.slug}.lvh.me:8000"
            return redirect(subdomain_url)
    else:
        form = SchoolSignupForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    # Assume the subdomain is the school's slug.
    subdomain = request.subdomain
    # Retrieve the school based on the subdomain.
    school = get_object_or_404(School, slug=subdomain)
    return render(request, 'schools/dashboard.html', {'school': school})