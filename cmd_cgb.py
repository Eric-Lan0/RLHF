# H100 (14d): os.system('sinteractive -A cgb-l -N1 -n32 --gpus-per-node=1 -t 14-00:00:00')
# A100 (14d): os.system('sinteractive -A cgb-n -N1 -n16 --gpus-per-node=1 -t 14-00:00:00')
# general (4h): os.system('sinteractive -A standby -N1 -n32 --gpus-per-node=1 -t 4:00:00')
# no need: $ module load anaconda
# no need: $ source activate rlhf
# run: $ python ~/RLHF/main.py
# check free GPUs: slist
# check quota: myquota
#
# module load anaconda/2020.11-py38
# conda activate /scratch/gilbreth/lan44/.conda/envs/rlhf_scratch
# accelerate config default
#
# export HF_HOME='/scratch/gilbreth/lan44/.cache/huggingface'
# export HF_DATASETs_CACHE=''
