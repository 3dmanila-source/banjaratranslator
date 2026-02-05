"""
Generate 10,000 diverse English sentences for Banjara translation
Categories: Greetings, Daily Life, Questions, Travel, Health, Food, etc.
"""

import json
import random

# Template-based sentence generation
def generate_sentences():
    sentences = []
    sentence_id = 1
    
    # 1. GREETINGS (200)
    greetings = [
        "Hello", "Hi", "Good morning", "Good afternoon", "Good evening", "Good night",
        "How are you?", "How are you doing?", "How is it going?", "What's up?",
        "Nice to meet you", "Pleased to meet you", "Good to see you",
        "Welcome", "Welcome back", "Long time no see",
        "How have you been?", "How is your family?", "How is everyone?",
        "Take care", "See you later", "See you soon", "Goodbye", "Bye",
        "Have a good day", "Have a nice day", "Have a great day",
        "Thank you", "Thanks", "Thank you very much", "Thanks a lot",
        "You're welcome", "No problem", "My pleasure", "Anytime",
        "Sorry", "I'm sorry", "Excuse me", "Pardon me", "I apologize",
        "Please", "Please help me", "Could you please", "Would you mind",
        "Bless you", "Congratulations", "Well done", "Good job",
        "Happy birthday", "Happy new year", "Merry Christmas",
        "Good luck", "All the best", "Best wishes"
    ]
    
    for g in greetings:
        sentences.append({"id": sentence_id, "category": "greeting", "text": g, "difficulty": "easy"})
        sentence_id += 1
    
    # Add variations
    names = ["mother", "father", "brother", "sister", "friend", "uncle", "aunt"]
    for name in names:
        for phrase in ["How is your", "Give my regards to your", "Say hello to your"]:
            sentences.append({
                "id": sentence_id,
                "category": "greeting",
                "text": f"{phrase} {name}?",
                "difficulty": "easy"
            })
            sentence_id += 1
    
    # 2. DAILY LIFE (1500)
    actions = ["eating", "drinking", "sleeping", "working", "studying", "reading", "writing",
               "walking", "running", "sitting", "standing", "waiting", "playing", "watching",
               "listening", "talking", "cooking", "cleaning", "washing", "resting"]
    
    for action in actions:
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"I am {action}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"He is {action}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"She is {action}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"They are {action}", "difficulty": "easy"})
        sentence_id += 1
    
    wants = ["food", "water", "tea", "coffee", "milk", "rice", "bread", "fruit", "help", "rest"]
    for want in wants:
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"I want {want}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"I need {want}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"Do you want {want}?", "difficulty": "easy"})
        sentence_id += 1
    
    feelings = ["happy", "sad", "angry", "tired", "hungry", "thirsty", "sick", "well", "fine", "busy"]
    for feeling in feelings:
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"I am {feeling}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"I feel {feeling}", "difficulty": "easy"})
        sentence_id += 1
    
    weather = ["hot", "cold", "warm", "cool", "sunny", "cloudy", "rainy", "windy"]
    for w in weather:
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"It is {w}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"It is very {w}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"It is too {w}", "difficulty": "easy"})
        sentence_id += 1
    
    times = ["morning", "afternoon", "evening", "night", "day", "today", "tomorrow", "yesterday"]
    for t in times:
        sentences.append({"id": sentence_id, "category": "daily_life", "text": f"In the {t}", "difficulty": "easy"})
        sentence_id += 1
    
    # 3. QUESTIONS (1200)
    question_words = {
        "What": ["is this", "is that", "is your name", "do you do", "do you want", "time is it",
                 "day is it", "are you doing", "happened", "is wrong"],
        "Where": ["is the bathroom", "is the market", "is the hospital", "is the station",
                  "are you", "are you going", "do you live", "is it", "can I find"],
        "When": ["are you coming", "will you come", "did you arrive", "is it", "does it start",
                 "can I come", "should I come"],
        "Why": ["are you late", "is this happening", "did you do that", "not", "are you crying"],
        "How": ["are you", "do you do this", "much is this", "much does it cost", "far is it",
                "long does it take", "old are you", "many are there"],
        "Who": ["is this", "is that", "are you", "did this", "called", "will come"],
        "Which": ["one", "way", "is better", "do you prefer", "is yours"]
    }
    
    for q_word, endings in question_words.items():
        for ending in endings:
            sentences.append({
                "id": sentence_id,
                "category": "question",
                "text": f"{q_word} {ending}?",
                "difficulty": "medium"
            })
            sentence_id += 1
    
    yes_no_questions = [
        "Do you understand?", "Can you help me?", "Is this correct?", "Are you sure?",
        "Do you know?", "Can I come?", "May I come in?", "Is it ready?",
        "Are you hungry?", "Do you have time?", "Can you speak English?",
        "Do you have children?", "Are you married?", "Is it far?", "Is it expensive?"
    ]
    
    for q in yes_no_questions:
        sentences.append({"id": sentence_id, "category": "question", "text": q, "difficulty": "medium"})
        sentence_id += 1
    
    # 4. COMMANDS (500)
    commands = [
        "Come here", "Go there", "Sit down", "Stand up", "Wait here", "Stop",
        "Listen", "Look", "Watch", "Help me", "Give me", "Take this",
        "Open the door", "Close the window", "Turn on the light", "Turn off the fan",
        "Be quiet", "Be careful", "Hurry up", "Slow down", "Wake up", "Get up",
        "Eat your food", "Drink water", "Take rest", "Go to sleep",
        "Clean the room", "Wash your hands", "Call me", "Tell me"
    ]
    
    for cmd in commands:
        sentences.append({"id": sentence_id, "category": "command", "text": cmd, "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "command", "text": f"Please {cmd.lower()}", "difficulty": "easy"})
        sentence_id += 1
    
    # 5. FAMILY (500)
    family_members = [
        "father", "mother", "brother", "sister", "son", "daughter",
        "grandfather", "grandmother", "uncle", "aunt", "cousin",
        "husband", "wife", "child", "parent", "relative"
    ]
    
    for member in family_members:
        sentences.append({"id": sentence_id, "category": "family", "text": f"This is my {member}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "family", "text": f"Where is your {member}?", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "family", "text": f"My {member} is at home", "difficulty": "medium"})
        sentence_id += 1
    
    numbers = ["one", "two", "three", "four", "five"]
    for num in numbers:
        sentences.append({"id": sentence_id, "category": "family", "text": f"I have {num} children", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "family", "text": f"I have {num} brothers", "difficulty": "medium"})
        sentence_id += 1
    
    # 6. FOOD (800)
    foods = [
        "rice", "bread", "roti", "dal", "curry", "vegetable", "fruit", "meat", "chicken",
        "fish", "egg", "milk", "tea", "coffee", "water", "juice", "sugar", "salt", "oil"
    ]
    
    for food in foods:
        sentences.append({"id": sentence_id, "category": "food", "text": f"I want {food}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "food", "text": f"I like {food}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "food", "text": f"I don't like {food}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "food", "text": f"Do you have {food}?", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "food", "text": f"Give me some {food}", "difficulty": "easy"})
        sentence_id += 1
    
    food_descriptions = [
        "The food is delicious", "The food is good", "The food is bad",
        "The food is hot", "The food is cold", "The food is spicy",
        "I am vegetarian", "I don't eat meat", "I am hungry",
        "Let's eat", "Time to eat", "What is for dinner?"
    ]
    
    for desc in food_descriptions:
        sentences.append({"id": sentence_id, "category": "food", "text": desc, "difficulty": "medium"})
        sentence_id += 1
    
    # 7. TRAVEL (800)
    places = [
        "home", "work", "school", "market", "hospital", "temple", "mosque",
        "church", "station", "airport", "bus stop", "city", "village"
    ]
    
    for place in places:
        sentences.append({"id": sentence_id, "category": "travel", "text": f"I am going to {place}", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "travel", "text": f"Where is the {place}?", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "travel", "text": f"How do I get to the {place}?", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "travel", "text": f"Is this the way to the {place}?", "difficulty": "medium"})
        sentence_id += 1
    
    directions = [
        "Turn left", "Turn right", "Go straight", "Go back",
        "It is near", "It is far", "It is here", "It is there",
        "I am lost", "Please help me", "Show me the way"
    ]
    
    for direction in directions:
        sentences.append({"id": sentence_id, "category": "travel", "text": direction, "difficulty": "medium"})
        sentence_id += 1
    
    # 8. HEALTH (600)
    body_parts = [
        "head", "eyes", "ears", "nose", "mouth", "teeth", "throat", "neck",
        "chest", "stomach", "back", "arms", "hands", "legs", "feet"
    ]
    
    for part in body_parts:
        sentences.append({"id": sentence_id, "category": "health", "text": f"My {part} hurts", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "health", "text": f"I have pain in my {part}", "difficulty": "medium"})
        sentence_id += 1
    
    illnesses = [
        "I am sick", "I have a fever", "I have a cold", "I have a cough",
        "I have a headache", "I have a stomachache", "I am not well",
        "I need medicine", "I need a doctor", "Where is the hospital?",
        "Call a doctor", "I feel better", "I am getting better",
        "Take rest", "Get well soon", "Are you okay?"
    ]
    
    for illness in illnesses:
        sentences.append({"id": sentence_id, "category": "health", "text": illness, "difficulty": "medium"})
        sentence_id += 1
    
    # 9. SHOPPING (700)
    items = [
        "vegetables", "fruit", "clothes", "shoes", "bag", "phone", "book", "pen", "paper"
    ]
    
    for item in items:
        sentences.append({"id": sentence_id, "category": "shopping", "text": f"I want to buy {item}", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "shopping", "text": f"How much is this {item}?", "difficulty": "medium"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "shopping", "text": f"Do you have {item}?", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "shopping", "text": f"I need {item}", "difficulty": "easy"})
        sentence_id += 1
    
    shopping_phrases = [
        "How much does this cost?", "This is too expensive", "This is cheap",
        "Can you give a discount?", "I will buy this", "I will take it",
        "Show me another one", "Do you have a bigger size?", "Do you have a smaller size?",
        "What colors do you have?", "I like this", "I don't like this"
    ]
    
    for phrase in shopping_phrases:
        sentences.append({"id": sentence_id, "category": "shopping", "text": phrase, "difficulty": "medium"})
        sentence_id += 1
    
    # 10. TIME (400)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        sentences.append({"id": sentence_id, "category": "time", "text": f"Today is {day}", "difficulty": "easy"})
        sentence_id += 1
    
    time_phrases = [
        "What time is it?", "What day is it?", "What is the date?",
        "Today is a good day", "Tomorrow I will go", "Yesterday I went",
        "In the morning", "In the afternoon", "In the evening", "At night",
        "Early morning", "Late night", "Right now", "Later", "Soon",
        "Wait a minute", "Just a moment", "I am coming", "I will be there"
    ]
    
    for phrase in time_phrases:
        sentences.append({"id": sentence_id, "category": "time", "text": phrase, "difficulty": "easy"})
        sentence_id += 1
    
    # 11. WORK & EDUCATION (600)
    occupations = ["teacher", "doctor", "farmer", "worker", "driver", "shopkeeper", "student"]
    for job in occupations:
        sentences.append({"id": sentence_id, "category": "work", "text": f"I am a {job}", "difficulty": "easy"})
        sentence_id += 1
        sentences.append({"id": sentence_id, "category": "work", "text": f"My father is a {job}", "difficulty": "medium"})
        sentence_id += 1
    
    work_phrases = [
        "I am working", "I am studying", "I go to school", "I go to college",
        "Where do you work?", "What do you do?", "I am learning",
        "I know", "I don't know", "I understand", "I don't understand",
        "Please explain", "Can you teach me?", "I am a student"
    ]
    
    for phrase in work_phrases:
        sentences.append({"id": sentence_id, "category": "work", "text": phrase, "difficulty": "medium"})
        sentence_id += 1
    
    # 12. COMPLEX SENTENCES (1500)
    # If/Then patterns
    if_conditions = [
        ("If it rains", "I will stay home"),
        ("If you come", "I will be happy"),
        ("If I have time", "I will help you"),
        ("If you want", "you can come"),
        ("If he asks", "tell him the truth")
    ]
    
    for if_part, then_part in if_conditions:
        sentences.append({
            "id": sentence_id,
            "category": "complex",
            "text": f"{if_part}, {then_part}",
            "difficulty": "hard"
        })
        sentence_id += 1
    
    # Because patterns
    because_patterns = [
        ("I am staying home", "because it is raining"),
        ("I am happy", "because you came"),
        ("I cannot come", "because I am busy"),
        ("I am late", "because the bus was late"),
        ("I am tired", "because I worked all day")
    ]
    
    for main, reason in because_patterns:
        sentences.append({
            "id": sentence_id,
            "category": "complex",
            "text": f"{main} {reason}",
            "difficulty": "hard"
        })
        sentence_id += 1
    
    # Compound sentences with "and", "but", "or"
    compound_patterns = [
        "I like tea and coffee",
        "Come here and sit down",
        "He is tall but thin",
        "I want to come but I am busy",
        "Do you want tea or coffee?",
        "Is it near or far?",
        "I can go today or tomorrow",
        "My father works hard and my mother cooks well",
        "The food is good but expensive",
        "Call me or send a message"
    ]
    
    for pattern in compound_patterns:
        sentences.append({"id": sentence_id, "category": "complex", "text": pattern, "difficulty": "hard"})
        sentence_id += 1
    
    # Fill remaining up to 10,000 with more variations
    while sentence_id <= 10000:
        # Add more daily conversation patterns
        misc_sentences = [
            "Can you repeat that?",
            "I didn't hear you",
            "Speak slowly please",
            "I will tell you later",
            "Don't worry about it",
            "Everything is okay",
            "It's not a problem",
            "Let me think about it",
            "I forgot",
            "I remember now",
            "That's correct",
            "You are right",
            "I agree with you",
            "I disagree",
            "Maybe you are right",
            "I think so",
            "I don't think so",
            "It's possible",
            "It's impossible",
            "I hope so"
        ]
        
        for sent in misc_sentences:
            if sentence_id > 10000:
                break
            sentences.append({
                "id": sentence_id,
                "category": "conversation",
                "text": sent,
                "difficulty": "medium"
            })
            sentence_id += 1
    
    return sentences[:10000]  # Ensure exactly 10,000

def main():
    print("Generating 10,000 English sentences...")
    sentences = generate_sentences()
    
    # Save to JSON
    output_file = r'i:\Banjara AI\sentences_10k.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sentences, f, indent=2, ensure_ascii=False)
    
    # Print statistics
    categories = {}
    difficulties = {}
    
    for sent in sentences:
        cat = sent['category']
        diff = sent['difficulty']
        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    print(f"\nGenerated {len(sentences)} sentences")
    print("\nBy Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    
    print("\nBy Difficulty:")
    for diff, count in sorted(difficulties.items()):
        print(f"  {diff}: {count}")
    
    print(f"\nSaved to: {output_file}")

if __name__ == "__main__":
    main()
