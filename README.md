# ITM 300 - Cloud Foundations Automation Scripts

This repository contains automation scripts designed to enhance the teaching experience for ITM 300 - Cloud Foundations. The `generate_student_list.py` script helps instructors quickly generate a student list in the format required for AWS Academy onboarding.

---

## How to Generate a Student List for AWS Academy

1. **Download Your Class List:**
   - Go to [BYU-Idaho Faculty Portal](https://student.byui.edu/ICS/Faculty/).
   - Navigate to the **Faculty** tab and select your class/Go Directly To "Class List".
   - Click the **Export to Excel** button.  
     > Note: The downloaded `.xls` file is actually an HTML table.

2. **Place the File:**
   - Move the downloaded `.xls` file into the `student_list` folder in this repository.

3. **Install [uv](https://github.com/astral-sh/uv):**
   - If you don't have `uv` installed, follow the instructions here: [https://github.com/astral-sh/uv#installation](https://github.com/astral-sh/uv#installation)

4. **Generate the Student List:**
   - Open a terminal in the repository root.
   - Run:
     ```sh
     uv run python generate_student_list.py student_list/YourClassList.xls
     ```
   - This will create a file named `YourClassList_students.txt` in the same folder.

5. **Result:**
   - The `.txt` file will contain each student's full name and email, one per line, ready for AWS Academy onboarding.

---

*For instructors: Use this script to save time and ensure a smooth start to each semester!*