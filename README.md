Link adaptable: https://centaurlib.adaptable.app/main/ 

- Cara mengimplementasi checklist:
    Membuat direktori dan repository
    1. Tambahkan direktori baru pada file lokal, direktori ini akan menjadi direktori utama.
    2. Buat pula repository baru pada GitHub dengan visibilitas "Public".

    Membuat proyek Django
    1. Buat berkas 'requirements.txt' pada direktori utama dan tambahkan beberapa dependencies yang dibutuhkan.
    2. Aktifkan Virtual Environment di Command Prompt dengan perintah 'python -m venv env', lalu "env\Script\activate.bat"
    3. Jalankan perintah 'pip install -r requirements.txt' untuk menginstall dependencies.
    4. Buat proyek Django dengan perintah 'django-admin startproject <NAMA_PROYEK> .' yang akan menjadi direktori proyek.
    5. Pada direktori proyek terdapat settings.py, di mana pada file tersebut perlu menambahkan '"*"' di antara kurung siku 'ALLOWED_HOSTS = [ ]'. Fungsinya sebagai daftar host yang diizinkan untuk mengakses aplikasi web.
    6. Pada direktori utama terdapat file manage.py yang perlu diaktifkan dengan perintah "python manage.py runserver".
    7. Periksa tautan http://localhost:8000 untuk melihat animasi roket yang merupakan tanda aplikasi Django berhasil dibuat.
    8. Nonaktifkan Virtual Environment dengan menekan Ctrl+C dan jalankan perintah 'deactivate'.

    Inisiasi direktori lokal dengan repository GitHub
    1. Jalankan Command Prompt pada direktori utama, selanjutnya jalankan perintah 'git init' untuk mengosongkan repositori git di dalam direktori.
    2. Lakukan konfigurasi nama pengguna dan surel dengan menjalankan perintah 'git config user.name "<NAME>"' dan 'git config user.email"<EMAIL>"'
    3. Membuat branch utama dengan nama 'main'. Caranya adalah menjalankan perintah 'git branch -M main' pada Command Prompt direktori utama.
    4. Menghubungkan direktori lokal dengan repository GitHub dengan cara menjalankan perintah 'git remote add origin <URL_REPO>'. Tautan URL HTTPS dapat diperoleh pada repository di GitHub
    5. Masih pada direktori utama, tambahkan berkas '.gitignore' yang berfungsi menentukan berbagai berkas dan direktori yang harus diabaikan Git.
    6. Setelah mengisi berkas '.gitignore' dengan teks yang dibutuhkan, lakukan add, commit, dan push pada Command Prompt sehingga direktori lokal dan repository dapat terhubung.

    Membuat aplikasi 'main' di dalam proyek
    1. Aktifkan kembali Virtual Environment pada Command Prompt direktori utama.
    2. Untuk membuat aplikasi baru, jalankan perintah 'python manage.py startapp main'.
    3. Untuk mendaftarkan aplikasi 'main' ke dalam proyek, buka berkas 'setting.py' pada direktori proyek. Pada berkas terdapat variabel 'INSTALLED_APPS', tambahkan 'main' ke dalam variabel tersebut.

    Implementasi Dasar Template, Models, dan Views
    1. Buat direktori baru di dalam direktori 'main' dengan nama 'templates'. Buat pula berkas dengan nama 'main.html' pada direktori tersebut.
    2. Isi berkas 'main.html' dengan informasi yang ingin ditampilkan, misalnya nama aplikasi, nama produk, jumlah, dan deskripsinya. 
    3. Pada implementasi models dilakukan pemasukan atribut-atribut yang akan digunakan nanti, seperti name, amount, description. Atribut-atribut ini harus didefinisikan dengan tipe yang sesuai, misal variabel 'name' dengan tipe CharField, 'amount' dengan tipe IntegerField, dan 'description' dengan tipe TextField.
    4. Lakukan migrasi model dengan menjalankan 'python manage.py makemigrations' dan 'python manage.py migrate'. Migrasi perlu dilakukan tiap kali model dimodifikasi.
    5. Menghubungkan view dengan template, dengan cara buka berkas view.py pada direktori 'main', lalu tambahkan baris impor 'from django.shortcuts import render'. Fungsinya untuk merender tampilan HTML serdasarkan data yang ada.
    6. Membuat fungsi 'show_main' dengan parameter 'request', tujuannya untuk memproses request HTTP dan mereturn tampilannya. Kodenya adalah sebagai berikut:
        def show_main(request):
            context = {
                'myname': 'Gina Afia',
                'myclass': 'PBP B',
                'name': 'Six of Crows',
                'description': 'Young adult fantasy series'
                'amount': '5'
            }

        return render(request, "main.html", context)
    7. Memodifikasi template dengan mengubah data yang sebelumnya dibuat secara statis menjadi kode Django sebagai contoh data sebelumnya yaitu: 
        <p>Six of Crows<p>
        maka harus diubah menjadi
        <p>{{ name }}<p>
        berdasarkan variabel atribut yang ada di models.py

    Mengonfigurasi routing URL
    1. Mengatur routing URL dilakukan agar aplikasi 'main' dapat diakses melalui peramban web. Langkahnya adalah membuat berkas 'urls.py' pada direktori 'main'.
    2. Isi berkas tersebut dengan kode berikut:
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    Fungsi 'urls.py' pada direktori main adalah bertanggung jawab mengatur rute URL pada tingkat aplikasi 'main'.
    3. Pada direktori proyek juga terdapat berkas 'urls.py', buka berkas tersebut lalu impor fungsi include dari django.urls.
    4. Tambahkan kode berikut:
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]
    Fungsinya 'urls.py' pada direktori proyek adalah bertanggung jawab mengatur rute URL tingkat proyek.
    5. Jalankan perintah 'python manage.py runserver' pada Command Prompt, lalu buka tautan http://localhost:8000/main/ untuk melihat tampilan halaman yang telah dibuat.

    Melakukan testing terhadap path '/main/' untuk mengetahui apakah path dapat diakses dan apakah dirender menggunakan template 'main.html'.
    1. Mengisi berkas tests.py pada direktori 'main' dengan kode berikut:
        from django.test import TestCase, Client

        class mainTest(TestCase):
            def test_main_url_is_exist(self):
                response = Client().get('/main/')
                self.assertEqual(response.status_code, 200)

            def test_main_using_main_template(self):
                response = Client().get('/main/')
                self.assertTemplateUsed(response, 'main.html')

    2. Menambahkan testing lain selain yang ada di tutorial: yaitu testing yang memeriksa apakah stok buku masih tersedia seperti berikut:
        def test_item_stock_is_exist(self): # Periksa apakah stok buku masih ada
            response = Client().get('/main/')
            self.assertNotEqual(response.context['amount'], 0)

    Perbaharui repositori GitHub
    1. Lakukan add, commit, dan push tiap kali melakukan perubahan atau modifikasi.

    Melakukan deployment ke Addaptable
    1. Buka laman Adaptable.io dan login menggunakan akun GitHub
    2. Tekan tombol "New App"
    3. Pilih "Connect an Existing Repository"
    4. Pada proses instalasi, pilih "All Repositories"
    5. Pilih repository proyek sebagai basis aplikasi, lalu pilih branch yang ingin di deploy, yaitu "main"
    6. Pilih template deployment "Python App Template"
    7. Pilih basis data "PosteSQL"
    8. Masukkan versi python 
    9. Jalankan perintah "python manage.py migrate && gunicorn <NAMA_DIREKTORI_PROYEK>.wsgi" pada Command Prompt
    10. Masukan nama aplikasi 
    11. Centang bagian "HTTP Listener on PORT", lalu tekan "Deploy App"

    Membuat README.md
    1. Tambahkan berkas 'README.md' pada direktori utama, berkas ini berisi jawaban dari soal-soal yang diberikan.
    2. Lakukan git add, commit, dan push kembali


