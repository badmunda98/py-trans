# Project: py-trans
# Author: itz-fork
import requests
from .language_codes import get_lang_name

class PyTranslator:
    """
    PyTranslator Class

    Note:
        Before Trying to Translate Create an instance of this with provider (Default provider is google)
    
    Providers:
        google - Google Translate
        libre - LibreTranslate Engine
        translate.com - translate.com Translate
        my_memory - MyMemory Translate

    Argument(s):
        provider - Provider of Translator. (Must be a supported provider)
    
    Example(s):
        pytranslator = PyTranslator(provider="google")
    """
    def __init__(self, provider="google"):
        self.providers = ["google", "libre", "translate.com", "my_memory"]
        if provider in self.providers:
            self.provider = provider
        else:
            self.provider = "google"
        # Headers
        self.gheader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        self.lheader = {"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"}

    def translate(self, text, dest_lang="en"):
        """
        Translator Function

        Argument(s):
            text - Source Text (Text that need to be translated)
            dest_lang - Destination Language
        
        Example(s):
            pytranslator.translate(text="Hi, How are you?", dest_lang="si")
        """
        if self.provider == "google":
            return self.google_translate(text, dest_lang)
        elif self.provider == "libre":
            return self.libre_translate(text, dest_lang)
        elif self.provider == "translate.com":
            return self.translate_com(text, dest_lang)
        elif self.provider == "my_memory":
            return self.my_memory(text, dest_lang)
        else:
            return
    
    # Google Translate
    def google_translate(self, text, dest_lang):
        r_url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest_lang}&q={text}"
        try:
            request_resp = requests.get(r_url, headers=self.gheader).json()
            translation = request_resp['sentences'][0]['trans']
            origin_text = request_resp['sentences'][0]['orig']
            origin_lang = get_lang_name(request_resp['src'])
            tr_dict = {"status": "success", "engine": "google", "translation": translation, "dest_lang": dest_lang, "orgin_text": origin_text, "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # LibreTranslate
    def _detect_lang(self, text):
        r_url = requests.post("https://libretranslate.com/detect", data={"q": str(text)}, headers=self.lheader).json()
        return r_url[0]["language"]
    
    def libre_translate(self, text, dest_lang):
        try:
            source_lang = self._detect_lang(text=text)
            r_url = requests.post("https://libretranslate.com/translate", data={"q": str(text), "source": source_lang, "target": dest_lang}, headers=self.lheader).json()
            translation = r_url["translatedText"]
            origin_lang = get_lang_name(source_lang)
            tr_dict = {"status": "success", "engine": "libre", "translation": translation, "dest_lang": dest_lang, "orgin_text": str(text), "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # Translate.com
    def translate_com(self, text, dest_lang):
        try:
            r_url = requests.post("https://www.translate.com/translator/ajax_translate", data={"text_to_translate": str(text), "translated_lang": dest_lang}).json()
            translation = r_url["translated_text"]
            origin_lang = get_lang_name(text)
            tr_dict = {"status": "success", "engine": "translate.com", "translation": translation, "dest_lang": dest_lang, "orgin_text": origin_lang, "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # My Memory
    def my_memory(self, text, dest_lang):
        try:
            source_lang = self._detect_lang(text=text)
            r_url = requests.get("https://api.mymemory.translated.net/get", params={"q": text, "langpair": f"{source_lang}|{dest_lang}"}).json()
            translation = r_url["matches"][0]["translation"]
            origin_lang = get_lang_name(source_lang)
            tr_dict = {"status": "success", "engine": "my_memory", "translation": translation, "dest_lang": dest_lang, "orgin_text": str(text), "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
