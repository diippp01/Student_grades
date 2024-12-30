import unittest
from student_grade import StudentGrades

class TestStudentGrades(unittest.TestCase):

    def setUp(self):
        """Set up test data for all test methods."""
        self.grades = StudentGrades()
        self.grades.add_grade("Alice", 85)
        self.grades.add_grade("Bob", 92)
        self.grades.add_grade("Charlie", 78)

    def test_add_grade(self):
        self.grades.add_grade("Daisy", 88)
        self.assertEqual(self.grades.get_grade("Daisy"), 88)
        with self.assertRaises(ValueError):
            self.grades.add_grade("Eve", 105)  # Invalid grade

    def test_get_grade(self):
        self.assertEqual(self.grades.get_grade("Alice"), 85)
        with self.assertRaises(KeyError):
            self.grades.get_grade("Unknown")  # Student not found

    def test_average_grade(self):
        self.assertAlmostEqual(self.grades.average_grade(), (85 + 92 + 78) / 3)
        self.grades.add_grade("Daisy", 88)
        self.assertAlmostEqual(self.grades.average_grade(), (85 + 92 + 78 + 88) / 4)

    def test_highest_grade(self):
        self.assertEqual(self.grades.highest_grade(), ("Bob", 92))
        self.grades.add_grade("Eve", 95)
        self.assertEqual(self.grades.highest_grade(), ("Eve", 95))

    def test_empty_grades(self):
        empty_grades = StudentGrades()
        with self.assertRaises(ValueError):
            empty_grades.average_grade()
        with self.assertRaises(ValueError):
            empty_grades.highest_grade()

if _name_ == "_main_":
    unittest.main()
