#INST 326 Final Project
#Project name: personality quiz
#Alisson Fortis Sanchez
#Shiqiong Lu
#Ann Hoang
#Hung Nguyen
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# Shiqiong Lu added codes for INST 326 Project GUI

import csv
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image


LARGE_FONT= ("Verdana", 18)

def get_user_info():
    #driver hung
    """ Users to enter their name. 
        Return:
            The user will return to the home page.
    """
    user_id=input("Please enter your name: ")
    return user_id

def presentquestions_getchoices(): # coded by Ann Hoang
    '''Display questions and choices, record answers from user
        
    Returns:
        field (int): field choice
        cube_texture (int): cube texture choice
        cube_color (int): cube color choice
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
        
    Raises:
        ValueError: user does not enter integer in given range
        
    Side effects:
        Prints quiz questions
        Prints error messages
    '''
    print("Please enter the corresponding number for each answer choice")
    
    while True:
        try:
            field = int(input('Think of an open field. Is it (1) dry and dead, (2) grassy and healthy, or (3) well-trimmed? '))
            if field in range(1, 4):
                break
            else:
                print('Please enter an integer from 1-3.')
                continue
        except ValueError:
            print('Please enter an integer from 1-3.')
            continue
        
    while True:
        try:
            cube_texture = int(input('Think of a cube. Is it (1) smooth, (2) rough, or (3) bumpy/spiky? '))
            if cube_texture in range(1, 4):
                break
            else:
                print('Please enter an integer from 1-3.')
                continue
        except ValueError:
            print('Please enter an integer from 1-3.')
            continue
    
    while True:
        try:
            cube_color = int(input('Is the cube (1) red, (2) yellow, (3) blue, (4) violet, (5) grey, (6) black, or (7) white? '))
            if cube_color in range(1, 8):
                break
            else:
                print('Please enter an integer from 1-7.')
                continue
        except ValueError:
            print('Please enter an integer from 1-7.')
            continue
    
    while True:
        try:
            ladder_length = int(input('Think of a ladder. Is it (1) short or (2) long? '))
            if ladder_length in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            ladder_dist = int(input('Is the ladder (1) near or (2) far? '))
            if ladder_dist in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            ladder_dist_cube = int(input('Is the ladder (1) near the cube or (2) far from the cube? '))
            if ladder_dist_cube in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            ladder_mat = int(input('Is the ladder made of (1) strong material or (2) weak material? '))
            if ladder_mat in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            horse_act = int(input('Think of a horse. What is it doing? Is it (1) playing, (2) running, or (3) sleeping/grazing? '))
            if horse_act in range(1, 4):
                break
            else:
                print('Please enter an integer from 1-3.')
                continue
        except ValueError:
            print('Please enter an integer from 1-3.')
            continue
    
    while True:
        try:
            horse_col = int(input('What color is the horse? Is it (1) brown, (2) black, or (3) white? '))
            if horse_col in range(1, 4):
                break
            else:
                print('Please enter an integer from 1-3.')
                continue
        except ValueError:
            print('Please enter an integer from 1-3.')
            continue
    
    while True:
        try:
            flowers = int(input('Think of flowers. Are there (1) few or are they (2) everywhere? '))
            if flowers in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            weather = int(input('Think of what the weather in the field is like. Is there (1) rain, (2) fog, (3) wind, or (4) sun? '))
            if weather in range(1, 5):
                break
            else:
                print('Please enter an integer from 1-4.')
                continue
        except ValueError:
            print('Please enter an integer from 1-4.')
            continue
    
    while True:
        try:
            storm_inten = int(input('Think of a storm. Is it (1) mild or (2) strong? '))
            if storm_inten in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    while True:
        try:
            storm_loc = int(input('Is the storm (1) in the background or (2) right above the cube? '))
            if storm_loc in range(1, 3):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
    return (field, cube_texture, cube_color, ladder_length, ladder_dist, 
            ladder_dist_cube, ladder_mat, horse_act, horse_col, flowers, 
            weather, storm_inten, storm_loc)

