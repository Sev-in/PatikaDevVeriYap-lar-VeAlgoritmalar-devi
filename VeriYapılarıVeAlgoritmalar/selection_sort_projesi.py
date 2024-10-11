
"""

Proje 1
[22,27,16,2,18,6] -> Insertion Sort
Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

1.adım-> Aynı kalır. [22,27,16,2,18,6]
2.adım-> 16 ile 27 yer değiştirir. [22,16,27,2,18,6]
3.adım-> 16 ile 22 yer değiştirir. [16,22,27,2,18,6]
4.adım-> 2 ile 27 yer değiştirir. [16,22,2,27,18,6]
5.adım-> 2 ile 22 yer değiştirir. [16,2,22,27,18,6]
6.adım-> 2 ile 16 yer değiştirir. [2,16,22,27,18,6]
7.adım-> 18 ile 27 yer değiştirir. [2,16,22,18,27,6]
8.adım-> 18 ile 22 yer değiştirir. [2,16,18,22,27,6]
9.adım-> 6 ile 27 yer değiştirir. [2,16,18,22,6,27]
10.adım-> 6 ile 22 yer değiştirir. [2,16,18,6,22,27]
11.adım-> 6 ile 18 yer değiştirir. [2,16,6,18,22,27]
12.adım-> 6 ile 16 yer değiştirir. [2,6,16,18,22,27]




Big-O gösterimini yazınız.
Big-O gösterimi selection sort için worst case ve avarege case değeri O(n^2) ama best case için O(n) çünkü hepsinin sıralandığını 
varsayıyoruz.
Bu durumda hepsi sıralanmış değildir. Bu yüzden Big-O notasyonumuz O(n^2) olur.




Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

1.Average case: Aradığımız sayının ortada olması
2.Worst case: Aradığımız sayının sonda olması
3.Best case: Aradığımız sayının dizinin en başında olması.

1.Avarage case olur.




[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

1.adım-> En küçük eleman bulunur ve en başa konulur.(2 ile 7 yer değiştirdi) [2,3,5,8,7,9,4,15,6]
2.adım-> Küçükten büyüğe sıraladığımızda oluşan 2.elemanı buluyoruz ve 2.sıraya koyuyoruz. [2,3,5,8,7,9,4,15,6]
3.adım-> Küçükten büyüğe sıraladığımızda oluşan 3.elemanı buluyoruz ve 3.sıraya koyuyoruz.(4 ile 5 yer değiştirdi) [2,3,4,8,7,9,5,15,6]
4.adım-> Küçükten büyüğe sıraladığımızda oluşan 4.elemanı buluyoruz ve 4.sıraya koyuyoruz.(5 ile 8 yer değiştirdi) [2,3,4,5,7,9,8,15,6]
"""

