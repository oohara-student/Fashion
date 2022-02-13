from django.shortcuts import render
from .models import Clothes
from .forms import ClothesAdd
from django.shortcuts import redirect 
import random

def index(request):
    test = "/media/"
    tops = Clothes.objects.filter(genre__name='トップス')
    outer = Clothes.objects.filter(genre__name='アウター')
    pants = Clothes.objects.filter(genre__name='パンツ')
    topss = Clothes.objects.filter(genre__name='トップス').count()
    outers = Clothes.objects.filter(genre__name='アウター').count()
    pantss = Clothes.objects.filter(genre__name='パンツ').count()
    tops_num = random.randrange(1,topss + 1)
    outer_num = random.randrange(1,outers + 1)
    pants_num = random.randrange(1, pantss + 1)
    
    my_dict4 = {
        'test':test,
        'tops':tops,
        'outer':outer,
        'pants':pants,
        'tops_num':tops_num,
        'outer_num':outer_num,
        'pants_num':pants_num,
        }
    return render(request, 'webtestapp/index.html', my_dict4)

def settei(request):
    return render(request, 'webtestapp/Configuration.html')

def otoi(request):
    return render(request, 'webtestapp/inquiry.html')

def topic(request):
    return render(request, 'webtestapp/topic.html')

def closet(request):
    return render(request, 'webtestapp/close.html')

def closet(request): #クローゼット
    images = Clothes.objects.all()
    test = "/media/"
    short_sleeves = Clothes.objects.filter(kinds__name='半袖')
    long_sleeves = Clothes.objects.filter(kinds__name='長袖')
    parker = Clothes.objects.filter(kinds__name='パーカー')
    sweater = Clothes.objects.filter(kinds__name='セーター')
    short_sleeve_shirt = Clothes.objects.filter(kinds__name='半袖シャツ')
    long_sleeve_shirt = Clothes.objects.filter(kinds__name='長袖シャツ')
    zipper_parker = Clothes.objects.filter(kinds__name='パーカー(チャックあり)')
    coat = Clothes.objects.filter(kinds__name='コート')
    down_jacket = Clothes.objects.filter(kinds__name='ダウンジャケット')
    shorts = Clothes.objects.filter(kinds__name='半ズボン')
    long_trousers = Clothes.objects.filter(kinds__name='長ズボン')

    my_dict3 = {
        'images':images,
        'test':test,
        'short_sleeves':short_sleeves,
        'long_sleeves':long_sleeves,
        'parker':parker,
        'sweater':sweater,
        'short_sleeve_shirt':short_sleeve_shirt,
        'long_sleeve_shirt':long_sleeve_shirt,
        'zipper_parker':zipper_parker,
        'coat':coat,
        'down_jacket':down_jacket,
        'shorts':shorts,
        'long_trousers':long_trousers,
    
        }
    return render(request, 'webtestapp/closet.html', my_dict3)

def riyou(request):
    return render(request, 'webtestapp/Terms of service.html')

def calendar(request):
    return render(request, 'webtestapp/calendar.html')

def timeline(request):
    return render(request, 'webtestapp/timeline.html')

def timelinew(request):
    return render(request, 'webtestapp/timelinewoman.html')

def toukou(request):
    return render(request, 'webtestapp/Post.html')

def code(request):
    return render(request, 'webtestapp/code.html')

def tuika(request):
    return render(request, 'webtestapp/Addcoordination.html')

def okiniiri(request):
    return render(request, 'webtestapp/favorite.html')

def sakujo(request):
    return render(request, 'webtestapp/Deletecode.html')

def honnninntoruroku(request):
    return render(request, 'webtestapp/registration.html')

def passward(request):
    return render(request, 'webtestapp/password.html')

def clothes_register(request):
    return render(request, 'webtestapp/clothes_register.html') #服登録

def clothes_register(request): #服登録
    modelform_dict1 = {
        'title':'服の登録',
        'form': ClothesAdd(),
    }
    return render(request, 'webtestapp/clothes_register.html', modelform_dict1)

def clothes_register(request): #服登録
    message = ''  # 初期表示ではカラ
    if (request.method == 'POST'):
        form = ClothesAdd(request.POST, request.FILES)
        if form.is_valid():
            form.image = request.FILES['image']
            form.save()
            return redirect(to='/closet')
        else:  
            message = '再入力して下さい'
            
    modelform_dict1 = {
        'title':'服の登録',
        'form': ClothesAdd(),
        'message': message,  # エラーメッセージ
    }
    return render(request, 'webtestapp/clothes_register.html', modelform_dict1)

def help(request):
    return render(request, 'webtestapp/help.html') 

def forget(request):
    return render(request, 'webtestapp/forgetpassword.html') 

def colour(request):
    return render(request, 'webtestapp/colour.html') 