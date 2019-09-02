from django.http import HttpResponse
from django.shortcuts import render
import operator

def wchomepage(request):
    return render(request, 'wchome.html')

def wccount(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increse
            worddictionary[word]+=1
        else:
            #add
            worddictionary[word]=1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'wccount.html',{'fulltext':fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})