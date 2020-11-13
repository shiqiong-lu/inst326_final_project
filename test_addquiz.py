
import addquiz as aq

#some happy path cases
def test_addquiz_happyz_path():
    """This function will test some happy of the sript addquiz
    """
    assert aq.Create_quiz("What is my favorite color","Red")
    assert aq.Create_quiz("What is my birthday","Octorber 27")
    assert aq.Create_quiz("What is my Chinese name","诗琼")
    


#some edges cases
def test_addquiz_edge_path():
    """This function will test some edges cased of the script addquiz
    """
    assert aq.Create_quiz("","")
    assert aq.Create_quiz("/./,,"")
    assert aq.Create_quiz("15.06485626","264")