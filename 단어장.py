#컴퓨터공학과 20244043 김민주
print('컴퓨터공학과 20244043 김민주')

def add_word(dictionary, word, meaning):
    dictionary[word] = meaning
    print(f"{word}: {meaning}이(가) 단어장에 추가되었습니다.")

def search_word(dictionary, word):
    if word in dictionary:
        print(f"{word}: {dictionary[word]}")
    else:
        print(f"{word}은(는) 단어장에 없습니다.")

def main():
    word_dict = {}  # 빈 단어장 생성

    while True:
        print("\n1. 단어 추가")
        print("2. 단어 검색")
        print("3. 종료")
        choice = input("선택: ")

        if choice == '1':
            word = input("영어 단어: ")
            meaning = input("뜻: ")
            add_word(word_dict, word, meaning)
        elif choice == '2':
            word = input("검색할 영어 단어: ")
            search_word(word_dict, word)
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()












