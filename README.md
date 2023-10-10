
Nama    : Yosef Nuraga Wicaksana
NPM     : 2206082751
Kelas   : PBP C
Tautan website: http://yosef-nuraga-tugas.pbp.cs.ui.ac.id
[Tugas 2](#tugas-2)
[Tugas 3](#tugas-3)
[Tugas 4](#tugas-4)
[Tugas 5](#tugas-5)
[Tugas 6](#tugas-6)


# Tugas 2 
## Membuat sebuah proyek Django baru.
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan *virtual environment* dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengan nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:`django`,`gunicorn`,`whitenoise`,`psycopg2-binary`,`requests`,`urllib3`.
5. Pastikan *virtual environment* menyala dan install *depedencies* dengan `pip install -r requirements.txt`.
6. Membuat proyek Django dengan `django-admin startproject nama_project`
7. Tambahkan `*` pada `ALLOWED HOST` di `settings.py`.
8. Jalankan proyek dengan `python manage.py runserver`
9. Buka dengan http://localhost:8000 dan tutup dengan `Ctrl+c`.
10. Matikan *vitual environment* dengan `deactivate`.

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan *virtual environment* dengan `env\Scripts\activate.bat`.
2. Dalam CMD jalankan `python manage.py startapp main` untuk membuat aplikasi bernama main.
3. Tambahkan `'main'` di variabel `INSTALLED_APPS` pada file `settings.py` di proyek Django yang telah dibuat. 

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat file `urls.py` di dalam  `main`  untuk mengatur rute jalan URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

2. Tambahkan path`('main/', include('main.urls'))` pada *file* `urls.py` di direktori proyek Django yang berbeda dengan file `urls.py` di direktori `main.

## Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.
1. Menambahkan atribut wajib `name` `price` `amount` pada `models.py` di direktori `main`
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
```
## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
1. Tambahkan `render` pada *file* `views.py` pada direktori main.
```python
from django.shortcuts import render
```

2. Tambahkan fungsi `show_main` pada *file* `views.py`
```python
def show_main(request):
    context = {
        'name': 'Yosef Nuraga Wicakasana',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```
3. Tambahkan direktori baru yakni `templates` di `main` dan buat `main.html` yang memiliki isi berikut. 
```html
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Masuk ke Adaptable.io. 
2. Pilih `New APP` lalu `Connect an Existing Repository`.
3. Pilih `All Repositories` untuk mengakses repository GitHub.
4. Pilih repository yang ingin di deploy.
5. Pada *template deployment* pilih `Pyhon App Template`.
6. Pada basis data pilih `PostgreSQL`.
7. Masukkan versi Python dan  perintah `python manage.py migrate && gunicorn nama_project.wsgi.`
8. Masukkan nama aplikasi lalu pilih `HTTP Listener on PORT` dan  `Deploy App` untuk melakukan *deployment*.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![MVT Design Architecture](https://github.com/yosefnuragaw/PBP-2/blob/main/MVT_Architecture_Tugas2.png)

Cara kerja ketiga bagian dalam arsitektur tersebut dimulai dengan pengguna yang mengirimkan HTTP request yang kemudian diolah oleh `urls.py` yang melakukan mapping kepada `views.py`. `views.py` akan mengirimkan permintaan kepada model untuk mengolah permintaan dari pengguna kemudian merender berkas `html` yang berada dalam direktori `Template` untuk dikirimkan kembali pada pengguna sehingga hasila dari permintaan tersebut dapat dilihat oleh pengguna.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
*Virtual environment* merupakan sebuah alat dalam pekerjaan development yang mengisolasi proyek yang dibuatsehingga memudahkan para *developer* untuk mengatur *dependencies* yang digunakan dalam proyek tersebut. Berikut merupakan rincian manfaat dari *Virtual Environment*.

Manajemen *Dependencies*: Dependencies dalam virtual environment lebih mudah dilacak dan mempermudah developer untuk mengetahui dependencies apa yang diperlukan dalam projek tersebut.

Isolation: Memudahkan developer untuk membuat beberapa projek bersamaan dalam satu device tanpa khawatir terdapat beda versi pada dependencies yang perlu diinstall.

Reproducibility dan Package Consistency: Mempermudah developer dalam membuat ulang projek tersebut kembali dan melakukan tracking pada versi dependencies yang digunakan sehingga memperlancar proses development proyek.

Testing and Development: Virtual environments are particularly useful for testing code on various versions of Python or trying out experimental packages without affecting the main development environment.

Proyek Django masih dapat berjalan apabila tanpa sebuah virtual envinronment. Akan tetapi penggunaan virtual envinronment merupakan sesuatu yang disarankan kepada para developer untuk memudahkan proses pengembangan proyek tanpa membuat dependencies projek dengan projek lainnya.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model - View - Controller)
MVC merupakan sebuah arsitektur yang sering digunakan dalam pengembangan aplikasi maupun websita dengan memishkan aplikasi menjadi tiga bagian yakni `Model` yang bertugas menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di *database*. Bagian kedua yakni `View` adalah bagian yang bertugas menampilkan informasi kepada pengguna dalam bentuk *Graphical User Interface* (GUI). Bagian terakhir yakni `Controller`bertugas  dalam menghubungkan `Model` dan `View`.

Sumber : https://www.dicoding.com/blog/apa-itu-mvc-pahami-konsepnya/ 

MVT (Model - View - Template)
MVT merupakan sebuah arsitektur yang digunakan dalam mengembangkan aplikasi dengan menggunakan Django dimana arsitektur ini terbagi menjadi tiga komponen yakni `Model` merupakan bagian yang mengatur seluruh data aplikasi dalam penambahan, pengubahan,pembacaan, dan hal lainnya dalam *database*. `View` merupakan sebuah bagian yang mengatur request HTTP kemudian mengolahnya dan mengembalikannya dalam bentuk HTTP kepada pengguna. Bagian ini akan memproses data dari `Model` dan merendernya menjadi HTML menggunakan `Template`. Bagian yang terakhir yakni `Template` adalah bagian yang menjadi struktur layout dalam aplikasi tersebut untuk dilihat kepada para pengguna.

Sumber : https://www.educative.io/answers/what-is-mvt-structure-in-django

MVVM (Model - View - ViewModel)

MVVM merupakan arsitektur yang dapat digunakan dalam pengembangan android. Arsitektur ini terbagi menjadi tiga bagian yakni `Model` yang bertugas untuk mengolah data dan logika dari aplikasi. `View` yang berisi *User Interface* Dari aplikasi dan bagaimana informasi yang akan ditampilkan. `ViewModel` yang bertugas dalam mengatur interaksi dengan `Model` untuk diteruskan menuju `View`.

Perbedaan dari ketiga arsitektur iniadalah alur bagaimana menangani permintaan pengguna yang tentu saja memiliki kelebihan masing - masing dalam setiap case. Akan tetapi inti dari ketiga arsitektur tersebut adalah menerima  input pengguna untuk diolah menggunakan model dan disalurkan kembali kepada pengguna. Mengetahui perbedaan yang ada pada ketiga arsitektur tersebut maka diperlukan analisis mendalam mengenai aplikasi yang akan dibuat untuk menentukan arsitektur yang akan dipakai.

# Tugas 3
## Apa perbedaan antara form POST dan form GET dalam Django?
### POST
1. Pengiriman data di encode
2. Data tidak terlihat pada URL
3. Baik digunakan untuk untuk request yang sensitif karena memiliki protection yakni CSRF protection
### GET
1. Pengiriman data berbentuk String
2. Data terlihat pada url
3. Baik digunakan untuk search karena mudah untuk di-bookmark atau dibagikan.

Sumber: https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST%20are%20typically,the%20state%20of%20the%20system.

##  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
### XML
XML merupakan sebuah *markup language* yang menggunakan struktur tag untuk merepresentasikan data yang tidak mampu mengolah array. XML hanya dapat diuraikan menggunakan pengurai XML. (XML starlet (LINUX))
### JSON
JSON (JavaScript Object Notation) merupakan sebuah file format yang menggunakan sturktur data key-item sehingga  dapat diolah mnggunakan sebuah fungsi JavaScript yang lebih mudah dibanding XML
### HTML
Tidak mampu melakukan pengiriman data karena hanya mengatur tata letak pada aplikasi

Sumber: https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=The%20differences%20between%20XML%2C%20JSON,how%20that%20data%20is%20displayed.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. Memiliki waktu pengiriman yang cepat karena berbasis text dan ringan.
2. Dengan struktur key - item memudahkan pengguna untuk melakukan parsing data
3. Mampu menyimpan temporary data
4. Memiliki struktur yang mudah dibaca sehingga memudahkan development
5. Menyimpan data ke dalam array untuk mempermudah pengiriman data
6. Memiliki kompabilitas dengan seluruh browser dan operating systemnya karena memiliki JSON Parser

sumber: https://www.oracle.com/id/database/what-is-json/#:~:text=readable%20JSON%20file.-,Why%20JSON%20is%20popular%20with%20developers,no%20additional%20code%20for%20parsing.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat direktori templates dengan file yakni `base.html` yang berisi kode berikut
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

2. Buka `settings.py` pada direktori project dan mengubah potongan kode berikut.
``` python
...
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        ...
    }
]
...
```

3. Membuat `forms.py` pada subdirektori main yang berisi kode berikut.
``` python 
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
4. Tambahkan beberapa fungsi pada `views.py`
``` python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Yosef Nuraga Wicaksana', 
        'class': 'PBP C', 
        'products': products,
        'stock' : products.count()
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```
5. Tambahkan kode pada `urls.py` untuk mengarahkan ke fungsi pada `views.py`
```python
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
```

6. Tambahkan `create_product.html` pada `templates` di `main` sebagai tata letak input aplikasi yang berisi kode berikut.
``` html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
7. Ubah `main.html` untuk menampilkan barang yang disimpan menjadi.
```html
{% extends 'base.html' %}

{% block content %}
    <h1>GAME STORE</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>


    <h5>Current Game Stock: {{stock}}</h5> <!--Bonus  Poin-->
    <table>
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>
    
        {% comment %} Stok Game yang tersedia {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    
{% endblock content %}
```

## Screenshot
### localhost/8000
!["Base"](https://github.com/yosefnuragaw/PBP-2/blob/main/image/base.png)
### localhost/8000/json
!["json"](https://github.com/yosefnuragaw/PBP-2/blob/main/image/json.png)
### localhost/8000/json/id
!["json_id"](https://github.com/yosefnuragaw/PBP-2/blob/main/image/json_id.png)
### localhost/8000/xml
!["xml"](https://github.com/yosefnuragaw/PBP-2/blob/main/image/xml.png)
### localhost/8000/xml/id
!["xml_id"](https://github.com/yosefnuragaw/PBP-2/blob/main/image/xml_id.png)


# Tugas 4
 
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm merupakan formulir bawaan yang disediakan oleh Django untuk mempermudah proses pembuatan user baru dalam aplikasi web yang menggunakan Django. Class ini termasuk dalam modul django.contrib.auth.forms dan digunakan untuk mengumpulkan data yang diperlukan untuk membuat akun pengguna.
Terdapat beberapa kelebihan dan kekurangan dalam menggunakan Django UserCreationForm, yakni:
1. Mudah digunakan
Bagi seorang developer aplikasi yang menggunakan Django, UserCreationForm sangat mempermudah developer dalam pembuatan alur register yang cepat dan mudah sehingga mempercepat proses pembuatan aplikasi
2. Terintegrasi dengan sistem keamanan Django
Password yang disimpan dari formulir ini akan di hash oleh django sehingga penyimpanan password dapat menjadi lebih aman
3. Memiliki syarat validasi password
Password pada formulir ini memiliki minimum jumlah kata dengan syarat beberapa karakter penting untuk harus tercantum pada password sehingga menjadi lebih kuat.

Kekurangan:
1. Hanya formulir standar
UserCreationForum hanya menerima input username, email dan password. Apabila memerlukan input lain maka formulir perlu dicustom terlebih dahulu
2. Tidak terverifikasi email
Formulir ini hanya digunakan untuk menerima input sebagai pembuatan user dalam aplikasi, akan tetapi jika diperlukan langkah lebih lanjut seperti verifikasi email maka perogram perlu dikustomisasi lebih lanjut

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah langkah dalam memverifikasi pengguna apakah pengguna yang berusaha akses adalah pengguna itu sendiri. Dalam django, verifikasi dilakukan dengan memverifikasi credential beruapa username maupun kata
Autentikasi adalah proses memverifikasi identitas pengguna. Ini memeriksa apakah pengguna yang mengakses aplikasi adalah orang yang mereka klaim. Dalam konteks Django, autentikasi biasanya melibatkan verifikasi bahwa kredensial (seperti nama pengguna dan kata sandi) yang dimasukkan oleh pengguna cocok dengan yang terdaftar di sistem dan diimplementasikan menggunakan modul django.contrib.auth. Sedangkan otorisasi merupakan pemberian hak akses pada user saat mengakses aplikasi yang dibuat. Hal ini dilakukan untuk membatasi akses pengguna pada website kita dengan contoh pengunjung hanya dapat melihat namun admin dapat mengubah - ubah file yang terdapat pada aplikasi.

Kedua hal tersebut penting karena termasuk dalam sistem keamanan dalam Django untuk mengamankan data pengguna yang mengakses, kemudian menjaga kontrol pada aplikasi, serta mempermudah audit log aplikasi untuk mengecek jalnnya sistem aplikasi.

 ## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah cara untuk menyimpan data kecil di sisi pengguna (browser) yang memungkinkan server untuk mengingat informasi penting antar kunjungan ke halaman web. Mereka sangat berguna dalam mengelola pengalaman pengguna, seperti menyediakan konten atau fungsionalitas yang sesuai dengan setiap pengguna yang terautentikasi. Selain itu, cookies juga memungkinkan penyimpanan preferensi pengguna, seperti bahasa atau tema tampilan favorit. Selain itu cookies juga sering digunakan untuk melacak aktivitas pengguna guna memahami bagaimana pengguna berinteraksi dengan situs web, yang penting dalam analisis dan pengembangan strategi untuk meningkatkan pengalaman pengguna oleh tim developer.

Dalam Django, cookies user akan digunakan untuk mengidentifikasi pengguna dengan disimpan terlebih dahulu dan digunakan untuk melakukan query sesuai dengan otorisasi pengguna tersebut.

 ## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara default cookiies masih belum aman dalam pengembangan web karena terdapat beberapa serang yang mampu mengeksploit cookies seperti:

### Session Hijacking:
Penyerang yang berhasil mencuri cookie pengguna dapat memanfaatkannya untuk mengambil alih sesi pengguna. Dengan ini, penyerang dapat melakukan aktivitas atas nama pengguna, termasuk mengakses data pribadi, mengubah pengaturan, atau bahkan melakukan tindakan finansial.

### Cross-Site Scripting:
Risiko ini muncul ketika penyerang mencoba mencuri cookies dari perangkat pengguna dengan menyisipkan skrip berbahaya pada halaman web yang dikunjungi oleh pengguna. Dengan cookies yang berhasil dicuri, penyerang dapat mengakses aplikasi web menggunakan identitas pengguna yang sah dan melakukan tindakan berbahaya tanpa sepengetahuan pengguna.

### Cross-Site Request Forgery:
Ancaman ini melibatkan penyerang yang mencoba memanipulasi pengguna agar melakukan tindakan tertentu dalam aplikasi web tanpa sepengetahuan mereka. Hal ini dapat memungkinkan penyerang untuk melakukan operasi yang tidak diinginkan atau bahkan mengubah data pengguna.

### Cookie Spoofing:
Dalam serangan semacam ini, penyerang dapat memalsukan atau mengganti cookie yang sudah diautentikasi dengan cookie palsu atau yang telah dimanipulasi. Hal ini dapat memberikan akses ilegal ke dalam aplikasi web, memungkinkan penyerang untuk melakukan tindakan tanpa otorisasi.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Registrasi
1. Menambahkan potongan kode berikut pada `views/py` dalam subdirektori `main`:
``` python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
2. Menambahkan sebuah fungsi register untuk dalam `views.py` untuk menangani register user
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. Menambahkan sebuah hml template dengan nama `register.html` sebagai template untuk laman register
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
4. Menyambungkan `register` dari `views.py` dengan `urls.py` dengan menambah path:
```python
...
path('register/', register, name='register'),
...
```

### Login
1. Mengimport function baru di dalam `views.py`:
```python
from django.contrib.auth import authenticate, login
```
2. Menambahkan sebuah fungsi untuk menangani login user di dalam `views.py`:
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

3. Membuat sebuah template html baru yakni `login.html` sebagai template laman login
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
4. Menyambungkan `login` dari `views.py` dengan `urls.py` dengan menambah path:
```python
...
path('login/', login_user, name='login'),
...
```
5. Merestriksi `main` untuk melakukan login terlebih dahulu dengan menambahkan potongan kode berikut pada `views.py`
```python
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='/login')
def show_main(request):
...
```
### Logout
1. Mengimport function baru di dalam `views.py`:
```python
from django.contrib.auth import logout
```
2. Menambahkan sebuah fungsi untuk menangani logout user di dalam `views.py`:
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

3. Menambahkan button logout pada `main.html` untuk melakukan logout
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
4. Menyambungkan `logout` dari `views.py` dengan `urls.py` dengan menambah path:
```python
...
path('logout/', logout_user, name='logout'),
...
```
### Menghubungkan `item` dan `User`
1. Mengimport function baru dalam `models.py` yakni:
```python
from django.contrib.auth.models import User
```
2. Menhubungkan product dengan user yakni dengan menambahkan user pada tiap product dengan:
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Karena pengubahan model kemudian diperlukan migration pada database agar aplikasi dapat berjalan, dalam migration akan disetting default value sebagai 1 untuk data yang sudah tersimpan

### Menampilkan Informasi pengguna
1. Menambahkan function `datetime` di `views.py` dari modul untuk mencatat waktu.
```python
import datetime
``` 
2. Mengubah function login dalam `views.py` untuk mencatat data login ke dalam cookies user:
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

3. Mengubah context pada show main untuk menampilkan terakhir login pengguna di `views.py` tepatnya fungsi `show_main`:
```python
context = {
        'name': request.user.username,
        'products': products,
        'stock' : products.count(),
        'last_login': request.COOKIES['last_login'],
    }
```

4. Delete cookie apabila user logout dengan :
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

5. Menampilkan last login pada `main.html`
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

1. Melakukan register pada aplikasi
2. Melakukan create_product sebanyak 3 kali
3. Mungulangi tahap 1 dan 2 sebanyak 2 kali

# Tugas 5
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
### 1. Universal selector
Selector yang memilih seluruh elemen tanpa pengecualian yang biasanya dilakukan dengan
```css
{ 
    margin: 0;
}
```
### 2. ID Selector
Selector yang memilih sebuah tag HTML yang memiliki atribut ID di dalamnya sehingga dapat memilih sebuah tag secara spesifik
```html
<input id="login_btn" type="submit" value="Login">
```
```css
#login_btn{
    color whitesmoke;
}
```

### 3. Class Selector
Selector yang memilih sebuah class HTML sehingga dapat mengubah beberapa objek sekaligus yang memiliki class sama
```html
<input class="btn" type="submit" value="Login">
<input class="btn" type="submit" value="Logout">
```
```css
.btn{
    color whitesmoke;
}
```

### 4. Atribute selector
Selector yang memilih sesuai dengan atribut yang dimiliki oleh sebuah tag.
```html
<button type="submit" class="btn btn-danger">Delete</button>
```
```css
button[type=submit]{
    color whitesmoke;
}
```
### 5. Element selector
Selector yang memilih sesuai dengan tag html
```html
<input class="btn" type="submit" value="Login">
<input class="btn" type="submit" value="Logout">
```
```css
input{
    color whitesmoke;
}
```
### 6. Pseudo class selector
Selector yang memilih berdasarkan keadaan web saat ini salah satu contohnya hover yang memberi desain saat pengguna menggerakan mousenya pada objekyang dituju
```html
<a class="btn register_btn" href="{% url 'main:register' %}">Register</a>
```
```css
.btn:hover {
    color: whitesmoke;
}
```

## HTML5 Tag
### <header>
<header> berfungsi untuk menetapkan bagian teratas atau kepala dari suatu elemen atau dokumen HTML. Biasanya, bagian ini memuat elemen-elemen seperti judul, logo, navigasi, dan elemen penting lain yang terkait dengan bagian atas dari halaman web.

### <nav>
<nav> digunakan untuk menentukan bagian navigasi dari suatu dokumen atau elemen HTML. Di dalamnya terdapat tautan atau link yang membantu pengguna untuk berpindah antara halaman atau bagian dari situs web.

### <section>
<section> mengelompokkan konten yang memiliki tema serupa dalam suatu dokumen HTML. Contohnya adalah artikel atau bagian dari artikel. Biasanya, tag <section> dimanfaatkan untuk memisahkan konten agar lebih mudah dipahami.

### <article>
<article> digunakan untuk mengelompokkan konten yang bersifat mandiri, independen, atau dapat berdiri sendiri. Sebuah artikel bisa berupa berita, posting blog, ulasan, atau konten mandiri lainnya.

### <aside>
<aside> digunakan untuk menandai konten yang berkaitan dengan konten utama dalam suatu dokumen, namun bisa berdiri sendiri. Biasanya, <aside> digunakan untuk elemen seperti sidebar atau informasi terkait yang tidak terlalu penting untuk konten utama.

### <footer>
<footer> mendefinisikan bagian bawah dari dokumen atau elemen HTML. Biasanya, di dalamnya terdapat informasi seperti hak cipta, tautan ke halaman lain, atau informasi kontak.

### <main>
<main> menandai konten utama dari sebuah dokumen HTML. Hanya boleh ada satu elemen <main> dalam satu halaman, dan elemen ini tidak boleh diletakkan dalam elemen <article>, <aside>, atau <header>.

### <figure>  
<figure> digunakan untuk mengelompokkan elemen seperti gambar, ilustrasi, diagram, atau kode

## Perbedaan Margin dan Padding
### Margin
Margin adalah ruang kosong di sekeliling elemen yang tidak memiliki warna (kosong) sehingga tidak mempengaruhi elemen lain di sekitarnya
```css
.element {
  margin: 10px; 
}
```
### Padding
Padding adalah ruang di antara batas elemen dan kontennya sehingga menciptakan ruang kosong di dalam eleemen yang tidak berpengaruh padabackground ataupun warna
```css
.element {
  padding: 10px; 
}
```

### Perbedaan
Dikarenakan Margin terletak di luar elemen maka hanya mempengaruhi jarak elemen dengan elemen lain, sedangkan padding yang berada di dalam elemen mempengaruhi bagaimana elemen tersebut ditempatkan

### Perbedaan tailwind dan bootstrap
tailwind dan bootstrap adalah sebuah framework yang digunakan dalam pengembangan web. Terdapat perbedaan pada kedua framework tersebut yakni
| Tailwind | Bootstrap |
| -------- | -------- |
| Membuat  tampilan dengan menggabungkan kelas-kelas utilitas yang sudah didefinisikan.   | Dapat menggunakan gaya atau komponen tampilan secara langsung.   |
| Ukuran file CSS lebih kecil   | Ukuran file CSS  lebih besar   |
| Fleksibilitas dan adaptabilitas tinggi   | Kurang fleksibel karena karena menggunakan komponen yang telah didefinisikan.   |
| Pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia  | Pembelajaran yang lebih cepat untuk pemula |

Pada dasarnya kedua framework baik digunakan namun tepat jika dalam beberapa kondisi. Apabila ingin membangun sebuah web yang fleksibel dan tampilannya dikontrol sesuai yang kita inginkan maka menggunakan tailwind adalah pilihan yang tepat. Penggunaan bootstrap tepat jika pembuatan web perlu diselesaikan dalam waktu yang singkat dengan tampilan dan perilaku yang konsisten.


## Langkah langkah menerapkan checklist
1. Menginstall bootstrap pada base template dan font yang digunakan
```html
...
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap">
    <link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap" rel="stylesheet">
...
```
2. Mengubah beberapa html pada `login.html`,`.register.html`, `main.html`
### login
```html
<div class="card login_card">

    <h1>GameStock</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td colspan="2" class="btn-container">
                    <input class="btn login_btn" type="submit" value="Login">
                    <a class="btn register_btn" href="{% url 'main:register' %}">Register</a>
                </td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
```
### register
```html
<div class="container">
    <div class="card register-card">
        <h1>Register</h1>

        <form method="POST" class="input-container">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td colspan="2" class="btn-container">
                        <button type="submit" class="btn btn-primary">Daftar</button>
                        <a href="{% url 'main:login' %}" class="btn btn-primary">Kembali</a>
                    </td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    </div>
</div>
```
### main
```html

    <div class="row">
        {% for product in products %}
            <div class="col-md-4">
                <div class="card product-card {% if forloop.last %}last-product{% endif %}">
                    <form action="{% url 'main:remove_product' %}" method="post">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        <button type="submit" class="btn btn-danger">Delete</button>
                    </form>
                    <h3>{{product.name}}</h3>
                    <p>Price: {{product.price}}</p>
                    <p>Description: {{product.description}}</p>
                    <p>Amount: {{product.amount}}</p>
                    <p>Date Added: {{product.date_added}}</p>
                    <form action="{% url 'main:add_product' %}" method="post">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        <button type="submit" class="btn btn-success">+</button>
                    </form>
                    <form action="{% url 'main:sell_product' %}" method="post">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        <button type="submit" class="btn btn-warning">-</button>
                    </form>
                </div>
            </div>
        {% endfor %}
    </div>

    <a href="{% url 'main:create_product' %}">
        <button class="btn btn-primary">
            Add New Product
        </button>
    </a>

    <a href="{% url 'main:logout' %}">
        <button class="btn btn-secondary">
            Logout
        </button>
    </a>
```
3. Menambahkan `<style></style>` pada `login.html`,`.register.html`, `main.html`
### login
```css
<style type="text/css">
    body {
        background-image: url("https://images.unsplash.com/photo-1696351383130-f3c9ed9e1bf0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2532&q=80");
        background-size: cover; 
        background-position: center; 
        background-repeat : no-repeat;
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
        
    .card.login_card {
        max-width: 300px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 35px;
        border: 1px solid rgba(255, 255, 255, .25);
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.45);
        box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        text-align: center; /* Center text within the card */
        margin: auto; /* Center the card on the page */
    }

    .card.login_card h1 {
        font-family: 'Pixelify Sans', cursive;
    }

    .btn-container {
        text-align: center; /* Center buttons within the container */
    }

    .btn {
        margin: 5px; /* Add some space between buttons */
        transition: background-color 0.3s, padding 0.3s; 
        background-color: transparent;
        border: none;
        outline: none;
        color: green;
    }
    .btn:hover {
        background-color: green; /* Change to blue on hover */
        color: whitesmoke;
         /* Increase padding on hover */
    }
</style>
```
### register
```css
<style type="text/css">
    body {
        background-image: url("https://images.unsplash.com/photo-1696351383130-f3c9ed9e1bf0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2532&q=80");
        background-size: cover; 
        background-position: center; 
        background-repeat : no-repeat;
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: flex-start; /* Move content to the left */
        align-items: center;
    }
    
    .card.register-card {
        max-width: 600px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 35px;
        border: 1px solid rgba(255, 255, 255, .25);
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.45);
        box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        text-align: center;
        margin: auto; /* Center the card vertically */
    }

    .helptext{
        display: none;
    }
    .card.register-card h1 {
        font-family: 'Pixelify Sans', cursive;
    }

    .btn-container {
    text-align: center;
    display: flex;
    justify-content: center; /* Center the buttons horizontally */
}

.btn {
    margin: 5px;
    transition: background-color 0.3s, padding 0.3s;
    background-color: transparent;
    border: none;
    outline: none;
    color: green;
}
.btn:hover {
    background-color: green;
    color: whitesmoke;
}   

</style>
```
### main
```css
    <style>
        .product-card {
            max-width: 300px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 10px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
        }
        
        .product-card form {
            display: inline-block;
        }

        .last-product {
            background-color: green;
        }
    </style>
```

# Tugas 6
## Perbedaan antara asynchronous programming dengan synchronous programming. 
Perbedaan antara asynchronus programming dengan synchronus programming dalam konteks web terletak pada perbedaan cara pemrosesannya. Sebuah web yang menggunakan synchronus programming menjadikan client harus menunggu server untuk memroses terlebih dahulu request yang dikirimkan oleh user karena pemrosesan dilakukan menggunakan satu thread. Sedangkan untuk asynchronus, program tidak dijalankan dengan menggunakan satu thread saja melainkan dapat dieksekusi secara bersamaan. Hal ini menjadikan web tetap dapat menampilkan thread lain walaupun terdapat pemrosesan sebuah thread request user.

source: https://community.algostudio.net/memahami-synchronous-dan-asynchronous-dalam-pemrograman/ 

## Paradigma event-driven programming
Paradigma event-driven programming merupakan pendekatan pada sebuah perangakat lunak ataupun web yang dipengaruhi oleh peristiwa (event) yang terjadi selama berinteraksi dengan pengguna. Untuk menangani event tersebut maka diperlukanlah sebuah event handler yang berfungsi untuk menangani peristiwa tersebut yang berbeda dari thread program utama sehingga terjadi sebuah asynchronus programming dalam event handler. Berakhirnya event handler ditandai dengan adanya callback function untuk kembali ke thread program utama.

## Penerapan asynchronous programming pada AJAX

Penerapan asynchronus programming pada AJAX terletak dalam kemampuannya untuk menmroses beberapa thread dalam sebuah web server tanpa memblokir thread satu sama lain. Hal ini dapat dilakukan karena javascript dapat mengolah permintaan pengguna dan menerima hasilnya tanpa memberhentikan thread utama dalam program web sehingga perubahan tidak perlu dilakukan dengan refresh web.

## Fetch API dan JQuery
### Fetch API
1. Fetch API adalah API modern dalam JavaScript yang menyediakan antarmuka untuk melakukan permintaan HTTP dan mengelola responsnya
2. Memerlukan polifil atau transpiler pada beberapa browser kuno karena tidak compatible.
3. Menggunakan Promise untuk mengelola respons dan error, yang membuat kodenya lebih bersih dan mudah dipahami.
### JQuery
1. jQuery adalah pustaka JavaScript yang memudahkan penggunaan dan manipulasi DOM, termasuk melakukan permintaan HTTP menggunakan teknik yang dikenal sebagai Ajax
2. Kompatibel dengan banyak browser, termasuk versi yang lebih lama.
3. Ketergantungan pada JQuery menyebabkan dapat  performa situs web menurun.

### Pilihan antara keduanya
Jika diminta mengenai pendapat terhadap dua hal tersebut saya lebih memilih untuk menggunakan Fetch API yang merupakan teknologi terbaru sehingga menghadirkan web dengan performa yang efisian dan dengan kompabilitas pada mayoritas browser saat kini.

## Langkah tugas 6
1. Tambahkan fitur ajax untuk add product dan delete dalam `views.py` seperti pada potongan kode berikut:

```python
def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, description=description, amount = amount,user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def del_product_ajax(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
        except Product.DoesNotExist:
            pass

        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()
```
2. Hubungkan fungsi tambahan dari `views.py` dengan `urls.py` dengan menambahkan path
```python
...
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-product-ajax/', del_product_ajax, name='del_product_ajax')
...
```
3. Tambahkan modal sebagai tampilan baru untuk menambah produk dalam web
```html
    <div class="modal fade" id="addModal" tabindex="-1" aria-labelledby="addModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="addModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                            <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>
```
3. Hapus `row card` pada `main.html` karena akan digantikan menggunakan javascript
```html
 <div class="row" id = "ItemCard"></div>
 ```

 4. Tambahkan script berikut untuk menangani sebuah event secara asynchronus
 ```html
 <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
        async function refreshProducts() {
        document.getElementById("ItemCard").innerHTML = ""
            const products = await getProducts()
            let htmlString = ``
            let totalAmount = 0;
            products.forEach((item,index) => {
                htmlString += 
                `\n<div class="col-md-4">
                <div class="card product-card ${index === products.length - 1 ? 'last-product' : ''}"> <!-- Bonus Poin -->
                    <h3>${item.fields.name}</h3>
                    <p>Price: ${item.fields.price}</p>
                    <p>Description: ${item.fields.description}</p>
                    <p>Amount: ${item.fields.amount}</p>
                    <p>Date Added: ${item.fields.date_added}</p>
                    
                    <form action="{% url 'main:add_product' %}" method="post">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="${item.pk}">
                        <button type="submit" class="btn btn-success">+</button>
                    </form>
                    <form action="{% url 'main:sell_product' %}" method="post">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="${item.pk}">
                        <button type="submit" class="btn btn-warning">-</button>
                    </form>
                        <input type="button" id= "del_button" class="btn btn-danger" value="Delete" onclick ="delProduct(${item.pk})">
                </div>
            </div>` 
            totalAmount += item.fields.amount
            })
            
            document.getElementById("ItemCard").innerHTML = htmlString
            document.getElementById("currentStock").innerText = `Current Game Stock: ${totalAmount}`;
        }
        refreshProducts()

        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }
        document.getElementById("button_add").onclick = addProduct
    
        function delProduct(key) {
            const formData = new FormData();
            formData.append('product_id', key);
            fetch("{% url 'main:del_product_ajax' %}", {
                method: "POST",
                body: formData
            }).then(refreshProducts)
            
            document.getElementById("form").reset()
            return false
        }
    </script>
 ```
 Penjelasan:
    `refreshProduct()` untuk melakukan refresh pada menampilkan produk produk dalam penyimpanan
    `addProduct()` untuk menambahkan produk  kedalam inventory user
    `delProduct()` untuk menghapus product dari inventory user

5. Melakukan collect static untuk mengumpulkan berbagai static file dalam project

6. Melakukan deployment ke PaaS Fasilkom