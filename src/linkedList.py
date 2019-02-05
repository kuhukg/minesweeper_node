class Node:
  def __init__(self, value=None):
    self.data = value
    self.next = None

class linkedList:
  def __init__(self):
    self.head = None
  def append(self, newVal):
    if (self.head == None):
      self.head = Node(newVal)
    else:
        node = self.head
      while (node.next != None):
        node = node.next
      node.next = Node(newVal)
  def pop(self):
    if (self.head == None):
        return None;
    else:
        returnval = self.head.data
        self.head = self.head.next
    return returnval
    
