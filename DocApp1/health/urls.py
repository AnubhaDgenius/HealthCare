from django.conf.urls import url, include
from django.contrib import admin
from health import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() 
router.register(r'notices', views.NoticeViewSet)
router.register(r'patient', views.PatientViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'disease', views.DiseaseViewSet)
router.register(r'ques', views.DiseaseViewSet)
router.register(r'book', views.BookViewSet)


urlpatterns = [ 
    url(r'^about/', views.about), 
    url(r'^health/', views.health), 
    url(r'^contact/', views.contact),
    url(r'^$', views.NoticeList.as_view(), name='notice_list'),
    url(r'combo_list/', views.NoticeList2.as_view(), name='notice_list2'),
    url(r'^(?P<pk>\d+)$', views.NoticeDetails.as_view(), name='notice_detail'),    
    url(r'^patient/edit/(?P<pk>\d+)$', views.PatientUpdate.as_view(), name='patient_edit'),  
    url(r'^new_book$', views.BookCreate.as_view(), name='book_new'),        
    url(r'^new_ques$', views.QuesCreate.as_view(), name='ques_new'),
       
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),        
]
   