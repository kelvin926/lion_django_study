from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    sentence = request.GET('sentence')
    wordlist = sentence.split()
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request, 'result.html',{'fulltext':sentence, 'count':len(wordlist), "wordDict":wordDict.items})