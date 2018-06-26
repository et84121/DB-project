from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, form
# Create your views here.


def index(request):
    if request.method == 'GET':
        Lat = request.GET.get('Lat')
        Long = request.GET.get('Long')
        if Lat is not None:
            request.session['Lat'] = Lat
            request.session['Long'] = Long
            posts = models.Post.objects.filter(
                located=models.Location.objects.get(
                    longitude=Long,
                    latitude=Lat
                )
            )
        else:
            posts = models.Post.objects.all()
    return render(request, 'home.html', locals())


def login(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        login_form = form.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
    return render(request, 'login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    return redirect("/")


def post(request):
    Lat = request.session['Lat']
    Long = request.session['Long']
    if request.method == "POST":
        post_form = form.PostForm(request.POST)
        if post_form.is_valid():
            mood = request.POST.get('mood')
            message = post_form.cleaned_data['message']
            models.Post.objects.create(
                content=message,
                user_who_posted=models.User.objects.get(
                    name=request.session['user_name']),
                located=models.Location.objects.get(
                    longitude=request.session['Long'],
                    latitude=request.session['Lat']
                ),
                mood=models.Mood.objects.get(name=mood)
            )
            info = '發文成功'
            return render(request, 'post.html', locals())
    else:
        post_form = form.PostForm()

    return render(request, 'post.html', locals())


def reply(request, post_id):
    if request.POST.get('content') is not None:
        models.comment.objects.create(
            content=request.POST.get('content'),
            user_who_made=models.User.objects.get(
                name=request.session['user_name']),
            which_post=models.Post.objects.get(id=post_id)
        )
        return HttpResponse('回覆成功')

    return HttpResponse('回覆失敗')
