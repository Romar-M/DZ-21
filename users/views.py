from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправляем приветственное письмо
        user = self.object
        send_mail(
            'Добро пожаловать в SkyStore!',
            f'Здравствуйте, {user.email}!\n\nСпасибо за регистрацию.',
            'noreply@skystore.ru',
            [user.email],
            fail_silently=False,
        )
        return response

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = '/'