class Quiz_results:
    # Driver: Alisson 
    # Navigator: Ann
    '''Class will calculate and display results
    Parameters:
    * field (int)
    * cube_texture (int)
    * cube_color (int)
    * ladder_length (int)
    * ladder_dist (int)
    * ladder_dist_cube (int)
    * ladder_mat (int)
    * horse_act (int)
    * horse_col (int)
    * flowers (int)
    * weather (int)
    * storm_inten (int)
    * storm_loc (int)
    
    
    Returns:
    * total_summary(): combination result of all factor results from quiz
    
    Side effects:
    * Prints messages on meaning of choice
    '''
    def __init__(self, field, cube_texture,cube_color,ladder_length, ladder_dist, ladder_dist_cube, ladder_mat, horse_act, horse_col, flowers, weather, storm_inten, storm_loc):
        '''Inititalize variables '''
        self.field = field
        self.cube_texture  = cube_texture
        self.cube_color = cube_color
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
    
    def field_result(self):
        '''Get user's field choice
            
        Returns:
            dead_result (str): if user entered 1 for field
            healthy_result (str): if user entered 2 for field
            trimmed_result (str): if user entered 3 for field
            
        Side effects:
            Prints meaning of choice
        '''
        
        field_representation = "The field represents your mind. Its size is the representation of your knowledge of the world, and how vast your personality is.\n"

        print (field_representation)
        
        dead_result = "Dry and Dead: You are feeling pessimistic."

        healthy_result = "Grassy and Healthy: You are feeling optimistic."

        trimmed_result = "Well-Trimmed: You are analytical and cautious."

        if self.field == 1 :
            return dead_result
        
        elif self.field == 2 :
            return healthy_result
        
        else:
            return trimmed_result
 
    def cube_texture_result (self):
        '''Get user's cube texture choice
            
        Returns:
            smooth_result (str): if user entered 1 for cube_texture
            rough_result (str): if user entered 2 for cube_texture
            bump_spike (str): if user entered 3 for cube_texture
            
        Side effects:
            Prints meaning of choice
        '''
        
        cube_representation = "The cube represents you. The size of the cube is your ego. The surface of the cube represents what is visibly observable about your personality, or maybe it is what you want others to think about you.\n"

        print (cube_representation)
        
        # Texture
        smooth_result = "Smooth: You are a gentle person who takes care not to hurt others or make them feel uncomfortable."

        rough_result = "Rough: You are more straightforward. You tend to be honest in everything you say, no matter how it might affect the person you're talking to."

        bump_spike = "Bumpy or Spiky: You have a tendency to criticize others in an attempt to make them feel inferior to you."

        # If Cube Texture
        if self.cube_texture == 1:
            return smooth_result
        
        elif self.cube_texture == 2:
            return rough_result
        
        else:
            return bump_spike
        
    def cube_color_result (self):
        '''Get user's cube color choice
            
        Returns:
            red_result (str): if user entered 1 for cube_color
            yellow_result (str): if user entered 2 for cube_color
            blue_result (str): if user entered 3 for cube_color
            violet_result (str): if user entered 4 for cube_color
            grey_result (str): if user entered 5 for cube_color
            black_result (str): if user entered 6 for cube_color
            white_result (str): if user entered 7 for cube_color
        '''
        
        # Color
        red_result = "Red: You are physically active and enjoy rich sensory experiences."

        yellow_result = "Yellow: You are sociable and cherish your individuality."

        blue_result = "Blue: You are intelligent and respect others' ideals."

        violet_result = "Violet: You are intelligent and a bit of a perfectionist. You are also mysterious."
 
        grey_result = "Grey: You are self-confident, independent, and not easily rattled."

        black_result = "Black: You have a strong sense of individuality and independence, and you put a high value on alone time."

        white_result = "White: You are kind, independent, and self-reliant."
        
         #If Cube Color

        if self.cube_color == 1:
            return red_result
        
        elif self.cube_color == 2:
            return yellow_result
        
        elif self.cube_color == 3:
            return blue_result
        
        elif self.cube_color == 4:
            return violet_result

        elif self.cube_color == 5:
            return grey_result
        
        elif self.cube_color == 6:
            return black_result
        
        else:
            return white_result
        
    def ladder_length_result(self):
        '''Get user's ladder length choice
            
        Returns:
            short_result (str): if user entered 1 for ladder_length
            long_result (str): if user entered 2 for ladder_length
            
        Side effects:
            Prints meaning of choice
        '''
        
        ladder_representation = "The ladder represents two different aspects of your life—your goals and your friendships. The location and material of your ladder can also tell you how close you are with your friends. \n"

        print(ladder_representation)
        
        # Length
        short_result = "Short: Your goals are realistic and simple."
        
        long_result = "Long: Your goals are more far fetched and difficult to attain."
         # If Ladder Lengths
        if self.ladder_length == 1:
            return(short_result)
        
        else:
            return(long_result)
        
        
    def ladder_distance_result(self):
        '''Get user's ladder distance choice
            
        Returns:
            near_result (str): if user entered 1 for ladder_dist
            far_result (str): if user entered 2 for ladder_dist
        '''
        
         # Distance
        near_result = "Near: You are putting maximum effort and focus into achieving your goals."
        
        far_result = "Far: Your aren't putting much thought or effort into achieving your goals."
         # If Ladder Distance
        if self.ladder_dist == 1:
            return(near_result)
        
        else:
            return(far_result)
        
    def ladder_cube_result(self):
        '''Get user's ladder distance to cube choice
            
        Returns:
            near_ladder (str): if user entered 1 for ladder_dist_cube
            far_ladder (str): if user entered 2 for ladder_dist_cube
        '''
        
         # Ladder Distance
        near_ladder = "Near: If your ladder is near the cube, you are very close with your friends. If it's actually leaning on the cube, it means your friends can lean on you for support."

        far_ladder = "Far: You have a hard time opening up to people and letting them get close to you."
         # If Ladder Cube Distance
        if self.ladder_dist_cube == 1:
            return(near_ladder)
        
        else:
            return(far_ladder)

    def ladder_material_result(self):
        '''Get user's ladder material choice
            
        Returns:
            strong_ladder (str): if user entered 1 for ladder_mat
            weak_ladder (str): if user entered 2 for ladder_mat
        '''
        
        # Ladder Material
        strong_ladder = "Strong: The stronger the material (e.g. stone, metal, etc.), the stronger the bond with those around you !"
        
        weak_ladder = "Weak: A weak ladder indicates a weak bond between you and those around you."
        # If Ladder Material
        if self.ladder_mat == 1:
            return(strong_ladder)
        
        else:
            return(weak_ladder)
        
        

    def horse_activity_result(self):
        '''Get user's horse activity choice
            
        Returns:
            playing_result (str): if user entered 1 for horse_act
            running_result (str): if user entered 2 for horse_act
            sleep_result (str): if user entered 3 for horse_act      
  
        Side effects:
            Prints meaning of choice
        '''
        
        horse_representation = "The horse represents your ideal partner.\n"

        print(horse_representation)
        print("You horse choices represents the following:")
        
        # Activity
        playing_result = "Playing: Your ideal partner doesn't take life too seriously and or get bogged down by the little stuff."
        
        running_result = "Running: Your ideal partner will respect your space and give you the alone time that you crave."
        
        sleep_result = "Sleeping or Grazing: Your ideal partner is calm and fully committed to you."
        
        # If Horse Action
        if self.horse_act == 1:
            return(playing_result)
        
        elif self.horse_act == 2:
            return(running_result)
        
        else:
            return(sleep_result)
        
    def horse_color_result(self):
        '''Get user's horse color choice
            
        Returns:
            brown_horse (str): if user entered 1 for horse_col
            black_horse (str): if user entered 2 for horse_col
            white_horse (str): if user entered 3 for horse_col
        '''
        
        # Color
        brown_horse = "Brown: You prize comfort and reliability above all else. Otherwise, you don't have a specific set of expectations for your partner."
        
        black_horse = "Black: Your idea partner is dominant, seductive, and sophisticated."
        
        white_horse = "White: You value loyalty and trust more than anything else in a relationship."
        
        # If Horse Color
        if self.horse_col == 1:
            return(brown_horse)
        
        elif self.horse_col == 2:
            return(black_horse)
        
        else:
            return(white_horse)
   
    def flower_result(self):
        '''Get user's flowers choice
            
        Returns:
            few_results (str): if user entered 1 for flowers
            everywhere_results (str): if user entered 2 for flowers
            
        Side effects:
            Prints meaning of choice
        '''
        
        '''
        Think of flowers.
        Where are the flowers in your field, and how many are there?
        '''
        flower_representation = "The flowers represent your family and friends.\n"

        print(flower_representation)
        
        #Quantity
        few_results = "Just a Few: You are close with your family and have a small, tight-knit group of friends."

        everywhere_results = "They're Everywhere!:You're a social butterfly! With family and friends too numerous to count, you'll never be lonely."

        # If Flower Quantity
        if self.flowers == 1:
            return few_results

        else:
            return everywhere_results
  
    def weather_result(self):
        '''Get user's weather choice
            
        Returns:
            rain_result (str): if user entered 1 for weather
            fog_result (str): if user entered 2 for weather
            wind_result (str): if user entered 3 for weather
            sun_result (str): if user entered 4 for weather
            
        Side effects:
            Prints meaning of choice
        '''
        
        
        weather_representation = "The weather in your field reflects your general outlook on life.\n"

        print(weather_representation)
        
        # Weather Conditions
        rain_result = "Rain: Rain symbolizes the problems in your life, thus the harder the rain, the bigger the problems."

        fog_result = "Fog: You feel uncertainty in life and may be struggling with your identity."

        wind_result = "Wind: Though you tend to worry about future issues, you generally don't let them get you down for long."
        
        sun_result = "Sun: You are optimistic and carefree!"

        # If Weather
        if self.weather == 1:
            return rain_result
        
        elif self.weather == 2:
            return fog_result
        
        elif self.weather == 3:
            return wind_result
        
        else:
            return sun_result
           
    def storm_magnitude_result(self):
        '''Get user's storm intensity choice
            
        Returns:
            mild_result (str): if user entered 1 for storm_inten
            strong_result (str): if user entered 2 for storm_inten
            
        Side effects:
            Prints meaning of choice
        '''
        
        
        storm_representation = "The strength and position of the storm reflect the stress you're feeling in life.\n"

        print (storm_representation)

        # Intensity
        mild_result = "Mild (Just Passing Through): While you aren't immune to stress, you know that all things must pass."
        
        strong_result = "Strong (In the Eye of the Storm): When you stress, you go all in and have a very hard time pulling yourself out again."
        
        


        # If Intensity
        if self.storm_inten == 1:
            return mild_result

        else:
            return strong_result

        
    def storm_location_result(self):
        '''Get user's storm location choice
            
        Returns:
            background_result (str): if user entered 1 for storm_loc
            above_result (str): if user entered 2 for storm_loc
        '''
        
        # Location
        background_result = "In the Background: Any obstacles that might be causing you grief are not at the forefront of your mind. You are good at managing your anxiety."
        
        above_result = "Right Above Your Cube: You are deeply affected by stress and have a hard time seeing past it to get back to the bigger picture."
        # If Location
        if self.storm_loc == 1:
            return background_result

        else:
            return above_result
        
