from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Shop, Product, Category, CustomUser
from .forms import RegisterForm, LoginForm, ShopForm, ProductForm




def register_view(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Xush kelibsiz, {user.username}! 🎉")
        return redirect('shop:home')
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Salom, {user.username}! 👋")
        return redirect(request.GET.get('next', 'shop:home'))
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Chiqish muvaffaqiyatli amalga oshirildi.")
    return redirect('shop:home')




def home(request):
    shops = Shop.objects.all().order_by('-created_at')[:6]
    products = Product.objects.filter(in_stock=True).order_by('-created_at')[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'shops': shops,
        'products': products,
        'categories': categories,
    })




def shop_list(request):
    shops = Shop.objects.all().order_by('-created_at')
    return render(request, 'store/shop_list.html', {'shops': shops})


def shop_detail(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    products = shop.products.all()
    in_stock_only = request.GET.get('in_stock')
    if in_stock_only:
        products = products.filter(in_stock=True)
    category_slug = request.GET.get('category')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(categories=selected_category)
    categories = Category.objects.filter(products__shop=shop).distinct()
    return render(request, 'store/shop_detail.html', {
        'shop': shop,
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'in_stock_only': in_stock_only,
    })


@login_required
def shop_create(request):
    form = ShopForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        shop = form.save(commit=False)
        shop.owner = request.user
        shop.save()
        messages.success(request, f"'{shop.name}' do'koni yaratildi! 🏪")
        return redirect('shop:shop_detail', slug=shop.slug)
    return render(request, 'store/shop_form.html', {'form': form, 'title': "Yangi do'kon"})




def product_list(request):
    products = Product.objects.all()
    in_stock_only = request.GET.get('in_stock')
    if in_stock_only:
        products = products.filter(in_stock=True)
    category_slug = request.GET.get('category')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(categories=selected_category)
    q = request.GET.get('q', '')
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'in_stock_only': in_stock_only,
        'q': q,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related = Product.objects.filter(
        categories__in=product.categories.all()
    ).exclude(pk=product.pk).distinct()[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
    })


@login_required
def product_create(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug, owner=request.user)
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.shop = shop
        product.save()
        form.save_m2m()
        messages.success(request, f"'{product.name}' mahsulot qo'shildi! ✅")
        return redirect('shop:shop_detail', slug=shop.slug)
    return render(request, 'store/product_form.html', {
        'form': form,
        'shop': shop,
        'title': 'Yangi mahsulot',
    })


@login_required
def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if product.shop.owner != request.user:
        messages.error(request, "Ruxsat yo'q! ⛔")
        return redirect('shop:product_detail', slug=slug)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Mahsulot yangilandi! ✏️")
        return redirect('shop:product_detail', slug=product.slug)
    return render(request, 'store/product_form.html', {
        'form': form,
        'shop': product.shop,
        'title': 'Tahrirlash',
        'product': product,
    })


@login_required
def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if product.shop.owner != request.user:
        messages.error(request, "Ruxsat yo'q! ⛔")
        return redirect('shop:product_detail', slug=slug)
    shop_slug = product.shop.slug
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Mahsulot o'chirildi! 🗑️")
        return redirect('shop:shop_detail', slug=shop_slug)
    return render(request, 'store/product_confirm_delete.html', {'product': product})


def category_filter(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(categories=category)
    in_stock_only = request.GET.get('in_stock')
    if in_stock_only:
        products = products.filter(in_stock=True)
    return render(request, 'store/category_filter.html', {
        'category': category,
        'products': products,
        'in_stock_only': in_stock_only,
    })
