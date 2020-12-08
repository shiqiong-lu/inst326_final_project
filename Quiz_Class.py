#Alisson Fortis Sanchez

class quiz_results：
    '''

    Class will calculate and display results

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
    
    # coded by Ann Hoang
    
    def present_question_user_choices():
    '''Display questions and choices, record answers from user
    
    Args:
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
    '''
    print("Please enter the corresponding number for each answer choice")
    
    while True:
        try:
            field = int(input('Think of an open field. Is it (1) dry and dead, (2) grassy and healthy, or (3) well-trimmed? '))
            if field in range(1, 3):
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
            if cube_texture in range(1, 3):
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
            if cube_color in range(1, 7):
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
            if ladder_length in range(1, 2):
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
            if ladder_dist in range(1, 2):
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
            if ladder_dist_cube in range(1, 2):
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
            if ladder_mat in range(1, 2):
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
            if horse_act in range(1, 3):
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
            if horse_col in range(1, 3):
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
            if flowers in range(1, 2):
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
            if weather in range(1, 4):
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
            if storm_inten in range(1, 2):
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
            if storm_loc in range(1, 2):
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



    #Alisson Fortis Sanchez    

    def field_result(self, field):
        
        field_representation = "The field represents your mind. Its size is the representation of your knowledge of the world, and how vast your personality is."

        print (field_representation)
        
        dead_result = "Dry and Dead: You are feeling pessimistic."

        healthy_result = "Grassy and Healthy: You are feeling optimistic."

        trimmed_result = "Well-Trimmed: You are analytical and cautious."


        # If Field Type

        if field = "1" :
            return dead_result
        
        if field = "2" :
            return healthy_result
        
        if field = "3":
            return trimmed_result

    
        

        
    def cube_result (self, cube_texture, cube_color):
        
        cube_representation = "The cube represents you. The size of the cube is your ego.\
        The surface of the cube represents what is visibly observable about your personality,\
        or maybe it is what you want others to think about you."

        print (cube_representation)
        
        # Texture
        smooth_result = "Smooth: You are a gentle person who takes care not to hurt others or make them feel uncomfortable."

        rough_result = "Rough: You are more straightforward. You tend to be honest in everything you say, no matter how it might affect the person you're talking to."

        bump_spike = "Bumpy or Spiky: You have a tendency to criticize others in an attempt to make them feel inferior to you."

        # Color
        red_result = "Red: You are physically active and enjoy rich sensory experiences."

        yellow_result = "Yellow: You are sociable and cherish your individuality.:

        blue_result = "Blue: You are intelligent and respect others' ideals."

        violet_result = "Violet: You are intelligent and a bit of a perfectionist. You are also mysterious."
 
        grey_result = "Grey: You are self-confident, independent, and not easily rattled."

        black_result = "Black: You have a strong sense of individuality and independence, and you put a high value on alone time."

        white_result = "White: You are kind, independent, and self-reliant."

        # If Cube Texture
        if cube_texture = "1":
            return smooth_result
        
        if cube_texture = "2":
            return rough_result
        
        if cube_texture = "3":
            return bump_spike

        #If Cube Color

        if cube_color = "1":
            return red_result
        
        if cube_color = "2":
            return yellow_result
        
        if cube_color = "3":
            return blue_result
        
        if cube_color = "4":
            return violet_result

        if cube_color = "5":
            return grey_result
        
        if cube_color = "6":
            return black_result
        
        if cube_color = "7":
            return white_result



        
    def ladder_result(self, ladder_length, ladder_dist, ladder_dist_cube, ladder_mat):
        
        ladder_representation = "The ladder represents two different aspects of your life—your goals and your friendships.\
        The location and material of your ladder can also tell you how close you are with your friends. "

        print(ladder_representation)

        # Length
        short_result = "Short: Your goals are realistic and simple."
        
        long_result = "Long: Your goals are more far fetched and difficult to attain."
        
        # Distance
        near_result = "Near: You are putting maximum effort and focus into achieving your goals."
        
        far_result = "Far: Your aren't putting much thought or effort into achieving your goals."

        # Ladder Distance
        near_ladder = "Near: If your ladder is near the cube, you are very close with your friends. \
        If it's actually leaning on the cube, it means your friends can lean on you for support."

        far_ladder = "Far: You have a hard time opening up to people and letting them get close to you."

        # Ladder Material
        strong_ladder = "Strong: The stronger the material (e.g. stone, metal, etc.), the stronger the bond!"
        
        weak_ladder = "Weak: A weak ladder indicates a weak bond between you and those around you."

        # If Ladder Length
        if ladder_length = "1":
            return short_result
        
        if ladder_length = "2":
            return long_result

        # If Ladder Distance
        if ladder_dist = "1":
            return near_result
        
        if ladder_dist = "2":
            return far_result

        # If Ladder Cube Distance
        if ladder_dist_cube = "1":
            return near_ladder
        
        if ladder_dist_cube = "2":
            return far_ladder

        # If Ladder Material
        if ladder_mat = "1":
            return strong_ladder
        
         if ladder_mat = "2":
            return weak_ladder


        
        
    def horse_result(self, horse_act, horse_col):
        
        horse_representation = "The horse represents your ideal partner."

        print(horse_representation)
        
        # Activity
        playing_result = "Playing: Your ideal partner doesn't take life too seriously and or get bogged down by the little stuff."
        
        running_result = "Running: Your ideal partner will respect your space and give you the alone time that you crave."
        
        sleep_result = "Sleeping or Grazing: Your ideal partner is calm and fully committed to you."

        # Color
        brown_horse = "Brown: You prize comfort and reliability above all else. Otherwise, you don't have a specific set of expectations for your partner."
        
        black_horse = "Black: Your idea partner is dominant, seductive, and sophisticated."
        
        white_horse = "White: You value loyalty and trust more than anything else in a relationship."
        
        # If Horse Action
        if horse_act = "1":
            return playing_result
        
        if horse_act = "2":
            return running_result
        
        if horse_act = "3":
            return sleep_result

        # If Horse Color
        if horse_col = "1":
            return brown_horse
        
        if horse_col = "2":
            return black_horse
        
        if horse_col = "3":
            return white_horse

    

        
    def flower_result(self, flowers):
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
        if flowers = "1":
            return rew_results

        if flowers = "2":
            return everywhere_results



        
    def weather_result(self, weather):
        
        weather_representation = "The weather in your field reflects your general outlook on life."

        print(weather_representation)
        
        # Weather Conditions
        rain_result = "Rain: Rain symbolizes the problems in your life, thus the harder the rain, the bigger the problems."

        fog_result = "Fog: You feel uncertainty in life and may be struggling with your identity."

        wind_result = "Wind: Though you tend to worry about future issues, you generally don't let them get you down for long."
        
        sun_result = "Sun: You are optimistic and carefree!"

        # If Weather
        if weather = "1":
            return rain_result
        
        if weather = "2":
            return fog_result
        
        if weather = "3":
            return wind_result
        
        if weather = "4":
            return sun_result
        


        
    def storm_result(self, storm_inten, storm_loc):
        
        storm_representation = "The strength and position of the storm reflect the stress you're feeling in life."

        print (storm_representation)

        # Intensity
        mild_result = "Mild (Just Passing Through): While you aren't immune to stress, you know that all things must pass."
        
        strong_result = "Strong (In the Eye of the Storm): When you stress, you go all in and have a very hard time pulling yourself out again."
        
        # Location
        background_result = "In the Background: Any obstacles that might be causing you grief are not at the forefront of your mind. You are good at managing your anxiety."
        
        above_result = "Right Above Your Cube: You are deeply affected by stress and have a hard time seeing past it to get back to the bigger picture."


        # If Intensity
        if storm_inten = "1":
            return mild_result

        if storm_inten = "2":
            return strong_result

        # If Location
        if storm_loc = "1":
            return background_result

        if storm_loc = "2":
            return above_result




# user_feedback function
def user_feedback():

'''
 Ask the user the quiz’s level of accuracy and display the survey results
 
Args:
* user_response:
    - (1) for accurate results
    - (2) for moderately accurate results
    - (3) for not accurate at all
Returns:
* User response
* Results: accurate, moderately accurate, or not at all.
'''
    user_response = input("Please enter whether you thougt this test was: (1) accurate, (2) moderately accurate, or (3) not accurate at all")

    if user_response = "1":
        return ("You agreed your results were very accurate!")
    
    if user_response = "2" :
        return ("You agreed that your results were somewhat, but not completely accurate!")

    if user_response = "3":
        return ("We are sorry your results were not accurate!")

                

