from parser_log_file import *
if __name__=="__main__":
    logs=load_logs(file_path=sys.argv[1])
    display_log_counts(count_logs_by_level(logs))
    if len(sys.argv)==3:
        print()
        print(f"Деталі логів для рівня '{sys.argv[2]}':")
        print(''.join(map(lambda x:f"{x['date']} {x['time']} - {x['message']}",filter_logs_by_level(logs,sys.argv[2]))))
    