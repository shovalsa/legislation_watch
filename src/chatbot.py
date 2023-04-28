import openai

import api_keys


def ask_if_affects_lgbt(text):
    openai.api_key = api_keys.openai

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user",
             "content": "does the text contain any resolution or suggestion that might affect lgbtq people?"
                        +
                        text
                        +
                        "if the response is negative just respond no, otherwise give an explanation why the answer is "
                        "yes."
             },
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)


if __name__ == "__main__":
    text = '''
    אני רוצה להפנות את הדברים שלי לחבר הכנסת נתניהו, ראש הממשלה המיועד. חבר הכנסת נתניהו, מאוד קל לומר באנגלית לתקשורת הזרה שאתה תומך בקהילת הלהט"ב. מאוד קל לתדרך מאחורי הקלעים את העיתונאים שאין מה לחשוש, שלא תהיה שום פגיעה בזכויות של קהילת הלהט"ב. אבל בוא, בוא נשמע אותך אומר את הדברים מעל בימה הזו, לנו וגם לשותפים שלך. בוא ותגיד את הדברים גם לשותפים ההומופובים שלך אבי מעוז, בצלאל סמוטריץ' ואורית סטרוק. בוא נשמע את כל ההבטחות האלה כאן בכנסת בעברית פשוטה וברורה. יותר מכך – בוא נראה מעשים. 
        '''
    ask_if_affects_lgbt(text)
