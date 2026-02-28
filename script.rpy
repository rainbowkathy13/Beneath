# 遊戲腳本位於此檔案。
define m =Character("若瑄")
define n =Character("我")
#計時器
screen general_timer(t):
    timer t action Jump("times_up")
    bar:
        value AnimatedValue(0,t, delay=t,old_value=t)
        xalign 0.5
        yalign 0.05
        xsize 800
        ysize 30

default total_time=0
default correct_score= 0

image movie_888 = Movie(play="images/888.webm", loop=True)
image movie_444 = Movie(play="images/444.webm", loop=True)

label start:
    show movie_888:
        xsize 1920 ysize 1080 
    "這是一座在2030年的島嶼，自稱為「地球小達人」的你四處飄流旅行，然後在這座島上看見了一位美麗卻憂鬱的長髮女孩。"
    m"歡迎來到這裡，我叫若瑄。"

    menu:
        "這裡是哪裡？":
            m"這裡是我的家鄉⋯⋯曾經。現在看起來很美對吧，但你要知道，「表面之下」可是藏著很多秘密的。"
        "你為何憂愁？":
            m"我很憂慮，這是顯而易見的對吧？可是，你有沒有看見⋯⋯那隱藏在「表面之下」的、小島的憂愁呢？"
        
    jump setion1

label setion1:
    $ correct_score = 0
    show movie_444:
        xsize 1920 ysize 1080 
        alpha 0.8    
    with fade          # 讓影片稍微透明一點點（露出底下的黑色）
    m"這裡是清澈與繽紛的淺海地區⋯⋯本該是這樣的。"
    m"既然你都自稱為「地球小達人」，那我就必須問問你關於這兒的一些問題了。"
    "第一題"

    show screen general_timer(40)

    python:
        Q1=["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10"]
        renpy.random.shuffle(Q1)
    jump Q1_loop

    label Q1_loop:

        if correct_score >= 3:
            hide screen general_timer
            jump setion1_finish
        python:
            if len(Q1) > 0:
                next_q = Q1.pop()
                renpy.jump(next_q)
                #如果剛才 pop 出來的是 "q3"，現在就會跳到 label q3: 開始進行遊戲
            else:
                renpy.jump(setion1_failed)
label q1:
    "哪個國家具有最大的珊瑚群？"
    menu:
        "澳門":
            "答錯了!重新答一次吧!"
            jump q1
        "澳洲":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "美國":
            "答錯了!重新答一次吧!"
            jump q1

label q2:
    "現今世界上存活著的最大的鯊魚種類是？"
    menu:
        "鯨鯊":
            $ correct_score += 1
            "答對了！那我們進行下一題!"
            jump Q1_loop
        "大白鯊":
            "答錯了!重新答一次吧!"
            jump q2
        "巨齒鯊":
            "答錯了!重新答一次吧!"
            jump q2

label q3:
    "矽藻屬於生態系統中的哪一類？"
    menu:
        "生產者":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "消費者":
            "答錯了!重新答一次吧!"
            jump q3
        "分解者":
            "答錯了!重新答一次吧!"
            jump q3

label q4:
    "哪個國家的海岸線最長？"
    menu:
        "加拿大":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "印尼":
            "答錯了!重新答一次吧!"
            jump q4
        "英國":
            "答錯了!重新答一次吧!"
            jump q4


label q5:
    "珊瑚白化的原因？"
    menu:
        "珊瑚礁死了":
            "答錯了!重新答一次吧!"
            jump q5
        "珊瑚蟲死了":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "珊瑚為了反射紅外線而變色":
            "答錯了!重新答一次吧!"
            jump q5

label q6:
    "章魚的心臟有幾顆？"
    menu:
        "是個沒心沒肺的傢伙":
            "答錯了!重新答一次吧!"
            jump q6
        "有一顆心啦，但依舊沒肺":
            "答錯了!重新答一次吧!"
            jump q6
        "三顆，還是沒肺":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
            

label q7:
    "魟魚別名？"
    menu:
        "扁魚":
            "答錯了!重新答一次吧!"
            jump q7
        "魔鬼魚":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "微笑天使":
            "答錯了!重新答一次吧!"
            jump q7

