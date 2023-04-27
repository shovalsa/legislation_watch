import requests
import json
from huggingface_hub.inference_api import InferenceApi
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM




english_example = """Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among
    those that will be taken down, the company said.  The policy includes the termination of accounts of anti-vaccine influencers.
      Tech giants have been criticised for not doing more to counter false health information on their sites.
      In July, US President Joe Biden said social media platforms were largely responsible for people's scepticism in
      getting vaccinated by spreading misinformation, and appealed for them to address the issue.  YouTube, which is
      owned by Google, said 130,000 videos were removed from its platform since last year, when it implemented a ban on
      content spreading misinformation about Covid vaccines.  In a blog post, the company said it had seen false claims
       about Covid jabs "spill over into misinformation about vaccines in general". The new policy covers long-approved
       vaccines, such as those against measles or hepatitis B.  "We're expanding our medical misinformation policies
       on YouTube with new guidelines on currently administered vaccines that are approved and confirmed to be safe and
       effective by local health authorities and the WHO," the post said, referring to the World Health Organization."""


hebrew_example = """
    כמו נשים יהודיות שומרות מצוות רבות, סנדי טפנאק מבקרת במקווה מדי חודש, בסוף המחזור החודשי, כדרך לשמירה על הלכות טהרת המשפחה. היא מנקה את גופה ביסודיות לפני שהיא טובלת שלוש פעמים, בזמן שהבלנית צופה בה מקיימת את המצווה שנשים יהודיות מקיימות אלפי שנים לפני האיחוד הפיזי עם בעליהן.

אך בניגוד למרבית הטובלות במקווה, לטפנאק מחכה בבית אישה – עובדה שגורמת לעורכת הדין בת ה-36 לחוש אי נוחות מסוימת במהלך הביקורים שלה במקווה האורתודוקסי הסמוך לביתה. "יש איזה חשש. מה אם הבלנית תדע? מה אם פקידת הקבלה שמקבלת את התשלום תדע?" אמרה טפנאק.
"זוהי התחושה העיקרית שעולה. האם אני באמת שייכת הנה? האם האנשים האלה חושבים שאני שייכת הנה? ואני מניחה שברמה האישית ביותר, נשאלת גם השאלה האם אני באמת מאמינה שאני שייכת הנה?"
טפנאק היא חלק מקבוצה קטנה אך צומחת של יהודים להט"בים שמאמצים את חוקי טהרת המשפחה לחיי הנישואים הפרטיים שלהם, וזאת למרות שחוקים אלה חלים על איחוד בין גבר לאישה. מכיוון שההנחיות עבור מי שאינו חי בנישואים הטרוסקסואלים מועטות מאד, רבים מסתמכים על רשתות חברתיות ועל שיחות בלתי פורמליות כדי לברר איך יתאים הנוהג למערכות היחסים שלהם.
    """

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))


def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer


def summarize(tokenizer, model, text):
    input_ids = tokenizer(
        [WHITESPACE_HANDLER(text)],
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        max_length=84,
        no_repeat_ngram_size=2,
        num_beams=4
    )[0]

    summary = tokenizer.decode(
        output_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )

    return summary

if __name__ == "__main__":
    with open('../secrets/tokens.json', 'r') as f:
        tokens = json.load(f)
        api_token = tokens['HF']

    text = """
    רבים מאיתנו התחילו כ-100% תומכי זכויות טרנסג’נדרים. קדימה, תהיו טרנסים וגאים, הייתה העמדה שלנו. אבל אז ראינו מה קרה. אנשים אלו לא היו מרוצים מכך שהם טרנסים וגאים. הם התעקשו שנעמיד פנים שהם באמת בפועל שינו מין! ואז הם התעקשו שעלינו להעמיד פנים שהם תמיד היו ממין נקבה. ואז הם אמרו שאנחנו לא יכולות להתייחס למחזור ווסת כנשי אלא אם כן זה מערב את הפטישים שיש להם בנוגע למחזור, ואז עלינו להעמיד פנים שהם באמת מקבלים מחזור אם הם טוענים שכן. 

זה לא היה רק כמה ‘תפוחים רקובים’ שהכריחו נשים לשתף פעולה. הם השתלטו על ארגון PLANNED PARENTHOOD (שהוא עכשיו הגורם המפיץ הכי גדול בארה”ב של הורמונים של המין השני). הם השתלטו על ארגוני סיוע בלידה. הם האשימו אותנו בכך שאנחנו מצמצמים נשים לאיברי המין שלהן, בזמן שהם פיתחו עבורנו שמות חדשים כמו ‘אנשים שנולדו עם פות’. הם התעקשו שנשים חייבות לקרוא לעצמם אנשים מבייצים, אנשים עם מחזור, אנשים בהריון. נשים שהטילו ספק בשינויים בשפה פוטרו והושמו ברשימות שחורות בנוגע לעבודה באקדמיה ובארגונים ללא כוונת רווח. 

אנס  על פי הודאתו שאומר שהוא אישה וניסה בכח להכניס אישה להריון כדי לעשות ‘תינוק קווירי’ קיבל זכות לדבר על במה ביום צעדת הנשים, ואוקיאנוס של נשים בכובעי “פוסי” ורודים הריעו לו, ואז הנשים האלו בעצמן הותקפו על “פשע השנאה” של ללבוש כובעי פוסי בגלל שהכובעים האלו היו טרנספובים. וכך זה המשיך עוד ועוד, ורבים מאיתנו התעוררו להכרה מעוררת האימה שאלו למעשה הפנים הטוטליטריות החדשות של הפטריארכיה. 
    """

    model_name = "google/mt5-small"
    model, tokenizer = load_model(model_name)
    summary = summarize(tokenizer, model, text)
    print(type(summary))
    print(summary)
