import os
from ruamel.yaml import YAML


def update_image_tag(file_path, new_tag):
    yaml = YAML()
    yaml.preserve_quotes = True

    # Đọc nội dung file YAML
    with open(file_path, "r") as file:
        data = yaml.load(file)

    # Cập nhật giá trị của image.tag
    data["image"]["tag"] = new_tag

    # Ghi lại file YAML với giá trị đã cập nhật
    with open(file_path, "w") as file:
        yaml.dump(data, file)


if __name__ == "__main__":
    # Đường dẫn đến file values.yaml
    file_path = "values.yaml"

    # Đọc giá trị tag mới từ biến môi trường NEW_TAG
    new_tag = os.getenv("NEW_TAG")

    if new_tag is None:
        print("Environment variable NEW_TAG is not set")
        exit(1)

    # Gọi hàm để cập nhật giá trị tag
    update_image_tag(file_path, new_tag)
