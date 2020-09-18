def digit_sum( n ): 
    if n == 0: 
        return 0
    return (n % 10 + digit_sum(int(n / 10))) 
  
def main():
    n=int(input("Enter an int: "))
    print(f"sum of digits of 1234 is {digit_sum( n )}")

if __name__ == "__main__":
  main()
