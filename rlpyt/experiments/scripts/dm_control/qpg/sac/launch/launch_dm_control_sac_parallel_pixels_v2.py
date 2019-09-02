
from rlpyt.utils.launching.affinity import encode_affinity
from rlpyt.utils.launching.exp_launcher import run_experiments
from rlpyt.utils.launching.variant import make_variants, VariantLevel

script = "rlpyt/experiments/scripts/dm_control/qpg/sac/train/dm_control_sac_parallel_v2.py"
affinity_code = encode_affinity(
    n_cpu_core=3,
    n_gpu=1,
    contexts_per_gpu=1,
    n_socket=2,
)

runs_per_setting = 2
default_config_key = "sac_parallel_pixels_v2"
experiment_title = "sac_dm_control_parallel_pixels_v2"
variant_levels = list()

domain = ['cloth_v0']
task = ['easy']
values = list(zip(domain, task))
dir_names = ["env_{}_{}".format(*v) for v in values]
keys = [('env', 'domain'), ('env', 'task')]
variant_levels.append(VariantLevel(keys, values, dir_names))

variants, log_dirs = make_variants(*variant_levels)

run_experiments(
    script=script,
    affinity_code=affinity_code,
    experiment_title=experiment_title,
    runs_per_setting=runs_per_setting,
    variants=variants,
    log_dirs=log_dirs,
    common_args=(default_config_key,),
)
