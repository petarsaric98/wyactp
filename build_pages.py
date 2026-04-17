import json, re

# ─────────────────────────────────────────────────────────────────────────────
# HELPER HTML BLOCKS
# ─────────────────────────────────────────────────────────────────────────────

def bullets(items):
    lis = ''.join(f'<li class="flex gap-3"><span class="text-cyan-500 mt-1 shrink-0">›</span><span>{item}</span></li>' for item in items)
    return f'<ul class="space-y-3 text-slate-600 dark:text-slate-400 text-base leading-relaxed mb-8">{lis}</ul>'

def concept_grid(cards):
    inner = ''
    for icon, title, desc in cards:
        inner += f'''<div class="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 rounded-2xl p-6 hover:shadow-lg hover:border-cyan-400/50 transition-all duration-300">
            <div class="text-3xl mb-3">{icon}</div>
            <h5 class="font-extrabold text-slate-900 dark:text-white text-base mb-2">{title}</h5>
            <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">{desc}</p>
        </div>'''
    return f'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 my-10" data-aos="fade-up">{inner}</div>'

def compare_table(headers, rows):
    ths = ''.join(f'<th class="text-left text-xs font-black uppercase tracking-widest text-cyan-400 pb-3 pr-6">{h}</th>' for h in headers)
    trs = ''
    for row in rows:
        tds = ''.join(f'<td class="py-3 pr-6 text-sm text-blue-100/80 align-top border-t border-white/10">{c}</td>' for c in row)
        trs += f'<tr>{tds}</tr>'
    return f'''<div class="my-10 rounded-2xl overflow-hidden bg-gradient-to-br from-blue-900 to-slate-900 border border-cyan-500/20 shadow-xl" data-aos="fade-up">
        <div class="px-8 py-4 border-b border-white/10"><span class="text-xs font-black tracking-widest text-cyan-400 uppercase">Comparison</span></div>
        <div class="overflow-x-auto px-8 py-6">
            <table class="w-full"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>
        </div>
    </div>'''

def case_study(title, body_html):
    return f'''<div class="my-12 rounded-3xl overflow-hidden bg-gradient-to-br from-blue-900 via-blue-950 to-slate-900 border border-cyan-500/20 shadow-2xl" data-aos="fade-up">
        <div class="px-8 py-4 border-b border-white/10 flex items-center gap-3">
            <span class="text-xs font-black tracking-widest text-cyan-400 uppercase">Deep Dive</span>
        </div>
        <div class="p-8 md:p-10 text-white space-y-4">
            <h4 class="text-2xl font-black text-white mb-4 leading-tight">{title}</h4>
            <div class="text-blue-100/80 leading-relaxed text-base space-y-4">{body_html}</div>
        </div>
    </div>'''

def callout(emoji, title, text):
    return f'''<div class="my-8 flex gap-5 bg-cyan-50 dark:bg-slate-800/50 border border-cyan-200 dark:border-cyan-900 rounded-2xl p-6" data-aos="fade-up">
        <div class="text-3xl shrink-0 mt-0.5">{emoji}</div>
        <div>
            <p class="font-black text-blue-900 dark:text-cyan-300 text-base mb-1">{title}</p>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">{text}</p>
        </div>
    </div>'''

def blockquote(text, attrib):
    return f'''<blockquote class="relative my-10 pl-6 py-4 border-l-4 border-cyan-500 dark:border-cyan-400" data-aos="zoom-in">
        <p class="text-xl italic font-semibold text-slate-700 dark:text-slate-200 leading-relaxed mb-2">"{text}"</p>
        <cite class="text-sm text-slate-400 font-medium not-italic">— {attrib}</cite>
    </blockquote>'''

def section(title):
    return f'<h3 class="text-xs font-black tracking-[0.2em] text-cyan-600 dark:text-cyan-400 uppercase mt-16 mb-4" data-aos="fade-up">{title}</h3>'

def h2(text):
    return f'<h2 class="text-3xl font-black text-slate-900 dark:text-white mt-6 mb-5 leading-tight" data-aos="fade-up">{text}</h2>'

def lead(text):
    return f'<p class="text-2xl font-bold text-slate-700 dark:text-slate-200 leading-snug mb-12 pb-10 border-b-2 border-slate-100 dark:border-slate-800" data-aos="fade-up">{text}</p>'

def para(text):
    return f'<p class="text-base text-slate-600 dark:text-slate-400 leading-relaxed mb-6 max-w-3xl" data-aos="fade-up">{text}</p>'

def hero_img(module_idx, caption):
    return f'''<figure class="my-14 rounded-3xl overflow-hidden shadow-2xl group relative" data-aos="zoom-in">
        <img src="inline_m{module_idx}.png" alt="Concept illustration" class="w-full object-cover max-h-[360px] transition-transform duration-700 group-hover:scale-[1.03]"/>
        <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-blue-950/90 to-transparent px-8 py-8">
            <p class="text-white/80 text-sm font-semibold tracking-wide">{caption}</p>
        </div>
    </figure>'''

def youtube_embed(video_id, caption):
    return f'''<figure class="my-12 rounded-3xl overflow-hidden shadow-2xl border border-slate-200 dark:border-slate-700" data-aos="zoom-in">
        <div class="relative" style="padding-top:56.25%">
            <iframe class="absolute inset-0 w-full h-full" src="https://www.youtube.com/embed/{video_id}" title="{caption}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <figcaption class="px-6 py-4 bg-slate-50 dark:bg-slate-800 text-sm text-slate-500 dark:text-slate-400 font-medium">{caption}</figcaption>
    </figure>'''

def divider():
    return '<hr class="my-14 border-slate-100 dark:border-slate-800"/>'

def pdf_download(filename, label):
    return f'''<div class="mt-14 mb-8 text-center border-t border-slate-200 dark:border-slate-800 pt-14" data-aos="fade-up">
        <a href="lectures/{filename}" download class="inline-flex items-center gap-3 px-8 py-4 bg-gradient-to-r from-blue-900 to-blue-950 hover:from-cyan-700 hover:to-blue-900 text-white font-bold rounded-2xl transition-all duration-300 hover:shadow-xl hover:shadow-cyan-900/40 hover:-translate-y-1 border border-blue-800/50">
            <span class="text-2xl">📥</span> 
            <span>{label}</span>
            <span class="ml-2 text-cyan-400 font-black text-lg">↓</span>
        </a>
    </div>'''

# ─────────────────────────────────────────────────────────────────────────────
# MODULE CONTENT
# ─────────────────────────────────────────────────────────────────────────────

