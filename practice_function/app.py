def say_hi():
    print("Hello User")

## call function
say_hi()

## add parameters
def say_hi_name(name):
    print("Hello " + name)

say_hi_name("Mike")

## add return
def cube(num):
    return num*num*num

print(cube(3))

result = cube(4)
print(result)