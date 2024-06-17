from faker import Faker
from backend_json import load_json, save_json
import base64
import secrets
import requests
faker = Faker()


def gen_articles(amount: int):
    for _ in range(amount):
        title = faker.sentence(nb_words=3)
        authors = []
        for _ in range(3):
            authors.append(faker.name())
        abstract = faker.text(1000)
        generated_articles = {"title": title, "authors": authors, "abstract": abstract}
        save_generated_articles(generated_dict=generated_articles, json_name="articles.json")


def save_generated_articles(generated_dict: dict, json_name: str) -> bool:
    articles_dict = load_json(json_name)
    new_index = str(len(articles_dict))
    articles_dict[new_index] = generated_dict 
    save_json(json_name, articles_dict)
    return True


# TODO
def gen_user(amount: int):
    for _ in range(amount):
        name = faker.name()
        email = faker.email()
        password = faker.password(
            length=8, special_chars=False, digits=True, upper_case=True, lower_case=True
        )
        picture = gen_picture()
        topics = get_topics()
        skills = get_skills_and_expertise()
        generated_user = {
                "name": name,
                "email": email,
                "password": password,
                "profile_picture": picture,
                "topics": topics,
                "skills": skills
                }
        save_generated_articles(generated_dict=generated_user, json_name="users.json")
        print(f"generated following user:\n{email}\n{password}\n{topics}\n{skills}")

def gen_picture():
    response = requests.get('https://thispersondoesnotexist.com/')
    return base64.b64encode(response.content).decode('utf-8')

def get_topics():
    topics_user = []
    secrange = secrets.SystemRandom().randint(1, 5)
    topics = [
        "Machine Learning",
        "Artificial Intelligence",
        "Data Science",
        "Quantum Computing",
        "Neuroscience",
        "Genomics",
        "Bioinformatics",
        "Renewable Energy",
        "Climate Change",
        "Nanotechnology",
        "Biomedical Engineering",
        "Cognitive Psychology",
        "Social Psychology",
        "Econometrics",
        "Astrophysics",
    ]
    for _ in range(0, secrange):
        secrange = secrets.SystemRandom().randint(0, 14)
        topics_user.append(topics[secrange]) 
    return topics_user

def get_skills_and_expertise():
    skills_user = []
    secrange = secrets.SystemRandom().randint(1, 5)
    skills_expertise = [
        "Python Programming",
        "Statistical Analysis",
        "Deep Learning",
        "Natural Language Processing",
        "Mathematical Modeling",
        "Laboratory Techniques",
        "Genetic Sequencing",
        "Project Management",
        "Scientific Writing",
        "Data Visualization",
        "Grant Writing",
        "Survey Design",
        "Field Research",
        "Qualitative Analysis",
        "Machine Learning Algorithms"
    ]
    for _ in range(0, secrange):
        secrange = secrets.SystemRandom().randint(0, 14)
        skills_user.append(skills_expertise[secrange]) 
    return skills_user

# gen_user(99)
