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
    """Test initializer and setters"""

    def test_subject_name_small_letters_only(self):
        self.assertRaises(subject.InvalidSubjectName, subject.Subject, 'algebra', 'COMPULSORY', 'Konstantin Tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1}, 10, 'Mnogo e pich, toq Tabakov be :)')

    def test_subject_name_forbiden_chars(self):
        self.assertRaises(subject.InvalidSubjectName, subject.Subject, 'Algebra$', 'COMPULSORY', 'Konstantin Tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_group(self):
        self.assertRaises(subject.InvalidSubjectGroup, subject.Subject, 'Algebra', 'random123', 'Konstantin Tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_person_small_letters(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'konstantin Tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_person_one_name(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'KonstantinTabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_person_only_one_capital(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_person_random_chars(self):
        self.assertRaises(subject.InvalidPersonName, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin1337Tabakov',
                          6.5, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_negative_credits(self):
        self.assertRaises(subject.InvalidECTSCredits, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov',
                          -3, 'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_lecture_type(self):
        self.assertRaises(subject.InvalidLectureType, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov',
                          6.5, 'poredna tupotiq', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  10,
                          'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_day(self):
        self.assertRaises(subject.InvalidWeekday, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Ponedelnik': (16, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_multiple_days(self):
        self.assertRaises(subject.InvalidWeekday, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (16, 19), 'Vtornik': (16, 19)}, 'FHF-210', {'ALL': 1},  10,
                          'Mnogo e pich, toq Tabakov be :)')

    def test_too_early_start_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (6, 9)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_too_late_start_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (23, 24)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_too_early_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (7, 7)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_too_late_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (22, 1)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_invalid_diff_between_start_and_end_hour(self):
        self.assertRaises(subject.InvalidWorkHour, subject.Subject, 'Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                          'L', {'Monday': (12, 19)}, 'FHF-210', {'ALL': 1},  10, 'Mnogo e pich, toq Tabakov be :)')

    def test_rating_too_small(self):
        my_subject = subject.Subject('Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                                     'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  0, 'Mnogo e pich, toq Tabakov be :)')
        self.assertEqual(my_subject.get_subject_rating().get_average_rating(),
                         1)  # by default if invalid it will be set to 1

    def test_rating_too_great(self):
        my_subject = subject.Subject('Algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5,
                                     'L', {'Monday': (16, 19)}, 'FHF-210', {'ALL': 1},  11, 'Mnogo e pich, toq Tabakov be :)')
        self.assertEqual(my_subject.get_subject_rating().get_average_rating(),
                         1)  # by default if invalid it will be set to 1

    def test_add_speciality_course_of_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'SI': 1}, 1, 'DIS + politika = klasika')
        comp_science = 'KN'
        course = 1
        calculus.change_speciality_course_of_signing_up_table(comp_science, course)
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 1, 'KN': 1})

    def test_add_invalid_speciality_to_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'SI': 1}, 1, 'DIS + politika = klasika')
        applied_maths = 'APM'
        course = 1
        try:
            calculus.change_speciality_course_of_signing_up_table(applied_maths, course)
        except subject.InvalidSpeciality:
            self.assertEqual(1, 1)

    def test_change_speciality_course_of_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'SI': 1}, 1, 'DIS + politika = klasika')
        soft_eng = 'SI'
        course = 3
        calculus.change_speciality_course_of_signing_up_table(soft_eng, course)
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 3})

    def test_remove_speciality_course_of_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 3}, 1, 'DIS + politika = klasika')
        soft_eng = 'SI'
        calculus.remove_speciality_from_signing_up_table(soft_eng)
        self.assertDictEqual(calculus.get_signing_up_table(), {'IS': 3, 'KN': 3})

    def test_remove_invalid_speciality_course_of_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 3}, 1, 'DIS + politika = klasika')
        math = 'MATH'
        try:
            calculus.remove_speciality_from_signing_up_table(math)
        except subject.InvalidSpeciality:
            self.assertEqual(1, 1)

    def test_remove_missing_speciality_course_of_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'KN': 1}, 1, 'DIS + politika = klasika')
        soft_eng = 'SI'
        try:
            calculus.remove_speciality_from_signing_up_table(soft_eng)
        except KeyError:
            self.assertEqual(1, 1)

    def test_parse_valid_signing_up_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'KN': 1}, 1, 'DIS + politika = klasika')
        calculus.set_signing_up_table({'SI': 3, 'IS': 3, 'KN': 3})
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 3, 'IS': 3, 'KN': 3})

    def test_parse_all_subjects_from_key_all(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'KN': 4}, 1, 'DIS + politika = klasika')
        calculus.set_signing_up_table({'IS': 3, 'SI': 1, 'ALL': 2})  # 'All' will overwrite the others
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 2, 'IS': 2, 'KN': 2})

    def test_set_all_subjects_and_change_individual_table(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'KN': 4}, 1, 'DIS + politika = klasika')
        calculus.set_signing_up_table({'ALL': 2, 'SI': 3})  # 'All' will overwrite the others
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 3, 'IS': 2, 'KN': 2})

    def test_invalid_parse_with_one_broken_speciality(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'KN': 4}, 1, 'DIS + politika = klasika')
        try:
            calculus.set_signing_up_table({'ALL': 2, 'APM': 2})  # APM is not allowed, so it will throw exception
        except subject.InvalidSpeciality:
            self.assertEqual(1, 1)

    def test_ok_subject(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 1},  1, 'DIS + politika = klasika')
        self.assertEqual(calculus.get_subject_name(), 'DIS')
        self.assertEqual(calculus.get_subject_group(), 'COMPULSORY')
        self.assertEqual(calculus.get_lecturer(), 'Vladimir Babev')
        self.assertEqual(calculus.get_ECTS_credits(), 8)
        self.assertEqual(calculus.get_lecture_type(), 'L')
        self.assertDictEqual(calculus.get_study_times(), {'Wednesday': (10, 14)})
        self.assertEqual(calculus.get_faculty(), 'FMI')
        self.assertEqual(calculus.get_room(), '325')
        self.assertDictEqual(calculus.get_signing_up_table(), {'SI': 1, 'IS': 1, 'KN': 1})
        self.assertEqual(calculus.get_subject_rating().get_average_rating(), 1)
        self.assertListEqual(calculus.get_reviews(), ['DIS + politika = klasika'])

    """Test more setters or advanced functions"""

    def test_change_invalid_faculty(self):  # There is probably a better way to do it
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 1},  1, 'DIS + politika = klasika')
        try:
            calculus.set_faculty('Rektorat')
        except subject.InvalidPlace:
            self.assertEqual(1, 1)

    def test_change_invalid_room(self):  # There is probably a better way to do it
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 1}, 1, 'DIS + politika = klasika')
        try:
            calculus.set_room('a21')
        except subject.InvalidPlace:
            self.assertEqual(1, 1)

    def test_add_review(self):
        original_review = ['DIS + politika = klasika']
        dis_review = original_review
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 1},  1, dis_review)
        my_review = '18-ti proizvodni ne mojem da namirame!'
        calculus.add_review(my_review)
        my_list = [original_review, my_review]
        self.assertListEqual(calculus.get_reviews(), my_list)

    def test_add_study_time(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14)}, 'FMI-325',
                                   {'ALL': 1},  1, '18-ti proizvodni ne mojem da namirame!')
        calculus.add_new_study_time('Monday', 16, 19)
        self.assertDictEqual(calculus.get_study_times(), {'Wednesday': (10, 14), 'Monday': (16, 19)})

    def test_remove_study_time(self):
        calculus = subject.Subject('DIS', 'COMPULSORY', 'Vladimir Babev', 8, 'L', {'Wednesday': (10, 14),
                                                                                   'Monday': (16, 19)}, 'FMI-325',
                                   {'ALL': 1},  1, '18-ti proizvodni ne mojem da namirame!')
        calculus.remove_study_time_by_day('Wednesday')
        self.assertDictEqual(calculus.get_study_times(), {'Monday': (16, 19)})


if __name__ == '__main__':
    unittest.main()
