# Soal 

## Instruction

Dikerjakan dalam format notebook isi notebook harus mengikuti outline ini :

- Perkenalan (Introduction)  
  Terdiri dari nama, batch dan objective.  
- Jawaban (Answer)  
  Gunakan markdown dan code untuk menjabarkan pertanyaan, jawaban dan penjelasan kode dengan `docstring` dan `comment`.

## Assignment Instructions and Cases

Eras Tour Concert sudah ada di bioskop namun memiliki rate movie R yaitu sebuah rate dimana seseorang berumur dibawah 17 tahun memerlukan pendampingan orang tua atau wali dewasa. Tugasmu adalah menentukan status apakah penonton tersebut perlu ditemani orang tua atau tidak. 


```py
Input : "2010-01-02"
Process : 
Maka umur dia adalah 13 tahun. 
Output : True 

Input : "2000-01-01"
Process : 
Maka umur dia adalah 23 tahun. 
Output : False

Input : "2006-12-30"
Process : 
Maka umur dia adalah 16 tahun,  
umurnya terhitung 16 karena dia belum ulang tahun pada tahun ini.
Output : True

Input : "2006-09-30"
Process : 
Maka umur dia adalah 17 tahun.
Output : False
```

Selain itu harga ticket konser terdapat beberapa kategori dan kualifikasi : 

- Jika penonton berumur diatas (>=) 17 tahun dan VIP maka harga tiket 200.000
- Jika penonton berumur dibawah 17 tahun dan VIP maka harga tiket 180.000
- Jika penonton menonon dengan kategori Regular maka harga tiket 100.000 

Tugasmu adalah menghitung total biaya

```py
Input :
Diberikan informasi berikut 
"2010-01-02" "VIP"
"2000-01-01" "VIP"

Process : 
Maka pembayaran tiket adalah 180.000 dan 200.000 

Output : 
380000
```