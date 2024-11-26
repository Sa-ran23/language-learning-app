import random

# Word dictionaries for each language
languages = {
    "Japanese": [
        {"Japanese": "こんにちは", "English": "hello"},
        {"Japanese": "ありがとう", "English": "thank you"},
        {"Japanese": "さようなら", "English": "goodbye"},
        {"Japanese": "はい", "English": "yes"},
        {"Japanese": "いいえ", "English": "no"},
        {"Japanese": "おはよう", "English": "good morning"},
        {"Japanese": "こんばんは", "English": "good evening"},
        {"Japanese": "おやすみ", "English": "good night"},
        {"Japanese": "すみません", "English": "excuse me / Sorry"},
        {"Japanese": "ごめんなさい", "English": "i’m sorry"},
        {"Japanese": "お願いします", "English": "please"},
        {"Japanese": "どういたしまして", "English": "you’re welcome"},
        {"Japanese": "わかります", "English": "i understand"},
        {"Japanese": "わかりません", "English": "i don’t understand"},
        {"Japanese": "もう一度", "English": "one more time"},
        {"Japanese": "ゆっくり", "English": "slowly"},
        {"Japanese": "こんにちは、元気ですか？", "english": "Hello, how are you?"},
        {"Japanese": "元気です", "English": "i’m fine"},
        {"Japanese": "名前", "English": "name"},
        {"Japanese": "私", "English": "i / me"},
        {"Japanese": "あなた", "English": "you"},
        {"Japanese": "彼", "English": "he"},
        {"Japanese": "彼女", "English": "she"},
        {"Japanese": "私たち", "English": "we"},
        {"Japanese": "彼ら", "English": "they"},
        {"Japanese": "これ", "English": "this"},
        {"Japanese": "それ", "English": "that"},
        {"Japanese": "あれ", "English": "that over there"},
        {"Japanese": "どれ", "English": "which"},
        {"Japanese": "ここ", "English": "here"},
        {"Japanese": "そこ", "English": "there"},
        {"Japanese": "あそこ", "English": "over there"},
        {"Japanese": "どこ", "English": "where"},
        {"Japanese": "いつ", "English": "when"},
        {"Japanese": "誰", "English": "who"},
        {"Japanese": "何", "English": "what"},
        {"Japanese": "どうして", "English": "why"},
        {"Japanese": "いくら", "English": "how much"},
        {"Japanese": "時間", "English": "time"},
        {"Japanese": "今", "English": "now"},
        {"Japanese": "今日", "English": "today"},
        {"Japanese": "明日", "English": "tomorrow"},
        {"Japanese": "昨日", "English": "yesterday"},
        {"Japanese": "毎日", "English": "every day"},
        {"Japanese": "月", "English": "month"},
        {"Japanese": "年", "English": "year"},
        {"Japanese": "人", "English": "person"},
        {"Japanese": "友達", "English": "friend"},
        {"Japanese": "家族", "English": "family"},
        {"Japanese": "学校", "English": "school"},
        {"Japanese": "会社", "English": "company"},
        {"Japanese": "先生", "English": "teacher"},
        {"Japanese": "学生", "English": "student"},
        {"Japanese": "仕事", "English": "work"},
        {"Japanese": "買い物", "English": "shopping"},
        {"Japanese": "食べ物", "English": "food"},
        {"Japanese": "飲み物", "English": "drink"},
        {"Japanese": "水", "English": "water"},
        {"Japanese": "お茶", "English": "tea"},
        {"Japanese": "コーヒー", "English": "coffee"},
        {"Japanese": "ご飯", "English": "meal / rice"},
        {"Japanese": "パン", "English": "bread"},
        {"Japanese": "肉", "English": "meat"},
        {"Japanese": "魚", "English": "fish"},
        {"Japanese": "野菜", "English": "vegetables"},
        {"Japanese": "果物", "English": "fruits"},
        {"Japanese": "犬", "English": "dog"},
        {"Japanese": "猫", "English": "cat"},
        {"Japanese": "車", "English": "car"},
        {"Japanese": "電車", "English": "train"},
        {"Japanese": "自転車", "English": "bicycle"},
        {"Japanese": "道", "English": "road"},
        {"Japanese": "家", "English": "house"},
        {"Japanese": "部屋", "English": "room"},
        {"Japanese": "ドア", "English": "door"},
        {"Japanese": "窓", "English": "window"},
        {"Japanese": "椅子", "English": "chair"},
        {"Japanese": "机", "English": "desk"},
        {"Japanese": "本", "English": "book"},
        {"Japanese": "ペン", "English": "pen"},
        {"Japanese": "紙", "English": "paper"},
        {"Japanese": "携帯", "English": "mobile phone"},
        {"Japanese": "テレビ", "English": "television"},
        {"Japanese": "インターネット", "English": "internet"},
        {"Japanese": "音楽", "English": "music"},
        {"Japanese": "映画", "English": "movie"},
        {"Japanese": "スポーツ", "English": "sports"},
        {"Japanese": "天気", "English": "weather"},
        {"Japanese": "雨", "English": "rain"},
        {"Japanese": "雪", "English": "snow"},
        {"Japanese": "風", "English": "wind"},
        {"Japanese": "太陽", "English": "sun"},
        {"Japanese": "月", "English": "moon"},
        {"Japanese": "星", "English": "star"},
    ],
    "Spanish": [
        {"Spanish": "hola", "English": "hello"},
        {"Spanish": "adiós", "English": "goodbye"},
        {"Spanish": "por favor", "English": "please"},
        {"Spanish": "gracias", "English": "thank you"},
        {"Spanish": "lo siento", "English": "sorry"},
        {"Spanish": "sí", "English": "yes"},
        {"Spanish": "no", "English": "no"},
        {"Spanish": "buenos días", "English": "good morning"},
        {"Spanish": "buenas tardes", "English": "good afternoon"},
        {"Spanish": "buenas noches", "English": "good night"},
        {"Spanish": "¿cómo estás?", "English": "how are you?"},
        {"Spanish": "muy bien", "English": "very well"},
        {"Spanish": "¿y tú?", "English": "and you?"},
        {"Spanish": "amigo", "English": "friend"},
        {"Spanish": "familia", "English": "family"},
        {"Spanish": "comida", "English": "food"},
        {"Spanish": "agua", "English": "water"},
        {"Spanish": "amor", "English": "love"},
        {"Spanish": "dinero", "English": "money"},
        {"Spanish": "trabajo", "English": "work"},
        {"Spanish": "escuela", "English": "school"},
        {"Spanish": "casa", "English": "house"},
        {"Spanish": "perro", "English": "dog"},
        {"Spanish": "gato", "English": "cat"},
        {"Spanish": "libro", "English": "book"},
        {"Spanish": "coche", "English": "car"},
        {"Spanish": "ciudad", "English": "city"},
        {"Spanish": "país", "English": "country"},
        {"Spanish": "feliz", "English": "happy"},
        {"Spanish": "triste", "English": "sad"},
        {"Spanish": "grande", "English": "big"},
        {"Spanish": "pequeño", "English": "small"},
        {"Spanish": "rápido", "English": "fast"},
        {"Spanish": "lento", "English": "slow"},
        {"Spanish": "caliente", "English": "hot"},
        {"Spanish": "frío", "English": "cold"},
        {"Spanish": "día", "English": "day"},
        {"Spanish": "noche", "English": "night"},
        {"Spanish": "hombre", "English": "man"},
        {"Spanish": "mujer", "English": "woman"},
        {"Spanish": "niño", "English": "boy"},
        {"Spanish": "niña", "English": "girl"},
        {"Spanish": "amable", "English": "kind"},
        {"Spanish": "difícil", "English": "difficult"},
        {"Spanish": "fácil", "English": "easy"},
        {"Spanish": "tiempo", "English": "time"},
        {"Spanish": "ayer", "English": "yesterday"},
        {"Spanish": "hoy", "English": "today"},
        {"Spanish": "mañana", "English": "tomorrow"},
        {"Spanish": "nunca", "English": "never"},
        {"Spanish": "siempre", "English": "always"}
    ],
    "French": [
        {"French": "le", "English": "the (masculine singular)"},
        {"French": "la", "English": "the (feminine singular)"},
        {"French": "les", "English": "the (plural)"},
        {"French": "un", "English": "a, an (masculine singular)"},
        {"French": "une", "English": "a, an (feminine singular)"},
        {"French": "et", "English": "and"},
        {"French": "à", "English": "to, at"},
        {"French": "de", "English": "of, from"},
        {"French": "en", "English": "in, on"},
        {"French": "dans", "English": "in"},
        {"French": "que", "English": "that, than"},
        {"French": "qui", "English": "who, that"},
        {"French": "pour", "English": "for"},
        {"French": "avec", "English": "with"},
        {"French": "sur", "English": "on, upon"},
        {"French": "par", "English": "by"},
        {"French": "se", "English": "oneself, himself, herself"},
        {"French": "il", "English": "he, it"},
        {"French": "elle", "English": "she, it"},
        {"French": "nous", "English": "we, us"},
        {"French": "vous", "English": "you (formal/plural)"},
        {"French": "ils", "English": "they (masculine)"},
        {"French": "elles", "English": "they (feminine)"},
        {"French": "je", "English": "I"},
        {"French": "tu", "English": "you (informal singular)"},
        {"French": "au", "English": "to the, at the (masculine singular)"},
        {"French": "aux", "English": "to the, at the (plural)"},
        {"French": "ce", "English": "this, that (masculine singular)"},
        {"French": "cette", "English": "this, that (feminine singular)"},
        {"French": "ces", "English": "these, those"},
        {"French": "son", "English": "his, her, its"},
        {"French": "sa", "English": "his, her, its (feminine singular)"},
        {"French": "ses", "English": "his, her, its (plural)"},
        {"French": "mon", "English": "my (masculine singular)"},
        {"French": "ma", "English": "my (feminine singular)"},
        {"French": "mes", "English": "my (plural)"},
        {"French": "ton", "English": "your (informal masculine singular)"},
        {"French": "ta", "English": "your (informal feminine singular)"},
        {"French": "tes", "English": "your (informal plural)"},
        {"French": "leur", "English": "their (singular)"},
        {"French": "leurs", "English": "their (plural)"},
        {"French": "mais", "English": "but"},
        {"French": "ou", "English": "or"},
        {"French": "si", "English": "if"},
        {"French": "non", "English": "no"},
        {"French": "oui", "English": "yes"},
        {"French": "bien", "English": "well, good"},
        {"French": "mal", "English": "bad, badly"},
        {"French": "tout", "English": "all, everything (masculine singular)"},
        {"French": "tous", "English": "all, everyone (masculine plural)"},
        {"French": "toutes", "English": "all (feminine plural)"}
    ],
}

def quiz_user(language, words):
    random.shuffle(words)
    score = 0

    print(f"\nStarting quiz for {language}!\n")
    for word in words:
        target_word = word[language]
        print(f"What is the English translation of '{target_word}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word["English"].lower()

        if user_answer == correct_answer:
            print("Correct Answer!\n")
            print("Enter 'exit' to exit !\n")
            score += 1
        elif user_answer == 'exit':
            break
        else:
            print(f"Wrong, The correct answer is '{word['English']}'.\n")
            print("Enter 'exit' to exit !\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}\n")


def main():
    print("Welcome to the Language Learning App!")
    print("Available languages to learn:")
    for i, lang in enumerate(languages.keys(), start=1):
        print(f"{i}. {lang}")

    while True:
        try:
            choice = int(input("\nEnter the number of the language you'd like to learn: "))
            selected_language = list(languages.keys())[choice - 1]
            break
        except (IndexError, ValueError):
            print("Invalid choice. Please try again.")

    input("Press Enter to start the quiz...")
    quiz_user(selected_language, languages[selected_language])


if __name__ == "__main__":
    main()
