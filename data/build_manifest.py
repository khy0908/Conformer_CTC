# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import os
import argparse
import sox

# Function to build a manifest
def build_manifest(data_dir: str, manifest_path: str, text_extension: str, audio_extension: str):
    # Create manifest with reference to this directory.
    f_out = open(manifest_path, "w")
    for src_path, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(audio_extension):
                # Duration
                audio_path = os.path.join(src_path, file)
                duration = sox.file_info.duration(audio_path)

                # Text
                text_path = audio_path.replace(audio_extension, text_extension)
                with open(text_path) as f_text:
                    transcript = f_text.read().strip("\n").lower()

                # Audio path
                metadata = {"audio_filepath": audio_path, "duration": duration, "text": transcript}
                json.dump(metadata, f_out)

                f_out.write('\n')
    f_out.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, 
                        help="Directory where wav files are located. Text files are located in the same place.")
    parser.add_argument("--manifest_dir", type=str, 
                        help="Directory where manifest files are located.")
    parser.add_argument("--text_extension", type=str, default=".txt")
    parser.add_argument("--audio_extension", type=str, default=".flac")

    args = parser.parse_args()

    if not os.path.exists(args.manifest_dir):
        os.mkdir(args.manifest_dir)

    # Building Manifests
    print("******")
    build_manifest(os.path.join(args.data_dir, "train"), 
                   os.path.join(args.manifest_dir, "train.json"), 
                   args.text_extension,
                   args.audio_extension)
    print(">>Train manifest created.")

    build_manifest(os.path.join(args.data_dir, "dev"), 
                   os.path.join(args.manifest_dir, "valid.json"), 
                   args.text_extension,
                   args.audio_extension)
    print(">>Valid manifest created.")

    build_manifest(os.path.join(args.data_dir, "test"), 
                   os.path.join(args.manifest_dir, "test.json"),
                   args.text_extension,
                   args.audio_extension)
    print(">>Test manifest created.")
    print("***Done***")
