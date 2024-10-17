from pathlib import Path


def read_log_file(file_path):
    with open(file_path, "r") as file:
        chunk = ""
        total_line_count = 0
        line_count = 0
        for line in file:
            total_line_count += 1
            line_count += 1
            chunk += f"\nLine {total_line_count}: {line.strip()}"
            if line_count >= 100:
                yield chunk
                chunk = ""
                line_count = 0
        yield chunk


def process_logs(logs):
    file_path = Path(__file__).parent / "errors.txt"
    with open(file_path, "a") as file:
        for log in logs.split("\n"):
            # print(log)
            if "ERROR" in log:
                file.write(log + "\n")


file_path = Path(__file__).parent / "log.txt"
gen = read_log_file(file_path)
# print(next(gen))
for log in gen:
    process_logs(log)
