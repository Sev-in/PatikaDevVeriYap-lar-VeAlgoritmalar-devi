
"""
Proje 2
[16,21,11,8,12,22] -> Merge Sort 

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
1.adım-> Öncelikle diziyi ikiye bölüyoruz. [16,21,11] , [8,12,22]
2.adım-> Böldüğümüz dizileri de ikiye bölüyoruz. [16,21] , [11] ; [8,12] , [22]
3.adım-> Tek eleman kalana kadar bölmeye devam ediyoruz. [16] , [21] ; [11]    ;   [8] , [12] ; [22]
4.adım-> Birbirinden en son ayrılan elemanları sıralamakla başlıyoruz.  [16,21] ; [11]    ;   [8,12] ; [22]
5.adım-> 2.adımda ayırdığımız elemanları sıralıyoruz. [11,16,21] ;   [8,12,22]
6.adım-> 1.adımda ayırdığımız elemanları sıralıyoruz. [8,11,12,16,21,22]

Big-O gösterimini yazınız.
İkiye bölerek ayırdığımız için O(logn) 
Sonra birleştirdiğimiz için O(n)
Sonuç = O(nlogn)

"""
