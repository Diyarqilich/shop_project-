# 🛍 ShopHub — Django Mini Loyiha

**MARS IT Academy | Module 9-10 | Hikmatillayev Murodjon**

---

## 📋 Loyiha haqida

Mahsulotlar va Do'konlar boshqaruv tizimi.

### Texnologiyalar
- Django 4.2+
- CustomUser (AbstractUser)
- ForeignKey & ManyToManyField
- Authentication (@login_required)
- Media fayllar (ImageField, Pillow)
- Django Admin
- Chiroyli CSS animatsiyalar

---

## ⚙️ O'rnatish

### 1. Loyihani klonlash / yuklab olish

```bash
cd shop_project
```

### 2. Virtual muhit yaratish

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Migratsiyalar

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser yaratish

```bash
python manage.py createsuperuser
```

### 6. Ishga tushirish

```bash
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## 🗃 Modellar

| Model | Fieldlar |
|-------|---------|
| **CustomUser** | AbstractUser + avatar, bio |
| **Shop** | owner (FK→User), name, logo, address, slug |
| **Category** | name, slug (auto) |
| **Product** | shop (FK), categories (M2M), name, price, image, in_stock, slug, created_at, description |

---

## ⚡️ Funksiyalar

- ✅ Ro'yxatdan o'tish / Kirish / Chiqish
- ✅ Do'konlar ro'yxati va detail sahifasi
- ✅ Mahsulotlar ro'yxati va detail sahifasi
- ✅ Mahsulot qo'shish (faqat do'kon egasi)
- ✅ Mahsulot tahrirlash (faqat do'kon egasi)
- ✅ Mahsulot o'chirish (faqat do'kon egasi)
- ✅ Kategoriya bo'yicha filter
- ✅ Qidiruv funksiyasi
- ✅ **BONUS**: Faqat mavjud mahsulotlar filtri (`?in_stock=1`)

---

## 📁 Loyiha tuzilmasi

```
shop_project/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/
│   ├── models.py        # CustomUser, Shop, Category, Product
│   ├── views.py         # Barcha views
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   ├── static/store/
│   │   ├── css/main.css
│   │   └── js/main.js
│   └── templates/store/
├── templates/
│   ├── base.html
│   └── registration/
├── media/
├── requirements.txt
└── manage.py
```

---

## 🎨 Dizayn

Dark luxury tema, CSS animatsiyalar, responsive dizayn.
