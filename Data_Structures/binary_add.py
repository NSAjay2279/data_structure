class Solution:

  def __init__(self):
    self.carry = "0"

  def add(self,x,y):
    if x=="0" and y=="0" and self.carry == "0":
      self.carry = "0"
      return "0"
    elif x=="0" and y=="0" and self.carry == "1":
      self.carry = "0"
      return "1"
    elif x=="0" and y=="1" and self.carry == "0":
      self.carry = "0"
      return "1"
    elif x=="0" and y=="1" and self.carry == "1":
      self.carry = "1"
      return "0"
    elif x=="1" and y=="0" and self.carry == "0":
      self.carry = "0"
      return "1"
    elif x=="1" and y=="0" and self.carry == "1":
      self.carry = "1"
      return "0"
    elif x=="1" and y=="1" and self.carry == "0":
      self.carry = "1"
      return "0"
    elif x=="1" and y=="1" and self.carry == "1":
      self.carry = "1"
      return "1"
    else:
      return None

  def binAdd(self,a,b):
    a = list(a)
    b = list(b)
    m = len(a)
    n = len(b)

    if m >= n:
      b = ["0"]*(m-n) + b
      
    else:
      a = ["0"]*(n-m) + a
      
    tot_len = max(m,n)
    # space complexity: O(n)
    c = ["0"] * tot_len

    # time complexity: O(n)
    for i in range(tot_len, 0, -1):
      c[i-1] = self.add(a[i-1], b[i-1])
    if self.carry == "1":
      c = ["1"] + c
      self.carry = "0"
    return "".join(c)



def main():
  sol = Solution()

  a1 = "11"
  b1 = "1"
  output1 = sol.binAdd(a1, b1)
  print(f"Binary addition of {a1} and {b1} is: {output1}") # Expected output: "100"
  
  a2 = "1010"
  b2 = "1011"
  output2 = sol.binAdd(a2, b2)
  print(f"Binary addition of {a2} and {b2} is: {output2}") # Expected output: "10101"
  
  a3 = "111"
  b3 = "10"
  output3 = sol.binAdd(a3, b3)
  print(f"Binary addition of {a3} and {b3} is: {output3}") # Expected output: "1001"

  a4 = "110"
  b4 = "001"
  output4 = sol.binAdd(a4, b4)
  print(f"Binary addition of {a4} and {b4} is: {output4}") # Expected output: "111"
 
  a5 = "0"
  b5 = "0"
  output5 = sol.binAdd(a5, b5)
  print(f"Binary addition of {a5} and {b5} is: {output5}") # Expected output: "0"



main()
