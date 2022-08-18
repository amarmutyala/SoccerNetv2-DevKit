python src/main.py --SoccerNet_path=/home/amar/Desktop/soccernet \
--features=ResNET_TF2_PCA512.npy \
--num_features=512 \
--model_name=CALF_calibration \
--batch_size 32 \
--evaluation_frequency 20 \
--chunks_per_epoch 18000 \
--backbone_player=3DConv \
--calibration --calibration_field --calibration_cone \
--backbone_feature=2DConv  \
 --feature_multiplier 2 \
--class_split visual


python src/main.py --SoccerNet_path=/home/amar/Desktop/soccernet --features=ResNET_TF2_PCA512.npy --num_features=512 --model_name=Calib_Best_VIS --batch_size 32 --backbone_player=3DConv --calibration --calibration_field --calibration_cone --backbone_feature=2DConv  --feature_multiplier 2 --with_resnet 34 --with_dense --class_split visual --test_only 


