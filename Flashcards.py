class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        #we will return a string
        return self.word+'('+self.meaning+')'
    flash=[]
    print("Welcome to the flashcard application")
    #the following loop will be repeates until 
    #user stops to add flashcards
    while(True):
        word=input("enter name you want to add in the flashcard")
        meaning=input("enter the meaning of the word:")
        flash.append(flashcard(word,meaning))
        option=int(input("enter 0,if you want to add another flash card otherwise enter 1:"))
        if(option):
            break
    print("\nYour flashcards")
    for i in flash:
      print(">",i)
                