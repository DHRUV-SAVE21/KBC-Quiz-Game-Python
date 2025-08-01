#KBC
#Questions written in the form of list [{""}]
questions=[
{
"Question":"What is the name of first president of India?",
"options":["Narendra Modi","Rajiv Gandhi","Pandit jawaralal nehru","N.P Shah"],
"Correctanswer":3
},
{
  "Question":"Who won the Ipl final of 2024?",
  "options":["KKR","MI","SRH","CSK"],
  "Correctanswer":1
},
{
  "Question":"What is the Full form of CSS in terms of Styling??",
  "options":["Client Side Scripting","Cascading Style Sheet","Client Side Sheet","Cascading Sheet Style"],
  "Correctanswer":2
},
{
  "Question":"Which of the following is the unit of electrical conductance?",
  "options":["Ohm","Siemens" ,"Ampere", "Volt"],
  "Correctanswer":2
},

]
print(type(questions))

def ask_question(question,options,correct_index):
  print("\n")
  print(question)
  
  for i,option in enumerate(options):
    print(f"{i+1}.{option}")                        #Formulated string 
  user_answer=int(input("Enter the correct answer(1,2,3,4):"))
  if user_answer==correct_index:
    print("Correct!")
    #print("Score:",i+1)
    return True
  else:
    print("Incorrect!")
    return False
  
def play_game():
  score=0
  for question in questions:
    if ask_question(question["Question"],question["options"],question["Correctanswer"]):
      score =score+1
  print(f"You scored {score} out of {len(questions)}.")

play_game()