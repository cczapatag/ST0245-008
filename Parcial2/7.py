class Stack:
  def __init__(self):
    self.stack = []

  def __str__(self):
    return str(self.stack)

  def is_empty(self):
    return len(self.stack) == 0

  def apilar(self, data):
    self.stack.append(data)

  def desapilar(self):
    assert not self.is_empty()
    return self.stack.pop()

  def punto_7(self):
    otraPila = Stack()
    for i in range(1, len(self.stack)):
      otraPila.apilar(self.stack[-i])
      otraPila.apilar(self.stack[0])
    for i in range(len(self.stack)):
      self.desapilar()
    return otraPila

def main():
  pila1 = Stack()
  for i in range(7):
    pila1.apilar(i)
  print('Pila inicial: ',pila1, sep='')
  pila2 = pila1.punto_7()
  print('Pila secundaria: ', pila2, sep='')
  print('Pila inicial vacia: ', pila1, sep='')

if __name__ == '__main__':
  main()