label q8:
    "海水溫度上升不會造成什麼影響？"
    menu:
        "食物鏈更加穩定":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "海平面上升":
            "答錯了!重新答一次吧!"
            jump q8
        "珊瑚白化":
            "答錯了!重新答一次吧!"
            jump q8

label q9:
    "為什麼海水溫度越來越高了？"
    menu:
        "反聖嬰現象":
            "答錯了!重新答一次吧!"
            jump q9
        "太陽快爆炸了，熱度上升":
            "答錯了!重新答一次吧!"
            jump q9
        "全球暖化":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
    

label q10:
    "珊瑚礁怎麼形成的？"
    menu:
        "珊瑚蟲的屍體堆積而成":
            "答錯了!重新答一次吧!"
            jump q10
        "珊瑚蟲的分泌物堆積而成":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q1_loop
        "它就自己長出來了":
            "答錯了!重新答一次吧!"
            jump q10

label setion1_finish:
    hide screen general_timer
    m"不錯呀，看來還是有點實力在身上的。"
    m"不過，「地球小達人」，答完這些題目之後，你有發現些什麼嗎？"
    n"（抬起頭，四處觀望，卻什麼都沒看到，回想了一下題目，還是沒理出什麼頭緒來。）"

    menu:
        "我需要發現什麼嗎？":
            m"不，沒事，沒發現也是正常的，畢竟都回復了⋯⋯。"
        "抱歉，沒發現什麼呢。怎麼了？":
            m"不，沒事，沒發現也是正常的，畢竟都回復了⋯⋯。"

    n"什麼意⋯⋯（遭到打斷）"
    m"（打斷）我帶你再更下去一點吧。"
    jump setion2

label times_up:
    hide screen general_timer
    m"時間到了！挑戰失敗。"
    jump setion1_failed

label setion1_failed:
    m"很遺憾，你還沒準備好成為地球小達人跟我一起挑戰。"
    show 66634:
        xsize 1920 ysize 1080
    with fade

    return


label setion2:
    $ correct_score = 0
    show 3589:
        xsize 1920 ysize 1080  
    with fade
    m"這裡是中水層，原本應該是沈靜與祥和的交會之處的。"
    m"「地球小達人」，你該接招了。"

    show screen general_timer(40)
    python:
        Q2=["q21","q22","q23","q24","q25","q26","q27","q28","q29","q210"]
        renpy.random.shuffle(Q2)
    jump Q2_loop

label Q2_loop:
    if correct_score >= 3:
        hide screen general_timer
        jump setion2_finish

    python:
        if len(Q2) > 7:
            next_q = Q2.pop()
            renpy.jump(next_q)
            #如果剛才 pop 出來的是 "q3"，現在就會跳到 label q3: 開始進行遊戲
        else:
            renpy.jump(setion2_finish)
label q21:
    "如何避免海洋垃圾量增加？"
    menu:
        "多使用一次性餐具":
            "答錯了!重新答一次吧!"
            jump q21
        "垃圾丟進垃圾桶":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "買包裝繁雜的物品":
            "答錯了!重新答一次吧!"
            jump q21

label q22:
    "海洋中的垃圾大約有幾成來源自陸地？"
    menu:
        "7成":
            "答錯了!重新答一次吧!"
            jump q22
        "8成":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "9成5":
            "答錯了!重新答一次吧!"
            jump q22

label q23:
    "若塑膠袋落入海裡，大約要多少年才可以完全分解？"
    menu:
        "5-10年":
            "答錯了!重新答一次吧!"
            jump q23
        "10-30年":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "50年以上":
            "答錯了!重新答一次吧!"
            jump q23

label q24:
    "中層海域中所謂的「海洋雪」是什麼？"
    menu:
        "冰晶":
            "答錯了!重新答一次吧!"
            jump q24
        "有機物":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "土壤粒":
            "答錯了!重新答一次吧!"
            jump q24

label q25:
    "鮟鱇魚為什麼可以發光？"
    menu:
        "餌球裡面有發光細菌":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "餌球裡面含有螢光素":
            "答錯了!重新答一次吧!"
            jump q25
        "餌球會吸收特定光後發出":
            "答錯了!重新答一次吧!"
            jump q25

