import unittest
import rating

class RatingTests(unittest.TestCase):
    """Test how well rating handles different lists"""

    def test_basic_rating(self):
        example_grades = 5, 7, 8
        my_rating = rating.Rating(example_grades)
        self.assertTrue(my_rating.get_scores(), example_grades)
        self.assertTrue(my_rating.get_count(), len(example_grades))
        self.assertTrue(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    def test_empty_list(self):
        example_grades = []
        my_rating = rating.Rating(example_grades)
        self.assertFalse(my_rating.get_scores(), example_grades)
        self.assertFalse(my_rating.get_count(), 0)
        self.assertTrue(my_rating.get_average_rating(), 1)

    def test_invalid_scores_only(self):
        example_grades = [-5, -1, 11, 23]
        my_rating = rating.Rating(example_grades)
        self.assertFalse(my_rating.get_scores(), example_grades)
        self.assertFalse(my_rating.get_count(), 0)
        self.assertTrue(my_rating.get_average_rating(), 1)

    def test_mixed_scores(self):
        example_grades = [-5, -1, 0, 5, 10,  11, 23]  # The only valid ones are 0, 5 and 10
        my_rating = rating.Rating(example_grades)
        self.assertTrue(my_rating.get_scores(), [0, 5, 10])
        self.assertTrue(my_rating.get_count(), 3)
        self.assertTrue(my_rating.get_average_rating(), 5)

    def test_invalid_score_adding(self):
        example_grades = 5, 7, 8
        inv_score = -5
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(inv_score)
        self.assertTrue(my_rating.get_scores(), example_grades)
        self.assertTrue(my_rating.get_count(), len(example_grades))
        self.assertTrue(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    """Test the operation of adding a new score to the active set"""

    def test_valid_score_to_add(self):
        example_grades = [5, 7, 8]
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)
        example_grades.append(valid_score)
        self.assertTrue(my_rating.get_scores(), example_grades)
        self.assertTrue(my_rating.get_count(), len(example_grades))
        self.assertTrue(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    def test_correct_rounding_downwards(self):
        # Notice the system usually works with int scores only, for testing we will use doubles also
        example_grades = [3, 3, 4, 4, 5, 5, 6, 4, 4, 5, 5, 6, 6]  # average_rating of 4.62, should give 60.06 when multiplied
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)  # 64.06 should be rounded to 64
        example_grades.append(valid_score)
        self.assertTrue(my_rating.get_scores(), example_grades)
        self.assertTrue(my_rating.get_count(), len(example_grades))
        self.assertTrue(my_rating.get_average_rating(), 64)

    def test_correct_rounding_upwards(self):
        example_grades = [3, 3, 4, 4, 5, 5, 6, 4, 4, 5, 5, 6, 6, 0.2]  # average_rating of 4.64, should give 64.96 when multiplied
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)  # 68.96 should be rounded to 69 (no dirty minds intended :P)
        example_grades.append(valid_score)
        self.assertTrue(my_rating.get_scores(), example_grades)
        self.assertTrue(my_rating.get_count(), len(example_grades))
        self.assertTrue(my_rating.get_average_rating(), 69)
