import re
#Уберите все символы пунктуации из предложения
sentence = """A, very very; irregular_sentence"""
result_str =  re.sub(r'([,;_])', ' ',sentence)
print(result_str)