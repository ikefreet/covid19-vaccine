from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reservation, Question
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .forms import ReservationForm, QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import pymysql

con = pymysql.connect(host='mydb', user='django', password='django', db='django', charset='utf8')
cur = con.cursor()
 

# Create your views here.
# 응답에 대한 처리 함수를 정의할 땐 무조건 매개변수 한 개 이사이 필요
def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date').using('slave')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj, 'state' : 'True'}
    return render(request, 'pybo/mainpage.html',context) 

# 공지사항 detail
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id).using('slave')
    context = {'question' : question}
    return render(request, 'pybo/Notification.html', context)


@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index') 
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/question_detail.html', context)

def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        n = "INSERT INTO pybo_reservation (NAME, BIRTH, HOSPITAL, VACCINE, DATE, HOUR) VALUE (%s, %s, %s, %s, %s, %s)"
        check = "select NAME from pybo_reservation where HOSPITAL=%s AND DATE=%s AND HOUR=%s"
        id = "select id from pybo_reservation where HOSPITAL=%s and HOUR=%s"
        cur.execute(check, [request.POST['HOSPITAL'], request.POST['DATE'], request.POST['HOUR']])
        x = cur.fetchone()
        if form.is_valid():
            if x is None:
                cur.execute(n, [request.POST['NAME'], request.POST['BIRTH'], request.POST['HOSPITAL'], request.POST['VACCINE'], request.POST['DATE'], request.POST['HOUR']])
                con.commit()
                cur.execute(id, [request.POST['HOSPITAL'], request.POST['HOUR']])
                y = cur.fetchone()
                context = {'state' : y[0]}
                return render(request, 'pybo/mainpage.html', context)
            else:
                context = { 'state' : 'False' }
                return render(request, 'pybo/mainpage.html', context)
    else:
        form = ReservationForm()
    context = {'form' : form}
    return render(request, 'pybo/reservation.html', context)

def reservation_check(request):
    if request.method == "POST":
        check = "select NAME from pybo_reservation where id=%s"
        id = request.POST['ID']
        st = "select * from pybo_reservation where id=%s"
        cur.execute(check, [id])
        x = cur.fetchone()
        if x is not None:
            cur.execute(st, [id])
            z = cur.fetchone()
            context = {'name' : z[1], 'hosp' : z[3], 'date' : z[5], 'hour' : z[6], 'vac' : z[4]}
            print(context)
            return render(request, 'pybo/reservation_check.html', context)
        else:
            context = { 'state' : 'Error' }
            return render(request, 'pybo/reservation_check.html', context)
    else:
        form = ReservationForm()
        info = Reservation.objects
    context = {'form' : form, 'info' : info, 'state' : 'True'}
    return render(request, 'pybo/reservation_check.html', context)

def reservation_delete(request):
    if request.method == "POST":
        check = "select NAME from pybo_reservation where id=%s"
        id = request.POST['ID']
        st = "delete from pybo_reservation where id=%s"
        cur.execute(check, [id])
        x = cur.fetchone()
        if x is not None:
            cur.execute(st, [id])
            con.commit()
            context = {'state' : 'Delete'}
            return render(request, 'pybo/mainpage.html', context)
        else:
            context = { 'state' : 'Error' }
            return render(request, 'pybo/mainpage.html', context)
    else:
        form = ReservationForm()
        info = Reservation.objects
    context = {'form' : form, 'info' : info}
    return render(request, 'pybo/reservation_check.html', context)
