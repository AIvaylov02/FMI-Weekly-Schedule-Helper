import rating
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

Faculty = ('FHF', 'FMI', 'FZF')

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


class InvalidPlace(InvalidInput):
    pass

class InvalidRating(InvalidInput):
    pass


class Subject:

    def __parse_raw_place(self, raw_place):
        faculty = raw_place[:3]
        if faculty not in Faculty:
            raise InvalidPlace
        if raw_place[3] != '-':
            raise InvalidPlace
        room = raw_place[4:]
        if not room.isdigit():
            raise InvalidPlace
        return faculty, room

    def __validate_study_times(self, study_times):
        # study_times is dict consisting pairs : string(day)-tuple(start_hour, end_hour)
        for day in study_times:
            if day not in Days:
                raise InvalidWeekday
            start_hour, end_hour = study_times[day]
            if start_hour < 7 or start_hour > 22:
                raise InvalidWorkHour
            if end_hour < 7 or end_hour > 24 or end_hour <= start_hour or end_hour - start_hour > 5:
                raise InvalidWorkHour

    def __init__(self, name, group, lecturer, ECTS_credits, lecture_type, study_times, raw_place, ratings=None, reviews=None):
        if is_valid_subject_name(name):
            self.__name = name
        else:
            raise InvalidSubjectName
        self.set_subject_group(group)
        self.set_lecturer(lecturer)
        self.set_ECTS_credits(ECTS_credits)
        self.set_lecture_type(lecture_type)
        self.set_study_times(study_times)
        self.__faculty, self.__room = self.__parse_raw_place(raw_place)
        self.__subj_rating = rating.Rating(ratings)
        if self.__subj_rating.get_average_rating() < 1 or self.__subj_rating.get_average_rating() > 10:
            raise InvalidRating
        self.__reviews = reviews

    def get_subject_name(self):
        return self.__name

    def get_subject_group(self):
        return self.__group

    def get_lecturer(self):
        return self.__lecturer

    def get_ECTS_credits(self):
        return self.__ECTS_credits

    def get_lecture_type(self):
        return self.__lecture_type

    def get_study_times(self):
        return self.__study_times

    def get_faculty(self):
        return self.__faculty

    def get_room(self):
        return self.__room

    def get_subject_rating(self):
        return self.__subj_rating

    def get_reviews(self):
        return self.__reviews

    def set_subject_group(self, group):
        if group in SubjectGroup:
            self.__group = group
        else:
            raise InvalidSubjectGroup

    def set_lecturer(self, lecturer):
        if is_valid_person_name(lecturer):
            self.__lecturer = lecturer
        else:
            raise InvalidPersonName

    def set_ECTS_credits(self, ECTS_credits):
        if 0 < ECTS_credits <= 10:
            self.__ECTS_credits = ECTS_credits
        else:
            raise InvalidECTSCredits

    def set_lecture_type(self, lecture_type):
        if lecture_type in LectureType:
            self.__lecture_type = lecture_type
        else:
            raise InvalidLectureType

    def set_study_times(self, new_study_times):
        self.__validate_study_times(new_study_times)
        self.__study_times = new_study_times

    def add_new_study_time(self, day, start_hour, end_hour):
        if day not in Days:
            raise InvalidWeekday
        if start_hour < 7 or start_hour > 22:
            raise InvalidWorkHour
        if end_hour < 7 or end_hour > 24 or end_hour < start_hour or end_hour - start_hour > 5:
            raise InvalidWorkHour
        self.__study_times[day] = start_hour, end_hour

    def remove_study_time_by_day(self, day):
        if day not in Days or day not in self.__study_times:
            raise InvalidWeekday
        self.__study_times.pop(day)

    def set_faculty(self, faculty_short):
        if faculty_short not in Faculty:
            raise InvalidPlace
        self.__faculty = faculty_short

    def set_room(self, new_room):
        if not new_room.isdigit():
            raise InvalidPlace
        self.__room = new_room

    def add_subject_score(self, score):
        self.__subj_rating.add_score(score)

    def add_review(self, review):
        if self.__reviews is None:
            self.__reviews = []
        self.__reviews.append(review)


""" TODO : We are ready to implement reading and writing from/to files here. Maybe after implementing class 
Timetable and Study_Plan, we should do this. For know we should focus on those 2 other classes as well as class User, who
should be trivial. GUI also remains to be done."""