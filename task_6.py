subj = {}
with open('hw_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, stats = line.split(':')
        subj_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        subj[subject] = subj_sum
    print(f'Общее количество часов по предмету: \n{subj}')
