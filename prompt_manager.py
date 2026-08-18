# AI 프롬프트 관리 프로그램

prompts = [
    {
        "title": "블로그 글 작성",
        "content": "주어진 주제로 초보자도 이해하기 쉬운 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "따뜻하고 감성적인 분위기의 일러스트 이미지를 만들어줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "발표 자료 작성",
        "content": "주어진 주제에 대해 발표용 PPT의 구성과 핵심 내용을 작성해줘.",
        "category": "자동화",
        "favorite": False
    }
]

categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]
def get_input(message):
    value = input(message).strip()

    if value.lower() == "q":
        print()
        print("========================================")
        print("          프로그램 종료")
        print("========================================")
        print()
        print("프로그램을 종료합니다.")
        print()
        exit()

    return value

def show_menu():
    print()
    print("========================================")
    print("       AI 프롬프트 관리 프로그램")
    print("========================================")
    print()

    print("[ 프롬프트 관리 ]")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 삭제")
    print("4. 프롬프트 수정")
    print()

    print("[ 프롬프트 조회 ]")
    print("5. 카테고리별 조회")
    print("6. 프롬프트 검색")
    print("7. 프롬프트 상세 보기")
    print()

    print("[ 즐겨찾기 ]")
    print("8. 즐겨찾기 추가/해제")
    print("9. 즐겨찾기 목록 보기")
    print()

    print("----------------------------------------")
    print("0. 프로그램 종료")
    print("========================================")


def add_prompt():
    print()
    print("========================================")
    print("             프롬프트 추가")
    print("========================================")
    print()

    while True:
        title = input("제목을 입력하세요: ")

        if not title:
            print("제목은 비워둘 수 없습니다.")
            print()
            continue

        duplicate = False

        for prompt in prompts:
            if prompt["title"].lower() == title.lower():
                duplicate = True
                break

        if duplicate:
            print("이미 같은 제목의 프롬프트가 있습니다.")
            print("다른 제목을 입력해주세요.")
            print()
            continue

        break

    while True:
        content = input("내용을 입력하세요: ")
        if content:
            break

        print("내용은 비워둘 수 없습니다.")
        print()

    print()
    print("[ 카테고리 선택 ]")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:
        category_choice = input("카테고리 번호를 선택하세요: ")

        if category_choice.isdigit():
            category_number = int(category_choice)

            if 1 <= category_number <= len(categories):
                category = categories[category_number - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print()
    print("✅ 프롬프트가 추가되었습니다!")
    print()

def show_list(prompt_list=None):
    print()
    print("========================================")
    print("            프롬프트 목록")
    print("========================================")
    print()

    if prompt_list is None:
        prompt_list = prompts

    if len(prompt_list) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompt_list, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(f"{i}. {prompt['title']}{favorite_mark}")
        print(f"   카테고리: {prompt['category']}")
        print()
def delete_prompt():
    print()
    print("========================================")
    print("             프롬프트 삭제")
    print("========================================")
    print()

    show_list()

    if len(prompts) == 0:
        return

    while True:
        choice = get_input("삭제할 프롬프트 번호를 입력하세요: ")

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    print()
    print(f"선택한 프롬프트: {prompt['title']}")

    while True:
        confirm = get_input("정말 삭제하시겠습니까? (y/n): ").lower()

        if confirm == "y":
            prompts.remove(prompt)
            print()
            print("✅ 프롬프트가 삭제되었습니다.")
            print()
            break

        elif confirm == "n":
            print()
            print("삭제가 취소되었습니다.")
            print()
            break

        else:
            print("y 또는 n을 입력해주세요.")

def edit_prompt():
    print()
    print("========================================")
    print("             프롬프트 수정")
    print("========================================")
    print()

    show_list()

    if len(prompts) == 0:
        return

    while True:
        choice = get_input("수정할 프롬프트 번호를 입력하세요: ")

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    print()
    print(f"현재 제목: {prompt['title']}")

    while True:
        new_title = get_input("새 제목을 입력하세요: ")

        if not new_title:
            new_title = prompt["title"]
            break

        duplicate = any(
            other_prompt["title"].lower() == new_title.lower()
            for i, other_prompt in enumerate(prompts)
            if i != number - 1
        )

        if duplicate:
            print("이미 같은 제목의 프롬프트가 있습니다.")
            print("다른 제목을 입력해주세요.")
        else:
            break

    print()
    print(f"현재 내용: {prompt['content']}")
    new_content = get_input("새 내용을 입력하세요: ")

    if not new_content:
        new_content = prompt["content"]

    prompt["title"] = new_title
    prompt["content"] = new_content

    print()
    print("✅ 프롬프트가 수정되었습니다!")
    print()
def show_categories():
    print()
    print("========================================")
    print("            카테고리별 조회")
    print("========================================")
    print()

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    print()

    while True:
        choice = input("카테고리 번호를 선택하세요: ")

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(categories):
                selected_category = categories[number - 1]
                break

        print("올바른 번호를 입력해주세요.")

    result = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            result.append(prompt)

    print()
    print(f"[ {selected_category} ]")
    print()

    if len(result) == 0:
        print("해당 카테고리의 프롬프트가 없습니다.")
    else:
        for i, prompt in enumerate(result, start=1):
            favorite_mark = " ⭐" if prompt["favorite"] else ""

            print(f"{i}. {prompt['title']}{favorite_mark}")
            print()


def search_prompt():
    print()
    print("========================================")
    print("             프롬프트 검색")
    print("========================================")
    print()

    keyword = get_input("검색할 키워드를 입력하세요: ")

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    result = []

    for prompt in prompts:
        title = prompt["title"].lower()
        content = prompt["content"].lower()
        category = prompt["category"].lower()

        if keyword.lower() in title or keyword.lower() in content or keyword.lower() in category:
            result.append(prompt)

    print()

    if len(result) == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"'{keyword}' 검색 결과")
        print()

        for i, prompt in enumerate(result, start=1):
            favorite_mark = " ⭐" if prompt["favorite"] else ""

            print(f"{i}. {prompt['title']}{favorite_mark}")
            print(f"   카테고리: {prompt['category']}")
            print()

