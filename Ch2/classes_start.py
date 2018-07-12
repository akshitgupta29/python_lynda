#
# Example file for working with classes
#
class MyClass ():
  def method1(self):
    print('in myclass method 1')
  def method2(self,spe):
    print ('myclass method2' +spe) 

class Another(MyClass):
  def method1(self):
    MyClass.method1(self)
    print ('another class')


  def method2(self, someString):
    print ("method2 other class")
def main():
  # c = MyClass()
  # c.method1()
  # c.method2('Hi')

  d = Another()
  d.method1()
  d.method2('hello')

  
if __name__ == "__main__":
  main()

