python process_asr_text_tokenizer.py \
    --manifest "/workspace/nemo_ctc/manifest/train.json,/workspace/nemo_ctc/manifest/valid.json,/workspace/nemo_ctc/manifest/test.json" \
    --data_root "/workspace/nemo_ctc/tokenizer" \
    --vocab_size 256 \
    --tokenizer "spe" \
    --spe_type "unigram"

