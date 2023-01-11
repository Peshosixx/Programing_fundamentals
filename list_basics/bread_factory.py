import re
initial_energy = 100
initial_coins = 100
working_day_events = input()
working_day_events = re.split('-|[|]', working_day_events)
event, amount = [], []
breaking_flag = False
for events in range(len(working_day_events)):
    if events % 2 == 0:
        event.append(working_day_events[events])
    else:
        amount.append(int(working_day_events[events]))
for process in range(len(event)):
    if event[process] == 'rest':
        if initial_energy < 100:
            if amount[process] > (100 - initial_energy):
                print(f'You gained {100-initial_energy} energy.')
                initial_energy += 100 - initial_energy
                print(f'Current energy: {initial_energy}.')
            else:
                print(f'You gained {amount[process]} energy.')
                initial_energy += amount[process]
                print(f'Current energy: {initial_energy}.')
        else:
            print('You gained 0 energy.')
            print(f'Current energy: {initial_energy}.')
    elif event[process] == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            print(f'You earned {amount[process]} coins.')
            initial_coins += amount[process]
        else:
            initial_energy += 50
            print('You had to rest!')
    else:
        if initial_coins >= amount[process]:
            print(f"You bought {event[process]}.")
            initial_coins -= amount[process]
        else:
            print(f"Closed! Cannot afford {event[process]}." )
            breaking_flag = True
            break
if not breaking_flag:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
