from django.urls import path
from . import views

app_name = 'root'


urlpatterns =[
   path('',views.index,name='index'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path('contact/',views.contact,name='contact'),
   path('join_us/',views.join_us,name='join_us'),
   path('activities/',views.activities,name='activities'),
   path('donate_us/',views.donate_us,name='donate_us'),
   path('social_contribution/',views.social_contribution,name='social_contribution'),
   path('publications/',views.publications,name='publications'),
   path('announcement/',views.announcement,name='announcement'),
   #social contributions
   path('social_1/',views.social_1,name='social_1'),#Empowerment of Persons
   path('social_2/',views.social_2,name='social_2'),#Women Empowerment 
   path('social_2_jamnagar/',views.social_2_jamnagar,name='social_2_jamnagar'),#Tailoring and Cutting Training at Jamanagar 
   path('social_3/',views.social_3,name='social_3'),#Self Help Group 
   path('social_4/',views.social_4,name='social_4'),#Self Employment Training 
   path('social_5/',views.social_5,name='social_5'),#Education for All 
   path('social_6/',views.social_6,name='social_6'),#AIDS Awareness 
   path('social_7/',views.social_7,name='social_7'),#Legal Aid 
   path('social_8/',views.social_8,name='social_8'),#Rural Development Program 
   path('social_9/',views.social_9,name='social_9'),#Computer literacy and awareness 
   path('social_10/',views.social_10,name='social_10'),#Safe Drinking Water for All 
   path('social_11/',views.social_11,name='social_11'),#Non Conventional Energy 
   path('social_12/',views.social_12,name='social_12'),#Children Rights and Child Protection 
   path('social_13/',views.social_13,name='social_13'),#Micro Finance 
   path('social_14/',views.social_14,name='social_14'),#Environmental Protection and Sustainable Development 
   #Professional Activities
   path('professional_activities',views.professional_activities,name='professional_activities'),
   path('prof_1',views.prof_1,name='prof_1'),#Research Counseling
   path('prof_2',views.prof_2,name='prof_2'),#Data Analysis
   path('prof_3',views.prof_3,name='prof_3'),#Application of Computer for Research
   path('prof_4',views.prof_4,name='prof_4'),#Research methods and methodology Report Writing
   path('prof_5',views.prof_5,name='prof_5'),#Communication Training
   path('prof_6',views.prof_6,name='prof_6'),#Corporate Communication
   path('prof_7',views.prof_7,name='prof_7'),#Content development
   path('prof_8',views.prof_8,name='prof_8'),#Financial advisory
   path('prof_9',views.prof_9,name='prof_9'), #Market Research 
   path('prof_10',views.prof_10,name='prof_10'), #Doctoral Counseling 
   path('prof_11',views.prof_11,name='prof_11'), #Research publication 
   path('prof_12',views.prof_12,name='prof_12'), #Career Counseling 
   path('prof_13',views.prof_13,name='prof_13'), #Personal Counseling 
   path('prof_14',views.prof_14,name='prof_14'), #Psychological Counseling
   path('prof_15',views.prof_15,name='prof_15'), #Corporate Counseling 
   path('prof_16',views.prof_16,name='prof_16'), #Family Counseling 
   path('prof_17',views.prof_17,name='prof_17'), #Web Designing 
   path('prof_18',views.prof_18,name='prof_18'), #Digital Marketing
   #################
   path('email/',views.email,name='email'),
   
]
