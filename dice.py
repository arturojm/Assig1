from random import *

aux = True

while(aux):
  opt = raw_input('Would you like to roll the dice? Y/N:  ')
  if(opt.lower() == 'y'):
    print ("Dice result: %s \n") % randrange(1,6)
  elif (opt.lower() == 'n'):
    print ("Good Bye!!")
    aux = False
  else:
    print ('Try again... \n')
exit()
