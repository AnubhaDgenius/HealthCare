

# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from health.models import Notice, Patient, Disease, Ques,Book
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls.base import reverse_lazy
from health.forms import PatientForm,BookForm
from rest_framework import viewsets, permissions
from health.serializers import NoticeSerializer, PatientSerializer,\
    UserSerializer, DiseaseSerializer,BookSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from health.permissions import MyPers2

def about(request):
    return render(request, "about.html");

def health(request):
    return render(request, "health.html");

def contact(request):
    return render(request, "contact.html");


@method_decorator(login_required, name='dispatch')
class NoticeList(ListView):
    model = Notice
    def get_queryset(self):
        si = self.request.GET.get('si')
        if si==None:
           si=''
        if self.request.user.is_superuser:
            return Notice.objects.all().filter(subject__icontains = si).order_by('-id')
#             si = self.request.GET.get('si')
#             if si:
#                 return Notice.objects.all().filter(subject__icontains = si)        
#             else:
#                 return Notice.objects.all().order_by('-id')
        else:
            st = Patient.objects.filter(user=self.request.user.id)[0]            
            if st!=None and st.disease !=None:
                return Notice.objects.all().filter(disease=st.disease.id, subject__icontains = si).order_by('-id')
            else:
                return Notice.objects.all().filter(disease=0)
    paginate_by = 7


@method_decorator(login_required, name='dispatch')
class NoticeList2(ListView):
    context_object_name = 'object_list'    
    template_name = 'health/combo_list.html'
    queryset = Notice.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NoticeList2, self).get_context_data(**kwargs)
        context['disease_list'] = Disease.objects.all()
        context['st_list'] = Patient.objects.all()
        # And so on for more models
        return context
    

@method_decorator(login_required, name='dispatch')
class NoticeDetails(DetailView):
    model = Notice
    
@method_decorator(login_required, name='dispatch')
class PatientUpdate(UpdateView):
    form_class=PatientForm
    model = Patient
    success_url = reverse_lazy('notice_list')     

class QuesCreate(CreateView):
    success_url = reverse_lazy('notice_list')
    model = Ques
    fields = ['question']
    def form_valid(self, form):
        form.instance.notice = Notice.objects.filter(id=self.request.GET.get('nid'))[0] 
        form.instance.user = self.request.user
        return super(QuesCreate, self).form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class BookCreate(CreateView):
    form_class=BookForm
    model = Book
    success_url = reverse_lazy('notice_list')     
   
    
    
# bellow code for API
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-cr_date')
    serializer_class = NoticeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-cr_date')
    serializer_class = PatientSerializer
    permission_classes = (MyPers2,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('date')
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)