def module1():
    return ''.join([
        lead("The World Youth Alliance was born in a UN conference room. Its founding question hasn't changed: does the state <em>give</em> human dignity — or does it merely <em>recognize</em> it?"),

        section("Part I — Before 1999"),
        h2("How Geopolitics Targeted the Human Person"),
        para("In 1974, Secretary of State Henry Kissinger drafted <strong>National Security Memorandum 200 (NSSM 200)</strong>. His argument: population growth in developing nations threatened American power. The solution — tie U.S. foreign aid to population reduction programs in 13 key countries."),
        bullets([
            "<strong>The cynical contradiction:</strong> Britain's Royal Commission found population decline <em>bad</em> for Britain's economy — but recommended it for British colonies to prevent them from growing too powerful.",
            "<strong>13 target nations:</strong> India, Bangladesh, Pakistan, Indonesia, Thailand, Philippines, Turkey, Nigeria, Egypt, Ethiopia, Mexico, Brazil, Colombia.",
            "<strong>The strategy:</strong> Repackage geopolitical control as humanitarian aid and 'individual rights' to avoid looking like foreign imposition.",
        ]),

        case_study("🏛️ 1999: Cairo+5 — The Birth of WYA",
            '''<p>At the 5-year review of the International Conference on Population and Development, 32 handpicked youth took the floor. They claimed to represent all <strong class="text-cyan-300">3 billion</strong> of the world's young people. Their demands:</p>
            <ul class="list-none space-y-2 my-4">
                <li>→ Abortion as an international human right</li>
                <li>→ Deletion of parental rights</li>
                <li>→ Sexual and reproductive services for children from age 10</li>
            </ul>
            <p>They refused to discuss clean water, education, or sanitation. <strong class="text-cyan-300">Anna Halpine</strong>, then 21, watched this unfold and acted. She printed a pink flyer stating: <em>"These youth don't speak for us."</em> She walked onto the conference floor and distributed it.</p>
            <p>The response was immediate. Delegates from developing nations crowded around her. "You must have a permanent presence at the UN," they told her. "Come to our countries. Work with our young people." The <strong class="text-cyan-300">World Youth Alliance</strong> was founded.</p>'''),

        divider(),

        section("Part II — Human Dignity and Totalitarianism"),
        h2("The Thinkers Who Shaped WYA"),
        para("At Beijing +5, the U.S. delegation proposed a chilling reversal: <em>\"Human rights grant human dignity.\"</em> If accepted, human dignity would become a gift of the state — and what the state gives, it can take away. WYA rejected this. But they drew on four key intellectual traditions to explain why."),

        hero_img(1, "Living in Truth: The foundation of individual resistance."),

        concept_grid([
            ("✊", "Václav Havel", "<em>The Power of the Powerless</em> — resistance is not political but cultural. Living 'within the truth' daily, in small acts, is what threatens regimes built on lies."),
            ("✝️", "Pope John Paul II", "<em>Centesimus Annus</em> (1991) — Communism didn't collapse for economic reasons. It collapsed because it was built on a lie about the human person."),
            ("🧠", "Viktor Frankl", "Auschwitz survivor and psychiatrist. Even in a death camp, man retains one freedom: the choice of his attitude. Dignity cannot be stripped — only surrendered."),
            ("⚖️", "Jacques Maritain", "A drafter of the Universal Declaration of Human Rights. Observed: people of opposing ideologies can agree on a <em>list</em> of rights — but they disagree on the <em>why</em>, the fundamental nature of the person."),
        ]),

        blockquote("Communism collapsed not for political or economic failure, but because it was based on a lie about the human person.", "Pope John Paul II, <em>Centesimus Annus</em>"),

        divider(),

        section("Part III — The WYA Charter"),
        h2("Core Convictions"),
        bullets([
            "<strong>Intrinsic Dignity:</strong> Possessed from conception to natural death. It cannot be granted or rescinded by any government, institution, or majority vote.",
            "<strong>Right to Life:</strong> The inalienable foundation of a free and just society. The state has an obligation to protect it — in law and in culture.",
            "<strong>The Family:</strong> The fundamental unit of society. The primary place where individuals learn freedom, solidarity, and obligation to others.",
            "<strong>Integral Development:</strong> Authentic progress is physical, spiritual, mental, and emotional — not merely economic.",
            "<strong>Culture as Resistance:</strong> Ideas shape societies. WYA cites composers like Paderewski and Shostakovich — whose art became acts of resistance in 'societies of lies.'",
        ]),
        callout("💡", "The Key Reversal", "WYA insists that dignity is NOT the product of rights. Rights are the product of dignity. Get this wrong and every human rights framework collapses."),

        divider(),

        section("Part IV — The Clash of Values"),
        h2("Two Visions in the Same Room"),
        para("In 1999, two groups stood in the same UN conference hall with radically different answers to the question: <em>What does a young person need?</em> Their incompatibility was total — not a matter of degree, but of first principles."),

        f'''<div class="my-10 grid grid-cols-1 md:grid-cols-2 gap-0 rounded-3xl overflow-hidden border border-slate-200 dark:border-slate-700 shadow-xl" data-aos="fade-up">
            <!-- Left: UNFPA Youth Caucus -->
            <div class="bg-slate-900 p-8 md:p-10">
                <div class="inline-block px-3 py-1 bg-red-900/50 text-red-400 rounded-full text-xs font-black tracking-widest uppercase mb-5 border border-red-800/50">UNFPA Youth Caucus — 1999</div>
                <p class="text-slate-400 text-sm leading-relaxed mb-6">32 handpicked youth, claiming to represent 3 billion. Their three demands:</p>
                <div class="space-y-4">
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-red-900/40 border border-red-700/50 flex items-center justify-center text-red-500 text-sm font-black shrink-0">1</span>
                        <div>
                            <p class="text-white font-bold text-sm">Abortion as a Human Right</p>
                            <p class="text-slate-500 text-xs mt-1">Codify abortion as an internationally protected right, removing any state restrictions.</p>
                        </div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-red-900/40 border border-red-700/50 flex items-center justify-center text-red-500 text-sm font-black shrink-0">2</span>
                        <div>
                            <p class="text-white font-bold text-sm">Deletion of Parental Rights</p>
                            <p class="text-slate-500 text-xs mt-1">Remove the legal authority of parents to direct the moral and religious education of their children.</p>
                        </div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-red-900/40 border border-red-700/50 flex items-center justify-center text-red-500 text-sm font-black shrink-0">3</span>
                        <div>
                            <p class="text-white font-bold text-sm">Sexual Rights for Children from Age 10</p>
                            <p class="text-slate-500 text-xs mt-1">Sexual and reproductive rights and services granted to children as young as 10, without parental consent.</p>
                        </div>
                    </div>
                </div>
                <p class="mt-6 text-slate-600 text-xs italic">Clean water, education, and sanitation were not mentioned once.</p>
            </div>
            <!-- Right: WYA Charter -->
            <div class="bg-gradient-to-br from-blue-900 to-blue-950 p-8 md:p-10">
                <div class="inline-block px-3 py-1 bg-cyan-500/20 text-cyan-300 rounded-full text-xs font-black tracking-widest uppercase mb-5 border border-cyan-500/30">WYA Charter — Response</div>
                <p class="text-blue-200/70 text-sm leading-relaxed mb-6">Founded on three irreversible affirmations about the human person:</p>
                <div class="space-y-4">
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 text-sm font-black shrink-0">1</span>
                        <div>
                            <p class="text-white font-bold text-sm">Life from Conception to Natural Death</p>
                            <p class="text-blue-300/70 text-xs mt-1">Every human being possesses inalienable dignity from the moment of conception through natural death. No state or institution can define otherwise.</p>
                        </div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 text-sm font-black shrink-0">2</span>
                        <div>
                            <p class="text-white font-bold text-sm">The Family as the Foundational Unit</p>
                            <p class="text-blue-300/70 text-xs mt-1">The family — with parents as primary educators — is the fundamental unit of human society. It is the first school of freedom, solidarity, and love.</p>
                        </div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="w-8 h-8 rounded-full bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 text-sm font-black shrink-0">3</span>
                        <div>
                            <p class="text-white font-bold text-sm">Integral Development of the Person</p>
                            <p class="text-blue-300/70 text-xs mt-1">Authentic human progress is physical, spiritual, mental, and emotional — not reducible to economic metrics or a single dimension of rights.</p>
                        </div>
                    </div>
                </div>
                <p class="mt-6 text-cyan-400/60 text-xs italic">"These rights are already protected by the Universal Declaration of Human Rights."</p>
            </div>
        </div>''',

        callout("🎯", "Why the Distinction Matters", "This is not a debate about policy details. The two sides have different understandings of what a human person <em>is</em>. If you accept that the state or an international body can define the person, every one of the UNFPA's three demands becomes logically consistent. If you insist dignity is intrinsic, all three collapse."),
        pdf_download("WYAlecture_1.pdf", "Download Full Lecture 1 (PDF)"),
    ])


