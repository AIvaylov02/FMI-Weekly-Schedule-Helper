import subject


class SelectableSubjects:
    def __init__(self, required_selectable_subjects, freely_chosen_subjects_table, min_credits_needed,
                 person_finished_subjects=None):
        self.__required_selectable_subjects = required_selectable_subjects
        # Count a category as passed if its value is equal or less than 0
        self.__freely_chosen_subjects_categories = freely_chosen_subjects_table
        self.__left_credits = min_credits_needed
        self.__person_finished_subjects = person_finished_subjects  # Lists of subjects the person has finished

    def __transfer_category_point(self, child_category, parent_category):
        while self.__freely_chosen_subjects_categories[child_category] < 0:
            self.__freely_chosen_subjects_categories[parent_category] -= 1
            self.__freely_chosen_subjects_categories[child_category] += 1

    def finish_subject(self, subj):
        subj_name = subj.get_subject_name()
        subj_group = subj.get_subject_group()
        """Clear a subject of its category. If it is already cleared, then clear its parent class(MATH/ COMP). 
                    If it also has been cleared, then subtract/clear the subject score from FREELY."""
        if subj_name in self.__required_selectable_subjects:
            subj_group = 'REQUIRED_CHOSEN'
            subj.set_subject_group(subj_group)
            self.__freely_chosen_subjects_categories[subj_group] -= 1
            self.__transfer_category_point('REQUIRED_CHOSEN', 'FREELY')

        elif subj_group in subject.SubjectGroup[2::]:
            if subj_group == 'OTHER':
                subj_group = 'FREELY'
            self.__freely_chosen_subjects_categories[subj_group] -= 1
            if subj_group in ('PURE_MATH', 'APM'):
                self.__transfer_category_point(subj_group, 'MATH')
                self.__transfer_category_point('MATH', 'FREELY')
            elif subj_group in ('CSF', 'CSC'):
                self.__transfer_category_point(subj_group, 'COMP')
                self.__transfer_category_point('COMP', 'FREELY')
            elif subj_group in ('CSP', 'REQUIRED_CHOSEN'):  # Just else would make an infinite loop of freely to freely
                self.__transfer_category_point(subj_group, 'FREELY')

        else:  # the subject group is not valid
            raise subject.InvalidSubjectGroup

        self.__left_credits -= subj.get_ECTS_credits()
        self.__person_finished_subjects.append(subj)

    def get_required_subject(self):
        return self.__required_selectable_subjects

    def get_freely_chosen_subjects_categories(self):
        return self.__freely_chosen_subjects_categories

    def get_remaining_credits_balance(self):
        return self.__left_credits

    def get_persons_finished_subjects_list(self):
        return self.__person_finished_subjects


DefaultRegularPlan_SI = (
    ('Algebra', 'Calculus 1', 'English', 'Discrete structures 1', 'Introduction to programming'),
    ('Geometry', 'Calculus 2', 'Computer english', 'Discrete structures 2', 'Object-oriented programming'),
    ('Computer architectures', 'Introduction to software engineering', 'Communication skills',
     'Data structures and algorithms'),
    ('Databases', 'Economics of software engineering', 'Software architectures and software development',
     'Computer networks', 'Operation systems', 'Differential equations and applications'),
    ('XML technologies for semantic web', 'Social aspects of IT', 'Statistics and empirical methods',
     'Quality assurance'),
    ('Web technologies', 'Requirements engineering', 'Design of human machine interface',
     'Distributed software architectures'),
    ('Data Mining', 'Design and integration of software systems', 'Projects management')
)

DefaultRegularPlan_IS = (
    ('Algebra', 'Calculus 1', 'Discrete structures', 'Introduction to programming'),
    ('Geometry', 'Calculus 2', 'Functional programming', 'Object-oriented programming',
     'Information systems basics 1'),
    ('Computer architectures', 'English 1', 'Information systems basics 2', 'Data structures',
     'Information systems - theory and practice'),
    ('Databases', 'English 2', 'Applied object-oriented programming 1', 'Computer networks',
     'Statistics and empirical methods'),
    ('XML technologies', 'Databases management systems', 'Systems based on knowledge', 'Specialized english',
     'Communication skills and teamwork'),
    ('Web technologies', 'Analysis and design of information systems', 'Distributed IT architectures'),
    ('E-Business systems', 'Projects management', 'Information security fundamentals')
)

