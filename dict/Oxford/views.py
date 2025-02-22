from django.shortcuts import render
from PyDictionary import PyDictionary  # Use the correct import

# Create your views here.
def home(request):
    return render(request, 'index.html', {'name': 'Deepika'})

def word(request):
    if request.method == 'POST':
        search = request.POST['search2']
        dictionary = PyDictionary()  # Create a dictionary object

        # Fetch meanings, synonyms, antonyms, and translations
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)
        translate = dictionary.translate(search, 'ta')  # Translation to Tamil (for example)

        # Safely access the meaning and check if the key exists
        noun_meaning = meaning.get('Noun', ['No meaning found'])[0] if meaning.get('Noun') else 'No meaning found'

        # If no synonyms or antonyms found, assign a default value
        synonyms = synonyms if synonyms else ['No synonyms found']
        antonyms = antonyms if antonyms else ['No antonyms found']

        # Prepare the context for the template
        context = {
            'search': search,
            'meaning': noun_meaning,
            'translate': translate,
            'synonyms': synonyms,
            'antonyms': antonyms
        }

        # Print for debugging
        print(f"Search: {search}")
        print(f"Meaning: {noun_meaning}")
        print(f"Synonyms: {synonyms}")
        print(f"Antonyms: {antonyms}")
        print(f"Translation: {translate}")

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
