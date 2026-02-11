from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # saves user to database
            login(request, user)  # logs in user immediately
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        # Update user email
        request.user.email = request.POST.get('email')
        request.user.save()
        return redirect('profile')

    return render(request, 'blog/profile.html')




# Step-by-step story of register_view
# 🟢 Step 1: User opens /register

# Browser sends a GET request

# Code goes here:

# else:
#     form = RegisterForm()


# 👉 An empty form is created
# 👉 It is sent to the template
# 👉 User sees input boxes

# 🟢 Step 2: User fills form and clicks “Sign Up”

# Browser sends a POST request

# Data is inside request.POST

# form = RegisterForm(request.POST)


# This line:

# Takes raw form data

# Puts it into the form object

# 🟢 Step 3: Validate data
# if form.is_valid():


# Django checks:

# Are passwords strong?

# Do passwords match?

# Is username taken?

# Is email valid?

# If any rule fails, Django sends errors back to template.

# 🟢 Step 4: Save user safely
# user = form.save()


# This:

# Hashes the password

# Creates a row in auth_user table

# Stores username + email

# You never touch passwords directly. That’s good backend practice.

# 🟢 Step 5: Log user in
# login(request, user)


# This:

# Creates a session

# Stores user ID in browser cookies

# Makes request.user available

# 🟢 Step 6: Redirect
# return redirect('profile')


# User is now:

# Registered

# Logged in

# Sent to profile page


from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

#show all posts accessible to everyone
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
 
 #view single post   
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
 #cretae a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
      
# LoginRequiredMixin → must be logged in
# form_valid() runs before saving
# form.instance.author = request.user
# 👉 this is where we attach the author automatically


#update  post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

#delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

