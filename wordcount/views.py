from django.http import HttpResponse    
from django.shortcuts import render 
def homepage(request):
    return render(request , 'home.html' , {'name':'I am Shubhkant'})
	
def count(request):
 data = request.GET['full']
 word_list = data.split()
 print(word_list)
 list_length = len(word_list)
 
 worddictionary = {}
 
 for word in word_list:
    if word in worddictionary:
         worddictionary[word]+= 1
    else:
         worddictionary[word] = 1
		 
 return render(request ,'count.html' , {'fulltext':data , 'words' : list_length , 'worddictionary': worddictionary })