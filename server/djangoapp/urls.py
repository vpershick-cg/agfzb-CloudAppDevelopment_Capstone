from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # about
    path(route='about/', view=views.about, name='about'),
    # contact us
    path(route='contact/', view=views.contact, name='contact'),
    # registration
    path(route='registration/', view=views.registration_request, name='registration'),
    # login
    path(route='login/', view=views.login_request, name='login'),
    # logout
    path(route='logout/', view=views.logout_request, name='logout'),
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)