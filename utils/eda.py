import re
from underthesea import word_tokenize

vn_synonym_dict = [
    ['bao nhiêu', 'mấy', 'bn', 'bao nhiu' , 'nhiêu', 'bao nhiu'],
    ['đầm', 'áo', 'set', 'váy'],
    ['vàng', 'xanh', 'đỏ', 'tím', 'hồng', 'cam', 'trắng', 'đen', 'nude', 'nút', 'màu'],
    ['size', 'sz', 'cỡ', 's', 'm', 'l', 'xl', 'xxl'],
    ['gửi', 'chụp', 'đưa', 'đặt', 'lấy', 'xem', 'coi'],
    ['không', 'ko'],
    ['được', 'đc', 'dc'],
    ['gì', 'nào', 'j'],
    ['chào', 'ơi', 'hello', 'hi']
]

def get_synonyms(term):
    for ele in vn_synonym_dict:
        if term in ele:
            return [_ for _ in ele if _ != term]
    return []

def synonym_replacement(src = ''):
    if src != '':
        words = word_tokenize(src)
        augmented_sentences = []
        for word in words:
            synonyms = get_synonyms(word)
            for synonym in synonyms:
                new_sentence = re.sub(word, synonym, src)
                print(new_sentence)
                augmented_sentences.append(new_sentence)
        return augmented_sentences
    return ''