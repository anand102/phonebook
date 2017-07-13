from django.conf.urls import url

from . import views

urlpatterns = [
				url(r'^$',views.index,name='index'),
				url(r'^login/',views.Login,name='login'),
				url(r'^signup/',views.Signup,name='signup'),
				url(r'^logout/',views.Logout,name='logout'),
				
			]