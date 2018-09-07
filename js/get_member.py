# coding=utf-8
with open('haha.txt') as f:
    member = list(set(f.readlines()))
    new_member = []
    for i in member:
        line = i.strip()
        if line:
            new_member.append(line)
    print "总人数", len(new_member)
    print ';'.join(new_member)