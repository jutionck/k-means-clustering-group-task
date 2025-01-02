# K-Means Clustering

Dataset ini dibuat secara random menggunakan python dan harusnya data dapat di dapat dari referensi seperti https://www.kaggle.com/ dan lainnya.

## Persiapan Dataset Dummy

Jalankan file `create_random_data.py` untuk menggenarate data yang akan di uji dengan `K-Means`.

Jalankan dengan perintah:

```bash
python create_random_data.py
```

Jika berhasil akan menghasilkan data dalam bentuk `.csv` berikut contoh sample datanya:

```csv
CustomerID,Age,Annual Income (k$),Spending Score (1-100)
1,56,115,82
2,46,26,91
3,32,81,34
4,60,79,91
5,25,88,17
6,38,57,43
7,56,58,59
8,36,43,51
9,40,26,54
10,28,109,24
11,28,60,25
12,41,144,71
13,53,49,52
14,57,95,70
15,41,104,88
16,20,22,33
17,39,107,49
18,19,104,29
```

## Pengujian Dataset

Setelah dataset tersedia berikutnya dilakukan pengujian, jalankan file `index.py` untuk membentuk beberapa `figure` mulai dari:

-
- Analisis Klaster memberikan wawasan mendalam untuk setiap segmen pelanggan, membantu pengambilan keputusan bisnis seperti:
  - Menargetkan pelanggan dengan promosi tertentu.
  - Mengidentifikasi pelanggan potensial untuk program loyalitas.

### Elbow Method

Elbow Method menentukan jumlah klaster optimal berdasarkan perubahan inertia.

![Elbow Method](assets/Elbow%20Method.png)

## K-Means Clustering

Analisis Klaster memberikan wawasan mendalam untuk setiap segmen pelanggan, membantu pengambilan keputusan bisnis seperti:

- Menargetkan pelanggan dengan promosi tertentu.
- Mengidentifikasi pelanggan potensial untuk program loyalitas.

![K-Means Clustering](<assets/K-Means%20Clustering%20(k=3).png>)
