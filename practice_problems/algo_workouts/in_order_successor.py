'''
minumumNode(node) 
  let curr = node;
  while(curr.left)
    curr = curr.left
  
  return curr.val

while curr
  if curr.value == target:
    if curr.right:
        return minimumNode(curr.right)
    return parent
  elif curr.value > target:
    parent = curr
    curr = curr.left
  else:
    curr = curr.right
    
'''