def module2():
    return ''.join([
        lead("Three thinkers. Three angles on the same question: What does it mean to be fully human — and what happens when we get the answer wrong?"),

        section("Text 1 — Charles Malik"),
        h2("Struggle, Care, and the Condition of Being Thrown"),

        # Malik profile bio card
        '''<div class="my-8 flex flex-col sm:flex-row gap-6 bg-slate-800/40 border border-slate-700 rounded-2xl p-6" data-aos="fade-up">
            <div class="flex-shrink-0">
                <div class="w-20 h-20 rounded-2xl bg-gradient-to-br from-blue-800 to-blue-950 border border-cyan-700/40 flex items-center justify-center text-4xl shadow-xl">🎓</div>
            </div>
            <div>
                <p class="text-xs font-black tracking-widest text-cyan-400 uppercase mb-1">Who Was He?</p>
                <p class="text-white font-black text-lg mb-2">Charles Malik (1906–1987)</p>
                <p class="text-slate-400 text-sm leading-relaxed">Lebanese Christian philosopher and statesman. Principal drafter of the <strong class="text-slate-300">Universal Declaration of Human Rights</strong> (1948). President of the <strong class="text-slate-300">UN General Assembly</strong> (1958–59). From 1945 to 1959 — fourteen continuous years — he was Lebanon's chief representative to the United Nations, present from the founding gavel in San Francisco through the Cold War's most dangerous years.</p>
            </div>
        </div>''',

        para("Malik opens his essay not with politics or law — but with an ontological shock: <em>we are thrown into this world of struggle and care.</em> We didn't choose our world, our bodies, our era, or our condition. And yet, here we are, minds already full of problems and concerns, before we've even asked why."),

        bullets([
            "<strong>'Fated' to be Free:</strong> 'Fate' in Malik's sense has nothing to do with fatalism. Man is <em>fated to be responsible</em> — doomed to choose. Any appeal to kismet or external forces to escape a decision is, to Malik, utterly foreign to human reality.",
            "<strong>The anguish of decision:</strong> Every choice involves the 'ruthless destruction of possibilities.' To say yes to one path is to categorically close off all others — forever. That weight is inseparable from being human.",
            "<strong>Heidegger's insight, grounded differently:</strong> Malik acknowledges he's building on Heidegger's notion of 'Thrownness' (Geworfenheit) and 'Care' (Sorge) — but insists Heidegger was drawing on the Judeo-Christian tradition while refusing to admit it.",
            "<strong>The Psalms as ontology:</strong> Malik argues the Book of Psalms is the greatest fundamental ontological-existential work ever written — portraying every possible human mood and the struggle with the 'ground of existence' in a way no philosophy textbook can match.",
        ]),

        # The Diplomat Smile — pull quote style feature block
        '''<div class="my-12 rounded-3xl overflow-hidden border border-amber-500/20 shadow-2xl bg-gradient-to-br from-amber-950/60 to-slate-900" data-aos="fade-up">
            <div class="px-8 py-4 border-b border-amber-500/20">
                <span class="text-xs font-black tracking-widest text-amber-400 uppercase">The Observation That Changes Everything</span>
            </div>
            <div class="p-8 md:p-10 flex flex-col md:flex-row gap-8 items-start">
                <div class="text-6xl shrink-0 md:mt-2">😏</div>
                <div>
                    <h4 class="text-2xl font-black text-white mb-4 leading-tight">Why Diplomats Smile</h4>
                    <p class="text-amber-100/80 text-lg leading-relaxed mb-4">Malik spent fourteen years in the UN watching diplomats negotiate peace between nations. And he came to a strange, subversive conclusion:</p>
                    <blockquote class="border-l-4 border-amber-500 pl-6 py-2 mb-4">
                        <p class="text-white text-xl italic font-semibold leading-relaxed">"That is why most diplomats smile: it is not hypocrisy — it is a sort of metaphysical awareness of the human impossibility of their task."</p>
                    </blockquote>
                    <p class="text-amber-100/70 text-base leading-relaxed">The diplomat smiles not because they are cynical or dishonest — but because they understand, at some deep level, the fundamental absurdity of trying to create outer peace while inner peace remains unachieved. It is the smile of someone who sees the paradox: <em>the blind leading the blind, the physician who cannot heal himself, trying to heal the world.</em></p>
                </div>
            </div>
        </div>''',

        para("This insight leads Malik to his sharpest critique: before peace-making can work, the peacemaker must <em>put his own spiritual house in order.</em> A civilization that has cut itself off from its own spiritual roots — that is too proud or embarrassed to acknowledge its ground — cannot actually make or sustain peace. It can only perform it."),

        concept_grid([
            ("🌀", "Existential Pride", "Malik's term for the core modern failure: man 'proudly refuses to acknowledge his ground, his origin, his dependence.' While this radical pride dominates an entire culture, he asks, can anyone 'with a broken and contrite heart' really expect peace?"),
            ("❤️‍🔥", "Augustine's Self-Love", "Malik invokes Augustine: if <em>self-love</em> is the ultimate governing principle, peace achieved through diplomacy is always a patch job, not a cure. The deeper struggle — coming to terms with one's own nature — is perpetually postponed."),
            ("🏛️", "The UN's Limit", "Malik was <em>inside</em> the UN for 14 years. His verdict: 'international peace and security' — the absence of armed conflict — is necessary but radically insufficient. It has nothing to say about whether the humans agreeing to coexist are themselves at peace with their own being."),
        ]),

        blockquote("There is something at once necessary and noble, and false and sad, about the struggle for peace.", "Charles Malik"),

        divider(),

        section("Text 2 — Martin Buber"),
        h2("I-You and I-It: The Two Worlds"),
        para("Jewish philosopher <strong>Martin Buber</strong> argues that human experience is divided into two fundamentally different modes of relating — not just to people, but to everything."),

        compare_table(
            ["Dimension", "I-You", "I-It"],
            [
                ["How you relate", "With your whole being; unmediated", "Perceiving, sensing, using; partial"],
                ["What you encounter", "A real presence — the You", "An object — classifiable, past"],
                ["Time quality", "Fulfilled present", "Exists only in the past"],
                ["Key element", "Relation", "Experience"],
                ["What it produces", "Love, responsibility", "Information, utility"],
            ]
        ),

        bullets([
            "<strong>Beyond Human Relation:</strong> Buber explicitly notes that an I-You relationship isn't just for humans. We can encounter a tree, an animal, or nature itself as a 'You' if we approach it with our whole being instead of merely observing it as an object.",
            "<strong>The Eternal You:</strong> In every genuine 'You,' Buber argues, a person reaches toward the <em>Eternal You</em> — God, the ultimate transcendent presence that cannot be reduced to an 'It'.",
            "<strong>Love is not a feeling:</strong> 'Feelings dwell in man; man dwells in his love.' Love is the responsibility of an I for a You — a cosmic force.",
            "<strong>The danger of objectification:</strong> A world lived entirely in 'I-It' mode treats everything — including people — as objects to be used and discarded.",
        ]),
        callout("🔍", "The Crisis of Modernity", "Our digital, transactional world aggressively pushes us toward I-It relations. Buber's insight: whenever you treat a person as a means to your end, you lose a piece of your own humanity."),

        hero_img(2, "The Missing Chest: The connection between intellect and sentiment."),

        divider(),

        section("Text 3 — C.S. Lewis"),
        h2("Men Without Chests"),
        para("<strong>C.S. Lewis</strong> opens <em>The Abolition of Man</em> (1943) by analyzing a school textbook that seems harmless — but is quietly teaching students that no value judgment is ever really about the world. It's only ever about <em>your feelings</em>."),

        f'''<div class="my-12 rounded-3xl overflow-hidden border border-slate-200 dark:border-slate-700 shadow-xl" data-aos="fade-up">
            <div class="px-8 py-4 border-b border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/50">
                <span class="text-xs font-black tracking-widest text-cyan-600 dark:text-cyan-400 uppercase">Three Case Studies in "Debunking" Reality</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-slate-200 dark:divide-slate-700">
                <!-- Example 1 -->
                <div class="bg-white dark:bg-slate-800 p-8">
                    <div class="text-4xl mb-4">🌊</div>
                    <h4 class="font-black text-slate-900 dark:text-white mb-3">The Waterfall</h4>
                    <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed mb-4">A textbook claims that calling a waterfall "sublime" only means "I have sublime feelings."</p>
                    <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-100 dark:border-red-800/30">
                        <p class="text-red-700 dark:text-red-400 text-sm font-semibold">The Result: All values become mere autobiography. Nothing is objectively beautiful.</p>
                    </div>
                </div>
                <!-- Example 2 -->
                <div class="bg-white dark:bg-slate-800 p-8">
                    <div class="text-4xl mb-4">🚢</div>
                    <h4 class="font-black text-slate-900 dark:text-white mb-3">The Ocean Cruise</h4>
                    <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed mb-4">A textbook mocks an ad for a cruise to inoculate the student against feeling awe for the ocean itself.</p>
                    <div class="bg-cyan-50 dark:bg-cyan-900/20 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/30">
                        <p class="text-cyan-700 dark:text-cyan-400 text-sm font-semibold">The Result: It creates the <strong class="text-cyan-800 dark:text-cyan-300">"Trousered Ape"</strong> — a person who can only see the Atlantic as "millions of tons of cold salt water."</p>
                    </div>
                </div>
                <!-- Example 3 -->
                <div class="bg-white dark:bg-slate-800 p-8">
                    <div class="text-4xl mb-4">🐎</div>
                    <h4 class="font-black text-slate-900 dark:text-white mb-3">The Willing Horse</h4>
                    <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed mb-4">A text mocks a passage praising horses as the "willing servants" of early colonists, wiping out prehistoric piety.</p>
                    <div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-xl border border-blue-100 dark:border-blue-800/30">
                        <p class="text-blue-700 dark:text-blue-400 text-sm font-semibold">The Result: Man's noble relationship with nature is severed, replaced by cold utility.</p>
                    </div>
                </div>
            </div>
            <div class="p-8 bg-slate-50 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-700">
                <p class="text-slate-600 dark:text-slate-400 text-sm italic">Lewis's counter: <strong class="text-slate-900 dark:text-white font-bold">This is a fatal philosophical mistake.</strong> If every moral or aesthetic statement is only autobiography, then nothing is objectively beautiful, good, or worthy of defense. And if nothing is worth defending, you cannot build — or protect — a civilization.</p>
            </div>
        </div>''',

        para("Lewis calls this teaching approach <em>'irrigating deserts'</em> — not cutting down jungles. The student isn't being freed from superstition; they're being starved of the moral imagination that makes human flourishing possible."),

        concept_grid([
            ("🧠", "The Head", "Pure reason. Calculates means, but cannot choose ends. Knows <em>how</em>, not <em>why something matters</em>."),
            ("❤️", "The Chest", "Trained sentiment — the moral imagination. Recognizes beauty, courage, and justice as real features of the world, not just preferences."),
            ("🔥", "The Belly", "Raw appetite. Grows to fill any vacuum left when the chest is absent. Cannot be reasoned with."),
        ]),

        blockquote("We make men without chests and expect of them virtue and enterprise. We laugh at honour and are shocked to find traitors in our midst.", "C.S. Lewis, <em>The Abolition of Man</em>"),

        callout("⚠️", "The Tao", "Lewis called the shared moral tradition of all humanity 'the Tao' — the cross-cultural intuition that cruelty is wrong, courage matters, loyalty binds. Destroy it and you have nothing left — not even a reason to be free."),
        pdf_download("WYA_Lecture_2.pdf", "Download Full Lecture 2 (PDF)"),
    ])


