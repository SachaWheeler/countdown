import random

add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b if a % b == 0 else 0/0

operations = [ (add, '+'),
               (sub, '-'),
               (mul, '*'),
               (div, '/')]

def one_from_the_top():
    return [25, 50, 75][random.randint(0,2)]

def one_of_the_others():
    return random.randint(1,10)

def evaluate(stack):
    try:
        total = 0
        last_operation = add
        for item in stack:
            if type(item) is int:
                total = last_operation(total, item)
            else:
                last_operation = item[0]

        return total
    except:
        return 0

def print_stack(stack):
    reps = [ str(item) if type(item) is int else item[1] for item in stack ]
    return ' '.join(reps)

def solve(target, numbers):

    def recurse(stack, nums):
        for n in range(len(nums)):
            stack.append( nums[n] )  # add a number

            remaining = nums[:n] + nums[n+1:]

            if evaluate(stack) == target:
                print(print_stack(stack))
                exit(0)

            if len(remaining) > 0:  # if there are still numbers to use
                for op in operations:
                    stack.append(op)  # append each operation
                    stack = recurse(stack, remaining)
                    stack = stack[:-1]  # remove that recent operation

            stack = stack[:-1]  # remove the most recent number

        return stack

    recurse([], numbers)


target = random.randint(100,1000)

numbers = [ one_from_the_top() ] + [ one_of_the_others() for i in range(5) ]

print(f"Target: {target} using {numbers}")

solve(target, numbers)
