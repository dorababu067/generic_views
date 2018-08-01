from django.shortcuts import render
from cbsviews.models import School
from django.urls import reverse_lazy
from django.views.generic import (	
									TemplateView,
									ListView,
									DetailView,
									CreateView,
									UpdateView,
									DeleteView,
								)
# Create your views here.
class IndexView(TemplateView):
	#model = School
	template_name = 'index.html'
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context={
			'data':'TemplateView Demo'
		}
		return context

class SchoolListView(ListView):
	model = School
	template_name = 'school_list.html'
	#by default context_object_Name is modelname_list
	#here we are over riding the default name with schools
	context_object_name = 'schools'

class SchoolDetailsView(DetailView):
	model = School
	template_name	= 'school_details.html'
	context_object_name = 'school'

class SchoolCreatView(CreateView):
	model 	=	School
	fields = '__all__'
	template_name = 'school_creat.html'

class SchoolUpdateView(UpdateView):
	model =	School
	fields	= '__all__'
	template_name = 'school_update.html'

class SchoolDeleteView(DeleteView):
	model 		=	School
	context_object_name = 'schooldata'
	template_name = 'school_delete.html'
	success_url	=   reverse_lazy('cbsviews:list')








