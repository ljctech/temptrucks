from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
import stripe
import sys
# import request



# from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
# from django.shortcuts import redirect

from django.template.loader import render_to_string
# from .forms import GenerateRandomUserForm
from core.tasks import create_random_user_accounts

def form_valid(request):
    # total = form.cleaned_data.get('total')
    stuff = create_random_user_accounts.delay()
    messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')

    args = {
    'stuff':stuff
    }
    return render(request,'accounts/stuff.html', stuff )

pub_key = "pk_test_X7PoHRBJhy8MtSyVZ3Jk1AIB"
secret_key = "sk_test_TTuVfc7WfjHjYgybmH8dBxE0"
stripe.api_key = secret_key

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email= request.POST['stripeEmail']
            source= request.POST['stripeToken']
            user = form.save()


            customer = stripe.Customer.create(
                email=email,
                card = source

            )

            charge = stripe.Charge.create(
                customer=customer.id,
                amount=4999,
                currency="USD",
                description='test',
                # source=request.POST['stripeToken']
            )
            # print("Customer id is : " + customer.id)

            subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'plan': 'prod_EGlUcpVm0g5yx9'}],
            )
            user.refresh_from_db()  # load the profile instance created by the signal
            user.email=email
            user.userprofile.stripe_id = subscription.id
            user.userprofile.save()
            user.save()

            args = {
            'user': customer.id,
            # 'email':
            }

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # return render(request, 'accounts/reg.html', args)

            return redirect('/saferdb/query')

        else:
            error = '<ul class="errorlist"><li>Username is already taken.</li></ul>'
            form = RegistrationForm(request.POST)
            args = {'form': form, 'pub_key': pub_key, 'error': error}
            return render(request, 'accounts/reg_form.html', args)
    else:
        form = RegistrationForm(request.POST)
        args = {'form': form, 'pub_key': pub_key}#
        return render(request, 'accounts/reg_form.html', args)

# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
# @login_required


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user )

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args )
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form, 'user':request.user}
        return render(request, 'accounts/edit_profile.html', args )

def cancel_subscription(request):

    instance = request.user

    customer = instance.userprofile.stripe_id
    # customer.cancel_subscription(at_period_end=True)
    subscription = stripe.Subscription.retrieve(customer)
    subscription.delete(at_period_end = True)

    args = {
    'user':customer
    }
    return render(request, 'accounts/cancelled.html', args )
    # else:
    #     args = "shit went wrong this is a get request."
    #     return render(request, 'accounts/cancelled.html', args )

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user )

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args )
