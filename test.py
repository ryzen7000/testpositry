class keshav(object):
  def __init__(self):
    self.items=[]

  def mamey(self):
    marks={"K":[100,97,98],"M":[97,98,89],"A":[35,67,80]}
    queriname = input("Enter name : ")
    a = 10
    for i in marks[queriname]:
      i=i+a
      a=i
    return format(i/3,".2f")


kholi = keshav()
print(kholi.mamey())
