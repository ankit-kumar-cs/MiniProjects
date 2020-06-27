flames=['f','l','a','m','e','s']
name_1=list(input('Enter First Person Name:').lower())
name_2=list(input('Enter Second Person Name:').lower())
count=0
for i in name_1:
  if i in name_2:
    name_2.remove(i)
    count+=1
result=(len(name_1)-count)+len(name_2)
while len(flames)!=1:
  x=len(flames)
  index=result%x
  if index==0:
    index=x-1
  else:
    index-=1
  flames=flames[index+1:]+flames[:index]
if flames[0]=='f':
  print('Friends')
elif flames[0]=='l':
  print("Love")
elif flames[0]=='a':
  print("Affection")
elif flames[0]=='m':
  print('Marry')
elif flames[0]=='e':
  print('Enemy')
elif flames[0]=='s':
  print('Siblings')
