# Tugas 2 Pemrograman Berbasis Platform 2022/2023
Nama    : Yosef Nuraga Wicaksana
NPM     : 2206082751
Kelas   : PBP C



# Membuat sebuah proyek Django baru.
1. Membuat sebuah direktori baru sebagai tempat proyek Django.
2. Membuka CMD dengan *path* direktori tersebut dan membuat *virtual environment* dengan `python -m venv env`
3. Mengaktifkan *virtual environment* dengan `env\Scripts\activate.bat` di CMD
4. Buat sebuah *file* untuk menentukan syarat *dependencies* seperti Nama        : Clement Samuel Marly
NPM         : 2206082114
Kelas       : PBP C
Adaptable   : https://gamestock.adaptable.app/main/

# Membuat sebuah proyek Django baru.
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengan nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:`django`,`gunicorn`,`whitenoise`,`psycopg2-binary`,`requests`,`urllib3`.
5. Pastikan *virtual environment* menyala dan install *depedencies* dengan `pip install -r requirements.txt`.
6. Membuat proyek Django dengan `django-admin startproject nama_project`
7. Tambahkan `*` pada `ALLOWED HOST` di `settings.py`.
8. Jalankan proyek dengan `python manage.py runserver`
9. Buka dengan http://localhost:8000 dan tutup dengan `Ctrl+c`.
10. Matikan *vitual environment* dengan `deactivate`.