# user_feedback function
def user_feedback(user_feedbackinput):
    '''Ask the user the quiz’s level of accuracy and display the survey results
    Args:
    user_feedbackinput:
        - (1) for accurate results
        - (2) for moderately accurate results
        - (3) for not accurate at all
        Returns:
        User response
        Results: accurate, moderately accurate, or not at all.
        '''
    
while True:
    try:
        if user_feedbackinput == 1:
            print ("You agreed your results were very accurate!")
        if user_feedbackinput == 2 :
            print ("You agreed that your results were somewhat, but not completely accurate!")
        if user_feedbackinput == 3:
            print ("We are sorry your results were not accurate!")
    except (ValueError):
        print (" The value you have entered is out of range. Please try again!)
 

def getfile_len(file_path):
    #Driver Hung Navigator: Shiqiong
     """Read the file for personality quiz.
    Return:
        Return the reader to home page.   
    """
    with open("quizdata.csv","r") as csvfile:
        reader=csv.reader(csvfile)
        reader_len=list(reader)
        return len(reader_len)

def record_data(path,name,field,cube_texture,
            cube_color,ladder_length,ladder_dist,ladder_dist_cube,ladder_mat,
            horse_act,horse_col,flowers,weather, storm_inten,storm_loc,user_feedback):
    #unpack field user input value to string
    #Driver Shiqiong navigator:hung
    """This record the variables of your input. 
    Args:
        fielddict (int): what kind of field you want.
        cube_texturedict (int): the cube features.
        cube_colordict (int): what kind of color for the cube.
        ladder_lengthdict (int): the length of the ladder.
        ladder_distdict (int): ladder distance. 
        ladder_dist_cubedict (int): ladder distance to the cube.
        ladder_matdict (int): the ladder material. 
        horse_actdict (int): what the horse is doing. 
        horse_coldict (int): color of the horse.
        flowersdict (int): how many flowers outside. 
        weatherdict (int): what the weather outside. 
        storm_intendict (int): the storm strength outside. 
        storm_locdict (int): the storm location. 
        user_feedbackdict (int): the users feedback of these questions. 
    Return:
        fieldnames(int): result of input of these variables.
    """
    
    fielddict={'field':['dry and dead','grassy and healthy','well-trimmed']}
    if field ==1:
        fieldw=fielddict['field'][0]
    elif field==2:
        fieldw=fielddict['field'][1]
    else:
        fieldw=fielddict['field'][2]
        
    cube_texturedict={'cube_texture':['smooth','rough','bumpy/spiky']}
    if cube_texture==1:
        cube_texturew=cube_texturedict['cube_texture'][0]
    elif cube_texture==2:
        cube_texturew=cube_texturedict['cube_texture'][1]
    else:
        cube_texturew=cube_texturedict['cube_texture'][2]
        
    cube_colordict={'cube_color':['red','yellow','blue','violet','grey','black','white']}
    if cube_color==1:
        cube_colorw=cube_colordict['cube_color'][0]
    elif cube_color==2:
        cube_colorw=cube_colordict['cube_color'][1]
    elif cube_color==3:
        cube_colorw=cube_colordict['cube_color'][2]
    elif cube_color==4:
        cube_colorw=cube_colordict['cube_color'][3]
    elif cube_color==5:
        cube_colorw=cube_colordict['cube_color'][4]
    elif cube_color==6:
        cube_colorw=cube_colordict['cube_color'][5]
    else:
        cube_colorw=cube_colordict['cube_color'][6]
        
    ladder_lengthdict={'ladder_length':['short','long']}
    if ladder_length==1:
        ladder_lengthw=ladder_lengthdict['ladder_length'][0]
    else:
        ladder_lengthw=ladder_lengthdict['ladder_length'][1]
        
    ladder_distdict={'ladder_dist':['near','far']}
    if ladder_dist==1:
        ladder_distw=ladder_distdict['ladder_dist'][0]
    else:
        ladder_distw=ladder_distdict['ladder_dist'][1]
        
    ladder_dist_cubedict={'ladder_dist_cube':['near the cube','far from the cube']}
    if ladder_dist_cube==1:
        ladder_dist_cubew=ladder_dist_cubedict['ladder_dist_cube'][0]
    else:
        ladder_dist_cubew=ladder_dist_cubedict['ladder_dist_cube'][1]
        
    ladder_matdict={'ladder_mat':['strong material','weak material']}
    if ladder_mat==1:
        ladder_matw=ladder_matdict['ladder_mat'][0]
    else:
        ladder_matw=ladder_matdict['ladder_mat'][1]
        
    horse_actdict={'horse_act':['playing','running','sleeping/grazing']}
    if horse_act==1:
        horse_actw=horse_actdict['horse_act'][0]
    elif horse_act==2:
        horse_actw=horse_actdict['horse_act'][1]
    else:
        horse_actw=horse_actdict['horse_act'][2]
        
    horse_coldict={'horse_col':['brown','black','white']}
    if horse_col==1:
        horse_colw=horse_coldict['horse_col'][0]
    elif horse_col==2:
        horse_colw=horse_coldict['horse_col'][1]
    else:
        horse_colw=horse_coldict['horse_col'][2]
        
    flowersdict={'flowers':['Just a few','They are everywhere']}
    if flowers==1:
        flowersw=flowersdict['flowers'][0]
    else:
        flowersw=flowersdict['flowers'][1]
        
    weatherdict={'weather':['rain','fog','wind','sun']}
    if weather==1:
        weatherw=weatherdict['weather'][0]
    elif weather==2:
        weatherw=weatherdict['weather'][1]
    elif weather==3:
        weatherw=weatherdict['weather'][2]
    else:
        weatherw=weatherdict['weather'][3]
        
    storm_intendict={'storm_inten':['mild','strong']}
    if storm_inten==1:
        storm_intenw=storm_intendict['storm_inten'][0]
    else:
        storm_intenw=storm_intendict['storm_inten'][1]
    storm_locdict={'storm_loc':['in the background ','right above the cube']}
    if storm_loc==1:
        storm_locw=storm_locdict['storm_loc'][0]
    else:
        storm_locw=storm_locdict['storm_loc'][1]
        
    user_feedbackdict={'user_feedback':['accurate results','moderately accurate results','not accurate at all']}
    if user_feedback==1:
        user_feedbackw=user_feedbackdict['user_feedback'][0]
    elif user_feedback==2:
        user_feedbackw=user_feedbackdict['user_feedback'][1]
    else:
        user_feedbackw=user_feedbackdict['user_feedback'][2]
        
    
    fieldnames=['id','name','field','cube texture',
                'cube color','ladder length','ladder distance',
                'ladder cube distance','ladder material','horse action',
                'horse color','flowers','weather','storm magnitude','storm location','user feedback']
    next_id=getfile_len(path)
    with open(path,"a") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({"id":next_id,
                          "name":name,
                          "field":fieldw,
                          "cube texture":cube_texturew,
                          "cube color":cube_colorw,
                          "ladder length":ladder_lengthw,
                          "ladder distance":ladder_distw,
                          "ladder cube distance": ladder_dist_cubew,
                          "ladder material":ladder_matw,
                          "horse action":horse_actw,
                          "horse color":horse_colw,
                          "flowers":flowersw,
                          "weather":weatherw,
                          "storm magnitude":storm_intenw,
                          "storm location":storm_locw,
                          "user feedback":user_feedbackw,
                          })
        
def user_datagraph():
    #Driver Shiqiong Navigator: Alisson Ann Hung
    """What kind of paragraph for the result of the personality quiz.
    Return:
        The result of your choose for your paragraph.
    """
    df=pd.read_csv("quizdata.csv")
    #print(df)
    sns.catplot(y='field',kind='count',palette="ch:.25",data=df)
    plt.ylabel('Field choices',fontsize=15)
    plt.savefig("field")
    plt.close()
    
    sns.catplot(y='cube texture',kind='count',palette="ch:.25",data=df)
    plt.ylabel('Cube texture choices',fontsize=15)
    plt.savefig("cube_texture")
    plt.close()
    
    sns.catplot(y='cube color',kind='count',palette="ch:.25",data=df)
    plt.ylabel('Cube color choices',fontsize=15)
    plt.savefig("cube_color")
    plt.close()
    
    sns.catplot(y='ladder length',kind='count',palette="ch:.25",data=df)
    plt.ylabel('ladder length choices',fontsize=15)
    plt.savefig("ladder_length")
    plt.close()
    
    sns.catplot(y='ladder distance',kind='count',palette="ch:.25",data=df)
    plt.ylabel('ladder distance choices',fontsize=15)
    plt.savefig("ladder_distance")
    plt.close()
    
    sns.catplot(y='ladder cube distance',kind='count',palette="ch:.25",data=df)
    plt.ylabel('ladder cube distance',fontsize=15)
    plt.savefig("ladder_cube_distance")
    plt.close()
    
    
    sns.catplot(y='ladder material',kind='count',palette="ch:.25",data=df)
    plt.ylabel('ladder material choices',fontsize=15)
    plt.savefig("ladder_material")
    plt.close()
    
    sns.catplot(y='horse action',kind='count',palette="ch:.25",data=df)
    plt.ylabel('horse action choices',fontsize=15)
    plt.savefig("horse_action")
    plt.close()
    
    sns.catplot(y='horse color',kind='count',palette="ch:.25",data=df)
    plt.ylabel('horse color choices',fontsize=15)
    plt.savefig("horse_color")
    plt.close()
    
    sns.catplot(y='flowers',kind='count',palette="ch:.25",data=df)
    plt.ylabel('flowers choices',fontsize=15)
    plt.savefig("flowers")
    plt.close()
    
    sns.catplot(y='weather',kind='count',palette="ch:.25",data=df)
    plt.ylabel('weather choices',fontsize=15)
    plt.savefig("weather")
    plt.close()
    
    sns.catplot(y='storm magnitude',kind='count',palette="ch:.25",data=df)
    plt.ylabel('storm magnitude choices',fontsize=15)
    plt.savefig("storm_magnitude")
    plt.close()
    
    sns.catplot(y='storm location',kind='count',palette="ch:.25",data=df)
    plt.ylabel('storm location choices',fontsize=15)
    plt.savefig("storm_location")
    plt.close()
    
    sns.catplot(y='user feedback',kind='count',palette="ch:.25",data=df)
    plt.ylabel('Did you get accurate results?',fontsize=15)
    plt.savefig("user_feedback")
    plt.close()
    plt.show()
class MainGUI(tk.Tk):
   # Driver: Shiqiong

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,
                  PageEight,PageNine,PageTen,PageEleven,PageTwelve,PageThirteen,PageFourteen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Personality Test: The Field, Cube, Ladder, Horse, and Flower graphical result", 
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Field result Graph",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Cube Texture result Graph",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        button3 = tk.Button(self, text="Cube color result graph",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        
        button4 = tk.Button(self, text="ladder length Result graph",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        
        button5 = tk.Button(self, text="ladder distance result graph",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        
        button6 = tk.Button(self, text="ladder cube distance result graph",
                            command=lambda: controller.show_frame(PageSix))
        button6.pack()
        
        button7 = tk.Button(self, text="ladder material result graph",
                            command=lambda: controller.show_frame(PageSeven))
        button7.pack()
        
        button8 = tk.Button(self, text="horse action result graph",
                            command=lambda: controller.show_frame(PageEight))
        button8.pack()
        
        button9 = tk.Button(self, text="horse color result graph",
                            command=lambda: controller.show_frame(PageNine))
        button9.pack()
        
        button10 = tk.Button(self, text="flowers result graph",
                            command=lambda: controller.show_frame(PageTen))
        button10.pack()
        
        button11 = tk.Button(self, text="weather result graph",
                            command=lambda: controller.show_frame(PageEleven))
        button11.pack()
        
        button12 = tk.Button(self, text="storm magnitude result graph",
                            command=lambda: controller.show_frame(PageTwelve))
        button12.pack()
        
        button13 = tk.Button(self, text="storm location result graph",
                            command=lambda: controller.show_frame(PageThirteen))
        button13.pack()
        
        button14 = tk.Button(self, text="Did you get accurate results?",
                            command=lambda: controller.show_frame(PageFourteen))
        button14.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Field result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("field.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cube Texture result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("cube_texture.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Three",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cube color result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("cube_color.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Four",
                            command=lambda: controller.show_frame(PageFour))
        button3.pack()
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ladder length Result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("ladder_length.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Three",
                            command=lambda: controller.show_frame(PageThree))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Five",
                            command=lambda: controller.show_frame(PageFive))
        button3.pack()
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ladder distance result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("ladder_distance.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Four",
                            command=lambda: controller.show_frame(PageFour))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Six",
                            command=lambda: controller.show_frame(PageSix))
        button3.pack()
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ladder cube distance result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("ladder_cube_distance.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Five",
                            command=lambda: controller.show_frame(PageFive))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Seven",
                            command=lambda: controller.show_frame(PageSeven))
        button3.pack()
class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ladder material result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("ladder_material.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Six",
                            command=lambda: controller.show_frame(PageSix))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Eight",
                            command=lambda: controller.show_frame(PageEight))
        button3.pack()
