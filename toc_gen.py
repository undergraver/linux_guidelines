#!/usr/bin/env python

# level 1 is plain text with no prefix
# level 2 starts with ###, level 3 with an extra #

def get_level(line):
    line = line.strip()
    if len(line) == 0:
        return 0

    if line[0] == '#':
        space_pos = line.find(' ')
        return space_pos - 1
        # 3 means level 2
        # 4 means level 3
        # ...
    return 1

def print_toc_chapter(line,lvl_stack):
    line = line.replace('# ','')
    line = line.replace('#','')
    print( ".".join([str(lvl) for lvl in lvl_stack]) + ' ' + line)


f = open('final_toc.txt')
all_lines = f.readlines()
f.close()

last_level = 1
level_stack = [ 0 ]


for line in all_lines:
    line = line.strip()
    level = get_level(line)
    if last_level < level:
        level_stack.append(1)
    elif last_level == level:
        level_stack[-1] += 1
    else: # last_level > level
        diff = last_level - level
        while diff > 0:
            diff -= 1
            level_stack.pop()
        level_stack[-1] += 1

    last_level = level

    print_toc_chapter(line, level_stack)
