from mission2.src.grade_definer.grade_command.interface_grade_command import IGrade

class GoldGrade(IGrade):
    GRADE_NAME = "GOLD"
    def is_valid(self):
        return self.points >= 50
