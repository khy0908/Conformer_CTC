# Conformer_CTC

This code is based on NVIDIA NeMo.

## Set environment
Install pytorch
```shell
git clone 
```
Install nemo_toolkit
```shell
apt-get update && apt-get install -y libsndfile1 ffmpeg
pip install Cython packaging
pip install nemo_toolkit['asr']==1.23.0
pip install -r requirements.txt
```
Build manifest
```shell
apt-get install sox
cd data
python build_manifest.py \
    --data_dir path/to/data \
    --manifest_dir /workspace/Conformer_CTC/manifest
```
Build tokenizer
```shell
python process_asr_text_tokenizer.py \
    --manifest "/workspace/Conformer_CTC/manifest/train.json,/workspace/Conformer_CTC/manifest/valid.json,/workspace/Conformer_CTC/manifest/test.json" \
    --data_root "/workspace/Conformer_CTC/tokenizer" \
    --vocab_size 256 \
    --tokenizer "spe" \
    --spe_type "unigram"
```
Train
```shell
python main.py --config_path config/conformer_ctc_bpe.yaml
```

