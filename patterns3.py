n = 5
m = 0
for i in range(1,n+1):
  for j in range(1,n+1):
      if j<=i:
        print(chr(65+m),end=" ")
        
  m= m+1
  print()
          
      
