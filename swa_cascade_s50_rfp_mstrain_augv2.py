_base_ = ['cascade_s50_rfp_mstrain_augv2-B.py', 'configs/_base_/swa.py']

only_swa_training = True
# whether to perform swa training
swa_training = True
# load the best pre_trained model as the starting model for swa training
swa_load_from = '/work/work_dirs/round2/cascade_s50_rfp_mstrain_aug_alldata_v2/latest.pth'
swa_resume_from = None

# swa optimizer
swa_optimizer = dict(_delete_=True, type='Adam', lr=7e-5)
swa_optimizer_config = dict(grad_clip=None)

# swa learning policy
swa_lr_config = dict(
    policy='cyclic',
    target_ratio=(1, 0.01),
    cyclic_times=12,
    step_ratio_up=0.0)
swa_total_epochs = 12

# swa checkpoint setting
swa_checkpoint_config = dict(interval=2, filename_tmpl='swa_epoch_{}.pth')
work_dir = '/work/work_dirs/round2/swa_cascade_s50_rfp_mstrain_aug_v2-B'