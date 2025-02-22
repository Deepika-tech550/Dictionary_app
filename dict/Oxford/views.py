from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def home(request):
	return render(request,'index.html',{'name':'Deepika'})

def word(requset):
	if requset.method=='POST':
		search=request.POST['search2']
		dictionary= PyDictionary()
		meaning= dictionary.meaning(search)
		synonyms= dictionary.synonym(search)
		antonyms=dictionary.antonym(search)
		translate= dictionary.translate(search,'ta')
		context={'search':search,'meaning':meaning['Noun'][0],'translate':translate,'synonyms':synonyms,'antonyms':antonyms}
		print(search)
		return render(request,'index.html',context)
	else:
		return render(request,'index.html')