label q26:
    "水滴魚為什麼看起來軟軟爛爛？"
    menu:
        "它本來就軟軟爛爛的":
            "答錯了!重新答一次吧!"
            jump q26
        "因為離開海之後它融化了":
            "答錯了!重新答一次吧!"
            jump q26
        "因為它是靠水壓保持身形的":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop

label q27:
    "水母如何在水中移動？"
    menu:
        "跟著水流漂浮":
            "答錯了!重新答一次吧!"
            jump q27
        "擺動觸手":
            "答錯了!重新答一次吧!"
            jump q27
        "噴出水流":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop

label q28:
    "海洋中的垃圾不會造成什麼影響？"
    menu:
        "海洋生物被勒死":
            "答錯了!重新答一次吧!"
            jump q28
        "海洋生物體內出現塑膠微粒":
            "答錯了!重新答一次吧!"
            jump q28
        "人變得更加健康":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop

label q29:
    "海膽和誰不是同一門的生物？"
    menu:
        "海葵":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "海膽":
            "答錯了!重新答一次吧!"
            jump q29
        "海百合":
            "答錯了!重新答一次吧!"
            jump q29

label q210:
    "塑膠微粒的大小限制？"
    menu:
        "5mm以下":
            "答錯了!重新答一次吧!"
            jump q210
        "25mm以下":
            "答對了！那我們進行下一題!"
            $ correct_score += 1
            jump Q2_loop
        "1mm以下":
            "答錯了!重新答一次吧!"
            jump q210

label setion2_finish:
    hide screen genera2_timer
    m"若是如此順利就答完這些題目，或許你有機會⋯⋯"
    
    menu:
        "什麼機會？":
            m"沒什麼，先看完你等一下的表現再說吧。"
        "我這叫很順利？":
            m"比起過往的那些人，你已經好多了。過往的那些人不重要，你也不必詢問他們是誰。"
        "謝謝你的稱讚啦，機會什麼的，就算了吧":
            m"是嗎？你的表現確實值得獲得一個掌聲。不過關於機會的部分，我希望你可以再考慮看看呢。"
    
    m"那麼，你的敏銳有讓你注意到什麼嗎？"
    n"（什麼都沒做，只是呆看著女子）"
    m"（歎一口氣）走吧，剩下最後一段了。"
    n"（無奈地點了點頭，跟在女子的身後）"
    jump setion3

label times_up2:
    hide screen genera2_timer
    m"時間到了！挑戰失敗。"
    jump setion2_failed

label setion2_failed:
    m"很遺憾，你還沒準備好成為地球小達人跟我一起挑戰。"
    show 66634:
        xsize 1920 ysize 1080
    with fade
    return



label setion3:
    $ correct_score = 0
    show 3456 :
        xsize 1920 ysize 1080
    with fade
    m"這裡是深海區，無盡的黑暗與靜謐將包裹著你，直到⋯⋯「它」的出現。"
    m"「地球小達人」，最後一次的表現，可要抓緊了。"

    show screen general_timer(40)
    python:
        Q3=["q31","q32","q33","q34","q35","q36","q37","q38","q39","q310"]
        renpy.random.shuffle(Q3)
    jump Q3_loop

label Q3_loop:
    if correct_score >= 3:
        hide screen general_timer
        jump setion3_finish

    python:
        if len(Q3) > 7:
            next_q = Q3.pop()
            renpy.jump(next_q)
            renpy.jump(setion3_finish)
label q31:
    "深海區的生物們因為環境幽黑，所以退化了何種感官，轉以其他感官偵測周圍？"
    menu:
        "觸覺":
            "答錯了!重新答一次吧!"
            jump q31
        "嗅覺":
            "答錯了!重新答一次吧!"
            jump q31
        "視覺":
            "答對了!"
            $ correct_score += 1
            jump Q3_loop

label q32:
    "海底蘊藏了很多的石油資源，我們是利用何種技術以取得海底下的石油資源？"
    menu:
        "挖礦":
            "答錯了!重新答一次吧!"
            jump q32
        "根本都還沒取得好嗎":
            "答錯了!重新答一次吧!"
            jump q32
        "海底鑽井":
            "答對了!"
            $ correct_score += 1
            jump Q3_loop

