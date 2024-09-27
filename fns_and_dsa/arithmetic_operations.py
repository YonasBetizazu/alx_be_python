def perform_operation(num1,num2,operation):
    match operation:
        case 'add':
         return float(num1)+float(num2)
        case 'subtract':
          return float(num2)+float(num1)
        case 'multiply':
          return float(num1)*float(num2)
        case 'divide':
          if float(num2)==0:
             print("undfined")
          else:
             return float(num1)/float(num2)