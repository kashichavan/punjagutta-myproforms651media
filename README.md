How to upload/take user input media files:
----------------------------------------

step 1: create media folder inside the project level dir

Setp 2: go to settings.py and register media folder

	i) MEDIA_ROOT=os.path.join(BASE_DIR,'media')

	ii) MEDIA_URL='media/'

step 3: go to urls.py inside project then update static files for urlpatterns

	first we need to import 
------------------------------------
	i) from django.conf.urls.static import static 

	ii) from django.conf import settings

step 4: update static object to urlpatterns

	if settings.DEBUG:
		urlspatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


step 5 ) create model first inside models.py
		
		from django.db import models

		# Create your models here.
		class Student(models.Model):
    			name=models.CharField(max_length=25)
    			image=models.ImageField(upload_to='imagesh/')
			

step 6 ) create a form which inherit from forms.Modelform
		
		ex:
		
		class StudentForm(forms.ModelForm):
    			class Meta:
        			model=Student
        			fields='__all__'

step 7) create a view  and whenever if the request is post then we need to create form object then for that form object we need to pass request.FILES as arguement

		def studentview(request):
    			if request.method=="POST":
        			form=StudentForm(request.POST,request.FILES)
        			if form.is_valid():
            				form.save(commit=True)
    
    			f=StudentForm()
    			return render(request,'student.html',context={'form':f})
