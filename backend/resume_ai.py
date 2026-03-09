import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skill_extractor import extract_skills

def extract_pdf(file):

    text=""

    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


def analyze_resumes(files, job):

    resumes=[]
    names=[]
    skills_list=[]

    for file in files:

        text = extract_pdf(file)

        resumes.append(text)
        names.append(file.filename)

        skills_list.append(extract_skills(text))

    documents=[job]+resumes

    vectorizer=TfidfVectorizer(stop_words="english")

    matrix=vectorizer.fit_transform(documents)

    similarity=cosine_similarity(matrix[0:1],matrix[1:]).flatten()

    results=[]

    for i in range(len(names)):

        results.append({
            "name":names[i],
            "score":round(similarity[i]*100,2),
            "skills":skills_list[i]
        })

    results.sort(key=lambda x:x["score"],reverse=True)

    return results