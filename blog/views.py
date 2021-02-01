from django.shortcuts import render
import requests


# Create your views here.

def home(request):
	headers = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
	response=requests.get('https://api.mentimeter.com/questions/48d75c359ce4', headers=headers).json()
	resss=requests.get('https://api.mentimeter.com/questions/48d75c359ce4/result', headers=headers).json()
	
	return render(request,'pavananna/home.html',{'response':response,'resss':resss})


def result(request):
	headers = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
	response=requests.get('https://api.mentimeter.com/questions/48d75c359ce4', headers=headers).json()
	resss=requests.get('https://api.mentimeter.com/questions/48d75c359ce4/result', headers=headers).json()
	
	return render(request,'pavananna/result.html',{'response':response,'resss':resss})
