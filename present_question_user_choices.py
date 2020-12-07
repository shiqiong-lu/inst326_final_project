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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
            continue
    
    while True:
        try:
            flowers = int(input('Think of flowers. Are there (1) few or (2) many? '))
            if flowers in range(1, 2):
                break
            else:
                print('Please enter 1 or 2.')
                continue
        except ValueError:
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
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
            print('Please enter an integer.')
            continue
    
    return (field, cube_texture, cube_color, ladder_length, ladder_dist, 
            ladder_dist_cube, ladder_mat, horse_act, horse_col, flowers, 
            weather, storm_inten, storm_loc)
