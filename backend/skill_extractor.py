skills_db = [
"python","java","c++","machine learning",
"data analysis","flask","django",
"react","sql","mongodb","html",
"css","javascript"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:
            found_skills.append(skill)

    return found_skills