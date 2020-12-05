#Alisson Fortis Sanchez
#Shiqiong Lu and Hung
def get_user_info():
    """This function will ask user's name.
    Returns:
       user_id(str): the name of the user.
    """
    user_id=input("Please enter your name: ")
    
    return user_id

def presentquestions_getchoices():
    '''Display questions and choices, record answers from user
    
    Args:
        field (int): field choice
        cube_texture (int): cube texture choice
        cube_color (int): cube color choice
        cube_other (int): possible other cube choices
        ladder_length (int): ladder length choice
        ladder_dist (int): ladder distance choice
        ladder_dist_cube (int): ladder distance to cube choice
        ladder_mat (int): ladder material choice
        horse_act (int): horse activity choice
        horse_col (int): horse color choice
        flowers (int): flowers choice
        weather (int): weather choice
        storm_inten (int): storm intensity choice
        storm_loc (int): storm location choice
        
    Returns:
        field (int): field choice
        cube_texture (int): cube texture choice
        cube_color (int): cube color choice
        cube_other (int): possible other cube choices
        ladder_length (int): ladder length choice
        ladder_dist (int): ladder distance choice
        ladder_dist_cube (int): ladder distance to cube choice
        ladder_mat (int): ladder material choice
        horse_act (int): horse activity choice
        horse_col (int): horse color choice
        flowers (int): flowers choice
        weather (int): weather choice
        storm_inten (int): storm intensity choice
        storm_loc (int): storm location choice
    '''
    print("Please enter the corresponding number for each answer choice")
    
    field = int(input('Think of an open field. Is it (1) dry and dead, (2) grassy and healthy, or (3) well-trimmed? '))
    cube_texture = int(input('Think of a cube. Is it (1) smooth, (2) rough, or (3) bumpy/spiky? '))
    cube_color = int(input('Is the cube (1) red, (2) yellow, (3) blue, (4) violet, (5) grey, (6) black, or (7) white? '))
    cube_other = int(input('Is the cube (1) transparent, (2) made out of water/ice, (3) hollow, or (4) made out of metal/rock? '))
    ladder_length = int(input('Think of a ladder. Is it (1) short or (2) long? '))
    ladder_dist = int(input('Is the ladder (1) near or (2) far? '))
    ladder_dist_cube = int(input('Is the ladder (1) near the cube or (2) far from the cube? '))
    ladder_mat = int(input('Is the ladder made of (1) strong material or (2) weak material? '))
    horse_act = int(input('Think of a horse. What is it doing? Is it (1) playing, (2) running, or (3) sleeping/grazing? '))
    horse_col = int(input('What color is the horse? Is it (1) brown, (2) black, or (3) white? '))
    flowers = int(input('Think of flowers. Are there (1) few or are they (2) everywhere? '))
    weather = int(input('Think of what the weather in the field is like. Is there (1) rain, (2) fog, (3) wind, or (4) sun? '))
    storm_inten = int(input('Think of a storm. Is it (1) mild or (2) strong? '))
    storm_loc = int(input('Is the storm (1) in the background or (2) right above the cube? '))
    
    return (field,cube_texture,
            cube_color,cube_other,
            ladder_length,ladder_dist,
            ladder_dist_cube,ladder_mat,
            horse_act,horse_col,flowers,weather,
            storm_inten,storm_loc)

