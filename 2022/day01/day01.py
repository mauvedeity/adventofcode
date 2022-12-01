#!env python3 
#      _              ___  _ 
#   __| | __ _ _   _ / _ \/ |
#  / _` |/ _` | | | | | | | |
# | (_| | (_| | |_| | |_| | |
#  \__,_|\__,_|\__, |\___/|_|
#              |___/         
# 
#

def process_a():
    with open('input.txt') as infile:
        curr_elf = 1
        best_elf = 0
        this_elf_cals = 0
        best_elf_cals = 0
        for li in infile:
            if li == '\n':
                if(this_elf_cals > best_elf_cals):
                    best_elf = curr_elf
                    best_elf_cals = this_elf_cals
                this_elf_cals = 0
                curr_elf += 1
            else:
                this_cals = int(li)
                this_elf_cals += this_cals
        print("Elfcount: ", curr_elf)
        print("Best elf is", best_elf, ", carrying ", best_elf_cals, "calories")
    return

def process_b():
    elfloads=[]
    with open('input.txt') as infile:
        this_elf_cals = 0
        for li in infile:
            if li == '\n':
                elfloads.append(this_elf_cals)
                this_elf_cals = 0
            else:
                this_cals = int(li)
                this_elf_cals += this_cals
        elfloads.append(this_elf_cals)
    elfloads.sort()
    print(elfloads[-3:])
    print(sum(elfloads[-3:]))
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()