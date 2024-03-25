import os
import json

def count_arrays_length(directory):
    total_operation_logs_length = 0
    total_activities_length = 0

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    json_obj = json.loads(line)
                    if 'operation_logs' in json_obj:
                        total_operation_logs_length += len(json_obj['operation_logs'])
                    if 'sales_activities' in json_obj:
                        for activity in json_obj['sales_activities']:
                            if 'activities' in activity:
                                total_activities_length += len(activity['activities'])

    return total_operation_logs_length, total_activities_length

directory_path = 'C:\\Users\\My\\Desktop\\ld_old_data\\customer_list_all'
total_operation_logs_length, total_activities_length = count_arrays_length(directory_path)

print("Total length of operation_logs arrays:", total_operation_logs_length)
print("Total length of activities arrays in sales_activities:", total_activities_length)
