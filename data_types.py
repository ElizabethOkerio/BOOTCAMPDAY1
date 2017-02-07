def data_type(input):
  
  if type(input)==str:
    
    return len(input)
    
  elif type(input)==bool:
    
    return input
    
  elif type(input)==int:
    
    if input<100:
      
      return 'less than 100'
      
    elif input>100:
      
      return 'more than 100'
      
    else:
      
      return 'equal to 100'
      
  elif type(input)==list:
    
    if len(input)<3:
      
      return None
      
    else:
      
      return input[2]
      
  else:
    
    return 'no value'

        
    
    
