#!/bin/python
# Day 4 > A&B

import re

class guard:
    def __init__(self, g_id):
        self.id = g_id
        self.total_sleep = 0
        self.sleep = {}
        for i in range(60):
            self.sleep[i] = 0

    def add_sleep_range(self, begin, end):
        for i in range(begin, end):
            self.sleep[i] += 1
        self.total_sleep += end-begin

    def print_hist(self):
        for i,j in enumerate(self.sleep.values()):
            print('{:2}'.format(i), '.'*j)

    def lazy_minute(self):
        return sorted(self.sleep.items(), key=lambda x: x[1], reverse=True)[0]

class timetable:
    def __init__(self):
        self.raw_entries = []
        self.entries = {}
        self.entries_sorted = []
        self.guards = {}
    
    def newEntry(self, n_entry):
        regex_date = r"(\d{4}-\d{2}-\d{2})"
        regex_time = r"(\d{2}:\d{2})"
        regex_id   = r"(\#\d*)"
        entry = []
        try:
            date = [int(i) for i in re.search(regex_date, n_entry).group().split('-')]
            entry.append(date)

            time = [int(i) for i in re.search(regex_time, n_entry).group().split(':')]
            entry.append(time)
            
            g_id = re.search(regex_id, n_entry)
            if(g_id != None):
                entry.append(int(g_id.group()[1:]))
                entry.append(0)
            else:
                entry.append(None)
                if(n_entry.find('wakes') != -1):
                    entry.append(2)
                else:
                    entry.append(1)
            self.raw_entries.append(entry)
        except:
            pass

    def entries_sort(self):
        etrs = self.entries
        for i in self.raw_entries:
            entry = []
            time_stamp = i[0][0]*10000 + i[0][1]*100 + i[0][2]
            entry.append(i[1][0]*60 + i[1][1])
            entry.append(i[2])
            entry.append(i[3])
            entry.append(i[0:2])

            if(time_stamp in etrs):
                etrs[time_stamp] += [entry]
            else:    
                etrs[time_stamp] = [entry]
        
        for i in etrs:
            etrs[i] = sorted(etrs[i], key=lambda x: x[0])
        self.entries_sorted = sorted(etrs.items(), key=lambda x: x[0])

    def create_guards(self):
        etrs = self.entries
        for i in etrs:
            for j in etrs[i]:
                if(j[2] == 0):
                    g_id = j[1]
                    if(not(g_id in self.guards)):
                        self.guards[g_id] = guard(g_id)

    def guard_analysis(self):
        etrs = self.entries_sorted
        curr_guard = 0
        for i in etrs:
            go_sleep = 0
            end_sleep = 0
            for j in i[1]:
                if(j[2] == 0):
                    curr_guard = j[1]
                elif(j[2] == 1):
                    go_sleep = j[0]
                elif(j[2] == 2):
                    end_sleep = j[0]
                    self.guards[curr_guard].add_sleep_range(go_sleep, end_sleep)

    def guard_most_sleep(self):
        sleep = []
        for i in self.guards.values():
            sleep.append([i.id, i.total_sleep])
        sleep = sorted(sleep, key=lambda x: x[1], reverse=True)
        return sleep[0]

    def print_guards_stats(self):
        for i in self.guards.values():
            print("Guard #{} > Total sleep: {}".format(i.id, i.total_sleep))

    def most_frequently_asleep_guard(self):
        stats = []
        for i in self.guards.values():
            stats.append([i.id]+list(i.lazy_minute()))
        return sorted(stats, key=lambda x: x[2], reverse=True)[0]
        
    def print_entries(self):
        etrs = self.entries_sorted
        for i in etrs:
            print(i[0])
            for j in i[1]:
                print(j)
            print()


input_file = open("input", 'r')
guards_table = input_file.read().split('\n')
input_file.close()

times = timetable()

for g in guards_table:
    times.newEntry(g)

times.entries_sort()
times.create_guards()
times.guard_analysis()

# times.print_guards_stats()

sleepy_guard = times.guard_most_sleep()
lazy_min = times.guards[sleepy_guard[0]].lazy_minute()
frequent_guard = times.most_frequently_asleep_guard()
# times.guards[sleepy_guard[0]].print_hist()

print("## Part A ##")
print("Sleepy guard: Elf with ID #{} sleeping a total of {} minutes".format(sleepy_guard[0], sleepy_guard[1]))
print("The most lazy minute was: {}".format(lazy_min[0]))
print("Solution: {}".format(lazy_min[0]*sleepy_guard[0]), end="\n\n")

print("## Part B ##")
print("Most frequently asleep guard: Elf with ID #{} sleeping at 00:{} {} times".format(frequent_guard[0], frequent_guard[1], frequent_guard[2]))
print("Solution: {}".format(frequent_guard[0]*frequent_guard[1]), end="\n\n")