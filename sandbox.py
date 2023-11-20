class Student () : 
  def __init__(self, name):
    self.name = name 
    self.scores = []
  def addReport(self, score):
    ''' 
    This function for add new value to attribute scores
    '''
    self.scores.append(score)

  def average(self):
    '''
    This function for calculate average score
    '''
    total = 0 
    for el in self.scores:
      total += el
    result = total / len(self.scores)
    return result

if __name__ == '__main__': 
  # Init variable 
  name = input("Siapa namamu? ")
  student = Student(name)
  while True: 
    # Showing menu 1-2
    print("\nMENU")
    print("1. Tambahkan nilai ")
    print("2. Rata-rata")
    print("3. Selesai")
    menuChoice = input("Silahkan pilih 1-2: ")

    # Decision base menuChoice
    if menuChoice == '1':
      score = int(input("Silahkan input score mu: "))
      student.addReport(score)
      pass
    elif menuChoice == '2':
      output = student.average()
      print(f'Nilai rata-ratanya adalah {output}')
    elif menuChoice == '3':
      break
    else:
      print("Input salah")
  