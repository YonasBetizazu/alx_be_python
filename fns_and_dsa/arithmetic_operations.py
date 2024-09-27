def perform_operation(num1,num2,"operation"):
    match operation:
        case 'add':
         return (num1)+(num2)
        case 'subtract':
          return (num2)+(num1)
        case 'multiply':
          return (num1)*(num2)
        case 'divide':
          if (num2)==0:
             print("undfined")
          else:
             return (num1)/(num2)
