# coded by Ann Hoang

def retry_it():
    '''Yes or no option to allow the user to retake the quiz
    
    Args:
        re_answer (int): yes or no to retaking quiz
    
    Returns:
        exit (function): no to retaking quiz
    '''
    re_answer = int(input('Retake quiz: (1) yes or (2) no? '))
    if re_answer == 1:
        main()
    else:
        return exit()