def module3():
    return ''.join([
        lead("Freedom is the most fiercely contested word in the modern world. George Weigel maps its philosophical history, and Viktor Frankl tests it inside a death camp. Together, they prove that meaning — not comfort — is what keeps us human."),

        section("Text 1 — George Weigel"),

        h2("Berlin's Wall: Positive vs. Negative Liberty"),
        para("Before diving into the deep history of the West, Weigel addresses the modern framework established by philosopher Isaiah Berlin during the Cold War. Berlin divided our understanding of freedom into two camps:"),

        f'''<div class="my-10 grid grid-cols-1 md:grid-cols-2 gap-6" data-aos="fade-up">
            <div class="bg-red-900/10 border border-red-500/30 rounded-2xl p-6 shadow-lg shadow-red-900/10">
                <h4 class="text-red-400 font-black text-lg mb-2">Positive Freedom (Freedom To)</h4>
                <p class="text-slate-300 text-sm leading-relaxed mb-4">Often aligned with socialist or utopian models. It seeks to use state power to liberate people for an <em>"alleged greater good"</em> or historical end — whether the people want it or not. Weigel notes this inevitably leads to coercion and totalitarianism.</p>
            </div>
            <div class="bg-cyan-900/10 border border-cyan-500/30 rounded-2xl p-6 shadow-lg shadow-cyan-900/10">
                <h4 class="text-cyan-400 font-black text-lg mb-2">Negative Freedom (Freedom From)</h4>
                <p class="text-slate-300 text-sm leading-relaxed mb-4">The classical liberal model. It defines freedom simply as <em>non-interference</em>. You are free as long as the state or others leave you alone to do what you want, provided you don't harm anyone else.</p>
            </div>
        </div>''',

        callout("⚠️", "The Material Will Trap", "While negative liberty is much safer than the coercions of positive liberty, Weigel argues <strong>both ultimately fail.</strong> Why? Because both models reduce the human person to sheer <em>material will</em>. Neither asks what the will should be aiming at, or what human nature actually requires. To understand how we lost the 'why' of freedom, Weigel says we must trace the error back 700 years."),

        divider(),

        h2("A Tale of Two Monks: The Battle Over Freedom"),
        para("Weigel traces this loss of depth to a conflict that started in the 13th century and still defines our political world today. Two medieval monks. Two radically different ideas of what freedom is <em>for</em>."),

        compare_table(
            ["", "St. Thomas Aquinas (13th c.)", "William of Ockham (14th c.)"],
            [
                ["Core idea", "Freedom for Excellence — choosing wisely toward human flourishing", "Freedom of Indifference — the will as sovereign, detached from nature or truth"],
                ["View of law", "An external aid that helps us achieve the goods we already seek", "A coercive external imposition — God's will or the state's will forcing compliance"],
                ["Result", "Virtue, ordered liberty, human excellence", "Radical autonomy, moral relativism, 'will to power'"],
                ["Modern heir", "'Ordered Liberty' — free and virtuous society", "Nihilism; the self as self-creating; power as the only relation between people"],
            ]
        ),

        bullets([
            "<strong>Aquinas:</strong> Learning freedom is like learning a musical instrument. You must do the 'drudgery' first before you can make music. You don't start by playing anything you want.",
            "<strong>Ockham's explosion:</strong> Weigel calls nominalism 'the first atomic explosion of the modern era.' It severed the connection between freedom and human nature — leaving pure will with nothing to aim at.",
            "<strong>The modern result:</strong> A society that can only say 'you can't impose your values' has no language left to explain why freedom is worth dying for — or why some things simply <em>shouldn't</em> be done.",
        ]),

        blockquote("Tyranny thrives in a world in which means always trump ends. The freedom of indifference cannot sustain a truly free society.", "George Weigel"),

        callout("⚠️", "The Biotechnology Warning", "Weigel points to Huxley's <em>Brave New World</em>: a society obsessed with eliminating all suffering eliminates the conditions for love, courage, and meaning. 'Willful man' — Homo voluntatis — cannot explain why some things that <em>can</em> be done <em>should not</em> be done."),

        hero_img(3, "The Will to Meaning: Freedom in the face of suffering."),

        divider(),

        section("Text 2 — Viktor Frankl"),
        h2("Man's Search for Meaning"),
        para("In 1946, <strong>Viktor Frankl</strong> — a Viennese psychiatrist who survived Auschwitz and Dachau — published his account. It is not about the great horrors. It is about the ordinary daily torments — and what he observed about the human mind under total destruction."),

        case_study("⚡ The Capos and the Unknown Victims",
            '''<p>Two types of prisoners emerged in the camps. The <strong class="text-cyan-300">Capos</strong> — prisoners granted privileges in exchange for supervising other prisoners — fared best materially. They were never hungry. Some were crueler than the SS guards themselves. They chose survival over solidarity.</p>
            <p>Then there were the <strong class="text-cyan-300">ordinary unknown victims</strong> — no rank, no privilege, barely any food. Yet Frankl watched some of them walk through the huts giving away the last of their bread and comforting the dying.</p>
            <p>His conclusion: <strong class="text-cyan-300">"Everything can be taken from a man but one thing — the last of the human freedoms: to choose one's attitude in any given set of circumstances."</strong></p>'''),

        section("The Three Phases"),
        bullets([
            "<strong>Admission (Shock):</strong> The 'delusion of reprieve' — hope that things won't be as bad as feared. Quickly replaced by grim humor and cold curiosity as psychological shields.",
            "<strong>Entrenchment (Apathy):</strong> Emotions blunt. Deaths and beatings stop registering. The prisoner regresses to primitive instinct — food, warmth, survival.",
            "<strong>Liberation (Depersonalization):</strong> Release feels unreal. The prisoner must slowly relearn joy in a world that may no longer contain the people he sustained himself by thinking about.",
        ]),

        section("The Sources of Meaning"),
        concept_grid([
            ("🛠️", "Achievement", "Creating something of value — a work, a task completed. The sense of having contributed something that would not exist without you."),
            ("💛", "Love", "The contemplation of a beloved person. In the depths of desolation, Frankl experienced bliss by holding his wife's image in his mind."),
            ("🩸", "Suffering", "How a man 'takes up his cross.' If life has meaning, then suffering must too — and bearing it with dignity is itself a form of contribution."),
        ]),

        blockquote("He who has a 'why' to live can bear with almost any 'how'.", "Friedrich Nietzsche, quoted by Frankl"),

        callout("💡", "Frankl's Reversal", "Stop asking what you expect from life. Ask what life expects from you. Each person, in each situation, has a unique answer — expressible only through action and conduct, not words."),
        pdf_download("WYA_Lecture_3.pdf", "Download Full Lecture 3 (PDF)"),
    ])


