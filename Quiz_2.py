
def get_animal(kind_of_sound):

   if kind_of_sound == "meow":
       return "Cat"
   elif kind_of_sound == "woof":
       return "Dog"  
   elif kind_of_sound == "quack":
       return "Duck"
   else:
       return "I don't recognize the animal sound" 

   
print("Welcome to the Animal Wizard!")
print("Do you want to be amazed?") 


kind_of_sound = str(input("Please enter you favorite animal sound and I will try to guess the animal for you: "))   
 
bot_response = get_animal(kind_of_sound)
print(bot_response)


