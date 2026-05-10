from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm

from django.contrib.auth import login

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сохраняем пользователя, но пока без коммита в БД
        user = form.save(commit=False)
        # Хешируем пароль
        user.set_password(form.cleaned_data['password1'])
        user.save()
        # Отправляем приветственное письмо
        send_mail(
            'Добро пожаловать в SkyStore!',
            f'Здравствуйте, {user.email}!\n\nСпасибо за регистрацию.',
            'noreply@skystore.ru',
            [user.email],
            fail_silently=False,
        )
        # Автоматически логиним после регистрации (опционально, можно убрать)
        # login(self.request, user)
        return redirect(self.success_url)

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = '/'