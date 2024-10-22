def Basiccalculator():
    print("Select operator:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4/)" )
        
        if choice in ['1', '2', '3', '4']:
            num1 =int(input("Enter fist number: "))
            num2 = int(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {(num1 + num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {(num1 - num2)}")
            elif choice == '3': 
                print(f"{num1} * {num2} = {(num1 * num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {(num1 / num2)}")
                
        else:
            print("Invalid Input")
            
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
        
if __name__== "__main__":
    Basiccalculator()