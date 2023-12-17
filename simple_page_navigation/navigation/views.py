from django.shortcuts import render




def about(request) :
    d={'author' :'Rahim' , 'age' : 20 ,
      'courses' : [ 
      {
          'id' :1 ,
          'name' : 'phitron'
      }
       ,{
       
          'id' :2 ,
          'name' : 'goja'
       }
       ,
       {
          'id' :3 ,
          'name' : 'moja'
      } ]
       }
    return render(request,'navigation/about.html',d) 

def contact(request) :
    return render(request,'navigation/contact.html')