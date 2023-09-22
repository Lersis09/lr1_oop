import math # підключення бібліотеки
def task_integer16():
    """A three-digit number is given. Output the number obtained by permuting the digits
    tens and ones of the original number (for example, 123 will become 132)."""
    try: # перевірка на помилки
        num = int(input("Enter a three-digit number: "))
    except: # якщо помилка
        print("Num must be an INTEGER !!!")
        input("Press enter for exit ...")
    else: # якщо немає помилки
        num = str(num)
        a = num[0];b = num[2];c = num[1]
        print(a + b + c)
      
def task_33():
    try: # перевірка на помилки
      x = float(input("x = "))
    except: # якщо помилка
        print("Wrong number!")
    else: # якщо немає помилки
        num1 = 2 * exp(x+0.5);
        num2 = sqrt(fabs(3*x - 2 * tan(5*x - radians(43))));
        x3 = x * x * x;
        try:
          denum = pow(pow(sin(x3), 2), 1.0/3.0) * log(fabs(x3), 5);
          y = num1 * num2 / denum;
        except:
          print("Error calculations!")
        else:
          print("y = ", y)
          
def task_boolean16():
    """Given a positive integer. Check the truth of the statement:"The given number is an even two-digit number.""""
    try:
        num = int(input("Num = "))
    except:
        print("Num MUST be an integer!!!")
        input("Press enter to exit ...")
    else:   
        if num >= 10 and num <= 99 and num % 2 == 0:
            print("Num is an even two-digit number: ", num)
        else:
            print("Num is not an even two-digit number.")
