import time

startMessage = "Great then. Lets start."
yes = ["y", "yes", "ya", "yep", "yup", "yaaaas", "totally", "totes", "sure", "you bet", "certainly", "definitely", "of course", "gladly", "indubitably", "absolutely", "indeed", "undoubtedly", "yeah, yeah, yeah", "fine", "affirmative", "very well", "obbviously", "aye", "forsooth", "yea", "verily", "surely", "why not", "https://www.inklyo.com/ways-to-say-yes-in-english/", "..."]
no =  ["n", "no", "certainly not", "by no means", "of course not", "not really", "no way", "no dice", "nope", "nah", "nay", "nix", "no can do", "not likely", "of course not", "over my dead body", "https://www.macmillandictionary.com/us/thesaurus-category/american/ways-of-saying-no"]
saveFile = open("saveFile.txt", "w+")

def start():
  file = open("file.txt", "w+");
  file.write("I hope this didn't take you too long.")
  print("..-. .. .-.. . .-.-.- - -..- -")

def yesOrNo(ans):
  if ans.lower() in yes:
    return "y"
  if ans.lower() in no:
    return "n"

ready = raw_input("This is a game. Are you ready? (hint, google is your friend) (y/n) ")
if yesOrNo(ready) == "n":
  time.sleep(3)
  ready = raw_input("Are you ready now? (y/n) ")
  if yesOrNo(ready) == "n":
    time.sleep(1)
    while yesOrNo(ready) == "n":
      time.sleep(1)
      ready = raw_input("How about now? (y/n) ")
    print(startMessage)
  elif yesOrNo(ready) == "y":
    print(startMessage)
    start()
elif yesOrNo(ready) == "y":
  print(startMessage)
  start()