label q33:
    "石油的形成？"
    menu:
        "古代生物遺骸在各式反應下形成":
            "答對了!"
            $ correct_score += 1
            jump Q3_loop
        "地底本來就有這個東西":
            "答錯了!重新答一次吧!"
            jump q33
        "土壤在各式反應下形成":
            "答錯了!重新答一次吧!"
            jump q33

label q34:
    "海底鑽井對地球會有什麼影響？"
    menu:
        "磁場改變":
            "答錯了!重新答一次吧!"
            jump q34
        "土壤液化、滑坡":
            "答對了!"
            $ correct_score += 1
            jump Q3_loop
        "全球暖化":
            "答錯了!重新答一次吧!"
            jump q34

label q35:
    "深海裡的巨型幽靈水母是如何捕獵的呢？"
    menu:
        "水母就用刺絲胞刺獵物阿":
            "答錯了!重新答一次吧!"
            jump q35
        "用它的長長觸手抓住獵物":
            "答對了!"
            $ correct_score += 1
            jump Q3_loop
        "直接靠近用嘴一口悶":
            "答錯了!重新答一次吧!"
            jump q35
label q36:
    "現在已經有了海底石油井，那麼請問最早的海底石油井是在哪裡出生的？"
    menu:
        "美國":
            "答對了！"
            $ correct_score += 1
            jump Q3_loop
        "俄國":
            "答錯了!重新答一次吧!"
            jump q36
        "英國":
            "答錯了!重新答一次吧!"
            jump q36

label q37:
    "2010年，墨西哥灣曾發生了石油井故障事件，請問造成了什麼影響？"
    menu:
        "漏油":
            "答對了！"
            $ correct_score += 1
            jump Q3_loop
        "沒辦法獲取石油":
            "答錯了!重新答一次吧!"
            jump q37
        "魚被機器傷到導致暴走":
            "答錯了!重新答一次吧!"
            jump q37


label q38:
    "大王魷魚最大紀錄為？"
    menu:
        "18公尺":
            "答對了！"
            $ correct_score += 1
            jump Q3_loop
        "15公尺":
            "答錯了!重新答一次吧!"
            jump q38
        "14公尺":
            "答錯了!重新答一次吧!"
            jump q38


label q39:
    "吸血鬼烏賊令許多科學家為之著迷，請問，它身上有什麼與烏賊的不同之處？"
    menu:
        "有觸腕":
            "答錯了!重新答一次吧!"
            jump q39
        "有十隻觸手":
            "答錯了!重新答一次吧!"
            jump q39
        "不噴墨":
            "答對了！"
            $ correct_score += 1
            jump Q3_loop


label q310:
    "下列何者不是非傳統的油氣資源？"
    menu:
        "頁岩氣":
            "答錯了!重新答一次吧!"
            jump q40
        "油砂提煉物":
            "答對了！"
            $ correct_score += 1
            jump Q3_loop
        "天然氣水合物":
            "答錯了!重新答一次吧!"
            jump q40
        
