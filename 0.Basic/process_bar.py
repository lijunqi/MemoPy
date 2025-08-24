import os
print(os.getcwd())

print(os.path.splitext('C:\\Users\\admin\\Desktop\\a.py'))


#############################################
# V1
#import sys, time
#for i in range(10):
#    sys.stdout.write('\r')
#    sys.stdout.write('{}% |{}'.format(i%10, (i//2)*'*'))
#    sys.stdout.write(str(i*2))
#    sys.stdout.flush()
#    time.sleep(1)
#
#sys.stdout.write('\n')

#############################################
# V2
import time
from tqdm import tqdm, trange
epi = tqdm(range(100), ncols=100, dynamic_ncols=False)
#epi = tqdm(range(100))
for i in epi:
    epi.set_description('Iter %3d' % (i))
    time.sleep(0.1)

#def action():
#    time.sleep(0.5)
#with tqdm(total=100000, desc='Example', leave=True, ncols=100, unit='B', unit_scale=True) as pbar:
#    for i in range(10):
#        action()
#        pbar.update(10000)
