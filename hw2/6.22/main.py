# Name: Samuel Barroso
# PSID: 1844307

def bruteForce(a1, b1, c1, a2, b2, c2):
  for x_temp in range(-10,10):
    for y_temp in range(-10,10):
      if ((a1*x_temp + b1*y_temp) == c1 and (a2*x_temp + b2*y_temp) == c2):
        return x_temp, y_temp
  return "No", "solution"

if __name__ == "__main__":
  a1 = int(input())
  b1 = int(input())
  c1 = int(input())
  a2 = int(input())
  b2 = int(input())
  c2 = int(input())

  x, y = bruteForce(a1, b1, c1, a2, b2, c2)
  print(x, y)