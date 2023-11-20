import unittest 
from sandbox import Student 

class TestCaseStudent(unittest.TestCase):
  def test_initValue(self):
    name = 'Ayu'
    student = Student(name)
    self.assertEqual(student.name, name)

  def test_addScore(self):
    # input 
    student = Student("Ayu")
    score = 90 
    # process 
    student.addReport(score)
    # ouput 
    self.assertEqual(len(student.scores), 1)
    self.assertEqual(student.scores[0], score)

  def test_average(self):
    # input 
    student = Student("Yuda")
    student.addReport(80)
    student.addReport(20)
    # process 
    result = student.average()
    # output
    self.assertEqual(result, 50.0)

unittest.main()