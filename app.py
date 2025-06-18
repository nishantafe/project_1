import easygui


def ask_question(the_question, the_image, the_correct_answer, the_score, the_app_name="MyApp"):
    answer = easygui.ynbox(msg=the_question,
                           title=the_app_name,
                           image=the_image)
    correct_answer = the_correct_answer.lower()
    if correct_answer != "yes":
        answer = not answer  # Change True to False
    if answer:
        easygui.msgbox(msg="You are right!", title=app_name, ok_button="Continue")
        the_score += 1
    else:
        easygui.msgbox(msg="You are wrong!", title=app_name, ok_button="Continue")
    return the_score


app_name = "MyApp"
score = 0

easygui.msgbox(msg="Welcome to my app", title=app_name, ok_button="Get started")
score = ask_question(the_question="Is the person in the image cooking",
                     the_image="cooking.gif",
                     the_correct_answer="yes",
                     the_score=score)

score = ask_question(the_question="Is the person in the image driving",
                     the_image="driving.png",
                     the_correct_answer="yes",
                     the_score=score)

easygui.msgbox(msg=f"Your final score is {score}", title=app_name, ok_button="Close")
