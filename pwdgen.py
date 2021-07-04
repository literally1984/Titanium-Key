import random
valnum = False
while valnum == False:
  print("How many characters do you want in your password? 10 characters and more usually creates a strong one.")
  pwdlen = input()
  if "0" in pwdlen or "1" in pwdlen or "2" in pwdlen or "3" in pwdlen or "4" in pwdlen or "5" in pwdlen or "6" in pwdlen or "7" in pwdlen or "8" in pwdlen or "9" in pwdlen:
    if "-" in pwdlen or pwdlen == "0":
      print("Enter a number greater than 0, please.")
      continue
    pwdlen = int(pwdlen)
    pwdlenguess = pwdlen
    pwdlenguesscont = pwdlen
    valnum = True
  else:
    print("Enter a valid number, please.")
print("Generating password...(this may take some time if the password length is very high)")
generationdict = {0:"5", 1:"3", 2:"8", 3:"1", 4:"6", 5:"7", 6:"4", 7:"9", 8:"2", 9:"0", 10:"t", 11:"b", 12:"u", 13:"R", 14:"N", 15:"T", 16:"d", 17:"U", 18:"G", 19:"I", 20:"y", 21:"s", 22:"B", 23:"L", 24:"X", 25:"A", 26:"k", 27:"g", 28:"D", 29:"V", 30:"v", 31:"m", 32:"o", 33:"Q", 34:"l", 35:"P", 36:"x", 37:"H", 38:"n", 39:"q", 40:"a", 41:"h", 42:"w", 43:"S", 44:"E", 45:"j", 46:"p", 47:"Y", 48:"r", 49:"c", 50:"f", 51:"C", 52:"F", 53:"i", 54:"W", 55:"z", 56:"M", 57:"e", 58:"J", 59:"K", 60:"O", 61:"Z", 62:"`", 63:"~", 64:"!", 65:"@", 66:"#", 67:"$", 68:"%", 69:"^", 70:"&", 71:"*", 72:"(", 73:")", 74:"-", 75:"_", 76:"+", 77:"=", 78:"[", 79:"{", 80:"]", 81:"}", 82:"\\", 83:"|", 84:";", 85:":", 86:"'", 87:"\"", 88:",", 89:"<", 90:".", 91:">", 92:"/", 93:"?"}
finalpwd = ""
while pwdlen > 0:
  rando = random.randrange(0,94)
  finalpwd = finalpwd + generationdict[rando]
  pwdlen -= 1
print("Your password: " + finalpwd)
valresponse = False
numtimes = 1000000000
guessedpwd = ""
corrguessornot = False
noornot = False
realnumtimes = 0
while valresponse == False:
  if corrguessornot == True:
    break
  yesorno = input("Should I check how strong the password is by trying to guess it? (keep in mind that this process could take an extremely long time) Y/N ")
  if yesorno == "Y":
    while numtimes > 0:
      if corrguessornot == True:
        break
      while pwdlenguess > 0:
        rando = random.randrange(0,94)
        guessedpwd = guessedpwd + generationdict[rando]
        pwdlenguess -= 1
        if guessedpwd == finalpwd:
          corrguessornot = True
          break
      pwdlenguess = pwdlenguesscont
      guessedpwd = ""
      numtimes -= 1
      realnumtimes += 1
  elif yesorno == "N":
    noornot = True
    break
  else:
    print("Enter either 'Y' for yes or 'N' for no, please.")
if corrguessornot == True:
  print("Oops, the generated password wasn't strong enough and was guessed in " + str(realnumtimes) + " guesses. Try generating a new password, and/or increasing the length of your generated password next time.")
elif corrguessornot == False and noornot == False:
  print("The generated password wasn't guessed in one billion guesses! This will make your password harder to crack in case of a hacker using a brute force attack.")
