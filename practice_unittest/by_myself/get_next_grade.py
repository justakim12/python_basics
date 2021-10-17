import constants


class ApplyPenalty():
    def __init__(self, grade):
        self.grade = grade

    @property
    def get_next_grade(self):
        if self.grade == constants.USER_GRADE.COMMON:
            return constants.USER_GRADE.GREY
        elif self.grade == constants.USER_GRADE.GREY:
            return constants.USER_GRADE.GREY_SECOND
        elif self.grade == constants.USER_GRADE.GREY_SECOND:
            return constants.USER_GRADE.GREY_THIRD
        elif self.grade == constants.USER_GRADE.GREY_THIRD:
            return constants.USER_GRADE.BLACK
        else:
            return self.grade
