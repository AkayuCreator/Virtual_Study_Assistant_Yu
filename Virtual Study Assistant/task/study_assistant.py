if __name__ == '__main__':
# Write your code here >>>
    subjects = {}

while True:

    subject = input("Enter subject name:")
    if subject == "":
        break
    while True:
        try:
            allocateTime = input(f'Enter time allocated for {subject}:').strip()
            if not allocateTime:
                print("input time should be an integer, please enter again!")
                continue
            num = int(allocateTime)
            if num < 0:
                print("input time should be an integer, please enter again!")
                continue
            break
        except ValueError:
            print("input time should be an integer, please enter again!")

    subjects[subject] = int(allocateTime)
    # print(subjects)
if subjects != {}:
    print("Your study plan:")
    for subject in subjects:
        print(f'{subject}: {subjects[subject]} minutes')
    total_study = sum(subjects.values())
    print(f'Total study time: {total_study} minutes')
    total_plus_rest = total_study // 45 * 15 + total_study
    print(f'Total time including breaks: {total_plus_rest} minutes')

    studied_time = int(input("Please enter your studied time:"))
    completeness = (studied_time / total_study) * 100

    if studied_time > total_study:
        print(f'You have completed 100.00% of your planned study time.')
    else:
        print(f"\nYou have completed {completeness:.2f}% of your planned study time.")
        with open('.env', 'r') as fp:
            HF_API_KEY = fp.read().strip()

        from huggingface_hub import InferenceClient

        client = InferenceClient(token=HF_API_KEY)
        prompt = """
        I have to prepare for my {subjects} exams. I've completed {completeness:.2f}% of my curriculum. My motivation should be:
        """.format(
        subjects=','.join(subjects.keys()),
        completeness = completeness
        )
        response = client.text_generation(
            prompt=prompt,
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            temperature=0.01,
            max_new_tokens=50,
            seed=42,
            return_full_text=True,
        )
        print(response)


