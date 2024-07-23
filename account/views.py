from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Account
from category.models import Category
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
# from account.EmailBackEnd import EmailBackEnd




def dashboard(request):
    return render(request, 'includes/main-dashboard.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, "You are now logged in.")
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("login-user")
    return render(request, 'account/login.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # Taking username from email id.
        username = email.split("@")[0]
        # username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if (password == password2):
            try:
                user = Account.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                # USER ACTIVATION
                current_site = get_current_site(request)
                mail_subject = "Please activate your account"
                message = render_to_string('account/account-verification-email.html', {
                    'user': user,
                    'domain': current_site,
                    # encoding user id - nobody can see the primary key
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    # create token for particular user
                    'token': default_token_generator.make_token(user),
                })
                # link send to email address.
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                messages.success(request, "Thank you for registering with us. We have sent you a verification email to your email address. Please verify it.")
                return redirect("register-user")
            except:
                messages.error(request, "Registration failed.!")
                return redirect('register-user')
        else:
            messages.error(request, "Password does not match.!")
    return render(request, 'account/register.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect('login-user')


def activate(request, uidb64, token):
    try:
        # decode token
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExists):
        user = None
    
    # change the is_active to true.
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login-user')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('register-user')


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Check for email exist or not.
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            # sending reset password email
            current_site = get_current_site(request)
            mail_subject = "Reset Your Password."
            message = render_to_string('account/reset-password-email.html', {
                'user': user,
                'domain': current_site,
                # encoding user id - nobody can see the primary key
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # create token for particular user
                'token': default_token_generator.make_token(user),
            })
            # link send to email address.
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect("login-user")
        else:
            messages.error(request, 'Your email not exists.')
            return redirect("forget-password")
    return render(request, 'account/forget-password.html')


def password_validate(request, uidb64, token):
    try:
        # Decoded token
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExists):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password.')
        return redirect('reset-password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login-user')

    
def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Your password has been changed.')
            return redirect('login-user')
        else:
            messages.error(request, 'Password do not match.')
            return redirect('reset-password')
    else:
        return render(request, 'account/reset-password.html')

# //----------------------ADMIN-DASHBOARD---------------------// #
# -------------------------------------------------------------  #

def admin_dashboard(request):
    return render(request, 'account/admin_panel/admin-dashboard.html')


def add_product(request):
    category_dropdown = Category.objects.all()
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        images = request.FILES.get('category_image')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        is_available = request.POST.get('is_availabe')
        if is_available in dict(Product.CHOICES).keys():
            product = Product(
                product_name = product_name,
                description = description,
                price = price,
                images = images,
                stock = stock,
                category_id = category_id,
                is_available = is_available
            )
            product.save()
            return redirect('view-product')
    context = {
        # 'category': category,
        'categories': category_dropdown
    }
    return render(request, 'store/add-product.html', context)


def view_product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/product-view.html',context)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    category = Category.objects.all()
    context = {
        'product': product,
        'id': product_id,
        'categories': category
    }
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        images = request.FILES.get('category_image')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        is_available = request.POST.get('is_available')

        if is_available in dict(Product.CHOICES).keys():
            product = Product.objects.get(id=product_id)
            product.product_name = product_name
            product.description = description
            product.price = price
            product.images = images
            product.stock = stock
            product.category_id = category_id
            product.is_available = is_available
            product.save()
            return redirect('view-product')
        context = {
            # 'category': category,
            'categories': category_dropdown
        }
    return render(request, 'store/edit-product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('view-product')
