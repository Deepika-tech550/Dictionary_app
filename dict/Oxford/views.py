from django.shortcuts import render
##from PyDictionary import PyDictionary
from AyDictionary import AyDictionary
from googletrans import Translator
# Create your views here.
def home(request):
	return render(request,'index.html',{'name':'Deepika'})

def word(request):
	if request.method=='POST':
		search=request.POST['search2']
		dictionary= AyDictionary()
		meaning= dictionary.meaning(search)
		#synonyms= dictionary.synonym(search)
		#antonyms=dictionary.antonym(search)
		translate= translator.translate(search,'ta')
		context={'search':search,'meaning':meaning['Noun'][0],'translate':translate}
		print(search)
		return render(request,'index.html',context)
	else:
		return render(request,'index.html')