DefaultRegularPlan_KN = (
    ('Algebra 1', 'Calculus 1', 'Discrete structures', 'Introduction to programming'),
    ('Geometry', 'Calculus 2', 'English', 'Languages, automatas, computability', 'Object-oriented programming'),
    ('Computer architectures', 'Computer english', 'Functional programming', 'Data structures and programming',
     'Computer graphics basics'),
    ('Operations Research', 'Algebra 2', 'Design and analysis of algorithms', 'Computer networks',
     'Operation systems'),
    ('Logical programming', 'Network programming', 'System programming', 'Social aspects of IT',
     'Numerical Analysis'),
    ('Databases', 'Probabilities and statistics', 'Parallel processing systems ', 'Software technologies'),
    ('Web technologies', 'Artificial Intelligence', 'Software architectures')
)


# todo maybe change the tuple of tuples into tuple of dicts, of key = <string>name and value = <double> ECTS credits from this subject
class StudyPlan:
    def __init__(self, speciality, semester, taken_subjects=None):
        self.__speciality = speciality
        if speciality == 'Software Engineering':
            self.__planned_regular = DefaultRegularPlan_SI
            self.__planned_additional = SelectableSubjects(('Operations Research', 'Numerical Analysis'),
                                                           {'CSF': 1, 'CSC': 1,
                                                            'COMP': 4, 'CSP': 2, 'PURE_MATH': 1, 'APM': 0, 'MATH': 2,
                                                            'REQUIRED_CHOSEN': 1, 'FREELY': 1}, 62)
        elif speciality == 'Information Systems':
            self.__planned_regular = DefaultRegularPlan_IS
            self.__planned_additional = SelectableSubjects(('Differential equations', 'Operations Research',
                                                            'Numerical Analysis', 'Algebra 2'),
                                                           {'CSF': 2, 'CSC': 2, 'COMP': 2, 'CSP': 3, 'PURE_MATH': 0,
                                                            'APM': 0,
                                                            'MATH': 3, 'REQUIRED_CHOSEN': 1, 'FREELY': 1}, 68)
        elif speciality == 'Computer science':
            self.__planned_regular = DefaultRegularPlan_KN
            self.__planned_additional = SelectableSubjects(('Programming languages semantics',
                                                            'Computability and complexity', 'Set theory'),
                                                           {'CSF': 3, 'CSC': 3, 'COMP': 0, 'CSP': 2, 'PURE_MATH': 0,
                                                            'APM': 0, 'MATH': 2, 'REQUIRED_CHOSEN': 1, 'FREELY': 0},
                                                           55.5)
        else:
            raise subject.InvalidSpeciality

        self.__semester = semester
        self.__taken_subjects = taken_subjects
        self.__subjects_left = []
        for curr_semester in range(semester):
            for curr_subject in self.__planned_regular[curr_semester]:
                try:
                    self.__taken_subjects.index(curr_subject)
                except ValueError or TypeError:  # The subject is not present in the taken subjects category or the list is empty
                    self.__subjects_left.append(curr_subject)

    def get_speciality(self):
        return self.__speciality

    def get_semester(self):
        return self.__semester

    def advance_semester(self):
        self.__semester += 1
        for curr_subject in self.__planned_regular[self.__semester]:
            self.__subjects_left.append(curr_subject)

    def taken_subjects(self):
        return self.__taken_subjects

    def finish_subject(self, subj):
        self.__taken_subjects.append(subj)
        if subj.get_subject_group() == 'COMPULSORY':
            self.__subjects_left.remove(subj)
        else:
            self.__planned_additional.finish_subject(subj)
# TODO add read/write from files


# TODO ADD tests for class study_plan. Class Schedule