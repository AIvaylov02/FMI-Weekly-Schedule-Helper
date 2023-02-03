SubjectGroup = ('COMPULSORY',  # They are given by the learning plan automatically
                'REQUIRED_CHOSEN',  # The so-called ZIP (You need to choose these subjects)
                # Below are only subject categories you can freely choose without constrain
                'MATH',
                'APM',  # Applied Math
                'CSF',  # Computer Science Fundamentals
                'CSC',  # Computer Science Core
                'CSP',  # Computer Science Practicum
                'OTHER')


LectureType = ('L',  # Lecture
               'TE',  # Theoretical Exercise
               'CPE')  # Computer Practicum Exercise


Days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'


def is_valid_subject_name(name):
    if name is None:
        return False
    elif not name[0].isupper():  # A valid subject name starts with capital letter
        return False
    else:
        remainder = name[1:]  # And has only letters, digits or these special symbols
        for curr_char in remainder:
            if not (curr_char.isalpha() or curr_char.isdigit() or curr_char in (',', '.', '(', ')', '-', ' ')):
                return False
    return True


def is_valid_person_name(name):
    if not is_valid_subject_name(name):
        return False
    else:
        remainder = name[1:]
        white_space_found = False
        second_capital_found = False
        for curr_char in remainder:  # A valid person name should consist of 2 names with space between
            if white_space_found:
                if curr_char.isupper():
                    second_capital_found = True
            elif curr_char == ' ':
                white_space_found = True
            elif not curr_char.islower():  # All other symbols should be lowercase
                return False
        if white_space_found == False or second_capital_found == False:
            return False
        else:
            return True


def are_valid_days(days):
    if type(days) == list:
        return all(i in Days for i in days)
    else:
        return days in Days


class InvalidInput(Exception):
    pass


class InvalidSubjectName(InvalidInput):
    pass


class InvalidPersonName(InvalidInput):
    pass


class InvalidSubjectGroup(InvalidInput):
    pass


class InvalidECTSCredits(InvalidInput):
    pass


class InvalidLectureType(InvalidInput):
    pass


class InvalidWeekday(InvalidInput):
    pass


class InvalidWorkHour(InvalidInput):
    pass


class InvalidRating(InvalidInput):
    pass


class Subject:
    def __init__(self, name, group, lecturer, ECTS_credits, lecture_type, studied_days, start_hour, end_hour, room,
                 rating=None, reviews=None):
        if is_valid_subject_name(name):
            self.name = name
        else:
            raise InvalidSubjectName
        if group in SubjectGroup:
            self.grop = group
        else:
            raise InvalidSubjectGroup
        if is_valid_person_name(lecturer):
            self.lecturer = lecturer
        else:
            raise InvalidPersonName
        if 0 < ECTS_credits <= 10:
            self.ECTS_credits = ECTS_credits
        else:
            raise InvalidECTSCredits
        if lecture_type in LectureType:
            self.lecture_type = lecture_type
        else:
            raise InvalidLectureType
        if are_valid_days(studied_days):
            self.studied_days = studied_days
        else:
            raise InvalidWeekday
        if 7 <= start_hour <= 22:
            self.start_hour = start_hour
        else:
            raise InvalidWorkHour
        # One lecture should be at least 1 hour and not more than 5 hours max
        if 7 <= end_hour <= 24 and end_hour > start_hour and end_hour - start_hour <= 5:
            self.end_hour = end_hour
        else:
            raise InvalidWorkHour
        self.room = room  # You could study from anywhere, so there are no restrictions here
        if 1 <= rating <= 10:
            self.rating = rating
        else:
            raise InvalidRating
        self.reviews = reviews

# my_hour = Subject('algebra', 'COMPULSORY', 'Konstantin Tabakov', 6.5, 'L', 'Monday', 16, 19, 210, 10, 'Mnogo e pich, toq Tabakov be :)')
