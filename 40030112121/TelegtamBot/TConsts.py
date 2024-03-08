__token  'Your_Own_Telegram_Token'

dictionary = {"intense": [
    {"tag": "sayHelloEng",
     "patterns": ["hello", "hi", "hey", "what's up", "greeting"],
     "response": ["Hello My Friend!", "What A Nice Pleasure", "Hellooo!!", "What Can I Do For You?"]},

    {"tag": "goodbyeEng",
     "patterns": ["bye", "goodbye", "see you later", "see you", "have a good day"],
     "response": ["See You Later!", "Goodbye!", "Bye Bye!!"]},

    {"tag": "sayHelloFa",
     "patterns": ["سلام", "وقت بخیر", "هی", "هوی", "اهای"],
     "response": ["سلام وقت بخیر!", "سلام علیکم و رحمت الله و برکاته", "سلام سلام!!", "سلاااامم"]},

    {"tag": "goodbyeFa",
     "patterns": ["بای", "خداحافظ", "خدافظ", "خدانگدار", "فعلا"],
     "response": ["در پناه حق مانا باشی!", "بازم به ما سر بزن", "بای بای!!", "خداحافظ"]},

    {"tag": "greetingsFa",
     "patterns": ["حالت خوبه", "چطوری", "حالت چطوره", "خوبی", "سلامتی"],
     "response": ["من خوبم! خودت چطوری؟", "من که عالیم تو چی؟", "ای بلا!!! حالا حال من مهم شد؟", "فدات شم خوبم"]},

    {"tag": "greetingBackNegativeFa",
     "patterns": ["خوب نیستم", "بد", "جالب نیست", "هعی"],
     "response": ["واااای بلا به دور باشه!!", "اینجوری نمیشه کهههه", "جمع کن خودتو",
                  "حیف صورت به این قشنگی نیست نخنده؟", "خودمونیم، موقع حال بدیات هم جذابیااا",
                  "اخ اخ اخ میگم چرا امروز مثل غروب جمعه است پس بخاطر تو بود"]},

    {"tag": "greetingBackPlusFa",
     "patterns": ["خوبم", "خداروشکر", "عالیم", "حمدلله"],
     "response": ["خب خداروشکر که خوبی", "همیشه سلامت و شاد باشی", "ماشالله ماشالله"]},

    {"tag": "BatterySaverBot",
     "patterns": ["نجات دهنده باطری", "باطری", "نجات باطری", "باطری بازی",],
     "response": ["حله بریم تو کارش", "رو چشمم", "بریم ربات باطری نجات ده", "حله چشاته"]
    },
]}