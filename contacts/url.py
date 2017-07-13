from django.conf.urls import url

from . import views

urlpatterns = [
				url(r'^$',views.index,name='index'),
				url(r'^login/',views.Login,name='login'),
				url(r'^signup/',views.Signup,name='signup'),
				url(r'^logout/',views.Logout,name='logout'),
				# url(r'^home/',views.Home,name='home'),
				url(r'^addcontact/',views.Add_contact,name='Add_contact'),
				url(r'^edit/(?P<id>[0-9]+)/$',views.Edit_contact,name='Edit_scontact'),
				url(r'^delete/(?P<id>[0-9]+)/$',views.Delete_contact)
			]