def split_file(filename, num_files):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    lines_per_file = total_lines // num_files

    for i in range(num_files):
        start_index = i * lines_per_file
        end_index = start_index + lines_per_file if i != num_files - 1 else None

        with open(f"{'major_detail'}_{i+1}.json", 'w') as output_file:
            output_file.writelines(lines[start_index:end_index])

    print(f"File '{filename}' has been split into {num_files} files.")

# 示例调用
split_file('/Users/xin/Desktop/major_detail.json', 10)
