def mohan(a):
   b=a[0]
   for i in range(1,len(a)):   
      if a[i-1]==' ':
        b=b+a[i]
   b=b.upper()
   return b  # code for each string in the list

p =input("data:")
list1=p.split(",")
e=''
for c in range(0,len(list1)):
   d=list1[c]
   e=e+" "+mohan(d)
   c=c+1
print("List:",list1)
print(e)   

