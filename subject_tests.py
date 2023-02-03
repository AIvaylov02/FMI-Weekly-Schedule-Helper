import unittest
import subject

class TestSubjectExceptions(unittest.TestCase):
    """Test for life of exceptions and the wanted inheritances(InvalidInput comes from Exception, all other should
    inherit InvalidInput"""

    def test_correct_input_parent(self):
        exception = subject.InvalidInput()
        self.assertIsInstance(exception, Exception)

    def test_correct_inheritance_of_input_to_subject_name(self):
        subj_name = subject.InvalidSubjectName()
        self.assertIsInstance(subj_name, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_person_name(self):
        person_name = subject.InvalidPersonName()
        self.assertIsInstance(person_name, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_subject_group(self):
        subject_group = subject.InvalidSubjectGroup()
        self.assertIsInstance(subject_group, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_credits(self):
        ECTScredits = subject.InvalidECTSCredits()
        self.assertIsInstance(ECTScredits, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_lecture(self):
        lecture = subject.InvalidLectureType()
        self.assertIsInstance(lecture, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_weekday(self):
        weekday = subject.InvalidWeekday()
        self.assertIsInstance(weekday, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_workhour(self):
        workhour = subject.InvalidWorkHour()
        self.assertIsInstance(workhour, subject.InvalidInput)

    def test_correct_inheritance_of_input_to_rating(self):
        rating = subject.InvalidRating()
        self.assertIsInstance(rating, subject.InvalidInput)


class TestSubject(unittest.TestCase):

# valid subject example ('Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
#                  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_subject_name_small_letters_only(self):
        self.assertRaises(subject.InvalidSubjectName, subject.Subject, 'algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_subject_name_forbiden_chars(self):
        self.assertRaises(subject.InvalidSubjectName, subject.Subject, 'Algebra$', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_group(self):
        self.assertRaises(subject.InvalidSubjectGroup, subject.Subject, 'Algebra', 'random123', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_person_small_letters(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_person_one_name(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'KonstantinTabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_person_only_one_capital(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_person_random_chars(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin1337Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_negative_credits(self):
        self.assertRaises(subject.InvalidECTSCredits, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', -3, 'L', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_lecture_type(self):
        self.assertRaises(subject.InvalidLectureType, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'poredna tupotiq', 'Monday', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_day(self):
        self.assertRaises(subject.InvalidWeekday, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Ponedelnik', 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_multiple_days(self):
        self.assertRaises(subject.InvalidWeekday, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', ('Monday', 'Vtornik'), 16, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_too_early_start_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 6, 9, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_too_late_start_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 23, 24, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_too_early_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 7, 7, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_too_late_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 22, 1, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_invalid_diff_between_start_and_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 12, 19, 210,
                                                                         10, 'Mnogo e pich, toq Tabakov be :)')
    def test_rating_too_small(self):
        self.assertRaises(subject.InvalidRating, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         0, 'Mnogo e pich, toq Tabakov be :)')
    def test_rating_too_great(self):
        self.assertRaises(subject.InvalidRating, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210,
                                                                         11, 'Mnogo e pich, toq Tabakov be :)')
    def test_ok_subject(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', 'Wednesday', 10, 14, 325, 1, 'DIS + politika = klasika')
        self.assertTrue(calculus.name, 'DIS')
        # TODO : make some attributes private and class RATING to keep track of ratings
if __name__ == '__main__':
    unittest.main()