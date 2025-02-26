import random

ques_dict = {
    1: "Which of the following is not a basic datatype in Python?",
    2: "What is the output of 3+2*2 ?",
    3: "What is the purpose of return statement?",
    4: "Which operator is used for exponentiation?",
    5: "Which method is used to remove an item from a list by value?"
}

choices = {
    1: ['int', 'char', 'float', 'string'],
    2: ['5', '8', '7', '10'],
    3: ['to return a value to caller', 'give output', 'to print value', 'to end value'],
    4: ['^', '*', '**', '//'],
    5: ['remove()', 'delete()', 'discard()', 'pop()']
}

crct_ans = {
    1: 'char',
    2: '7',
    3: 'to return a value to caller',
    4: '**',
    5: 'remove()'
}

def quiz(ques, choices, c_ans):
    q_no = list(ques.keys())
    random.shuffle(q_no)
    num = 1
    score = 0
    total_questions = len(q_no)

    for i in q_no:
        print(f"Question {num}: {ques[i]}")
        options = ['A', 'B', 'C', 'D']
        
        # Display answer choices
        for j, option in enumerate(choices[i]):
            print(f"{options[j]}. {option}")
        
        # Get user input and validate
        while True:
            user_input = input("Enter your answer (A, B, C or D): ").upper()
            if user_input in options:
                break
            print("Invalid choice! Please enter A, B, C, or D.")
        
        selected_option = options.index(user_input)
        user_answer = choices[i][selected_option]

        # Check answer and update score
        if user_answer.lower() == c_ans[i].lower():
            print('✅ Correct answer!')
            score += 1
        else:
            print('❌ Wrong answer.')
            print(f"Correct answer is: {c_ans[i]}")
        
        print()
        num += 1

    # Display final score
    print(f"Your final score: {score}/{total_questions} ({(score/total_questions) * 100:.2f}%)")
    if score == total_questions:
        print("🎉 Excellent! You got all answers correct!")
    elif score >= total_questions / 2:
        print("😊 Good job! Keep practicing.")
    else:
        print("😢 Better luck next time! Keep learning.")

quiz(ques_dict, choices, crct_ans)
