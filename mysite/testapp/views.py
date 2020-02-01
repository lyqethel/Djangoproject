from django.shortcuts import render

def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request,'home.html',{"api":api})

def user(request):
    import requests
    import json
    if request.method =='POST':
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)
        return render(request,'user.html',{'user':user,'username':username})
    else:
        notfound = "请在搜索框输入您需要查询的用户......."
        return render(request,'user.html',{'notfound':notfound})