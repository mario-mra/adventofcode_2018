#!/bin/python

# Day 7 A&B

from string import ascii_uppercase as au

class steps_obj:
    def __init__(self, steps_l=[], verbose=False):
        self.steps = {}
        self.start = []
        self.end  = None
        self.steps_count = 0
        self.verbose = verbose
        for l in au:
            self.steps[l] = [[], []] # [[Requirements], [Results]]
        for s in steps_l:
            self.steps[s[1]][0].append(s[0])
            self.steps[s[0]][1].append(s[1])
        for l, r in self.steps.items():
            if(r != [[],[]]):
                self.steps_count += 1
                if(len(r[0]) == 0):
                    self.start.append(l)
                elif(len(r[1]) == 0):
                    self.end = l

    def solve_steps_alone(self):
        step_dic = self.steps
        next_step = [i for i in self.start]
        done = ''
        while(len(next_step)!=0):
            next_step = sorted(next_step)
            for i, s in enumerate(next_step):
                (print("Checking {} requirements. ".format(s), end='') if self.verbose else None)
                rqr = [0 if i in done else 1 for i in step_dic[s][0]]
                if(sum(rqr) == 0):
                    (print("Success!") if self.verbose else None)
                    done += s
                    next_add = [s if not(s in next_step) else None for s in step_dic[next_step.pop(i)][1]]
                    [next_add.remove(None) for i in range(next_add.count(None))]
                    next_step += next_add
                    break
                else:
                    (print("Fail!") if self.verbose else None)
                    
        return done

    def solve_steps(self, elf_count=4, base_time=60):
        step_dic = self.steps
        next_step = [i for i in self.start]
        done = ''
        time = -1
        workers = [[None, 0] for i in range(elf_count+1)] # [doing, remaining_time]
        while(len(done) !=  self.steps_count):
            time += 1
            (print("\nCurrent time = {}s".format(time)) if self.verbose else None)
            for work_num, work_state in enumerate(workers):
                if(work_state[0] != None):
                    if(work_state[1] == 0):
                        (print("Worker #{} has done the step {}!".format(work_num, work_state[0])) if self.verbose else None)
                        done += work_state[0]
                        work_state[0] = None
                    elif(work_state[1] > 0):
                        work_state[1] -= 1
                        
            for work_num, work_state in enumerate(workers):
                next_step = sorted(next_step)
                if(work_state[0] == None):
                    for step_num, step_val in enumerate(next_step):
                        (print("Worker #{}. Checking {} requirements. ".format(work_num, step_val), end='') if self.verbose else None)
                        rqr = [0 if i in done else 1 for i in step_dic[step_val][0]]
                        if(sum(rqr) == 0):
                            (print("Success!") if self.verbose else None)
                            work_state[0] = step_val
                            work_state[1] = base_time+ord(step_val)-ord('A')
                            # print(work_state[1])
                            (print("Worker #{} is starting the step {}!".format(work_num, work_state[0])) if self.verbose else None)
                            next_add = [s if not(s in next_step) else None for s in step_dic[next_step.pop(step_num)][1]]
                            [next_add.remove(None) for i in range(next_add.count(None))]
                            next_step += next_add
                            break
                        else:
                            (print("Fail!") if self.verbose else None)

        return done, time

    def print_step_dic(self):
        for l, r in self.steps.items():
            if(r != [[],[]]):
                print("For the step {}, it requires {} to product {}".format(l, r[0], r[1]))

if __name__ == "__main__":
    # input_file = open('./input_test', 'r')
    input_file = open('./input', 'r')
    steps_l = [[i[5], i[36]] for i in input_file.readlines()]
    input_file.close()

    steps = steps_obj(steps_l, verbose=True)

    # print("Start: {}. End: {}.".format(steps.start, steps.end))

    print("\nPart A")
    print("Doing it alone the order will be: {}".format(steps.solve_steps_alone()))

    print("\nPart B")
    elfs = 3
    base_time = 60
    result_B = steps.solve_steps(elf_count=elfs, base_time=base_time)
    print("With {} workers and a base time of {}s, It will take {}s to complete all the steps.".format(elfs+1, base_time, result_B[1]))
    print("The order will be {}".format(result_B[0]))