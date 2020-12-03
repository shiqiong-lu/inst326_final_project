# coded by Ann Hoang

def present_question_user_choices():
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
    flowers = int(input('Think of flowers. Are there (1) few or (2) many? '))
    weather = int(input('Think of what the weather in the field is like. Is there (1) rain, (2) fog, (3) wind, or (4) sun? '))
    storm_inten = int(input('Think of a storm. Is it (1) mild or (2) strong? '))
    storm_loc = int(input('Is the storm (1) in the background or (2) right above the cube? '))
    
    return field
    return cube_texture
    return cube_color
    return cube_other
    return ladder_length
    return ladder_dist
    return ladder_dist_cube
    return ladder_mat
    return horse_act
    return horse_col
    return flowers
    return weather
    return storm_inten
    return storm_loc
