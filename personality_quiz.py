#INST 326 Final Project
#Project name: personality quiz
#This personality quiz content is coded based on this website: https://owlcation.com/social-sciences/quick-personality-test
#Alisson Fortis Sanchez
#Shiqiong Lu
#Ann Hoang
#Hung Nguyen

import csv
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image

"""This script will display a personality quiz to the user, asking user input, decided the user quiz result,
display the quiz result to the user, write each user input into a csv file to make bar graphs of all responder's result,
displaying a GUI to allow the user to check each input with the bar graph, allow the user to retake the quiz or exit the script.

"""

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
        '''Inititalize new class Quiz_result object variables
        Args:
           See class parameter documentation
        '''
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
def user_feedback(user_response):
    '''Ask the user the quiz’s level of accuracy and display the survey results
    Args:
    user_feedbackinput(int):
        - (1) for accurate results
        - (2) for moderately accurate results
        - (3) for not accurate at all
    Side effects:
        Raise ValueError
        '''
    
    while True:
        try:
            if user_response == 1:
                print ("You agreed your results were very accurate!")
                break
            elif user_response == 2 :
                print ("You agreed that your results were somewhat, but not completely accurate!")
                break
            else:
                print ("We are sorry your results were not accurate!")
            break
        except ValueError:
            print("Please enter a valid number")
            continue

def getfile_len(file_path):
    """Read the file length from the csv file.
    Args:
        file_path(str): the path of the csv file.
    Return:
        len(reader_len)(int): the length of the csv file.
    Side effect:
        Return the length of the csv database.
    """
    #Driver Hung Navigator: Shiqiong
    with open(file_path,"r") as csvfile:
        reader=csv.reader(csvfile)
        reader_len=list(reader)
        return len(reader_len)

