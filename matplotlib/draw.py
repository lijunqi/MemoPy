import matplotlib.pyplot as plot

class Record:
    def __init__(self, n_execution, ori_elapsed_time, cur_elapsed_time, wf_id):
        self.n_execution = int(n_execution)
        self.ori_t = float(ori_elapsed_time)
        self.cur_t = float(cur_elapsed_time)
        self.wf_id = wf_id

def comp(rec1, rec2):
    return rec1.n_execution - rec2.n_execution

f = open('dev_full.csv', 'r')
line = f.readline()
n_lines = 0
records_dict = {}

while line:
    n_lines += 1
    (n_execution, ori, cur, wf_id) = line.split(',')
    if n_execution in records_dict.keys():
        records_dict[n_execution]['cnt'] += 1
        records_dict[n_execution]['rec'].ori_t += float(ori)
        records_dict[n_execution]['rec'].cur_t += float(cur)
    else:
        records_dict[n_execution] = {
            'cnt': 1,
            'rec': Record(n_execution, ori, cur, wf_id)
        }
    line = f.readline()

print("N lines: ", n_lines)

records = []
for k, v in records_dict.items():
    cnt = float(v['cnt'])
    records.append(Record(k, float(v['rec'].ori_t)/cnt, float(v['rec'].cur_t)/cnt, v['rec'].wf_id))

records.sort(key=lambda x: int(x.n_execution))


fig, ax = plot.subplots()
x_axis = [x.n_execution for x in records]
ax.plot(x_axis, [x.ori_t for x in records], 'o-', label="Origin")
ax.plot(x_axis, [x.cur_t for x in records], 'o-', label="New")
ax.legend()

plot.xlim(0)
plot.ylim(0)

plot.xlabel("Number of Executions")
plot.ylabel("Average Elapsed Time(s)")
plot.title('Workflow detail page "get_execution" function(Ori vs. New)')
plot.show()