class Quiz_results:
    '''Class will calculate and display results

    Args:
    * field_result(): 
    * cube_result ():Texture & Color
    * ladder_result(): Length & Distance
    * horse_result(): Activity & Color
    * flower_result(): Quantity
    * weather_result():Conditions
    * storm_result(): Location & Intensity

    Returns:
    * total_summary(): combination result of all factor results from quiz

    '''
    def __init__(self, field, cube_texture,cube_color, cube_other, ladder_length, ladder_dist, ladder_dist_cube, ladder_mat, horse_act, horse_col, flowers, weather, storm_inten, storm_loc):
        self.field = field
        self.cube_texture  = cube_texture
        self.cube_color = cube_color
        self.cube_other = cube_other
        self.ladder_length = ladder_length
        self.ladder_dist = ladder_dist
        self.ladder_dist_cube = ladder_dist_cube
        self.ladder_mat = ladder_mat
        self.horse_act = horse_act
        self.horse_col = horse_col
        self.flowers = flowers
        self.weather = weather
        self.storm_inten = storm_inten
        self.storm_loc = storm_loc

    # coded by Ann Hoang
    #Alisson Fortis Sanchez
    
    def field_result(self):
        
        field_representation = "The field represents your mind. Its size is the representation of your knowledge of the world, and how vast your personality is.\n"

        print (field_representation)
        
        dead_result = "Dry and Dead: You are feeling pessimistic."

        healthy_result = "Grassy and Healthy: You are feeling optimistic."

        trimmed_result = "Well-Trimmed: You are analytical and cautious."

        if self.field == "1" :
            return dead_result
        
        elif self.field == "2" :
            return healthy_result
        
        else:
            return trimmed_result
 
    def cube_texture_result (self):
        
        cube_representation = "The cube represents you. The size of the cube is your ego.\
        The surface of the cube represents what is visibly observable about your personality,\
        or maybe it is what you want others to think about you."

        print (cube_representation)
        
        # Texture
        smooth_result = "Smooth: You are a gentle person who takes care not to hurt others or make them feel uncomfortable."

        rough_result = "Rough: You are more straightforward. You tend to be honest in everything you say, no matter how it might affect the person you're talking to."

        bump_spike = "Bumpy or Spiky: You have a tendency to criticize others in an attempt to make them feel inferior to you."

        # If Cube Texture
        if self.cube_texture =="1":
            return smooth_result
        
        elif self.cube_texture == "2":
            return rough_result
        
        else:
            return bump_spike
        
    def cube_color_result (self):
        # Color
        red_result = "Red: You are physically active and enjoy rich sensory experiences."

        yellow_result = "Yellow: You are sociable and cherish your individuality."

        blue_result = "Blue: You are intelligent and respect others' ideals."

        violet_result = "Violet: You are intelligent and a bit of a perfectionist. You are also mysterious."
 
        grey_result = "Grey: You are self-confident, independent, and not easily rattled."

        black_result = "Black: You have a strong sense of individuality and independence, and you put a high value on alone time."

        white_result = "White: You are kind, independent, and self-reliant."
        
         #If Cube Color

        if self.cube_color == "1":
            return red_result
        
        elif self.cube_color == "2":
            return yellow_result
        
        elif self.cube_color == "3":
            return blue_result
        
        elif self.cube_color == "4":
            return violet_result

        elif self.cube_color == "5":
            return grey_result
        
        elif self.cube_color == "6":
            return black_result
        
        else:
            return white_result
        
    def ladder_length_result(self):
        
        ladder_representation = "The ladder represents two different aspects of your life—your goals and your friendships.\
        The location and material of your ladder can also tell you how close you are with your friends. "

        print(ladder_representation)
        
        # Length
        short_result = "Short: Your goals are realistic and simple."
        
        long_result = "Long: Your goals are more far fetched and difficult to attain."
         # If Ladder Lengths
        if self.ladder_length == "1":
            return(short_result)
        
        else:
            return(long_result)
    def ladder_distance_result(self):
         # Distance
        near_result = "Near: You are putting maximum effort and focus into achieving your goals."
        
        far_result = "Far: Your aren't putting much thought or effort into achieving your goals."
         # If Ladder Distance
        if self.ladder_dist == "1":
            return(near_result)
        
        else:
            return(far_result)
        
    def ladder_cube_result(self):
         # Ladder Distance
        near_ladder = "Near: If your ladder is near the cube, you are very close with your friends. \
        If it's actually leaning on the cube, it means your friends can lean on you for support."

        far_ladder = "Far: You have a hard time opening up to people and letting them get close to you."
         # If Ladder Cube Distance
        if self.ladder_dist_cube == "1":
            return(near_ladder)
        
        else:
            return(far_ladder)

    def ladder_material_result(self):
        # Ladder Material
        strong_ladder = "Strong: The stronger the material (e.g. stone, metal, etc.), the stronger the bond with those around you !"
        
        weak_ladder = "Weak: A weak ladder indicates a weak bond between you and those around you."
        # If Ladder Material
        if self.ladder_mat == "1":
            return(strong_ladder)
        
        else:
            return(weak_ladder)

    def horse_activity_result(self):
        horse_representation = "The horse represents your ideal partner."

        print(horse_representation)
        print("You horse choices represents the following:")
        
        # Activity
        playing_result = "Playing: Your ideal partner doesn't take life too seriously and or get bogged down by the little stuff."
        
        running_result = "Running: Your ideal partner will respect your space and give you the alone time that you crave."
        
        sleep_result = "Sleeping or Grazing: Your ideal partner is calm and fully committed to you."
        
        # If Horse Action
        if self.horse_act == "1":
            return(playing_result)
        
        elif self.horse_act == "2":
            return(running_result)
        
        else:
            return(sleep_result)
        
    def horse_color_result(self):
        # Color
        brown_horse = "Brown: You prize comfort and reliability above all else. Otherwise, you don't have a specific set of expectations for your partner."
        
        black_horse = "Black: Your idea partner is dominant, seductive, and sophisticated."
        
        white_horse = "White: You value loyalty and trust more than anything else in a relationship."
        
        # If Horse Color
        if self.horse_col == "1":
            return(brown_horse)
        
        elif self.horse_col == "2":
            return(black_horse)
        
        else:
            return(white_horse)
   
    def flower_result(self):
        '''
        Think of flowers.
        Where are the flowers in your field, and how many are there?
        '''
        flower_representation = "The flowers represent your family and friends."

        print(flower_representation)
        
        #Quantity
        few_results = "Just a Few: You are close with your family and have a small, tight-knit group of friends."

        everywhere_results = "They're Everywhere!:You're a social butterfly! With family and friends too numerous to count, you'll never be lonely."

        # If Flower Quantity
        if self.flowers == "1":
            return few_results

        else:
            return everywhere_results
  
    def weather_result(self):
        
        weather_representation = "The weather in your field reflects your general outlook on life."

        print(weather_representation)
        
        # Weather Conditions
        rain_result = "Rain: Rain symbolizes the problems in your life, thus the harder the rain, the bigger the problems."

        fog_result = "Fog: You feel uncertainty in life and may be struggling with your identity."

        wind_result = "Wind: Though you tend to worry about future issues, you generally don't let them get you down for long."
        
        sun_result = "Sun: You are optimistic and carefree!"

        # If Weather
        if self.weather == "1":
            return rain_result
        
        elif self.weather == "2":
            return fog_result
        
        elif self.weather == "3":
            return wind_result
        
        else:
            return sun_result
           
    def storm_magnitude_result(self):
        
        storm_representation = "The strength and position of the storm reflect the stress you're feeling in life."

        print (storm_representation)

        # Intensity
        mild_result = "Mild (Just Passing Through): While you aren't immune to stress, you know that all things must pass."
        
        strong_result = "Strong (In the Eye of the Storm): When you stress, you go all in and have a very hard time pulling yourself out again."
        
        


        # If Intensity
        if self.storm_inten == "1":
            return mild_result

        else:
            return strong_result

        
    def storm_location_result(self):
        # Location
        background_result = "In the Background: Any obstacles that might be causing you grief are not at the forefront of your mind. You are good at managing your anxiety."
        
        above_result = "Right Above Your Cube: You are deeply affected by stress and have a hard time seeing past it to get back to the bigger picture."
        # If Location
        if self.storm_loc == "1":
            return background_result

        else:
            return above_result
        
