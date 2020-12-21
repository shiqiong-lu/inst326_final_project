#Driver Shiqiong Lu
#Navigators Alisson Fortis Sanchez Hung Nguyen Ann Hoang

"""This script will test the personality_quiz.py with some happy cases and edge cases.
"""
import personality_quiz as pq
import pytest

#some happy path cases
def test_addquiz_happyz_path():
    """This function will test some happy of the sript personality_quiz.py
    """
    assert pq.presentquestions_getchoices()==(1,1,1,1,1,1,1,1,1,1,1,1,1)
    assert pq.presentquestions_getchoices()==(1,2,2,2,1,2,1,2,2,2,1,2,1)
    assert pq.presentquestions_getchoices()==(3,2,2,2,1,2,1,2,2,2,1,2,1)
    
    assert pq.user_feedback(1)==1
    assert pq.user_feedback(2)==2
    assert pq.user_feedback(3)==3
    
    assert pq.retry_it()==1
    assert pq.retry_it()=='yes'
    assert pq.retry_it()=='no'
    assert pq.retry_it()==2
    
#some edges cases
def test_addquiz_edge_path():
    """This function will test some edges cased of the script personality_quiz.py
    """
    #test time invalid entry like characters balck space and punctions
    assert pq.presentquestions_getchoices()==('q',2,2,2,1,2,1,2,2,2,1,2,1)
    assert pq.presentquestions_getchoices()==('.',2,2,2,1,2,1,2,2,2,1,2,1)
    assert pq.presentquestions_getchoices()==(' ',2,2,2,1,2,1,2,2,2,1,2,1)
 
    
    assert pq.user_feedback(1)=='yes'
    assert pq.user_feedback(2)=='afdaf'
    assert pq.user_feedback(3)==',./'
    
    assert pq.retry_it()==1
    assert pq.retry_it()=='daf'
    assert pq.retry_it()=='.../'
