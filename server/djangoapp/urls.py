from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='about/', view=views.about, name='about'),

    # path for contact us view
    path(route='contact/', view=views.contact, name='contact'),

    # path for registration
    path(route='signuppage/', view=views.signuppage, name='signuppage'),

    path(route='signup/', view=views.signup, name='signup'),
    # path for login
    path(route='loginpage/', view=views.login_page, name='loginpage'),

    path(route='login/', view=views.login_request, name='login'),

    # path for logout
    path(route='logout/', view=views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    path(route='dealer/<int:dealerid>/<str:dealername>/', view=views.get_dealer_details, name='dealer_details'),

    path(route='addreview2/<int:dealerid>/', view=views.add_review, name='add_review'),

    path(route='addreview/<str:dealername>/<int:dealerid>/', view=views.add_review_page, name='add_review_page'),



    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)