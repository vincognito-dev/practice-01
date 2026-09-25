quiz_data = [
    {
        "Question": "what color is a banana?", "Option": ["a: red", "b: yellow", "c: burgundy", "d: blue"], "Answer": "b"  
    },
    {
        "Question": "what is the capital of Nigeria?", "Option": ["a: lagos", "b: kaduna", "c: abuja", "d: kanu"], "Answer": "c"
    },
    {
        "Question": "which of these animals is an aquatic animal?", "Option": ["a: goat", "b: tiger", "c: snake", "d: oyster"], "Answer": "d"
    }
]
score = 0

    for question in quiz_data:
        print(question["Question"])
        for opt in question["Option"]:
            print(opt)
        choice = input("Enter the right answer: ")
        if choice == question["Answer"]:
            print("You are correct")
            score += 1
        else:
            print("Wrong answer, you failed")

print(f"You got {score} out of {len(quiz_data)}")
