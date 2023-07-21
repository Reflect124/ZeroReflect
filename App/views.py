from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from App.models import Carousel, About, Bolg, ClientProfile, Service, Footer
from .forms import ContactForms
# Create your views here.
def home(request):
    carouselData = Carousel.objects.all()
    aboutData = About.objects.all()[:1]
    blogData = Bolg.objects.all()[:3]
    serviceData = Service.objects.all()[:3]
    clientProfileData = ClientProfile.objects.all()
    footerData = Footer.objects.all()
    context = {
        "carousels": carouselData,
        "abouts": aboutData,
        'blogs': blogData,
        'clients': clientProfileData,
        'services': serviceData,
        'footers': footerData,
    }
    return render(request, 'Home/index.html', context)


def category(request):
    return render(request, 'Home/category.html')


def about(request):
    #aboutData = About.objects.get(id=post_id)
    aboutData = About.objects.all()
    footerData = Footer.objects.all()
    context ={
        'about':aboutData,
        'footers': footerData,
    }
    return render(request, 'Home/about.html',context)


def contact(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            html = render_to_string('gmail/contactForm.html',
                                    {
                                        'name': name,
                                        'phone': phone,
                                        'email': email,
                                        'comment': comment,
                                    })
            send_mail('The contact form ZeroReflect', 'This is the message', 'zeroreflect124@gmail.com',
                      ['admin@zeroreflect.com'], html_message=html)
            return redirect('index')

    else:
        form = ContactForms()


    footerData = Footer.objects.all()
    context = {
        'footers': footerData,
        'form': form,
    }
    return render(request, 'Home/contact.html',context)

def postDetails(request, post_id):
    blogData = get_object_or_404(Bolg,pk=post_id)
    footerData = Footer.objects.all()

    context ={
        'blog':blogData,
        'footers': footerData,
    }
    return render(request, 'Home/postDetails.html', context)
