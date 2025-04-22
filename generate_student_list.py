import sys
import os
from bs4 import BeautifulSoup

def parse_student_name(name):
    name = name.strip('"')
    if ',' in name:
        last, first_middle = name.split(',', 1)
        last = last.strip()
        first_middle = first_middle.strip().replace('_', ' ')
        return f"{first_middle} {last}"
    return name

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_student_list_htmltable.py <input.xls>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_txt = os.path.splitext(input_file)[0] + "_students.txt"

    with open(input_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, "html.parser")

    # Find the table and all rows
    table = soup.find("table")
    rows = table.find_all("tr")

    # Find header row (should be the second <tr>)
    headers = [th.get_text(strip=True) for th in rows[1].find_all("th")]
    student_idx = headers.index("Student")
    email_idx = headers.index("Email")

    with open(output_txt, 'w', encoding='utf-8') as outfile:
        for row in rows[2:]:
            cells = row.find_all("td")
            if len(cells) > max(student_idx, email_idx):
                student = cells[student_idx].get_text(strip=True)
                email = cells[email_idx].get_text(strip=True)
                if student and email:
                    name = parse_student_name(student)
                    outfile.write(f"{name}, {email}\n")

if __name__ == "__main__":
    main()