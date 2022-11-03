#question

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def chechAnswer(self,answer):
        return self.answer==answer

q1=Question('which one is better program languague ?',['C#','Python','Java','C'],'Python')
q2=Question('which one is most popular program languague ?',['C#','Python','Java','C'],'Python')
q3=Question('which one is most expensive program languague ?',['C#','Python','Java','C'],'Python')

# print(q1.chechAnswer('Python'))
# print(q2.chechAnswer('Java'))
# print(q3.chechAnswer('C'))
#quiz


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]


questions=[q1,q2,q3]

quiz=Quiz(questions)

question=quiz.getQuestion()

print(question.text)
print(question)



