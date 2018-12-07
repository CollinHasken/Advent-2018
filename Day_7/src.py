

def part_1():
    with open("Day_7/part1.txt", 'r') as file:
        step_requirements = {}
        step_pre_requirements = {}
        steps = set()
        for line in file:
            pre_step = line[5]
            post_step = line[-13]
            steps.add(pre_step)
            steps.add(post_step)
            if pre_step not in step_requirements:
                step_requirements[pre_step] = []
            step_requirements[pre_step].append(post_step)
            if post_step not in step_pre_requirements:
                step_pre_requirements[post_step] = []
            step_pre_requirements[post_step].append(pre_step)
        ready_steps = []
        for step in steps:
            if step not in step_pre_requirements:
                ready_steps.append(step)
        list_of_steps = []
        while len(steps) is not 0:
            ready_steps.sort()
            step = ready_steps[0]
            ready_steps.remove(step)
            list_of_steps.append(step)
            steps.remove(step)
            if step not in step_requirements:
                continue
            for post_step in step_requirements[step]:
                step_pre_requirements[post_step].remove(step)
                if step_pre_requirements[post_step] == []:
                    ready_steps.append(post_step)
        print("".join(list_of_steps))


ord_offset = 4


def part_2():
    with open("Day_7/part1.txt", 'r') as file:
        step_requirements = {}
        step_pre_requirements = {}
        steps = set()
        for line in file:
            pre_step = line[5]
            post_step = line[-13]
            steps.add(pre_step)
            steps.add(post_step)
            if pre_step not in step_requirements:
                step_requirements[pre_step] = []
            step_requirements[pre_step].append(post_step)
            if post_step not in step_pre_requirements:
                step_pre_requirements[post_step] = []
            step_pre_requirements[post_step].append(pre_step)
        ready_steps = []
        for step in steps:
            if step not in step_pre_requirements:
                ready_steps.append(step)
        list_of_steps = []
        workers = [[0, ''] for x in range(5)]
        time = 0
        while len(steps) is not 0:

            # Wait until worker unlocks something
            while ready_steps == []:
                workers.sort(key=lambda x: x[0] if x[1] != '' else 999)
                time += workers[0][0]
                workers = [[worker[0] - workers[0][0], worker[1]] for worker in workers]
                workers = [[0, worker[1]] if worker[0] < 0 else worker for worker in workers]
                for worker in workers:
                    if worker[0] != 0 or worker[1] == '':
                        continue
                    step = worker[1]
                    worker[1] = ''
                    list_of_steps.append(step)
                    if step in step_requirements:
                        for post_step in step_requirements[step]:
                            step_pre_requirements[post_step].remove(step)
                            if step_pre_requirements[post_step] == []:
                                ready_steps.append(post_step)

            # Wait until worker is free
            if all([worker[0] for worker in workers]):
                workers.sort(key=lambda x: x[0] if x[1] != '' else 999)
                time += workers[0][0]
                workers = [[worker[0] - workers[0][0], worker[1]] for worker in workers]
                workers = [[0, worker[1]] if worker[0] < 0 else worker for worker in workers]
                for worker in workers:
                    if worker[0] != 0 or worker[1] == '':
                        continue
                    step = worker[1]
                    worker[1] = ''
                    list_of_steps.append(step)
                    if step in step_requirements:
                        for post_step in step_requirements[step]:
                            step_pre_requirements[post_step].remove(step)
                            if step_pre_requirements[post_step] == []:
                                ready_steps.append(post_step)
            while ready_steps != [] and not all([worker[0] for worker in workers]):
                ready_steps.sort()
                step = ready_steps[0]
                ready_steps.remove(step)
                steps.remove(step)

                workers.sort(key=lambda x: x[0])
                workers[0] = ord(step) - ord_offset, step
        while any([worker[0] for worker in workers]):
            workers.sort(key=lambda x: x[0] if x[1] != '' else 999)
            time += workers[0][0]
            workers = [[worker[0] - workers[0][0], worker[1]] for worker in workers]
            workers = [[0, worker[1]] if worker[0] < 0 else worker for worker in workers]
            for worker in workers:
                if worker[0] != 0 or worker[1] == '':
                    continue
                step = worker[1]
                worker[1] = ''
                list_of_steps.append(step)
                if step in step_requirements:
                    for post_step in step_requirements[step]:
                        step_pre_requirements[post_step].remove(step)
                        if step_pre_requirements[post_step] == []:
                            ready_steps.append(post_step)

        print(time)


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
