"""This script is allowing the user create their own quiz

"""
import csv
class Createquiz:
    """This class will allow user create their own quiz
    Attributes:
      path(str): a csv file which allow to write in the quiz questions and answer
      
    """
    def __init__(self):
        """ Initialize new Player object.

            Side effects:
                Sets attributes name, position.
           """
           
    
        # fh = open ('quizdata.csv','w')
        # spreadsheet=csv.writer(fh)# create the csv handle
        # spreadsheet.writerow(["question","answer"])
    
    def get_question_answer(self,user_id):
        questions=[]
        answers=[]
        userkey=[]
        question_answer={}
        
      
            
        user_question=str(input("""Please built your question, hit "Enter" key to quit\n"""))
        questions.append(user_question)
        user_answer=str(input("""Please enter the answer for your question,hit "Enter" key to quit\n"""))
        answers.append(user_answer)
        while (user_question!=""or user_answer!=""):
            user_question=str(input("""Please built your question, hit "Enter" key to quit\n"""))
            questions.append(user_question)
            user_answer=str(input("""Please enter the answer for your question,hit "Enter" key to quit\n"""))
            answers.append(user_answer)
            # except ValueError:
            #     print("input must be a string")
        print(questions,answers)
        for index in questions:
            userkey.append((user_id,index))
        print(userkey)
        
        question_answer=dict(zip(userkey,answers))
        print(question_answer)
    #def display_quiz(self):
        
        
            
        
        
if __name__ =="__main__":
    myquiz=Createquiz()
    myquiz.get_question_answer("Joanna")
        
        

