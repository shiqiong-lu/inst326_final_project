"""This script is allowing the user create their own quiz

"""
import csv
class Createquiz:
    """This class will allow user create their own quiz
    Attributes:
      questions(list):
      
    """
    def __init__(self):
        """ Initialize new Player object.

            Side effects:
                Sets attributes questions, answers,userkey,question_answer.
        """
        self.questions=[]
        self.answers=[]
        self.userkey=[]
        self.question_answer={}
           
    
        # fh = open ('quizdata.csv','w')
        # spreadsheet=csv.writer(fh)# create the csv handle
        # spreadsheet.writerow(["question","answer"])
    
    def get_question_answer(self,user_id):
        
        
      
            
        user_question=str(input("""Please built your question, hit "Enter" key to quit\n"""))
        self.questions.append(user_question)
        user_answer=str(input("""Please enter the answer for your question,hit "Enter" key to quit\n"""))
        self.answers.append(user_answer)
        while (user_question!=""or user_answer!=""):
            user_question=str(input("""Please built your question, hit "Enter" key to quit\n"""))
            self.questions.append(user_question)
            user_answer=str(input("""Please enter the answer for your question,hit "Enter" key to quit\n"""))
            self.answers.append(user_answer)
            # except ValueError:
            #     print("input must be a string")
        #print(self.questions,self.answers)
        for index in self.questions:
            if self.questions=="":
                continue
            else:
                self.userkey.append((user_id,index))
        #print(self.userkey)
        
        self.question_answer=dict(zip(self.userkey,self.answers))
        #print(self.question_answer)
        return self.question_answer
    
    def display_addquiz(self):
        print("Here are the questions and answers you built for your own quiz:")
        k=1
        for key,value in self.question_answer.items():
           
            print(f"Question:{k}. {key[1]} Answer: {value}")
            k+=1
        
if __name__ =="__main__":
    myquiz=Createquiz()
    myquiz.get_question_answer("Shiqiong")
    myquiz.display_addquiz()
        
        
        
        

