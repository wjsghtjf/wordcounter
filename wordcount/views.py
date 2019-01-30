from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def result(request):
    text=request.GET['full_text']
    splited=text.split()
    word_dic ={}
    count=0
    for word in splited:
        if word in word_dic:
            word_dic[word]+=1
            count=count+1
            if count%5==0:
                count=0
        else:
            word_dic[word] =1   
            count=count+1
            if count%5==0:
                count=0
    return render(request, 'result.html',{'full':text, 'length':len(splited), 'dictionary' :word_dic.items(),'count':count})  
  