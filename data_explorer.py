import os
import json
import shutil

json_file = "aggregated_output.json"

if __name__ == "__main__":

    def copy_file(src_path: str) -> None:
        path_prefix = "/Users/shanky/Documents/MyDrive/Takat/Personal/Gym/gym/webp/"
        replace_path = "/Users/shanky/Documents/MyDrive/Learning/Development/Github/dockerized-takat-app/ExerciseValidator.github.io/assets/images/webp/"

        if not os.path.isfile(src_path):
            raise FileNotFoundError(f"Source file not found: {src_path}")

        dst_path = src_path.replace(path_prefix, replace_path)

        target_dir = os.path.dirname(dst_path)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)

        shutil.copy2(src_path, dst_path)


    with open(json_file, "r", encoding="utf-8") as f:
        records = json.load(f)
        for record in records:
            csv_image_paths = record["csv_image_paths"]
            webp_image_paths = record["webp_image_paths"]
            code = record["code"]
            if not csv_image_paths or not csv_image_paths["360_path"]:
                print(code)
                print(webp_image_paths["360_path"])
                copy_file(webp_image_paths["360_path"])
