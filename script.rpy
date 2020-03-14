# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# Characters.

define unknown = Character("?")
define shirou = Character("Shirou")
define sakura = Character("Sakura")

# Fades

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define longflash = Fade(3.0, 0.0, 0.5, color="#fff")

# The game starts here.

label start:
# Shiro's nightmare scene

scene allblack

with fade

play music bgm43 fadeout 0.0 fadein 1.0

scene hellscape1

with fade

"-----When I came to, I was in a burning field."
"I guess there was a fire."
"The familiar town had turned to ashes and it looked like the remains of a bettlefield from a movie."
"-----But that didn't last long either"
"The fire had died down by the time the sun rose."
"The tall wall of flame had shortened, and most of the buildings had falled."
"...It felt strange, being the only thing in that place that still had its original form."
"I was the only one still alive around here."
"I must have been really luck, or my house was built in a very lucky spot."
"I don't know which it was, but the point is, I was the only one left alive."
"I felt that since I survived, I should live on."
"I started Walking aimlessly, because I thought it would be dangerous to stay there."
"I wasn't really concerned about getting burned up like the people lying around me."
"...Probably because, over and above not wanting to be like them, I had a stronger feeling in my mind."

with flash

"But still, I had no hope."
"It was already a wonder I was still alive, so I couldn't expect to be saved."
"I won't survive."
"Whatever happens, I won't be able to escape from this red world."
"It was such an absolute hell that even a small child could understand it."

scene sky1

with fade

"And I collapsed."
"Was it because there was no air? Was it because no function was left in my body?"
"Anyway, I collaspsed and stared up at the clouded sky."
"Everything around me was burned up and I could see many shriveled people."
"The dark clouds loomed overhead, telling me it would ran soon."
"...That's good. The fire will be put out once it rains."
"In the end, I sighed deeply and looked up at the sky."
"I say to myself that it hurts."
"A say so on behalf of all people who couldn't even say so."

scene allwhite

with longflash

stop music fadeout 2.0

"-----That was ten years ago."
"After that, I was miraculously saved."
"My body survived."
"But I think all the other things about me burned up and were reduced to ashes."
"If you take away a child's parents, home, and all such things, there's nothing left for him."
"That's why there was only my body."
"I think it's a simple story."
"In other words, In order to let my body live..."
"My heart died."

scene allblack

with fade

play music bgm42 fadeout 0.0 fadein 2.0

"-------------------I'm dreaming."

scene allwhite

with squares

unknown "--------Huh!?"
"I squint my eyes at the white light."
unknown "So bright."
"It was just light enterying my eyes when I woke up, but I'm not used to it."
"I probably didn't even understand what the bright light meant."

scene hospital1

with dissolve

unknown "Huh?"
"When my eyes focus, I'm surprised."
"I'm lying on an unfamiliar bed, in an unfamiliar room."
"I'm surprised, but the room is so white and clean that I feel safe."
unknown "...Where am I?"
"I look around."
"The room is big and there are many beds."
"A person is in each bed, and everyone seems to be hurt."
"But nothing feels ill in this room."
"Everyone who's hurt is someone who was saved."
"-------"
"I relax and let my eyes wander."

scene sky2

with dissolve

"-------Outside the window,"
"The bright blue sky was unbelievably beautiful."

scene allwhite

with blinds

scene hospital1

with dissolve

"After a few days, I finally understood."
"I could clearly remember what had happened in the past few days."
"Even so, I was no different from a newborn baby."
"Not just a metaphor, it was close to the truth."
"anyway, it was a terrible fire."
"I had been saved from it, was in the hospital with my body wrapped in bandages, and my parents were gone."
"I didn't get the situation, but I vaguely understood that I was alone."
"I think I understood quickly."
"...Well, there was nothing but children in similar situations around me, so all I could do was absorb the fact."
"-----And after that."
"That man came, right when I was beginning to worry what would happen to me next."
"He came on the day my bandages were taken off and I was able to eat without help."
"Wrinkled coat and uncombed hair."
"The man, a bit younger than the doctor, felt more like a big brother than a father."
unknown "Hello. You must be Shirou-kun."
"A smile that seems to melt into the white sunlight."
"I think it was a suspicious voice, but a very kind voice."
unknown "I'll ask you directly. Which would you prefer? To go to an orphanage, or to be adopted by this man you've never seen before?"
"That man was saying he could adopt me."
"When I was asked him if he was a relative of mine, he said he was just a stranger."
"...He looked like an unreliable guy with no future."
"But it made no difference, as I knew nothing about either one: him or the orphanage."
"So I decided to go with him."
unknown "I see, that's good. Get ready quickly, then. You should get used to your new place as fast as you can."
"The guy quickly started packing my stuff."
"His packing wasn't very good, even in the eyes of a child."
"Then, after making a big mess..."
unknown "Oh, I forgot to mention something important."
unknown "I have to tell you one thing before you come with me."
unknown "Is that okay?"
"He turns to me lightheartedly and says,"
unknown "Yeah."
unknown "To start off with, I'm a sorcerer."
"He says it in a serious, exaggerated tone."
"It happened in an instant."
"Come to think of it now, I was really a child back then."
"I automatically believed those words."
shirou "-------Wow, you're awesome."
"I guess I said so with bright eyes."

