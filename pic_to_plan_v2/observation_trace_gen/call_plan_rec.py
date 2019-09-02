import os
import time
import tarfile

def call_plan_rec():
    t0 = time.time()
    obs_trace_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
    print(obs_trace_dir)
    os.chdir("/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/")
    #os.system("python2 ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G \
    #    -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2")

    ###example call
    #os.execvp("/usr/bin/python", ["/usr/bin/python" ,"/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py",  "-G", \
    #    "-e", "/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2"])

    #works, but replaces process, s.t. the whole program terminates when this call is terminated
    #os.execvp("/usr/bin/python", ["/usr/bin/python" ,"/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py",  "-G", \
    #    "-e", "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/sample.tar.bz2"])

    #working call to pr
    os.system("/usr/bin/python /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G \
            -e /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/sample.tar.bz2")

    results = tarfile.open("/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/results.tar.bz2", "r:bz2")

    results = tarfile.open("/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/results.tar.bz2", "r:bz2")
    report = results.extractfile("report.txt")
    max_prob = 0
    for l in report:
        l = str(l).split("=")
        l0 = l[0]
        if "Hyp_Prob_O" in l0:
            l1 = l[1].strip("\\n'")
            l1_float = float(l1)
            max_prob = max(max_prob, l1_float)
    print(max_prob)

    os.chdir(obs_trace_dir)
    t1 = time.time()
    duration = t1 - t0
    print(duration)
    #TODO why are the different calls to prob_PR.py from this script so much slower than in the terminal?

    return max_prob
    #Terminal call:
    #python ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2

if __name__ == "__main__":
    call_plan_rec()