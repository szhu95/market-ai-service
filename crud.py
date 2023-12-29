from sqlalchemy.orm import Session
import models, schemas

from openai import OpenAI

client = OpenAI()

def create_prompt(db: Session, prompts: schemas.PromptsRequest):
    response = client.completions.create(model="text-davinci-002",
    max_tokens=500,
    prompt=generate_prompt(prompts.name, prompts.role, prompts.company, prompts.solution, prompts.metric),
    temperature=0.6)
    result = response.choices[0].text
    
    db_prompts = models.Prompts(name=prompts.name, email=result)
    db.add(db_prompts)
    db.commit()
    db.refresh(db_prompts)
    return db_prompts

def generate_prompt(name, role, company, solution, metric):
    return """I would like to draft an email to {}, 
    {} at {} regarding using {} to {}""".format(
        name.capitalize(),
        role.capitalize(),
        company.capitalize(),
        solution.capitalize(),
        metric.capitalize()
    )

def read_prompts(db: Session):
        return db.query(models.Prompts).all()

def read_prompt(db: Session, id: int):
    return db.query(models.Prompts).filter(models.Prompts.id == id).first()

def update_prompt(db: Session, id: int, prompts: schemas.PromptsRequest):
    db_prompts = db.query(models.Prompts).filter(models.Prompts.id == id).first()
    if db_prompts is None:
        return None
    response = client.completions.create(model="text-davinci-002",
    prompt=generate_prompt(prompts.name, prompts.role, prompts.company, prompts.solution, prompts.metric),
    temperature=0.6,
    )
    
    result = response.choices[0].text
    db.query(models.Prompts).filter(models.Prompts.id == id).update({'name': prompts.name, 'email': result})
    db.commit()
    db.refresh(db_prompts)
    return db_prompts

def delete_prompt(db: Session, id: int):
    db_prompt = db.query(models.Prompts).filter(models.Prompts.id == id).first()
    if db_prompt is None:
        return None
    db.query(models.Prompts).filter(models.Prompts.id == id).delete()
    db.commit()
    return True

def create_social(db: Session, socials: schemas.SocialsRequest):
    response = client.completions.create(model="text-davinci-002",
    max_tokens=500,
    prompt=generate_social(socials.name, socials.company, socials.achievement, socials.metric),
    temperature=0.6)
    result = response.choices[0].text
    
    db_socials = models.Socials(name=socials.name, post=result)
    db.add(db_socials)
    db.commit()
    db.refresh(db_socials)
    return db_socials

def generate_social(name, company, achievement, metric):
    return """I would like to draft a social media post to highlight {} 
    at {} for accomplishing {} by {}""".format(
        name.capitalize(),
        company.capitalize(),
        achievement.capitalize(),
        metric.capitalize()
    )

def read_socials(db: Session):
        return db.query(models.Socials).all()

def read_social(db: Session, id: int):
    return db.query(models.Socials).filter(models.Socials.id == id).first()

def update_social(db: Session, id: int, socials: schemas.SocialsRequest):
    db_socials = db.query(models.Socials).filter(models.Socials.id == id).first()
    if db_socials is None:
        return None
    response = client.completions.create(model="text-davinci-002",
    prompt=generate_social(socials.name, socials.company, socials.achievement, socials.metric),
    temperature=0.6,
    )
    
    result = response.choices[0].text
    db.query(models.Socials).filter(models.Socials.id == id).update({'name': socials.name, 'post': result})
    db.commit()
    db.refresh(db_socials)
    return db_socials

def delete_social(db: Session, id: int):
    db_social = db.query(models.Socials).filter(models.Socials.id == id).first()
    if db_social is None:
        return None
    db.query(models.Socials).filter(models.Socials.id == id).delete()
    db.commit()
    return True