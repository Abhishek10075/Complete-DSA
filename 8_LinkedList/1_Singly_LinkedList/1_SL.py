'''
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3
print(node3.val)

'''
class Node:
  def __init__(self,val):
    self.val=val
    self.next=None
class SinglyLinkedList:
  def __init__(self):
    self.head=None

  def append(self,val):
    new_node=Node(val)
    if self.head==None:
      self.head=new_node
    else:
      curr=self.head
      while curr.next is not None:
        curr=curr.next
      curr.next=new_node

  def traverse(self):
    curr=self.head
    if self.head==None:
      print('SLL is empty')
    else:
      while curr is not None:
        print(curr.val,end='->')
        curr=curr.next

  
  def insert_at(self,val,pos):
    new_node=Node(val)
    if pos==0:
      new_node.next=self.head
      self.head=new_node
    else:
      prev=None
      curr=self.head
      count=0
      while curr is not None and count<pos:
        prev=curr
        curr=curr.next
        count+=1
      prev.next=new_node
      new_node.next=curr

  def delete(self,target):
    temp=self.head
    if temp is None:
      print("List is empty")
      return
    if temp.val==target:
      self.head=temp.next
      temp.next=None
      del temp
    else:
      temp=self.head
      prev=None
      curr=temp
      while temp is not None:
        if curr.val==target:
          prev.next=curr.next
          curr.next=None
          del curr
          return
        prev=curr
        curr=curr.next
obj=SinglyLinkedList()
obj.traverse()
obj.append(5)
obj.append(10)
obj.append(15)
obj.traverse()
obj.insert_at(20,2)
obj.insert_at(0,0)
print()
obj.traverse()
obj.delete(0)
print("After delete")
obj.traverse()
obj.delete(20)
print('After delete')
obj.traverse()