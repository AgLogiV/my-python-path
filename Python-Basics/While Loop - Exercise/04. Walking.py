steps_goal = 10000
total_steps = 0

while total_steps < steps_goal:
    steps = input()
    if steps == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    current_steps = int(steps)
    total_steps += current_steps

diff = abs(steps_goal - total_steps)
if total_steps >= steps_goal:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
