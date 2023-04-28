# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm  # 追記
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)    # 変更
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView
)    # 追記

# ここから
from django.contrib.auth import get_user_model


from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)    # 変更
from django.views.generic import (
    DetailView,
    UpdateView,
)    # 変更
from django.urls import reverse    # 追記
from django.views.generic import DetailView
# 省略

from django.contrib.auth.mixins import UserPassesTestMixin    # 追記

# 省略

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser
User = get_user_model()
# ここまで

class UserCreateAndLoginView(CreateView):
    # form_class = UserCreationForm
    form_class = CustomUserCreationForm   # 変更
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        # username = form.cleaned_data.get("username")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response
    
# ここから
class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
# ここまで

class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
    
# 省略
class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/user_detail.html'


class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')