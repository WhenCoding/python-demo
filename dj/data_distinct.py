def remove_duplicates(input_filename, output_filename):
    with open(input_filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        
    # 去除每行末尾的换行符
    lines = [line.strip() for line in lines]
    
    # 将每行的数组转换为集合，去除重复元素
    unique_lines = list(set(lines))
    
    # 将去重后的数组写入新文件中
    with open(output_filename, 'w', encoding="utf-8") as file:
        for line in unique_lines:
            file.write(line + '\n')
    
    return unique_lines

# 示例用法
input_filename = 'major_detail_turn_img.json'
output_filename = 'major_detail_turn_imgdistinct.json'
unique_arrays = remove_duplicates(input_filename, output_filename)

