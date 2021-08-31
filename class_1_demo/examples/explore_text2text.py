
# 사전훈련된 모델로 간다하게 프로토타이핑.
from transformers import pipeline


def main():
    text2text_generator = pipeline("text2text-generation")
    # text 에서 text를 생성해내는 것이 가능할 것.
    ans = text2text_generator("question: What is 42 ? context: 42 is the answer to life, the universe and everything")
    print(ans)


if __name__ == '__main__':
    main()