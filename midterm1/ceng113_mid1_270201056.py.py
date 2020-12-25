x = input("Enter a file path:")

while x != quit:
  
    


  letters= input("Enter a list of letters:")
  a = letters.lower()
  print(a)
  search=[]
  search1=()
  for i in range(len(a)):
    if a[i] == "a" or "b"or "c"or "d"or "e"or "f"or "g"or "h"or "i"or "k"or "l"or "m"or "n"or "o"or"p"or "q"or"r"or"s"or "t"or "u"or "v"or "w"or "x"or "y"or "z":
      search.append(a[i])
    else :
      search.remove(a[i])
  search
  print(search)

  if x == "story1":
    story = open("story1","r")
    a = story.readlines()
    search= letters
    search_words= []
    story_words1= a[0].split(" ")
    for i in range(len(story_words1)):
      count = story_words1[i].find(search)
      if count>= 0 :
        search_words.append(story_words1[i])   
    for z in range(len(search_words)):
      search_words[z] = search_words[z].replace(".","")
      search_words[z] = search_words[z].replace("“","")
      search_words[z] = search_words[z].replace("”\n","")
      search_words[z] = search_words[z].replace("”","")
      search_words[z] = search_words[z].replace("'","")
      search_words[z] = search_words[z].replace(",","")
      search_words[z] = search_words[z].replace("’","")
      search_words[z] = search_words[z].replace("‘","")
    lens=[]
    for z in range(len(search_words)):
      lena = len(search_words[z])
      lens.append(lena)
    long=max(lens)
    a=lens.index(long)
    print(search,":",search_words[a])
    story.close()

  elif x == "story2":
    story = open("story2","r")
    a = story.readlines()
    search= letters
    search_words= []
    story_words1= a[0].split(" ")
    for i in range(len(story_words1)):
      count = story_words1[i].find(search)
      if count>= 0 :
        search_words.append(story_words1[i])   
    for z in range(len(search_words)):
      search_words[z] = search_words[z].replace(".","")
      search_words[z] = search_words[z].replace("“","")
      search_words[z] = search_words[z].replace("”\n","")
      search_words[z] = search_words[z].replace("”","")
      search_words[z] = search_words[z].replace("'","")
      search_words[z] = search_words[z].replace(",","")
      search_words[z] = search_words[z].replace("’","")
      search_words[z] = search_words[z].replace("‘","")
    lens=[]
    for z in range(len(search_words)):
      lena = len(search_words[z])
      lens.append(lena)
    long=max(lens)
    a=lens.index(long)
    print(search,":",search_words[a])

  story.close()
    
  
  x = input("Enter *path* for a new path, *list* for a new list of letters and *quit* to quit:list")




#if search in 
#find = story_words1.find(search)
#print(find)

#story_words = story.remove(",")



#Once upon a time, a young man named Sunan was traveling aimlessly when he came upon an old beggar at the side of a lonely road. Sunan's heart went out to the man. He stopped and said, “Sir, I have little, but I wish to share my bread and water with you. Eat heartily.”
#The beggar ate, and when he was finished, Sunan bowed and prepared to leave, but the man seized his hand. “Wait, I wish to thank you properly for your generosity. I offer you a magic spell that will be useful to you.”


#The room was lit by light coming through cracks in the scaffold floor above, and, significantly, from around the edges of the large trapdoor. The hinges of said door were being carefully oiled by a man in a hood.
#He stopped when he saw the party had arrived and said, “Good morning, Mr. Spangler.” He raised the hood helpfully. “It’s me, sir, Daniel ‘One Drop’ Trooper. I am your executioner for today, sir. Don’t you worry, sir. I’ve hanged dozens of people. We’ll soon have you out of here.”

