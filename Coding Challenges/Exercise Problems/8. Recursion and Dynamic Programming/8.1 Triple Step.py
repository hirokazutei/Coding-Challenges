# 8.1 Triple Step
# A child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

# You can use a bottom-up approach to create all possible ways.

class Stairs:
    def __init__(self, steps):
        self.steps = steps
        self.possibility = None

    def TripleStep(self, step_variation, step = 0, remaining = None):
        if remaining is None:
            remaining = self.steps
            self.possibility = 0
        remaining -= step
        if remaining == 0:
            self.possibility += 1
            return
        elif remaining < 0: #This assumes that you cannot take "2-steps" when there is only one step
            return
        for i in step_variation:
            self.TripleStep(step_variation, i, remaining)



stair = Stairs(10)
step_variation = [1, 2, 3, 4]
stair.TripleStep(step_variation)
print(stair.possibility)
