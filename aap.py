from flask import Flask, render_template, request

app = Flask(__name__)

# Example student data
students = {
    "101": {"name":"Ravi", "gujarati": 85, "english": 78, "maths": 92, "science": 88, "social": 70},
    "102": {"name":"Seema", "gujarati": 65, "english": 72, "maths": 60, "science": 75, "social": 80},
}

def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B+"
    elif marks >= 60: return "B"
    elif marks >= 50: return "C"
    else: return "F"

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method=="POST":
        roll_no = request.form.get("roll_no")
        if roll_no in students:
            student = students[roll_no]
            subjects = ["gujarati","english","maths","science","social"]
            total_marks = 0
            subject_details = []
            
            for sub in subjects:
                marks = student[sub]
                grade = get_grade(marks)
                total_marks += marks
                subject_details.append({"subject": sub.capitalize(), "marks": marks, "grade": grade})
            
            total_possible = len(subjects) * 100
            overall_grade = get_grade(total_marks // len(subjects))
            
            result = {
                "student_name": student["name"],
                "roll_no": roll_no,
                "subjects": subject_details,
                "total_marks": total_marks,
                "total_possible": total_possible,
                "overall_grade": overall_grade
            }
        else:
            result = {"error": "No result found for Roll No "+roll_no}
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)
