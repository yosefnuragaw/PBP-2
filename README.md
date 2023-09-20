
Nama    : Yosef Nuraga Wicaksana
NPM     : 2206082751
Kelas   : PBP C

[Tugas 2](#Tugas-2-Pemrograman-Berbasis-Platform-2022/2023)
[Tugas 3](#Tugas-3-Pemrograman-Berbasis-Platform-2022/2023)


# Tugas 2 Pemrograman Berbasis Platform 2022/2023
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

# Tugas 3 Pemrograman Berbasis Platform 2022/2023
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