def show_detail():
    print()
    print("========================================")
    print("           프롬프트 상세 보기")
    print("========================================")
    print()

    show_list()

    if len(prompts) == 0:
        return

    while True:
        print("번호를 입력할 준비가 되었습니다.")

        choice = input("상세히 볼 프롬프트 번호를 입력하세요: ")

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    print()
    print("----------------------------------------")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")

    if prompt["favorite"]:
        print("즐겨찾기: ⭐")
    else:
        print("즐겨찾기: 없음")

    print("----------------------------------------")
    print("내용:")
    print(prompt["content"])
    print("----------------------------------------")


def toggle_favorite():
    print()
    print("========================================")
    print("         즐겨찾기 추가 / 해제")
    print("========================================")
    print()

    show_list()

    if len(prompts) == 0:
        return

    while True:
        choice = input("즐겨찾기를 변경할 프롬프트 번호를 입력하세요: ")

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                prompt["favorite"] = not prompt["favorite"]

                if prompt["favorite"]:
                    print()
                    print("⭐ 즐겨찾기에 추가되었습니다!")
                else:
                    print()
                    print("즐겨찾기에서 해제되었습니다.")

                print()
                break

        print("올바른 프롬프트 번호를 입력해주세요.")


def show_favorites():
    print()
    print("========================================")
    print("            즐겨찾기 목록")
    print("========================================")
    print()

    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if len(favorites) == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, start=1):
        print(f"{i}. {prompt['title']} ⭐")
        print(f"   카테고리: {prompt['category']}")
        print()


# 프로그램 시작
while True:
    show_menu()

    choice = get_input("메뉴 번호를 선택하세요: ")

    if choice == "1":
        add_prompt()

    elif choice == "2":
        show_list()

    elif choice == "3":
        delete_prompt()

    elif choice == "4":
        edit_prompt()

    elif choice == "5":
        show_categories()

    elif choice == "6":
        search_prompt()

    elif choice == "7":
        show_detail()

    elif choice == "8":
        toggle_favorite()

    elif choice == "9":
        show_favorites()

    elif choice == "0":
        print()
        print("========================================")
        print("          프로그램 종료")
        print("========================================")
        print()
        print("프로그램을 종료합니다.")
        print()
        break

    else:
        print()
        print("----------------------------------------")
        print("⚠ 잘못된 메뉴 번호입니다.")
        print("0~9 사이의 번호를 입력해주세요.")
        print("----------------------------------------")