def record_data(path,name,field,cube_texture,
            cube_color,ladder_length,ladder_dist,ladder_dist_cube,ladder_mat,
            horse_act,horse_col,flowers,weather, storm_inten,storm_loc,user_feedback):
    #Driver Shiqiong navigator:hungs
    """This record the variables of your input. 
    Args:
        path(str):path of the csv file 
        name(str): name of the user 
        field(int): field choice the user made
        cube_texture(int): cube texture choice the user made
        cube_color(int): cube color choice the user made
        ladder_length(int): ladder length choice the user made
        ladder_dist(int): ladder distance choice the user made
        ladder_dist_cube(int): ladder distance cube choice the user made
        ladder_mat(int): ladder material choice the user made
        horse_act(int): horse action choice the user made
        horse_col(int): horse color choice the user made
        flowers(int): flowers choice the user made
        weather(int): weather choice the user made
        storm_inten(int): storm intense choice the user made
        storm_loc(int):storm location choice the user made
        user_feedback(int): feedback choice the user made
    """
    #unpack field user input value to string
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
    next_id=getfile_len(path) #get the Id number form the getfile_len to write the data correspondingly
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
    """This function create a dataframe with the data on a csv file. Then make a bar graph.
    side effects:
        make 14 png bargraph with assinged names and save them in the same directory of the script.
    """
    #Driver Shiqiong Navigator: Alisson Ann Hung
    df=pd.read_csv("quizdata.csv")
    #print(df)
    
    g=sns.catplot(y='field',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)#adjust the graph's position
    g.fig.suptitle('Field Choices', fontsize=14) # add a graph title
    plt.ylabel('')#remove the unessessary y label content
    plt.savefig("field.png")
    plt.close()
    
    g=sns.catplot(y='cube texture',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('Cube texture choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("cube_texture.png")
    plt.close()
    
    g=sns.catplot(y='cube color',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('Cube color choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("cube_color")
    plt.close()
    
    g=sns.catplot(y='ladder length',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('ladder length choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("ladder_length")
    plt.close()
    
    g=sns.catplot(y='ladder distance',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('ladder distance choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("ladder_distance")
    plt.close()
    
    g=sns.catplot(y='ladder cube distance',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('ladder cube distance', fontsize=14)
    plt.ylabel('')
    plt.savefig("ladder_cube_distance")
    plt.close()
    
    
    g=sns.catplot(y='ladder material',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('ladder material choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("ladder_material")
    plt.close()
    
    g=sns.catplot(y='horse action',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('horse action choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("horse_action")
    plt.close()
    
    g=sns.catplot(y='horse color',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('horse color choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("horse_color")
    plt.close()
    
    g=sns.catplot(y='flowers',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('flowers choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("flowers")
    plt.close()
    
    g=sns.catplot(y='weather',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('weather choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("weather")
    plt.close()
    
    g=sns.catplot(y='storm magnitude',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('storm magnitude choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("storm_magnitude")
    plt.close()
    
    g=sns.catplot(y='storm location',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('storm location choices', fontsize=14)
    plt.ylabel('')
    plt.savefig("storm_location")
    plt.close()
    
    g=sns.catplot(y='user feedback',kind='count',palette="ch:.25",height=4.25, aspect=1/0.7,data=df)
    g.fig.subplots_adjust(bottom=0.1)
    g.fig.suptitle('Did you get accurate results?', fontsize=14)
    plt.ylabel('')
    plt.savefig("user_feedback")
    plt.close()
def image_choice(imagename):
    """This function will open a image and resize the image. Put it on frame as a label.
    Args:
       imagename(str):the name of the graph.
    side effects:
       global variable picture(label) has been created here!
       pack on the frame as a label.
    """
    # The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    # License: http://creativecommons.org/licenses/by-sa/3.0/	
    # Shiqiong Lu changed it as a function to use on GUI with instructor Cruz review session instructions.
    global picture# make a global variable picture to allow the get_image function access this label
    img = Image.open(f"{imagename}.png")
    newsize = (610, 430) 
    img = img.resize(newsize) 
    img = ImageTk.PhotoImage(img)
    picture = tk.Label(lower_frame,image = img)
    picture.image = img
    picture.pack()
    
def get_image(user_input):
    """This function reads the input from the GUI entry box and append it to the globel variable picturelist.
    Then decide which photoname to put in the image_choice function.
    Args:
      user_input(str): user input number choice as string.
    """
    picturelist.append(user_input)# append the user input to the list
    if int(user_input)==1:
        # if the picture label had been put on the frame, disapear this picture before displaying another one.
        if len(picturelist) > 1:
            picture.pack_forget()
        #call the image_choice to choose displaying image on the GUI
        image_choice("field")

    elif int(user_input)==2:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("cube_texture")
  
    elif int(user_input)==3:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("cube_color")

    elif int(user_input)==4:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("ladder_length")
        
    elif int(user_input)==5:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("ladder_distance")
        
    elif int(user_input)==6:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("ladder_cube_distance")

    elif int(user_input)==7:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("ladder_material")

    elif int(user_input)==8:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("horse_action")
    
    elif int(user_input)==9:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("horse_color")
    
    elif int(user_input)==10:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("flowers")

    elif int(user_input)==11:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("weather")
        
    elif int(user_input)==12:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("storm_magnitude")
        
    elif int(user_input)==13:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("storm_location")
        
    elif int(user_input)==14:
        if len(picturelist) > 1:
            picture.pack_forget()
        image_choice("user_feedback")
    else:
        #display the user's invalid input if the choice is not on the label description
        print(f"invalid input {user_input} Please enter an number on the list!")

    
def main():
    """This function will allow the user to take the personality quiz and display their personality result,
    as well as dispalying a GUI to let the user to check all responders result.
    Returns:
       Print the outcome of your result for finishing the quiz. 
       
    Side effects:
       globle variable has been lower_frame
       globle variable picturelist(list) has been created
       Print what your instructions and presonality quiz result are.
    """
    # Dirver: Shiqiong 
    # Ann & Alisson & Hung
    
    #ask for user's name(name can be any characters or numbers, as well as combinations)
    myid=get_user_info()
    print("\n")
    
    #output personality quiz description
    print("Welcome to the Remeo Antolin Cube Personality Test\n")
    print("It's important that you describe whatever comes to your mind first for each question.\n")
    print("I also recommend writing your answers down so that it's easier to figure out your results at the end\n")
    print("and harder to waffle about your answers or change them for a result that you prefer!\n")
    print("\n")
    
    #present the questions to the user and ask for corresponding input choices
    personalityquiz=presentquestions_getchoices()
    #print("Your inputs are ",personalityquiz)
    (input_field,input_cube_texture,
            input_cube_color,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)=personalityquiz
   
    #determine the quiz result from the user
    personalityresult=Quiz_results(input_field,input_cube_texture,
            input_cube_color,input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc)
    print("\n")
    
    #displaying the quiz result
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
    
    #Ask user's feedback
    user_feedbackinput= int(input("Please enter whether you thougt this test was (1) accurate, (2) moderately accurate, or (3) not accurate at all: "))
    user_feedback(user_feedbackinput)
    
    #write the user response into the database
    record_data("quizdata.csv",myid,input_field,input_cube_texture,
            input_cube_color,
            input_ladder_length,input_ladder_dist,
            input_ladder_dist_cube,input_ladder_mat,
            input_horse_act,input_horse_col,input_flowers,input_weather,
            input_storm_inten,input_storm_loc,user_feedbackinput)
    
    #make the bar graphs to show in the GUI with user's choice
    user_datagraph()
    
    #The basic structure of this GUI is coming from https://www.youtube.com/watch?v=D8-snVfekto video tutorial,
    #Shiqiong Lu coded this GUI other features such as allow a graph change size and remove from the GUI with 
    #different user input request
    HEIGHT=800
    WIDTH=800
    
    global picturelist
    picturelist=[]#which will allow the get_image function to append the user input(str) in
    
    root=tk.Tk() # main window which contains everything

    canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
    canvas.pack()# put it on the window
    
    #set up a background photos with the personality quiz cover https://owlcation.com/social-sciences/quick-personality-test
    backgroundfile='background.png'
    background_image=tk.PhotoImage(file=backgroundfile)
    background_label=tk.Label(root, image=background_image)
    background_label.place(relwidth=1,relheight=1)

    # A Container to hold this button
    frame=tk.Frame(root,bd=3)  
    frame.place(relx=0.5,rely=0.1,relwidth=0.8,relheight=0.1,anchor='n') #1 will fill the whole screen
    #create a label to display the choice for the user
    label = tk.Label(root,text='Enter 1 for field, 2 for cube texture, 3 for cube color, 4 for ladder length, 5 for ladder distance,6 for ladder cube distance,\
        7 for ladder material, 8 for horse action, 9 for horse color, 10 for flowers, 11 for weather, 12 storm magnitude,\
                13 for storm location, 14 accuracy to check the personality quiz result from all responders!',wraplength=630)
    label.place(relwidth=1,relheight=0.1)
    
    #make the entry box and put it on the frame to read the choice input choice
    entry=tk.Entry(frame,font=40)
    entry.place(relwidth=0.65,relheight=0.65)

    #button will read the real-time input from the user can call the get_image function
    button = tk.Button(frame,text='Enter',fg='blue',command=lambda:get_image(entry.get()))
    button.place(relx=0.7,relwidth=0.2,relheight=0.65)
    
    #make a frame placed at a lower place to hold the graphs
    global lower_frame # the function image_choice can access it to put the resized graphs on this frame
    lower_frame=tk.Frame(root,bd=10)
    lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
    
    #make a GUI title
    root.title("Personality quiz graphic result")

    root.mainloop() # make it run in the window
    
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
