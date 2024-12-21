import exp_root.exponentiation
import exp_root.root
import factorial.factorial
import logarithm.logarithm

def inp(text,range=0,type='float'):
    while True:
        inp0 = input(text)
        try:
            if type == 'int':
                inp0 = int(inp0)
            elif type == 'float':
                inp0 = float(inp0)
            
            if range == 10:
                if inp0 <= 0:
                    raise TypeError
            elif range == 11:
                if inp0 < 0:
                    raise TypeError
            elif range == -10:
                if inp0 >= 0:
                    raise TypeError
            elif range == -11:
                if inp0 > 0:
                    raise TypeError
            elif range == 0:
                pass
            break
        except ValueError:
            print(f'Please input a{'n' if type=='int' else ''} {type} type, try again')
        except TypeError:
            print(f'Please input a number {'higher' if range>0 else 'lower'} {'or equal to' if range%10==1 else 'than'} 0')
    return inp0
            
def main():
    funclist = ['log','lg','ln','exp2','exp3','root2','root3','factorial']
    print('The functions are:',' '.join(funclist))
    choice = input('Choose a function: ')
    if choice == 'log':
        while TypeError:
            a = inp('Base is ',10,'float')
            if a == 1:
                print('Base cant equal to 1')
            else:
                break
        b = inp('Number is ',10,'float')
        print(f'The log of {b} in base {a} is {logarithm.logarithm.log(a,b)}')
    elif choice == 'lg':
        b = inp('Number is ',10,'float')
        print(f'The log10 of {b} is {logarithm.logarithm.lg(b)}')
    elif choice == 'ln':
        b = inp('Number is ',10,'float')
        print(f'The natural log of {b} is {logarithm.logarithm.ln(b)}')
    elif choice == 'exp2':
        num = inp('Input a number ')
        print(f'The number raised to the power of 2 is {exp_root.exponentiation.exp2(num)}')
    elif choice == 'exp3':
        num = inp('Input a number ')
        print(f'The number raised to the power of 3 is {exp_root.exponentiation.exp3(num)}')
    elif choice == 'root2':
        num = inp('Input a number ',11)
        print(f'The square root from the number is {exp_root.root.root2(num)}')
    elif choice == 'root3':
        num = inp('Input a number ')
        print(f'The square root from the number is {exp_root.root.root3(num)}')
    elif choice == 'factorial':
        num = inp('Input a number ',11,'int')
        print(f'The factorial of the number is {factorial.factorial.fact(num)}')
    else:
        print('Oops! Youve chosen something that isnt an option.')
main()
if __name__ == "main":
    main()