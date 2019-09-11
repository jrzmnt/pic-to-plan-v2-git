from datetime import datetime
import pic_to_plan_v2.observation_trace_gen.parse_ontology as parse_ontology_mod
import pic_to_plan_v2.observation_trace_gen.watch_video as watch_video_mod
import pic_to_plan_v2.uct.uct_dag as uct_dag_mod
import copy
import os
import shutil

start_time = datetime.now()
#config_file_name = "cut_cucumber_bread_config_1.txt"
config_file_name = "ccb_minimal_domain_config_1.txt"
config_file_dir = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/experiment_configurations/"
config_file_path = config_file_dir + config_file_name
with open(config_file_path, "r") as f:
    for l in f:
        if l[0] != ";": #; denotes comment
            l = l.strip().split(" ")
            if l[0] == "experiment_name:":
                experiment_name = (" ").join(l[1:])
            elif l[0] == "experiment_comment:":
                experiment_comment = (" ").join(l[1:])
            elif l[0] == "domain:":
                domain_path = l[1]
            elif l[0] == "instance:":
                instance_path = l[1]
            elif l[0] == "goals:":
                goal_path = l[1]
            elif l[0] == "ontology:":
                ontology_path = l[1]
            elif l[0] == "possible_actions:":
                possible_actions_path = l[1]
            elif l[0] == "time:":
                time = int(l[1])
                if time == -1:
                    time = None
            elif l[0] == "results_dir:":
                results_dir = l[1]
            elif l[0] == "session_name:":
                session_name = l[1]
            elif l[0] == "save_after_X_iterations:":
                save_after_X_iterations = int(l[1])

print(experiment_name)
print(experiment_comment)
print(instance_path)
###parse ontology
parse_ontology_mod.main_parse_ontology(ontology_path, domain_path, instance_path)

###watch video
#watch_video_mod.main_watch_video(domain_path, instance_path, session_name, ontology_path)

domain_inserted_predicates_path = domain_path.replace(".pddl", "-inserted-predicates.pddl")
instance_inserted_predicates_path = instance_path.replace(".pddl", "-parsed-objects.pddl")

###uct dag
current_results_dir = results_dir + experiment_name
shutil.rmtree(current_results_dir)
os.mkdir(current_results_dir)
uct_search = uct_dag_mod.UCTSearch(domain_inserted_predicates_path, instance_inserted_predicates_path, session_name, ontology_path, save_after_X_iterations, experiment_name, current_results_dir, goal_path)
uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), time_limit=time)

end_time = datetime.now()
print("DONE", experiment_name, "\nStart:", start_time, "\nEnd:", end_time, "\nDuration:", end_time - start_time)