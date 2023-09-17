# Tugas 2 Pemrograman Berbasis Platform 2022/2023
Nama    : Yosef Nuraga Wicaksana
NPM     : 2206082751
Kelas   : PBP C

# Membuat sebuah proyek Django baru.
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

# Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan *virtual environment* dengan `env\Scripts\activate.bat`.
2. Dalam CMD jalankan `python manage.py startapp main` untuk membuat aplikasi bernama main.
3. Tambahkan `'main'` di variabel `INSTALLED_APPS` pada file `settings.py` di proyek Django yang telah dibuat. 

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
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

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.
1. Menambahkan atribut wajib `name` `price` `amount` pada `models.py` di direktori `main`
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
```
# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
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

# Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Masuk ke Adaptable.io. 
2. Pilih `New APP` lalu `Connect an Existing Repository`.
3. Pilih `All Repositories` untuk mengakses repository GitHub.
4. Pilih repository yang ingin di deploy.
5. Pada *template deployment* pilih `Pyhon App Template`.
6. Pada basis data pilih `PostgreSQL`.
7. Masukkan versi Python dan  perintah `python manage.py migrate && gunicorn nama_project.wsgi.`
8. Masukkan nama aplikasi lalu pilih `HTTP Listener on PORT` dan  `Deploy App` untuk melakukan *deployment*.