def module4():
    return ''.join([
        lead("Solidarity is not a sentiment. It is an act. Three stories — from India, Burma, and Brussels — show what it looks like when people choose the common good over personal safety."),

        section("Text 1 — Mahatma Gandhi"),
        h2("Satyagraha: Not Passive Resistance"),
        para("<strong>Mahatma Gandhi</strong> was clear: the English term 'passive resistance' was inaccurate and dangerous. Passive resistance, he noted, was sometimes deployed by the weak out of hatred — like the Suffragettes who burned houses. His movement was something different entirely."),

        case_study("✊ What is Satyagraha?",
            '''<p><em>Satyagraha</em> — "clinging to Truth" — was born in South Africa in 1908. It is a weapon of the <strong class="text-cyan-300">strong</strong>, not the weak. It requires:</p>
            <ul class="list-none space-y-2 my-4 text-blue-100/80">
                <li>→ Absolute belief that Truth triumphs — and that it must not be renounced even unto death</li>
                <li>→ No ill-will toward the adversary — seek to convert, not destroy</li>
                <li>→ No firearms, no infliction of pain</li>
                <li>→ Willingness to suffer personally — <em>tapasya</em> — because reform without suffering is an illusion</li>
            </ul>
            <p>In South Africa, Indians resisting unjust laws were jailed constantly. Gandhi's reflection: <strong class="text-cyan-300">"The prison was a palace to them, and its doors the gateway to freedom."</strong> When you shed the fear of death, no power can stop you.</p>'''),

        bullets([
            "<strong>Soul-Force vs. Physical Force:</strong> Physical might (symbolized by Ravana) is based on arms. Soul-force (symbolized by Rama) is based on knowledge, love, and self-conquest.",
            "<strong>Universal Application:</strong> Satyagraha isn't just for political movements. Gandhi saw it operating in families daily — a father and son, a husband and wife — wherever anger is conquered through submission and refusal to obey unjust rules.",
            "<strong>Historical figures who practiced it:</strong> Harishchandra, Prahlad, Mirabai, Socrates, Jesus Christ.",
        ]),

        blockquote("Non-violence in its active form is love. This force sustains the world.", "Mahatma Gandhi"),

        divider(),

        section("Text 2 — The Solidarity Revolution"),
        h2("Poland's 'Perfect Storm' and the Collapse of Communism"),
        para("The Solidarity movement in Poland represents a unique 'perfect storm' of political, social, and religious factors that successfully challenged and eventually dismantled communist rule. It serves as a successful revolutionary paradigm that capitalized on exceptional circumstances to trigger the eventual collapse of the Soviet Union in 1991."),

        f'''<p class="text-center mt-6 mb-10" data-aos="fade-up"><a href="https://www.youtube.com/watch?v=rX2hlHRtA6E" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 bg-red-600/90 hover:bg-red-500 text-white font-bold rounded-full transition-colors shadow-lg shadow-red-900/20 border border-red-500/50"><span class="text-xl">▶</span> Solidarity movement video</a></p>''',

        bullets([
            "<strong>A Legacy of Unrest:</strong> Poland's liberation was the culmination of decades of internal economic strain and failed uprisings across the Eastern Bloc (East Germany '53, Hungary '56, Czechoslovakia '68).",
            "<strong>The Gdansk Strike (1980):</strong> Organized by electrician Lech Wałęsa at the Lenin shipyards. His vision was inclusive: <em>'We will go and strike for everyone... we don't want anymore to deal with the communism.'</em>",
            "<strong>Rapid Expansion:</strong> Within months, Solidarity's ranks swelled from an illegal labor union to 10 million members — representing 80% of the Polish workforce.",
        ]),

        case_study("⚡ The Confluence of Factors",
            '''<p><strong class="text-cyan-300">The Role of the Catholic Church:</strong> The 1979 visit of Pope John Paul II attracted millions and served as a powerful challenge to communist authority. Global recognition provided a layer of international protection.</p>
            <p><strong class="text-cyan-300">International Support:</strong> Support from the West, particularly the Reagan Administration's economic sanctions, kept the movement alive during state repression. In 1983, Wałęsa was awarded the Nobel Peace Prize.</p>
            <p><strong class="text-cyan-300">The Irony of Repression:</strong> A labor union challenged a 'workers' state.' The government's brutal 1981 martial law crackdown (arresting 5,000 members including Wałęsa) only solidified the movement's resolve and ensured the regime's downfall.</p>'''),

        para("By 1989, the survival of Solidarity forced the government to accept political reform. The Round Table Talks led to the legalization of Solidarity as a political party. In 1990, Lech Wałęsa was elected as the first Polish president by popular vote, providing a blueprint for neighboring countries to demand their own reforms."),

        divider(),

        section("Text 3 — The 88 Generation"),
        h2("Burma: The Fight for Democracy"),
        para("In 2006, a WYA member from Burma — studying in London on a privileged visa, thanks to a father favored by the junta — sat in his college room watching the rain and felt something break."),

        hero_img(4, "Soul-Force: The power of solidarity and truth."),

        bullets([
            "<strong>The '88 Generation'</strong> emerged as a dissident group after the 2007 Saffron Revolution, when the military junta tortured Buddhist monks — a violation of the sacred that united an entire society.",
            "<strong>A choice of solidarity:</strong> Activists from privileged backgrounds began refusing personal benefits — diplomas, travel, comfort — in solidarity with those suffering under the regime.",
            "<strong>The Solidarity model:</strong> The Burmese struggle explicitly drew on Poland's resistance to communism. Key ideological imports: prioritizing the common good over personal safety, building free society even while imprisoned.",
        ]),
        callout("🌏", "The Pattern", "From Poland to Burma, the pattern repeats: a regime that divides can only be defeated by people who choose unity — not out of self-interest, but out of commitment to the truth about what human community is."),

        divider(),

        section("Text 4 — WYA Declaration on the Family"),
        h2("The Family: School of Deeper Humanity"),
        para("The <strong>WYA Declaration on the Family</strong> (Brussels, 2004) makes a specific claim: democracy is not self-sustaining. It requires families — places where human dignity, solidarity, and the gift of self are first learned."),

        concept_grid([
            ("🏠", "First School", "The family is where a child first understands their intrinsic, inviolable dignity — not as a theory, but as lived experience."),
            ("🤝", "Gift of Self", "Through mother and father — equal in dignity — children learn that freedom is most fully lived when given away for the good of another."),
            ("❤️", "Unconditional Love", "Enduring love within the family is an image of transcendent love — the kind necessary for full human fulfillment."),
            ("🗳️", "Forming Citizens", "Free and responsible citizens are best formed in families. Democratic stability depends on this — not just on constitutions."),
            ("🛡️", "Care for the Vulnerable", "The family is the first to care for the weakest — the young, the old, the sick. It performs what no state apparatus can fully replicate."),
            ("♾️", "Sustainability", "The family ensures the continuation of life, culture, and civilization. Weaken it, and everything built on top of it weakens too."),
        ]),

        compare_table(
            ["Who", "What the Declaration Asks"],
            [
                ["Individuals", "Strengthen your own family through daily acts of solidarity."],
                ["Business & Media", "Create a family-friendly climate in workplaces and public culture."],
                ["Politicians", "Establish legal frameworks that protect and support the family unit."],
            ]
        ),

        callout("💡", "The Synthesis", "Gandhi, the Burmese student, and the Brussels Declaration reach the same conclusion: <em>the transformation of society happens from the inside out</em>. Soul-force, solidarity, and the family are not soft alternatives to power — they are the only durable ones."),
        pdf_download("WYA_Lecture_4.pdf", "Download Full Lecture 4 (PDF)"),
    ])

