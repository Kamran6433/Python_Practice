# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# My answer: This is a 5 kyu question which I thought I could answer.
def pig_it(text):
    counter = []
    for index, i in enumerate(text):
        counter.append(text[index])
        if counter[index] == " ":
            counter[0] = counter.remove(0)
            counter[index - 1] = counter[0] + "ay"

    return counter

# string = "Kamran is the best"
# new_list = []
# new_list.append(string[0])
# print(new_list)


print(pig_it("Kamran "))

# This is the answer I got from a source on GitHub by ellismckenzielee:
#
# def pig_it(text):
#     '''Converts text into pig-latin'''
#     split_text = text.split(' ')
#     pig_sentence = ' '
#
#     for word in split_text:
#         if word in '!.%&?':
#             pig_sentence = pig_sentence + word
#         else:
#             pig_word = word[1:] + word[0] + 'ay'
#             pig_sentence = pig_sentence + pig_word + ' '
#
#     return pig_sentence.strip(' ')
