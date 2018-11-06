Program 


Fungsi yang digunakan:
	Baca(I,x,y): yang berfungsi membentuk list dengan isi berupa kumpulan titik-titik dari grafik yang akan dibuat
	Translate(a,b): berfungsi untuk melakukan translasi pada bangunan geometri sebesar a terhadap sumbu x dan sebesar b terhadap sumbu y
	Dilate(k): berfungsi untuk dilatasi objek dengan factor scalling sebesar k
	Rotate(deg, a, b): berfungsi untuk merotasi objek sebesar deg derajat dan diputar dengan sumbu rotasi pada titik(a,b)
	Reflect(param): berfungsi untuk merefleksi objek sesuai masukan param bisa terhapa sumbu y, sumbu x, y=x, y=-x, dan lain sebagainya.
	Shear(param,k): berfungsi untuk menggeser objek dengan param sebagai acuan digeser pada sumbu y atau x dan k sebagai besar pergeseran
	Stretch(param,k): berfungsi untuk menggeser objek dengan factor pengali sebesar k dan mengacu pada param pergeserannya apakah dia pada sumbu x atau pada sumbu y
	Custom(a,b,c,d): berfungsi untuk melakukan transformasi linier pada objek dengan matriks(a,b,c,d)
	Multiple(n): berfungsi untuk melakukan serangkaian perintah diatas secara sekaligus
	Reset(): berfungsi mengembalikan objek kepada keadaan semula
	Exit(): berfungsi untuk keluar dari program
	Kotak(): berfungsi untuk membuat bentuk geometri
	Menu(): berfungsi sebagai penjalan program dan pengeksekusiannya 

Atribut yang digunakan:
	Vertices : untuk menyimpan titik yang akan membentuk geometri
	Simpanan:untuk menyimpan keadaan awal dari titik yang dibentuk
	Edges: untuk menyimpan hubungan antar titik
