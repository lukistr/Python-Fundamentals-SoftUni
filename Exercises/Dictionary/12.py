def process_submission(submission, participants, banned_users, language_submissions):
    username, language, points = submission.split("-")
    points = int(points)

    if username in banned_users:
        return

    if username not in participants:
        participants[username] = points
    else:
        participants[username] = max(participants[username], points)

    if language not in language_submissions:
        language_submissions[language] = 1
    else:
        language_submissions[language] += 1

def ban_user(username, participants, banned_users):
    if username in participants:
        del participants[username]
    banned_users.add(username)

def print_results(participants):
    print("Results:")
    for username, points in sorted(participants.items(), key=lambda x: (-x[1], x[0])):
        print(f"{username} | {points}")

def print_language_submissions(language_submissions):
    print("Submissions:")
    for language, count in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
        print(f"{language} - {count}")

participants = {}
banned_users = set()
language_submissions = {}

while True:
    submission = input()
    if submission == "exam finished":
        break

    if "-banned" in submission:
        username = submission.split("-")[0]
        ban_user(username, participants, banned_users)
    else:
        process_submission(submission, participants, banned_users, language_submissions)

print_results(participants)
print_language_submissions(language_submissions)
