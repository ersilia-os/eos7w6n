input=$2
output=$3
data_dir=$(dirname $input)
python $1/code/scripts/save_features.py --data_path $input \
                                       --save_path $data_dir/features.npz \
                                       --features_generator rdkit_2d_normalized \
                                       --restart

python $1/code/main.py fingerprint --data_path $input \
                                  --features_path $data_dir/features.npz \
                                  --checkpoint_path $1/../checkpoints/grover_large.pt \
                                  --fingerprint_source both \
                                  --output $output \
                                  --no_cuda \

rm -f "$data_dir/features.npz"