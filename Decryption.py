import random

ogdict= ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','1','2','3','4','5','6','7','8','9','0',' ','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|', ':',';','"','<',',','.', '>','?','\n','\t','\'','\r','\v','\f', '–','’', 'ł','í','¿','é' ]



x = len(ogdict)


plainText= open('encryption2.txt', 'r')


def decrypt2(plainText):

  #print(ogdict)

  print('How many monkeys are jumping on the bed?')

  y = int(input())

  newdict = ogdict[y:]+ogdict[:y]

  newdict2 = newdict[:-y]+newdict[-y:]


  decryption= " "

 

  f= open('decryption2.txt','w')

  for line in plainText:

    for a in line:

      bindex = newdict.index(a)

      if bindex is not False:

        decryption = decryption + ogdict[bindex]

      else:

        decryption = decryption + a

  w = f.write(decryption)

 #print(newdict2)

  #print(decryption)

  f.close

  plainText.close


decrypt2(plainText)




#Written using the “repl.it” Python 3 IDE
