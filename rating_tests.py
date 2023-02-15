import unittest
import rating

class RatingTests(unittest.TestCase):
    """Test how well rating handles different lists"""

    def test_basic_rating(self):
        example_grades = [5, 7, 8]
        my_rating = rating.Rating(example_grades)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), len(example_grades))
        self.assertEqual(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    def test_empty_list(self):
        example_grades = []
        my_rating = rating.Rating(example_grades)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), 0)
        self.assertEqual(my_rating.get_average_rating(), 1)

    def test_invalid_scores_only(self):
        example_grades = [-5, -1, 11, 23]
        my_rating = rating.Rating(example_grades)
        self.assertListEqual(my_rating.get_scores(), [])
        self.assertEqual(my_rating.get_count(), 0)
        self.assertEqual(my_rating.get_average_rating(), 1)

    def test_mixed_scores(self):
        example_grades = [-5, -1, 0, 5, 10,  11, 23]  # The only valid ones are 5 and 10
        my_rating = rating.Rating(example_grades)
        self.assertListEqual(my_rating.get_scores(), [5, 10])
        self.assertEqual(my_rating.get_count(), 2)
        self.assertEqual(my_rating.get_average_rating(), 7.5)

    def test_invalid_score_adding(self):
        example_grades = [5, 7, 8]
        inv_score = -5
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(inv_score)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), len(example_grades))
        self.assertEqual(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    """Test the operation of adding a new score to the active set"""

    def test_valid_score_to_add(self):
        example_grades = [5, 7, 8]
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)
        example_grades.append(valid_score)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), len(example_grades))
        self.assertEqual(my_rating.get_average_rating(), sum(example_grades) / len(example_grades))

    def test_correct_rounding_downwards(self):
        # Notice the system usually works with int scores only, for testing we will use doubles also
        example_grades = [3, 3, 4, 4, 5, 5, 6, 4, 4, 5, 5, 6, 6]  # average_rating of 4.62, should give 60.06 when multiplied
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)  # 64.06 should be rounded to 64
        example_grades.append(valid_score)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), len(example_grades))
        self.assertEqual(my_rating.get_average_rating() * len(example_grades), 64)

    def test_correct_rounding_upwards(self):
        example_grades = [3, 3, 4, 4, 5, 5, 6, 4, 4, 5, 5, 6, 6, 1.8]  # average_rating of 4.414, should give 61.796 when multiplied
        valid_score = 4
        my_rating = rating.Rating(example_grades)
        my_rating.add_score(valid_score)  # 65.796 should be rounded to 66
        example_grades.append(valid_score)
        self.assertListEqual(my_rating.get_scores(), example_grades)
        self.assertEqual(my_rating.get_count(), len(example_grades))
        self.assertEqual(my_rating.get_average_rating() * len(example_grades), 66)
