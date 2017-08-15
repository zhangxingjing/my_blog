from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def test(request):
    #查
    # usermessage = UserMessage.objects.filter(name='xxx')
    # for user in usermessage:
    #     print(user.name)
    #删
    #     user.delete()
    #增
    # user_message = UserMessage()
    # user_message.name = 'xxx'
    # user_message.email = 'zzz@hotmail.com'
    # user_message.address = 'yyy'
    # user_message.message = 'zzz'
    # user_message.save()
    #提交表单
    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     email = request.POST.get('email','')
    #     address = request.POST.get('address', '')
    #     message = request.POST.get('message', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.email = email
    #     user_message.address = address
    #     user_message.message = message
    #     user_message.save()
    usermessage = UserMessage.objects.filter(name='a').first()
    return render(request,'test.html',{
        'usermessage':usermessage
    }
    )


def index(request):
    return render(request,'index.html')