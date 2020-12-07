# coded by Ann Hoang

def retry_it():
    '''Yes or no option to allow the user to retake the quiz
    
    Args:
        re_answer (int): yes or no to retaking quiz
    
    Returns:
        exit (function): no to retaking quiz
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
            print('Please enter an integer.')
            continue
