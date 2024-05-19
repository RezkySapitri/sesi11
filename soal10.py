def cekAnagram(kata1, kata2):
    kata1_sort = sorted(kata1)
    kata2_sort = sorted(kata2)
    return kata1_sort == kata2_sort

kata1 = "listen"
kata2 = "silent"
print(cekAnagram(kata1, kata2))