scene allblack

with fade

"Since that time, I became his child."
"Actually, I don't remember what I said back then."
"But my father would always talk about that day."
"He would remember and retell the story again and again."
"So for my father, Emiya Kiritsugu, that might have been the happiest day of his life."
"...So."
"I guess it was strange for my father to tell me that he was a sorcerer, but I was strange for admiring that."
"And thus, I became an adtopted sone, and my land name became Emiya."
"Emiya Shirou."
"When I said my name, I was really proud of having the same last name as Kiritsugu."

scene allwhite

with longflash

stop music fadeout 2.0

"...I'm dreaming."
"A story from my childhood."
"It was when I was finally convinced my father to make me his student, so it must have been about eight years ago."
"When I was old enough to stay at home by myself, Kiritsugu started to leave the house on a regular basis."
"He would say in his normal tone that he would -travel the world-, and actually act on these words."
"That's how it was after that."
"It was normal for him to leave the house empty for a month, and he sometimes wouldn't come home for half a year."
"The Emiya house is a big japanese-style house, and Kiritsugu and I were the only ones living there."
"I was perplexed in this house at times, as it was too big for a child."
"But still, I liked my life here."
"Emiya Kiritsugu would come home from his journeys and tell me lots of stories like a child."
"And the child who shared his last name would be at home waiting for those stories."
"I was always alone in the house, but that loneliness would all fade with the stories he brought back."
"------The father who was always chasing his dreams like a kid."
"His attitude was astounding, but he always seemed dazzling to me."
"That might be why I wanted to be like him someday."
"Well, on top of that..."
"Looking at my ever-dreaming father, I felt I should become reliable myself-----------"

scene allblack

with fade

scene chaptercard1

with wiperight

pause

scene allblack

with fade

pause 0.5

play sound dooropening

"...I head a sound."

"I hear an old, heavy, rusty sound as the door opens."

scene allwhite

with fade

pause 0.1

scene allblack

with fade

"Light enters the dark shed."
shirou "Uh."
"My mind, waking up..."
unknown "Senpai, are you awake?"
"...Feels the cold  air and the approaching footsteps."

play music bgm03

scene allwhite

with fade

scene sakura1

with dissolve

shirou "...Mm. Good Morning, Sakura."
sakura "Ah, yes. Good morning, Senpai."
"Sakura smiles and nods as if accustomed to this situation."
sakura "Senpai, it's morning already. You have some more time, but Fujimura-Sensai will get mad if you stay asleep here."
shirou "Oh... you're right. Thanks for coming to wake me up."
sakura "It's no problem at all. You're always up so early."
sakura "I can only come and wake you up like this occasionally."
"...?"
"Sakura seems more upbeat than usual today as if she's happy about something."
shirou "...Really? I think you wake me up quite often."
"Though, Fuji-Nee always hits me to wake me up, so I'd rather you wake me up... Well, I'll try harder next time."
"...I answer her with a sleepy head."
"I don't know what I'm saying with my mind not fully awake."
"Alright. But I'm happier when you don't try."
"Sakura is giggling."
"...Gah, I guess my head was still dozing and I said something weird."
shirou "Give me a second, I'll wake up."
"The cold outdoor air helps in situations like this."
"The chilld works well to beat the sleepiness out of my head."
"...In front of me is Matou Sakura, my junior at school."
"This place is a shed behind my house, and the time is siz six o'clock."
sakura "...Senpai?"
shirou "Yeah, I'm awake now. Sorry, I guess I did it again."
shirou "I have to help you cook breakfast too."
sakura "It's fine. You were up late last night again, right? So you should take your time in the morning. I'll get breakfast ready."
"Sakura says so in a happy tone."
"...It's unusual. Sakura really seems to be in a good mood this morning."
shirou "I can't let you do that. I'll get up right now, so let's go to the kitchen together."

scene allblack

with fade

scene shed1

with blinds

show sakura32 at center

with dissolve

shirou "Alright, I'm all set. Let's go, Sakura."

hide sakura32

show sakura81 at center

with dissolve

sakura "Ah... um, Senpai..."
shirou "Hm? What, is something wrong?"
sakura "No, it's nothing, but... you I think you should change before you go back to the house."

hide sakura81

show sakura82 at center

with dissolve

shirou "Oh."

"That said, I look down at myself."
"I fell asleep while I was working, so I'm still wearing my overalls."
"Being my work clothes, they're pretty dirty. I can't imagine what Fuji-Nee would say to me if I went into the house like this."
shirou "Ugh... I guess I'm not awake yet. I'm a bit out of it this morning."

hide sakura82

show sakura48 at center

with dissolve

sakura "That could be. So you rest here for a bit and I'll take care of breakfast. And you know, if you keep this place a mess, Fujimura-Sensei will get mad at you."

shirou "...You're right. I'll go after I get changed. You go on ahead."

hide sakura48

show sakura66 at center

with dissolve

sakura "Yes, I'll be waiting, Senpai."

hide sakura66

with blinds

"Sakura leaves."









"End of Dev."
# This ends the game.

return
