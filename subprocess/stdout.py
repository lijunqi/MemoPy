import shlex
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
LOG = logging.getLogger()

if __name__ == "__main__":
    LOG.info("=== Start ===")
    cmd = shlex.split("python subproc_example.py")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    with open('output.txt', 'bw') as f:
        while p.poll() is None:
            if p.stdout is None:
                LOG.info("STDOUT is None.")
            else:
                line = p.stdout.readline()
                if line:
                    f.write(line)
                    #LOG.info("[StdLog]: %s", line.decode('utf-8', 'ignore'))
                    #LOG.info("[StdLog]: %s", line.decode('unicode_escape'))
                    #LOG.info("[StdLog]: %s", line.decode('utf-8'))
                    #print("stdlog: ", line.decode('utf-8'))

    if p.returncode == 0:
        LOG.info("[Success]Subprocess exit.")
    else:
        LOG.info("[Failed]Subprocess exit.")