# ─────────────────────────────────────────────────────────────────────────────
# SHARED PARTS
# ─────────────────────────────────────────────────────────────────────────────

NAV_TOGGLE = '''
<button id="theme-toggle" type="button" class="text-slate-500 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg p-2.5 transition-colors">
    <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
    <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
</button>'''

THEME_JS = '''    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ once: true, offset: 60, duration: 700 });
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
            document.getElementById('theme-toggle-light-icon')?.classList.remove('hidden');
        } else {
            document.getElementById('theme-toggle-dark-icon')?.classList.remove('hidden');
        }
        document.getElementById('theme-toggle')?.addEventListener('click', function() {
            document.getElementById('theme-toggle-dark-icon').classList.toggle('hidden');
            document.getElementById('theme-toggle-light-icon').classList.toggle('hidden');
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        });
    </script>'''

PROGRESS_JS = '''    <script>
        window.addEventListener('scroll', function() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            document.getElementById("scroll-progress").style.width = (winScroll / height * 100) + "%";
        });
    </script>'''

def HEAD(title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>tailwind.config = {{ darkMode: 'class' }}</script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="antialiased flex flex-col min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300">'''

# ─────────────────────────────────────────────────────────────────────────────
# INDEX
# ─────────────────────────────────────────────────────────────────────────────

module_titles = [
    "The Defense of Human Dignity",
    "The Human Condition",
    "Freedom and Meaning",
    "Principles of Solidarity",
]
module_intros = [
    "From Kissinger's Realpolitik to Anna Halpine's pink flyer — and the philosophical tradition of Havel, Maritain, and Frankl that backs it all up.",
    "Malik on struggle and care. Buber on I-You versus I-It. C.S. Lewis on what happens when we educate out the moral imagination.",
    "George Weigel traces two ideas of freedom from medieval monks to modern crises. Viktor Frankl tests them inside Auschwitz.",
    "Gandhi's Soul-Force. Burma's 88 Generation. And the WYA Declaration on the Family as the foundation of free society.",
]
icon_map = ["🛡️", "🤝", "🕊️", "🌍"]

index_html = HEAD("WYA CTP VIENNA 2026") + f'''
    <nav class="sticky top-0 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md shadow-sm z-50 border-b border-slate-200 dark:border-slate-800">
        <div class="max-w-6xl mx-auto px-6 flex justify-between items-center h-16">
            <a href="index.html" class="flex items-center hover:opacity-80 transition-opacity">
                <img src="wyalogo.png" class="h-9 w-auto max-w-[180px] object-contain" alt="World Youth Alliance" />
            </a>
            <span class="font-black text-sm text-blue-950 dark:text-slate-300 hidden md:block tracking-widest uppercase">CTP Vienna 2026</span>
            {NAV_TOGGLE}
        </div>
    </nav>

    <main class="flex-grow">
        <section class="relative bg-blue-950 overflow-hidden min-h-[480px] flex items-center">
            <div class="absolute inset-0">
                <img src="wya_hero_bg.png" class="w-full h-full object-cover mix-blend-overlay opacity-60" alt="" />
                <div class="absolute inset-0 bg-gradient-to-r from-blue-950 via-blue-950/70 to-transparent"></div>
            </div>
            <div data-aos="fade-up" class="relative z-10 max-w-6xl mx-auto px-6 py-24">
                <div class="inline-block px-4 py-1.5 bg-cyan-500 text-white rounded-full text-xs font-black tracking-widest uppercase mb-6">Core Curriculum</div>
                <h1 class="text-5xl md:text-7xl font-black text-white leading-tight max-w-3xl">Building a <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-200">Culture of Life</span></h1>
                <p class="mt-6 text-xl text-blue-100 max-w-2xl leading-relaxed">Four lectures. Four foundational ideas. Built to challenge how you see the world.</p>
            </div>
        </section>

        <section class="max-w-6xl mx-auto px-6 py-20">
            <p data-aos="fade-up" class="text-sm font-black tracking-widest uppercase text-slate-400 dark:text-slate-500 mb-10">Select a Module</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
'''

for i in range(4):
    index_html += f'''
                <a href="module{i+1}.html" data-aos="fade-up" data-aos-delay="{i*100}"
                   class="group flex flex-col bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 rounded-3xl p-10 hover:shadow-2xl hover:shadow-cyan-500/10 hover:-translate-y-2 transition-all duration-400">
                    <div class="flex items-center gap-4 mb-8">
                        <div class="w-14 h-14 bg-blue-50 dark:bg-slate-700 rounded-2xl flex items-center justify-center text-2xl shadow-inner group-hover:scale-110 transition-transform">{icon_map[i]}</div>
                        <span class="text-xs font-black tracking-widest text-slate-400 dark:text-slate-500 uppercase">Module {i+1}</span>
                    </div>
                    <h3 class="text-2xl font-black text-slate-900 dark:text-white mb-4 group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition-colors">{module_titles[i]}</h3>
                    <p class="text-slate-500 dark:text-slate-400 leading-relaxed flex-grow text-sm">{module_intros[i]}</p>
                    <div class="mt-8 flex items-center text-cyan-600 dark:text-cyan-400 font-bold text-sm gap-2">
                        <span>Start Learning</span>
                        <span class="transform group-hover:translate-x-1 transition-transform">&#8594;</span>
                    </div>
                </a>'''

index_html += '''
            </div>
        </section>

        <!-- Official Links Section -->
        <section class="max-w-6xl mx-auto px-6 pb-20">
            <div data-aos="fade-up" class="bg-gradient-to-r from-blue-900 to-cyan-900 rounded-3xl p-8 md:p-12 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-8 border border-blue-700/50">
                <div>
                    <h2 class="text-3xl font-black text-white mb-2">Dive Deeper</h2>
                    <p class="text-blue-100/80 leading-relaxed max-w-xl text-sm">Ready to take the next step in understanding human dignity? Explore the official Certified Training Program platform, or visit the main WYA website to learn how to get involved.</p>
                </div>
                <div class="flex flex-col sm:flex-row gap-4 w-full md:w-auto shrink-0">
                    <a href="https://education.wya.net/" target="_blank" class="flex items-center justify-center gap-2 px-6 py-4 bg-white hover:bg-slate-50 text-blue-950 font-bold rounded-xl transition-transform hover:-translate-y-1 shadow-lg text-center">
                        📚 WYA CTP Platform
                    </a>
                    <a href="https://wya.net/" target="_blank" class="flex items-center justify-center gap-2 px-6 py-4 bg-cyan-500 hover:bg-cyan-400 text-white font-bold rounded-xl transition-transform hover:-translate-y-1 shadow-lg shadow-cyan-500/20 text-center border border-cyan-400/50">
                        🌍 Official WYA Site
                    </a>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 border-t border-slate-800 py-10 text-center text-sm text-slate-500 font-semibold tracking-widest uppercase">
        World Youth Alliance &copy; 2026
    </footer>
'''
index_html += THEME_JS + '\n</body>\n</html>'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# ─────────────────────────────────────────────────────────────────────────────
# MODULE PAGES
# ─────────────────────────────────────────────────────────────────────────────

module_content_funcs = [module1, module2, module3, module4]

for i in range(4):
    idx = i + 1
    title = module_titles[i]
    content_html = module_content_funcs[i]()

    prev_link = f'<a href="module{idx-1}.html" class="flex items-center gap-2 text-sm font-bold text-slate-400 hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">&#8592; Module {idx-1}</a>' if idx > 1 else ''
    next_link = f'<a href="module{idx+1}.html" class="ml-auto flex items-center gap-2 text-sm font-bold text-slate-400 hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">Module {idx+1} &#8594;</a>' if idx < 4 else ''

    page = HEAD(f"{title} | WYA CTP VIENNA 2026") + f'''
    <div class="fixed top-0 left-0 w-full h-1 bg-slate-200 dark:bg-slate-800 z-[60]">
        <div id="scroll-progress" class="h-full bg-gradient-to-r from-blue-600 to-cyan-400 w-0 transition-all duration-100"></div>
    </div>

    <nav class="sticky top-1 z-50 bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl border-b border-slate-200 dark:border-slate-800 shadow-sm">
        <div class="max-w-5xl mx-auto px-6 flex justify-between items-center h-14">
            <a href="index.html" class="text-sm font-bold text-slate-400 hover:text-blue-600 dark:hover:text-cyan-400 transition-colors flex items-center gap-2 shrink-0">
                &#8592; Back
            </a>
            <a href="index.html" class="flex items-center hover:opacity-80 transition-opacity">
                <img src="wyalogo.png" class="h-8 w-auto max-w-[160px] object-contain" alt="World Youth Alliance" />
            </a>
            {NAV_TOGGLE}
        </div>
    </nav>

    <header class="relative bg-blue-950 min-h-[44vh] flex items-end overflow-hidden">
        <div class="absolute inset-0">
            <img src="module{idx}_hero.png" class="w-full h-full object-cover mix-blend-overlay opacity-40" alt="" />
            <div class="absolute inset-0 bg-gradient-to-t from-blue-950 via-blue-950/50 to-transparent"></div>
        </div>
        <div data-aos="fade-up" class="relative z-10 max-w-5xl mx-auto px-6 py-16 w-full">
            <p class="text-xs font-black tracking-[0.25em] text-cyan-400 uppercase mb-4">Masterclass &middot; Module {idx}</p>
            <h1 class="text-4xl md:text-6xl font-black text-white leading-tight">{title}</h1>
        </div>
    </header>

    <main class="bg-white dark:bg-slate-900">
        <div class="max-w-4xl mx-auto px-6 py-20">
            {content_html}
        </div>
    </main>

    <div class="bg-slate-50 dark:bg-slate-900 border-t border-slate-100 dark:border-slate-800 py-10">
        <div class="max-w-4xl mx-auto px-6 flex items-center">
            {prev_link}
            {next_link}
        </div>
    </div>

    <footer class="bg-slate-900 border-t border-slate-800 py-10 text-center text-sm text-slate-500 font-semibold tracking-widest uppercase">
        World Youth Alliance &copy; 2026
    </footer>
'''
    page += '\n' + PROGRESS_JS + '\n' + THEME_JS + '\n</body>\n</html>'

    with open(f'module{idx}.html', 'w', encoding='utf-8') as f:
        f.write(page)

print("Done: index.html + 4 module pages built.")
