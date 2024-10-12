"""

Proje 3
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

1.adım-> Genellikle ilk eleman root olarak seçilir. Biz de öyle yapalım. root = 7
2.adım->   7
          /
        5
3.adım->    7
          /  
        5 
       /
      1   
4.adım->   7
          / \
        5    8
       /
      1   
5.adım->   7
          / \
        5    8
       / 
      1
       \
        3  
6.adım->   7
          / \
        5    8
       / \
      1   6
       \
        3  
7.adım->   7
          / \
        5    8
       / \
      1   6
     / \
    0   3  
8.adım->   7
          / \
        5    8
       / \    \
      1   6    9
     / \
    0   3  
9.adım->   7
          / \
        5    8
       / \    \
      1   6    9
     / \
    0   3 
         \
          4 
10.adım->  7
          / \
        5    8
       / \    \
      1   6    9
     / \
    0   3 
       / \
      2   4 
      
 Not! Mesela 10.adımda 4'ü eklememiz gerekiyor. Önce root'a bakıyoruz 4'ten büyük mü küçük mü diye. Küçük bu yüzden sol alt ağaca
iniyoruz. 4, 5'ten büyük mü küçük mü? Elbette küçük bu yüzden 5'in de sol alt ağacına iniyoruz. Sonrasında 4 için 1'e bakıyoruz,
4, 1'den büyük bu yüzden sağ alt ağaca iniyoruz. Son olarak 4, 3'ten büyük olduğu için sağ alta yerleştirdik.






"""
