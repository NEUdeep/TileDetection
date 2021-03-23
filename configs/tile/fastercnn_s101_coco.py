_base_ = './fasterrcnn_r50_fpn_coco.py'

norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    pretrained='open-mmlab://resnest101',
    backbone=dict(
        type='ResNeSt',
        stem_channels=128,
        depth=101,
        radix=2,
        reduction_factor=4,
        avg_down_stride=True,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=norm_cfg,
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True),
        norm_eval=True,
        style='pytorch'),
    roi_head=dict(
        bbox_head=dict(
            type='Shared4Conv1FCBBoxHead',
            conv_out_channels=256,
            norm_cfg=norm_cfg)))
# # use ResNeSt img_norm
img_norm_cfg = dict(
    mean=[123.68, 116.779, 103.939], std=[58.393, 57.12, 57.375], to_rgb=True)

data = dict(samples_per_gpu=5)
resume_from = None
load_from = None

log_config = dict(
    interval=10,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])

work_dir = 'work_dirs/faster_s101_coco'
resume_from = None