import json

case_studies = {
    'WYA_lecture1_brief.docx': """

[CASE_STUDY_START]
### Historical Context: Kissinger's Realpolitik vs. Human Dignity

In 1974, Secretary of State Henry Kissinger drafted National Security Memorandum 200 (NSSM 200). He recommended tying U.S. development aid to population control in 13 key developing nations, arguing that unchecked population growth threatened American strategic and economic interests. It was an approach rooted purely in **Realpolitik**—using the world's most vulnerable people as geopolitical pawns. 

Decades later, at the 1999 UN Conference on Population and Development, a group of 32 handpicked youth claimed to represent all 3 billion of the world's young people, demanding radical social redefinitions while ignoring basic needs like clean water, education, and shelter. In an act of resistance, 21-year-old Anna Halpine went to the assembly floor and distributed flyers objecting to this coercion. Her simple act of "living in truth" resonated with delegates from developing nations, leading to the immediate founding of the **World Youth Alliance**—a movement built on the absolute premise that human dignity must be the center of all global policy, not a variable to be managed.
[CASE_STUDY_END]
""",
    
    'WYA_lecture2dignity_brief.docx': """

[CASE_STUDY_START]
### Literary Example: C.S. Lewis & Coleridge at the Waterfall

In his book *The Abolition of Man*, C.S. Lewis critiques a modern school textbook (which he pseudonymously calls *The Green Book*) to illustrate how modern education secretly debunks objective value. 

He recounts the story of Samuel Taylor Coleridge at a waterfall: Two tourists are present. One calls the waterfall **"sublime,"** and the other calls it merely **"pretty."** Coleridge mentally endorsed the first judgment and rejected the second. However, the authors of *The Green Book* instruct children that when the man said "This is sublime," he was not making a remark about the waterfall at all, but rather saying, *"I have sublime feelings."* 

Lewis argues this is a fatal philosophical error. If all statements of value are merely statements about the speaker's psychological state, then nothing is objectively beautiful, good, or true. This reductionism produces what Lewis famously called **"Men Without Chests"**—intellects severed from the trained, ordinate emotions that recognize true reality.
[CASE_STUDY_END]
""",

    'WYA_lecture3freedom_brief.docx': """

[CASE_STUDY_START]
### Historical Example: Viktor Frankl & The Psychology of the Concentration Camp

In *Man’s Search for Meaning*, psychiatrist Viktor Frankl chronicles his experiences in Auschwitz and Dachau, but he focuses heavily on the ordinary daily torments rather than the macro-scale horrors. 

He draws a stark contrast between two types of prisoners. The **"Capos"**—prisoners granted special privileges in exchange for acting as trustees and supervisors—often fared better materially, were never hungry, and could be crueler to their fellow inmates than the SS guards themselves. They traded their interior freedom and solidarity for survival.

Conversely, Frankl witnessed the heroism of the **"great army of unknown and unrecorded victims."** Men who walked through the huts comforting others and giving away their last piece of bread. These men proved that everything can be taken from a man but one thing: **the last of the human freedoms—to choose one's attitude in any given set of circumstances, to choose one's own way.** This "Will to Meaning" allowed them to retain their spiritual freedom and human dignity even in the most degrading conditions imaginable.
[CASE_STUDY_END]
""",

    'WYA_lecture4solidarity_brief.docx': """

[CASE_STUDY_START]
### Concrete Example: Gandhi's "Satyagraha" vs. Passive Resistance

Mahatma Gandhi insisted his movement in South Africa was entirely distinct from what the West called "passive resistance." 

He noted that the burning of houses by Suffragettes in England or their fasting in prison was classified as "passive resistance," yet it was often a weapon born of weakness and hatred. In contrast, Gandhi coined the term **Satyagraha** (Truth-Force or Soul-Force). Satyagraha is the weapon of the strong. It requires intense spiritual activity and absolute definiteness of purpose. 

A true *Satyagrahi* does not inflict pain on the adversary or seek their destruction; they seek to convert them through love and voluntary self-suffering. With the conviction that Truth is not to be renounced even unto death, they shed the fear of death entirely. In the cause of Truth, "the prison was a palace to them and its doors the gateway to freedom."
[CASE_STUDY_END]
"""
}

with open('lectures_formatted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for key in data:
    if key in case_studies:
        # Instead of putting it at the very bottom, let's insert it right in the middle 
        # (approx halfway point) to interrupt the text block nicely.
        parts = data[key].split('\n\n')
        mid = len(parts) // 2
        parts.insert(mid, case_studies[key])
        data[key] = '\n\n'.join(parts)

with open('lectures_formatted.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Cases fully injected into the JSON!")
