import time
from codestuffdontread import end


print('You wake up to find pitchforks and fire coming to your house')
time.sleep(2)
print('The vliiagers are shouting "DEATH TO THE WITCH"')
time.sleep(5)
print('"Oh no", you think "They know the witch is here"')
time.sleep(7)
print('What do you want to do?')
time.sleep(2)
print('Type 1 To try to trick the villagers to set fire to A diffrent house')
print('Type 2 to try to set fire to them')
print('Type 3 to splash them in water')
print('Type 4 to run')
q1 = input("What do you want to do?: ")
if q1 == '1':
  print('You leave your house and start talking')
  time.sleep(2)
  print('"What witch?" You ask')
  time.sleep(2)
  print('"Dont play dumb with us" someone shouts back')
  time.sleep(2)
  print('"Ohhhh the one at tommys house" you reply')
  time.sleep(2)
  print('"No i dont have a witch at my house" tommy replys')
  time.sleep(2)
  print('"Ive seen it" you say')
  time.sleep(2)
  print('Tommy says "no you havent"')
  time.sleep(2)
  print('"You havent come out of your house in 3 days"')
  time.sleep(7)
  print('Your house is destoryed, and you are hanged for your crime')
  time.sleep(2)
  end()
if q1 == '2':
  time.sleep(2)
  print('How do you want to set them on fire')
  time.sleep(2)
  print('Type 1 to come out and use a candle to light them on fire')
  print('Type 2 to throw paper planes (with fire) at them')
  time.sleep(4)
  q22 = input('Whats your pic?: ')
  if q22 == '1':
    print('When lighting the candle you set fire to your self')
    time.sleep(2)
    print('You died')
    time.sleep(2)
    print('You have failed')
    time.sleep(2)
    print('Thanks for playing')
    time.sleep(10)
  if q22 == '2':
    print('After lighting the paper planes you thow them')
    time.sleep(2)
    print('You miss you target and hit a child')
    time.sleep(2)
    print('He runs seting fire to every one before jumping in to a river')
    time.sleep(2)
    print('The child lives but everyone else does not')
    time.sleep(2)
    print('You left the candle you used to light the plane under your bed and its now on fire')
    time.sleep(4)
    print('It sets fire to your house and you')
    time.sleep(2)
    print('You died for allmost killing a child')
    time.sleep(6)
    end()
if q1 == '3':
  time.sleep(4)
  print("How do you want to do it?")
  time.sleep(2)
  print('Type 1 to use the hose')
  print('type 2 to use some random jars filled with water')
  time.sleep(5)
  q13 = input("Whats your pic?")
  if q13 == '1':
    time.sleep(10)
    print('When you tern on the hose the pipes explode from under the vliagers and you knock them of there feet')
    time.sleep(2)
    print('The water puts out the fire')
    time.sleep(2)
    print('The villagers are running for you')
    time.sleep(2)
    print('What do you want to do?')
    time.sleep(4)
    print('Type 1 to run')
    print('Type 2 to eat a snack')
    print('Type 3 to do nothing')
    q23 = imput('Whats your pic?: ')
    if q23 == 2:
      time.sleep(2)
      print('Before geting your snack you get killed by the villagers')
      time.sleep(2)
      end()
    if q23 == 3:
      time.sleep(2)
      print('The villagers kill you')
      time.sleep(2)
      end()
  elif q13 == '2':
    time.sleep(2)
    print('The jars are not filled with water')
    time.sleep(6)
    print('The jars do nothing to the fire and your house is berned to the ground')
    time.sleep(3)
    end()