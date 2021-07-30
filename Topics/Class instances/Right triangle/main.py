class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = round(self.a * self.b / 2, 1)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
print(RightTriangle(input_c, input_a, input_b).area
      if input_c * input_c == input_a * input_a + input_b * input_b else 'Not right')
