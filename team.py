# possibles is the list a list of groups for each group where it has no conflict where the 2 persons in a group are not in the other group 
# each group with non conflicting group tuple
possibles = {
 1: (6,  9, 'd', 'a', 'e', 'f'), 
 2: (5,  8, 'c', 'a', 'e', 'f'), 
 3: (4,  7, 'a', 'b',  'e',  'f'), 
 4: (3, 8, 'c', 9, 'd', 'f'), 
 5: (2, 7, 9, 'b', 'd', 'f'),
 6: (1, 7, 8, 'b', 'c', 'f'),
 7: (3, 5, 6, 'c', 'd', 'e'),
 8: (2, 4, 6, 'b', 'd', 'e'),
 9: (1, 4, 5, 'b', 'c', 'e'),
 'a': (1, 2, 3, 'b', 'c', 'd'),
 'b': (3, 5, 6, 8, 9, 'a'),
 'c': (2, 4, 6, 7, 9, 'a'),
 'd': (1, 4, 5, 7, 8, 'a'),
 'e': (1, 2, 3, 7, 8, 9),
 'f': (1, 2, 3, 4, 5, 6)
}

# DONE TODO naming --  an alphanum like 'e' or 1: is called a group, 3 alpha num in a set/list like {1, 'e', 9}: is called a day, 5 days is called week []
# DONE TODO make a the 3 letter group a set instead of a list so that we don't get [1,6,'f] and [f,1,5] as two different entities 


def make_valid_days():
    valid_days = []
    # loop over dict
    for key, values in possibles.items():
        # Loop over tuple of each key
        for y in values:
            # get a list for each 
           listB = possibles[y]
           for z in listB:
               if z in values:
                   new_g = {key,y,z}
                   if new_g not in valid_days:
                        valid_days.append({key,y,z})
    return valid_days
                       

valid_days = make_valid_days()
print(valid_days)
print(len(valid_days))    

# result days before eleminating redundancy #90 as hypothesized 15 * 6 * 1
'''#  [[1, 6, 'f'], [1, 9, 'e'], [1, 'd', 'a'], [1, 'a', 'd'], [1, 'e', 9], [1, 'f', 6], [2, 5, 'f'], [2, 8, 'e'], 
# [2, 'c', 'a'], [2, 'a', 'c'], [2, 'e', 8], [2, 'f', 5], [3, 4, 'f'], [3, 7, 'e'], [3, 'a', 'b'], [3, 'b', 'a'], 
# [3, 'e', 7], [3, 'f', 4], [4, 3, 'f'], [4, 8, 'd'], [4, 'c', 9], [4, 9, 'c'], [4, 'd', 8], [4, 'f', 3], [5, 2, 'f'],
#  [5, 7, 'd'], [5, 9, 'b'], [5, 'b', 9], [5, 'd', 7], [5, 'f', 2], [6, 1, 'f'], [6, 7, 'c'], [6, 8, 'b'], 
# [6, 'b', 8], [6, 'c', 7], [6, 'f', 1], [7, 3, 'e'], [7, 5, 'd'], [7, 6, 'c'], [7, 'c', 6], [7, 'd', 5], [7, 'e', 3], 
# [8, 2, 'e'], [8, 4, 'd'], [8, 6, 'b'], [8, 'b', 6], [8, 'd', 4], [8, 'e', 2], [9, 1, 'e'], [9, 4, 'c'], [9, 5, 'b'],
#  [9, 'b', 5], [9, 'c', 4], [9, 'e', 1], ['a', 1, 'd'], ['a', 2, 'c'], ['a', 3, 'b'], ['a', 'b', 3], ['a', 'c', 2],
#  ['a', 'd', 1], ['b', 3, 'a'], ['b', 5, 9], ['b', 6, 8], ['b', 8, 6], ['b', 9, 5], ['b', 'a', 3], ['c', 2, 'a'], ['c', 4, 9], ['c', 6, 7], ['c', 7, 6], ['c', 9, 4], 
# ['c', 'a', 2], ['d', 1, 'a'], ['d', 4, 8], ['d', 5, 7], ['d', 7, 5], ['d', 8, 4], ['d', 'a', 1], ['e', 1, 
# 9], ['e', 2, 8], ['e', 3, 7], ['e', 7, 3], ['e', 8, 2], ['e', 9, 1], ['f', 1, 6], ['f', 2, 5], ['f', 3, 4], ['f', 4, 3], ['f', 5, 2], ['f', 6, 1]]
'''
# day after eleminating identical days - {1, 'd', 'a'} == {'d', 'a', 1}
# [{1, 'f', 6}, {'e', 1, 9}, {'d', 1, 'a'}, {2, 'f', 5}, {8, 2, 'e'}, {2, 'a', 'c'}, {3, 4, 'f'}, {'e', 3, 7}, {'b', 3, 'a'}, {8, 4, 'd'}, 
# {9, 4, 'c'}, {'d', 5, 7}, {'b', 9, 5}, {'c', 6, 7}, {8, 'b', 6}]
# 15 unique non conflict days (non conflict mean all 6 members of the team exists - no member exist in 2 groups - no members is missing)

def get_week(day_init = []):
    week = day_init
    done_groups = []
    # this if we have an input group already ignore this
    for day in week:
        for group in day:
            if group not in done_groups:
                done_groups.append(group)
            else:
                print('conflicting groups and days')
                return week
    # TODO make it recursive
    for day in valid_days:
        unique_group = 0
        # check if x is in the unique group
        for group in day:
            if group in done_groups:
                break
            else:
                unique_group += 1
            
        if unique_group == 3:
            for group in day:
                done_groups.append(group)
            week.append(day)
    return week

valid_week = get_week()
print(valid_week)
# valid_week = get_week( [[1,6,'f'],[2,8,'c'],[9,'b',5]])
# print(valid_week)

# wohoo [[1, 6, 'f'], [2, 8, 'e'], [3, 'a', 'b'], [4, 'c', 9], [5, 7, 'd']]

def get_some_weeks():
    some_weeks = []
    # brute force O(n**4)- TODO make a better algo
    mod_days = valid_days.copy()
    for day1 in mod_days:
        mod_days.remove(day1)
        week = get_week([day1])
        if len(week) == 5:
            print('success', week)
            some_weeks.append(week)

    return some_weeks
    
all_weeks = get_some_weeks()
print('\n----allweeks-----\n\n')
f = open('all_Possilbe_weeks_new_norepetetion_remove_way', 'wt')
for week in all_weeks:
    f.write(f"{week}\n")
    print(week)

