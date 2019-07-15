zz = input()
if ((zz>'a' and zz<='z')or(zz>='A' and zz<='Z')):
  if(zz == 'a' or zz == 'e' or zz == 'i' or zz == 'o' or zz == 'u' or zz == 'A' or zz == 'E' or zz == 'I' or zz == 'O' or zz == 'U'):
  print('Vowel')
  else:
    print('Consonant')
else:
    print('Invalid')
