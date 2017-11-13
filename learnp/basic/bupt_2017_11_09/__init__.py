a =str(99*91)
l = ((len(a)-1)>>1)+1
print("a[:{}]({}) == a[{}:]{}".format(l,a[:((len(a)-1)>>1)+1],((len(a)-1)>>1),a[((len(a)-1)>>1):]))
print()
print(a[:((len(a)-1)>>1)+1] == a[(len(a)-1)>>1:][::-1])