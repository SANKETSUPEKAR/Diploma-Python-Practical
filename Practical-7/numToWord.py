# 3. Print the number in words for Example: 1234 => One Two Three Four
word = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
for x in input("Enter : "):
    print(word[int(x)], end=" ")
