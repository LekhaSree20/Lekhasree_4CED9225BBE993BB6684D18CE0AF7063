def fact_class(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_class(n - 1)


num = int(input("Enter the Number:"))
result = fact_class(num)
print("The factorial Value {} is {}".format(num, result))
