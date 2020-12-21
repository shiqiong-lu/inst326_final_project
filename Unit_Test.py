# Unit Test

from personality_quiz import presentquestions_getchoices

class TestInt(presentquestions_getchoices):
    def test_int(presentquestions_getchoices):
        ''' Test presentquestions_getchoices method from personality_quiz '''
        assert field == 1 or 2 or 3
        assert cube_texture == 1 or 2 or 3
        assert cube_color == 1 or 2 or 3 or 4 or 5 or 6 or 7
        assert ladder_length == 1 or 2
        assert ladder_dist == 1 or 2
        assert ladder_dist_cube == 1 or 2
        assert ladder_mat == 1 or 2
        assert horse_act == 1 or 2 or 3
        assert horse_col == 1 or 2 or 3
        assert flowers == 1 or 2
        assert weather == 1 or 2 or 3 or 4
        assert storm_inten == 1 or 2
        assert storm_loc == 1 or 2

if __name__=="__main__":
    test_int(presentquestions_getchoices)
        
