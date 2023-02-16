import subject


class ViewedSubject(subject.Subject):
    """The class may be overkill, but I think it would give class Schedule managable and nice interface for the GUI"""

    def __init__(self, name, group, lecturer, ECTS_credits, lecture_type, study_times, raw_place,
                 can_be_signed_up_by_table, background_color, font_color, priority=None, ratings=None, reviews=None):
        super().__init__(name, group, lecturer, ECTS_credits, lecture_type, study_times, raw_place,
                         can_be_signed_up_by_table, ratings, reviews)
        self.__background_color = None
        self.set_background_color(background_color)
        self.__font_color = None
        self.set_font_color(font_color)
        self.__priority = None
        self.set_priority(priority)

    def get_background_color(self):
        return self.__background_color

    def get_font_color(self):
        return self.__font_color

    def get_priority(self):
        return self.__priority

    def set_background_color(self, color):
        color = color.lower()
        self.__background_color = color

    def set_font_color(self, color):
        color = color.lower()
        self.__font_color = color

    def set_priority(self, priority):
        if priority is None or priority < 0:
            self.__priority = 0
        else:
            self.__priority = priority

    def increment_priority(self):  # This may be a perfect situation to implement __methods__
        self.__priority += 1

    def decrement_priority(self):
        if self.__priority > 0:
            self.__priority -= 1

    def __lt__(self, other_subj):
        return self.__priority < other_subj.get_priority()

    def __le__(self, other_subj):
        return self.__priority <= other_subj.get_priority()

    def __eq__(self, other_subj):
        return self.__priority == other_subj.get_priority()


class Schedule:

    def __init__(self, speciality, regular_subjects=None, choosable_subjects=None):
        self.__weekly_table = {'Monday': {}, 'Tuesday': {}, 'Wednesday': {}, 'Thursday': {}, 'Friday': {}, 'Saturday': {},
                                'Sunday': {}}  # dict of <day>:dict. The second dict consists of <hour> subject
        self.__unique_compulsory_subjects = []
        self.__unique_choosable_subjects = []
        # overlaps should be dealt with from the programme by putting the highest priority subject of given hour in the front of the list

    def can_add_choosable_subj(self):
        return len(self.__unique_choosable_subjects) <= 5

    def add_subject(self, subj):
        if subj.get_group() == 'COMPULSORY':
            try:
                self.__unique_compulsory_subjects.index(subj)
            except ValueError:  # the value has not yet been added
                self.__unique_compulsory_subjects.append(subj)
                self.__manipulate_subject_times(subj, 'add')
        else:
            try:
                self.__unique_choosable_subjects.index(subj)
            except ValueError:  # the value has not yet been added
                self.__unique_choosable_subjects.append(subj)
                self.__manipulate_subject_times(subj, 'add')

    def __manipulate_subject_times(self, subj, mode):
        study_times = subj.get_study_times()
        for key, value in study_times.items():
            start_hour, end_hour = value
            while start_hour < end_hour:
                if mode == 'remove':
                    self.__weekly_table[key][start_hour].remove(subj)
                else:  # we add subject
                    self.__weekly_table[key][start_hour].append(subj)
                start_hour += 1

    def remove_subject(self, subj):
        if subj.get_group() == 'COMPULSORY':
            return
        try:
            self.__unique_choosable_subjects.remove(subj)
        except ValueError:
            return
        self.__manipulate_subject_times(subj, 'remove')

    def finish_subject(self, subj):
        # tick the study_plan
        if subj.get_group() != 'COMPULSORY':
            self.remove_subject(subj)
        else:
            try:
                self.__unique_compulsory_subjects.remove(subj)
            except ValueError:
                return
            self.__manipulate_subject_times(subj, 'remove')