label setion3_finish:
    hide screen general3_timer
    m"恭喜你，完成了專屬於你的最後一場試煉，「地球小達人」。"
    m"現在你或許很迷茫，或許早已知道故事的結局，但我想告訴你，故事還沒有結束。"
    m"但是，無論如何，我都要問你這個問題。"
    m"你願意接受這個「機會」嗎？"
    n"什麼機會？"
    m"你無需得知，你只需告訴我要或不要。"
    "面對女子的神秘「機會」邀請，你選擇？"

    menu:
        "接受":
            m"感謝你，「地球小達人」。"
            m"現在，讓我告訴你何為「機會」吧。"
            m"首先，我得先坦承，我不是個人。"
            m"我是個靈魂體，準確來說，我是個守護靈。"

        "不接受":
            m"也是，畢竟你就是這樣子性格的人呀⋯⋯我也無法強求。"
            m"只能告訴你一小部分了。"
            m"我是一個靈魂體。"
            n"⋯⋯啊！"
            m"我並非活人，這是一個隱藏在我「肉體」表面之下的真相。"
            m"親愛的「地球小達人」，我揭開了一個「表面之下」了，那是你所遺漏的線索之一。"
            m"不過⋯⋯你還記得我最一開始和你說過的話嗎？「表面之下」的部分。"
            m"我期待你可以找到那些我曾給過你的、明晃晃的暗示。"
            m"再見了，「地球小達人」。願，不再相見。"
            "女子剛講完話，一陣不知從何而來的水流便朝兩人席捲而來。女子成為了一堆氣泡，溶進了水流中，跟著消逝。"
            "水流將她的面貌與聲音完全抹去，徒留另一人呆呆地盯著虛無的前方，似乎還沒從剛剛的震撼宣言裡緩回來。"
            n"（突然聽見有奇怪的聲音。）"
            "那種聲音變得越來越大聲，逐漸逼近搖滾演唱會的等級。"
            n"（摀住耳朵）這是什麼聲音？我的耳朵要聽不到了！"
            n"先往上游吧，說不定就聽不到了。"
            "你就這樣往上游了一段，回到了中水層。"
            "沒想到映入眼簾的卻是一番恐怖的景象。"
            "海洋中竟漂出了一個破破爛爛的塑膠袋！有一就有二，吸管、破碎的瓶蓋也在上升的同時陸續出現。"
            n"這根本不是她帶我看過的海洋！"
            n"這都是幻覺而已，一定是我待在水下太久了！"
            "上升到淺海區了，可是你依舊沒有開心起來。"
            "映入眼簾的不是生機盎然的明亮海域，而是一片死氣沈沈的白化珊瑚礁群。"
            n"為什麼？為什麼啊？為什麼她一消失就變成這樣了？"
            "絕望的你抱著一絲僥倖的希望回到了小島上。"
            "但那不過是讓你更絕望而已。"
            "小島直接變成了一座垃圾山，矗立在你的眼前。"
            n"（跪地）她⋯⋯她真的是守護靈啊！"
            show 236:
                xsize 1920 ysize 1080
            with fade
       
            return

    menu:
        "我早就知道了":
            m"不愧是「地球小達人」，觀察力真好。可你為何沒有看見那些隱藏之物呢？"
        "啊？":
            m"不是自稱「地球小達人」嗎？怎麼連這個最明顯的隱藏之物都發現不了呢？"
        

    m"可別忘了我曾經說過，「表面之下」的那種話。"
    m"這是第一個。肉體的「表面之下」，藏著一個守護靈的真實身份。"
    m"其他的⋯⋯算了別耽誤時間，我直接讓你親眼感受一下吧。（彈指）"
    "彈指之後，原本靜謐的午夜區突然出現了些微刺耳的聲音。"
    m"這是鑽井的聲音，我已經使用我的力量將其壓抑了，否則你們將會聽到堪比搖滾樂演唱會現場的巨大聲響。"
    m"其他層也是這樣，中水層漂浮著垃圾的碎屑、淺海區的珊瑚白化已經無法挽救，甚至當初你看到我的那一個小島，其實也是垃圾島。"
    "說著說著，你和女子已經又回到了中水層，映入眼簾的是許多半透明的塑膠碎片和塑膠袋。"
    m"會是半透明的是因為我一樣把它壓住了，要是完全顯出來，這些會吃下肚的。（指了指身旁的魚們)"
    m"不過，我的神力已經快要枯竭了。沒過多久我就會煙消雲散，而原本被我壓制的東西們又會再度跑出來作亂。"
    m"我想要解決這個問題，所以當我遇見人時，我就會詢問他們問題，以確保他們夠格幫助我。而你，是第一個通過我測試的人。"
    m"現在，因為鑽井不能破壞，會漏油，而珊瑚白化是不可逆的，所以只能麻煩你來幫忙「淨海」了。"
    m"這就是「機會」，你願意接受這個恢復海洋的任務嗎？"
    n"我願意。"
    show 236:
        xsize 1920 ysize 1080
    with fade
 

    return

label times_up3:
    hide screen genera3_timer
    "時間到了！挑戰失敗。"
    jump setion3_failed
    

label setion3_failed:
    "很遺憾，你還沒準備好成為地球小達人跟我一起挑戰。"
    show 66634:
        xsize 1920 ysize 1080
    with fade

    return