class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="horse action result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("horse_action.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Seven",
                            command=lambda: controller.show_frame(PageSeven))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Nine",
                            command=lambda: controller.show_frame(PageNine))
        button3.pack()
class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="horse color result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("horse_color.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Eight",
                            command=lambda: controller.show_frame(PageEight))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Ten",
                            command=lambda: controller.show_frame(PageTen))
        button3.pack() 
class PageTen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="flowers result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("flowers.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Nine",
                            command=lambda: controller.show_frame(PageNine))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Eleven",
                            command=lambda: controller.show_frame(PageEleven))
        button3.pack() 
class PageEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="weather result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("weather.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Ten",
                            command=lambda: controller.show_frame(PageTen))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Eleven",
                            command=lambda: controller.show_frame(PageTwelve))
        button3.pack() 
class PageTwelve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="storm magnitude result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("storm_magnitude.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Eleven",
                            command=lambda: controller.show_frame(PageEleven))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Thirteen",
                            command=lambda: controller.show_frame(PageThirteen))
        button3.pack() 

class PageThirteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="storm location result", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("storm_location.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Twelve",
                            command=lambda: controller.show_frame(PageTwelve))
        button2.pack()
        
        button3 = tk.Button(self, text="Page Fourteen",
                            command=lambda: controller.show_frame(PageFourteen))
        button3.pack() 
class PageFourteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Did you get accurate results?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("user_feedback.png")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Thirteen",
                            command=lambda: controller.show_frame(PageThirteen))
        button2.pack()
         
def main():
    # Dirver: Shiqiong 
    # Ann & Alisson & Hung
    """This function will allow the user to take the personality quiz and display their personality result.
    Returns:
       Print the outcome of your result for finishing the quiz. 
       
    Side effects:
       Print what your presonality is.
    """
    myid=get_user_info()
    print("Welcome to the Remeo Antolin Cube Personality Test\n")
    print("It's important that you describe whatever comes to your mind first for each question.\n")
    print("I also recommend writing your answers down so that it's easier to figure out your results at the end\n")
    print("and harder to waffle about your answers or change them for a result that you prefer!\n")
    print("\n")
   
    personalityquiz=presentquestions_getchoices()
    #print("Your inputs are ",personalityquiz)
    (input_field,input_cube_texture,
            input_cube_color,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)=personalityquiz
   
    
    personalityresult=Quiz_results(input_field,input_cube_texture,
            input_cube_color,input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)
    print("\n")
   
    print(f"You choose field, {personalityresult.field_result()}\n")
    print("\n")
    
    print(f"You choose cube texure, {personalityresult.cube_texture_result()}\n")
    print(f"You choose cube color, {personalityresult.cube_color_result()}\n")
    print("\n")
 
    print(f"You choose ladder length, {personalityresult.ladder_length_result()}\n")
    print(f"You choose ladder distance, {personalityresult.ladder_distance_result()}\n")
    print(f"You choose ladder cude distance, {personalityresult.ladder_cube_result()}\n")
    print(f"You choose ladder material, {personalityresult.ladder_material_result()}\n")
    print("\n")
   

    print(f"You choose horse activity, {personalityresult.horse_activity_result()}\n")
    print(f"You choose horse color, {personalityresult.horse_color_result()}\n")
    print("\n")
    

    print(f"You choose flower, {personalityresult.flower_result()}\n")
    print(f"You choose weather, {personalityresult.weather_result()}\n")
    print("\n")
    
    print(f"You choose storm magnitude, {personalityresult.storm_magnitude_result()}\n")
    print(f"You choose storm location, {personalityresult.storm_location_result()}\n")
    print("\n")
    
    
    user_feedbackinput= int(input("Please enter whether you thougt this test was (1) accurate, (2) moderately accurate, or (3) not accurate at all: "))
    user_feedback(user_feedbackinput)
    #write the user response into the database
    record_data("quizdata.csv",myid,input_field,input_cube_texture,
            input_cube_color,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc,user_feedbackinput)
    #display the graph
    user_datagraph()
    app = MainGUI()
    app.title("Personality quiz graphic result")
    app.mainloop()
    
def retry_it(): # coded by Ann Hoang
    '''Yes or no option to allow the user to retake the quiz
    
    Returns:
        exit (function): no to retaking quiz
        
    Raises:
        ValueError: user does not enter integer in given range
        
    Side effects:
        Runs program again
    '''
    while True:
        try:
            re_answer = int(input('Retake quiz: (1) yes or (2) no? '))
            if re_answer == 1:
                main()
            elif re_answer == 2:
                return exit()
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter 1 or 2.')
            continue
    
if __name__=="__main__":
    # Driver: Alisson
    main()
    retry_it()
