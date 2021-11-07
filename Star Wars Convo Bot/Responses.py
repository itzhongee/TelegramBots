from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","hey","sup"):
        return "Hey! How's it going?"
    
    if user_message in ("May the force be with you!", "May the force be with you", "may the force be with you!", "may the force be with you"):
        return "May the force be with you too"
    
    if user_message in ("hello there", "Hello There", "Hello there", 
    "hello there!", "Hello There!", "Hello there!"):
        return "General Kenobi"
    
    if user_message in ("I am the senate!", "i am the senate!", "i am the senate", "I am the senate"):
        return "Not yet"
    
    if user_message in ("Exeute Order 66!", "execute order 66!", "Execute Order 66", "execute order 66"):
        return "It will be done, my lord"
    
    if user_message in ("You turned her against me!", "you turned her against me!", "You turned her against me", "you turned her against me"):
        return "You have done that yourself"

    if user_message in ("I have brought peace, freedom, justice and security to my new empire!", "i have brought peace, freedom, justice and security to my new empire!", 
    "I have brought peace, freedom, justice and security to my new empire", "i have brought peace, freedom, justice and security to my new empire"):
        return "Your new empire?"
    
    if user_message in ("If you're not with me, then you're my enemy!", "if you're not with me, then you're my enemy!",
    "If you're not with me, then you're my enemy","if you're not with me, then you're my enemy",
    "If you are not with me, then you are my enemy!", "if you are not with me, then you are my enemy!",
    "If you are not with me, then you are my enemy","if you are not with me, then you are my enemy"):
        return "Only a Sith deals in absolute. I will do what I must"

    if user_message in ("It's over Anakin, I have the high ground!", "it's over Anakin, I have the high ground!",
    "It's over Anakin, I have the high ground","it's over Anakin, I have the high ground",
    "It's over Anakin, I have the highground!","it's over Anakin, I have the highground!",
    "It's over Anakin, I have the highground","it's over Anakin, I have the highground",
    "It's over anakin, I have the high ground!", "it's over anakin, I have the high ground!",
    "It's over anakin, I have the high ground","it's over anakin, I have the high ground",
    "It's over anakin, I have the highground!","it's over anakin, I have the highground!",
    "It's over anakin, I have the highground","it's over anakin, I have the highground",
    "It's over Anakin, i have the high ground!", "it's over Anakin, i have the high ground!",
    "It's over Anakin, i have the high ground","it's over Anakin, i have the high ground",
    "It's over Anakin, i have the highground!","it's over Anakin, i have the highground!",
    "It's over Anakin, i have the highground","it's over Anakin, i have the highground",
    "It's over anakin, i have the high ground!", "it's over anakin, i have the high ground!",
    "It's over anakin, i have the high ground","it's over anakin, i have the high ground",
    "It's over anakin, i have the highground!","it's over anakin, i have the highground!",
    "It's over anakin, i have the highground","it's over anakin, i have the highground"):
        return "You understandestimate my power!"

    if user_message in ("Luke, I am your father!","Luke, i am your father!",
    "luke, I am your father!", "luke, i am your father!",
    "Luke, I am your father","Luke, i am your father",
    "luke, I am your father", "luke, i am your father"):
        return "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
    
    if user_message in ("who are you","who are you?"):
        return "I am a star wars conversation bot!"
    
    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time) 
    
    return "I don't understand you"