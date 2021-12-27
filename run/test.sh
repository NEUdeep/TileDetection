


./tools/dist_test.sh cascade_s50_rfp_mstrain_augv2-B.py work_dirs/round2/cascade_s50_rfp_mstrain_aug_alldata_v2-B/epoch_1.pth 1 --format-only --options "jsonfile_prefix=work_dirs/round2/cascade_s50_rfp_mstrain_aug_alldata_v2-B/cascade_s50_rfp_mstrain_aug_alldata_v2-B-epoch1"

./tools/dist_test.sh cascade_s50_rfp_mstrain_augv2-B.py work_dirs/round2/cascade_s50_rfp_mstrain_aug_alldata_v2-B/epoch_1.pth 1  --eval bbox #用于评估检测map; 