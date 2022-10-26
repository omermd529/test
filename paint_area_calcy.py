#Write your code below this line 👇
def paint_calc(height,width,cover):
  raw_material=(height*width)/cover
  round_off_cans=round(raw_material)
  inr_bill = round_off_cans*50*80
  print(inr_bill)







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

