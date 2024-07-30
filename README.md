# Conformer_CTC

This code is based on NVIDIA NeMo.

## Set environment
Install conda environment
```shell
conda create --name nemo python==3.10.12
conda activate nemo
```
Install pytorch
```shell
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
Install nemo_toolkit
```shell
apt-get update && apt-get install -y libsndfile1 ffmpeg
pip install Cython packaging
pip install nemo_toolkit['asr']
```