- Bagan:
    ![This is an image](https://github.com/ginafia/tugas-2/blob/6122e48cbb7d31787e8e0ba94e203c6371fa339c/bagan%20tugas%202.png)
    1. Klien membuat request ke aplikasi web Django dengan mengakses URL tertentu
    2. Routing pada "urls.py", dimana berkas ini akan menangani request klien dengan memetakan URL dari klien ke fungsi tampilan pada berkas "views.py"
    3. Berkas "views.py" akan menentukan fungsi yang sesuai dengan request URL klien, berkas ini juga berinteraksi dengan model, dan merender berkas HTML
    4. Berkas HTML dikirimkan dalam bentuk tampilan browser kepada klien


- Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual Environment berfungsi menciptakan lingkungan terisolasi yang tidak bisa diakses dari luar. Program yang berjalan di dalamnya pun memiliki modul-modul tersendiri sesuai versinya. Tujuan penggunaan virtual environment adalah sebagai pengelola dependensi, menjadi wadah bagi aplikasi yang dibuat dari berbagai versi Django agar tetap dapat beroperasi meskipun versi modul global sudah berubah/diupdate.

    Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Aplikasi yang dibuat akan mengakses modul yang terinstal secara global, namun akibatnya aplikasi akan sulit dioperasikan apabila versi modul diupdate di kemudian hari.

- Penjelasan
    MVC (Model-View-Controller)
    Model = Berisi data dan logika bisnis dalam aplikasi
    View = Menampilkan data ke pengguna dan merespon tindakan pengguna
    Controller = Mengontrol alur program, menerima dan memproses input dari pengguna, dan berinteraksi dengan model

    MVT (Model-View-Template) = 
    Model = Berisi data dan logika bisnis dalam aplikasi
    View = Menampilkan data ke pengguna dan merespon tindakan pengguna
    Template = Berisi tampilan interface yang menghubungkan data dari model ke view

    MVVM (Model-View-ViewModel) = 
    Model = Berisi data dan logika bisnis dalam aplikasi
    View = Manampilkan data ke pengguna
    ViewModel = Sebagai perantara antara model dan view, mengelola tampilan data dari model dan merespon input pengguna.
