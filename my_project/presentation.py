#import Information.people.student as info
from Information.people.student import student_information
import people

if __name__=="__main__":
    print("Hi I am currently in the presentation script:")
    student_information("Kai",age=40)
    people.student_information("Joe",age=35)