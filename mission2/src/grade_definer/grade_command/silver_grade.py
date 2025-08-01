from mission2.src.grade_definer.grade_command.interface_grade_command import IGrade

class SilverGrade(IGrade):
    GRADE_NAME = "SILVER"
    def is_valid(self):
        return 50 > self.points >= 30
