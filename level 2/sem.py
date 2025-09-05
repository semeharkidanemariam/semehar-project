phrase= "welcome to the quiz spot"
print(phrase.upper())

def quiz():
         ans_count = 0
         
         #question 2

         print("1. what is the capital city of france \n"
        "a. roman\n" \
        "b. paris \n" \
        "c. brazil \n" \
        "d. addis ababa")
         choose = input("make a choice:")
         if  choose =="b":
           print("you are right")
           ans_count += 1
         else:
                print("you are not correct")
         # question 2 
         print(" 2.what is the power of house cell\n"
                   "A.mithocondria\n"\
                   "B. ribosom\n"\
                   "C.protien\n"\
                   "D. none\n")
         choose = input("make a choice:") 
         if choose.lower() == "a":
                print("you are correct")
                ans_count += 1
         else:
                print("you are not correct") 
         # question 3 
         print("3. how many countery in africa \n"
               "A. 34\n"
               "B.67\n"
               "C.54\n"
               "D.89 ") 
         choose = input("make a choice:")
         if choose.lower() == "c":
                print("you are correct")
                ans_count += 1
         else:
                print("you are not correct")                   
        

         print("your score is " + str(ans_count) +"/3")
quiz()             
     
    
      


                  