# user_feedback function
def user_feedback(user_response):
    '''Ask the user the quiz’s level of accuracy and display the survey results
    Args:
    user_response:
        - (1) for accurate results
        - (2) for moderately accurate results
        - (3) for not accurate at all
        Returns:
        User response
        Results: accurate, moderately accurate, or not at all.
        '''
    

    if user_response == "1":
        print ("You agreed your results were very accurate!")
    
    if user_response == "2" :
        print ("You agreed that your results were somewhat, but not completely accurate!")

    if user_response == "3":
        print ("We are sorry your results were not accurate!")

class Createquiz:
    """This class will allow user create their own quiz
    Attributes:
      questions(list): questions the user build
      answers(list): answers the user build
      userkey(list):tuple of the user_id, name of the user, and questions
      question_answer(dictionary):userkey(list) which contains user_id and question as a tuple, answer for as the key
      
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
        """This method will allow the user to built in questions with answers
        Args:
           user_id(str):name of the user
        Returns:
           self.question_answer(dic{(str:str):str}): user_id and question as a tuple, answer for as the key
        Side effects:
           change the user_id
        
        """
        
        
      
            
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
        """This methods will display the quiz the user created to them
        Side effects:
            output the key and value of the dictionary self.question_answer
        """
        print("Here are the questions and answers you built for your own quiz:")
        k=1
        for key,value in self.question_answer.items():
           
            print(f"Question:{k}. {key[1]} Answer: {value}")
            k+=1
        

def main():
    """This function will allow the user to take the personality quiz and display their personality result.
    It aslo allow the user to buid their own fun quiz.
       
       
       Side effects:
       output personality quiz information to the user for the corresponding choice they made.
       
    """
    myid=get_user_info()
    print("Welcome to the Remeo Antolin Cube Personality Test\n")
    print("It's important that you describe whatever comes to your mind first for each question.\n")
    print("I also recommend writing your answers down so that it's easier to figure out your results at the end\n")
    print("and harder to waffle about your answers or change them for a result that you prefer!\n")
    personalityquiz=presentquestions_getchoices()
    print("Your input are",personalityquiz)
    (input_field,input_cube_texture,
            input_cube_color,input_cube_other,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)=personalityquiz
    
    personalityresult=Quiz_results(input_field,input_cube_texture,
            input_cube_color,input_cube_other,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)
    
    print(f"You choose field, {personalityresult.field_result()}\n")
    print(f"You choose cube texure, {personalityresult.cube_texture_result()}\n")
    print(f"You choose cube color, {personalityresult.cube_color_result()}\n")
    
    print(f"You choose ladder length, {personalityresult.ladder_length_result()}\n")
    print(f"You choose ladder distance, {personalityresult.ladder_distance_result()}\n")
    print(f"You choose ladder cude distance, {personalityresult.ladder_cube_result()}\n")
    print(f"You choose ladder material, {personalityresult.ladder_material_result()}\n")

    print(f"You choose horse activity, {personalityresult.horse_activity_result()}\n")
    print(f"You choose horse color, {personalityresult.horse_color_result()}\n")

    print(f"You choose flower, {personalityresult.flower_result()}\n")
    print(f"You choose weather, {personalityresult.weather_result()}\n")
    print(f"You choose storm magnitude, {personalityresult.storm_magnitude_result()}\n")
    print(f"You choose storm location, {personalityresult.storm_location_result()}\n")
    
    user_feedbackinput= input("Please enter whether you thougt this test was: (1) accurate, (2) moderately accurate, or (3) not accurate at all")
    user_feedback(user_feedbackinput)
    
    myquiz=Createquiz()
    user_choice=input("Would you like to build a fun quiz to share with others? yes/no")
    user_validation=user_choice.upper()
    
    if user_validation=="YES":
        myquiz.get_question_answer(myid)
        myquiz.display_addquiz()
   
    
    
if __name__=="__main__":
    main()

                
