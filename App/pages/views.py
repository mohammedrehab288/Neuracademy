from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request, 'pages/sign_in.html')

def teacher_sign_up(request):
    return render(request, 'pages/teacher_sign_up.html')

def teacher_complete_account(request):
    return render(request, 'pages/teacher_complete_account.html')