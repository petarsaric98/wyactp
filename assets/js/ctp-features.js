/**
 * WYA CTP - Advanced Educational Features
 * Handles Reading Time, Glossary Tooltips, and Interactive Quizzes
 */

const CTP_DATA = {
    glossary: {
        en: {
            "NSSM 200": "National Security Study Memorandum 200 (1974), which argued that population growth in developing nations threatened U.S. security.",
            "Realpolitik": "A system of politics or principles based on practical rather than moral or ideological considerations.",
            "Intrinsic Dignity": "The belief that every human being possesses value that is inherent and cannot be given or taken away by any state.",
            "Living in Truth": "A concept by Václav Havel about resisting totalitarianism through small, honest daily actions.",
            "Integral Development": "WYA's concept that authentic progress must be physical, spiritual, mental, and emotional.",
            "Soul-Force": "Gandhi's concept of Satyagraha, or the power of truth and non-violence in social change.",
            "I-Thou": "Martin Buber's philosophical concept of a relationship built on mutual recognition of personhood, rather than 'I-It' objectification.",
            "I-You": "Same as I-Thou; a relationship where the other is encountered as a unique, whole being.",
            "I-It": "A relationship where the other is treated as an object, a tool, or a means to an end.",
            "The Tao": "C.S. Lewis's term for the universal moral law shared across human civilizations.",
            "Men Without Chests": "Lewis's description of people who have intellect and appetites but lack the moral imagination to bridge them.",
            "Ontological": "Relating to the branch of philosophy that deals with the nature of being.",
            "Sublime": "Of such excellence, grandeur, or beauty as to inspire great admiration and awe.",
            "Relativism": "The doctrine that knowledge, truth, and morality exist in relation to culture, society, or historical context, and are not absolute.",
            "Relationism": "The objective method of discovering truth by relating things to fixed points (e.g., ground vs. train).",
            "Sovereignty": "Supreme power or authority; in WYA terms, often discussed regarding the person vs. the state.",
            "Satyagraha": "Gandhi's term meaning 'clinging to Truth' or 'Truth-force'.",
            "Concupiscence": "In Pieper's sense, a restless, superficial pursuit of impressions that destroys real sight.",
            "Totalitarian Work State": "A state where work is idolized and leisure is destroyed, reducing persons to functional units.",
            "Malthusian": "Relating to the theory that population growth will always outpace food supply, leading to catastrophe (falsified by human ingenuity).",
            "Inalienable": "Unable to be taken away from or given away by the possessor (e.g., human rights).",
            "Jurisprudence": "The theory or philosophy of law."
        },
        hr: {
            "NSSM 200": "Memorandum o nacionalnoj sigurnosti br. 200 (1974.), koji je tvrdio da rast stanovništva u zemljama u razvoju ugrožava američku sigurnost.",
            "Realpolitik": "Sustav politike ili načela utemeljen na praktičnim, a ne moralnim ili ideološkim razmatranjima.",
            "Urođeno dostojanstvo": "Uvjerenje da svako ljudsko biće posjeduje vrijednost koja mu je svojstvena i koju mu država ne može dati niti oduzeti.",
            "Živjeti u istini": "Koncept Václava Havela o odupiranju totalitarizmu kroz male, iskrene svakodnevne postupke.",
            "Integralni razvoj": "Koncept SSM-a (WYA) prema kojem autentičan napredak mora biti fizički, duhovan, mentalni i emocionalni.",
            "I-Ti": "Filozofski koncept Martina Bubera o odnosu izgrađenom na uzajamnom priznavanju osobnosti, umjesto objektivizacije 'Ja-Ono'.",
            "I-Ono": "Odnos u kojem se drugi tretira kao objekt, alat ili sredstvo za postizanje cilja.",
            "Tao": "Pojam C.S. Lewisa za univerzalni moralni zakon zajednički svim ljudskim civilizacijama.",
            "Ljudi bez prsa": "Lewisov opis ljudi koji imaju intelekt i prohtjeve, ali im nedostaje moralna mašta koja bi ih povezala.",
            "Relativizam": "Doktrina prema kojoj znanje, istina i moral ovise o kulturi, društvu ili povijesnom kontekstu i nisu apsolutni.",
            "Satyagraha": "Gandhijev pojam koji znači 'ustrajnost u istini' ili 'sila istine'.",
            "Jurisprudencija": "Teorija ili filozofija prava."
        }
    },
    quizzes: {
        "module1": {
            en: {
                title: "Knowledge Check: Module 1",
                questions: [
                    {
                        q: "What was the primary argument of NSSM 200?",
                        options: ["Population growth is good for U.S. economy", "Population growth in developing nations threatens U.S. power", "Human aid should be unconditional"],
                        correct: 1,
                        feedback: "Kissinger argued that population growth in 13 key countries was a threat to American interests."
                    },
                    {
                        q: "Who founded WYA with a 'pink flyer' at the UN?",
                        options: ["Václav Havel", "Viktor Frankl", "Anna Halpine"],
                        correct: 2,
                        feedback: "Anna Halpine founded WYA in 1999 during the Cairo+5 conference."
                    },
                    {
                        q: "According to WYA, what is the relationship between rights and dignity?",
                        options: ["Rights grant human dignity", "Rights are the product of intrinsic dignity", "Dignity is granted by international law"],
                        correct: 1,
                        feedback: "WYA insists that rights exist because of our intrinsic dignity, not the other way around."
                    }
                ]
            },
            hr: {
                title: "Provjera znanja: Modul 1",
                questions: [
                    {
                        q: "Što je bio glavni argument memoranduma NSSM 200?",
                        options: ["Rast stanovništva je dobar za ekonomiju SAD-a", "Rast stanovništva u zemljama u razvoju ugrožava moć SAD-a", "Humanitarna pomoć treba biti bezuvjetna"],
                        correct: 1,
                        feedback: "Kissinger je tvrdio da je rast stanovništva u 13 ključnih zemalja prijetnja američkim interesima."
                    },
                    {
                        q: "Tko je osnovao SSM (WYA) s 'ružičastim letkom' u UN-u?",
                        options: ["Václav Havel", "Viktor Frankl", "Anna Halpine"],
                        correct: 2,
                        feedback: "Anna Halpine je osnovala WYA 1999. godine tijekom konferencije Kairo+5."
                    },
                    {
                        q: "Prema SSM-u, kakav je odnos između prava i dostojanstva?",
                        options: ["Prava daju ljudsko dostojanstvo", "Prava su proizvod urođenog dostojanstva", "Dostojanstvo dodjeljuje međunarodno pravo"],
                        correct: 1,
                        feedback: "SSM inzistira na tome da prava postoje zbog našeg urođenog dostojanstva, a ne obrnuto."
                    }
                ]
            }
        },
        "module2": {
            en: {
                title: "Knowledge Check: Module 2",
                questions: [
                    {
                        q: "According to Charles Malik, why do many diplomats smile?",
                        options: ["They are being hypocritical", "They have a metaphysical awareness of the human impossibility of their task", "They are confident in their negotiations"],
                        correct: 1,
                        feedback: "Malik noted that diplomats often smile because they realize the absurdity of seeking outer peace without inner peace."
                    },
                    {
                        q: "What is the key difference between Buber's I-You and I-It?",
                        options: ["I-You is only for religion", "I-It treats the other as an object or tool", "I-You is about biological perception"],
                        correct: 1,
                        feedback: "I-It is the mode of experience and utility; I-You is the mode of genuine relation and presence."
                    },
                    {
                        q: "What does C.S. Lewis mean by 'Men Without Chests'?",
                        options: ["People who lack physical strength", "People who lack the moral imagination to bridge intellect and appetite", "People who have no feelings"],
                        correct: 1,
                        feedback: "The 'Chest' represents trained sentiment and the Tao, which governs the appetites via the intellect."
                    }
                ]
            },
            hr: {
                title: "Provjera znanja: Modul 2",
                questions: [
                    {
                        q: "Prema Charlesu Maliku, zašto se diplomati često smiješe?",
                        options: ["Zato što su licemjerni", "Zbog metafizičke svijesti o ljudskoj nemogućnosti njihovog zadatka", "Zato što su uvjereni u uspjeh pregovora"],
                        correct: 1,
                        feedback: "Malik je primijetio da se diplomati smiješe jer uviđaju apsurdnost traženja vanjskog mira dok unutarnji mir nije postignut."
                    },
                    {
                        q: "Koja je ključna razlika između Buberovih odnosa I-Ti i I-Ono?",
                        options: ["I-Ti je samo za religiju", "I-Ono tretira drugoga kao objekt ili alat", "I-Ti se odnosi na biološku percepciju"],
                        correct: 1,
                        feedback: "I-Ono je način iskustva i korisnosti; I-Ti je način istinskog odnosa i prisutnosti."
                    },
                    {
                        q: "Što C.S. Lewis misli pod pojmom 'Ljudi bez prsa'?",
                        options: ["Ljudi kojima nedostaje fizička snaga", "Ljudi kojima nedostaje moralna mašta koja povezuje intelekt i prohtjeve", "Ljudi koji nemaju nikakve osjećaje"],
                        correct: 1,
                        feedback: "'Prsa' predstavljaju odgojeni osjećaj i Tao, koji putem intelekta upravlja prohtjevima."
                    }
                ]
            }
        },
        "module3": {
            en: {
                title: "Knowledge Check: Module 3",
                questions: [
                    {
                        q: "George Weigel discusses two ideas of freedom. Which one did he favor?",
                        options: ["Freedom of Indifference", "Freedom for Excellence", "Freedom as lack of constraint"],
                        correct: 1,
                        feedback: "Freedom for Excellence is the power to be who you ought to be, not just the power to do whatever you want."
                    },
                    {
                        q: "In Viktor Frankl's account, what is the 'last of the human freedoms'?",
                        options: ["The right to vote", "To choose one's attitude in any given set of circumstances", "Freedom from physical pain"],
                        correct: 1,
                        feedback: "Even in Auschwitz, Frankl argued that man could choose his own inner attitude toward his suffering."
                    }
                ]
            },
            hr: {
                title: "Provjera znanja: Modul 3",
                questions: [
                    {
                        q: "George Weigel raspravlja o dvije ideje slobode. Koju on zagovara?",
                        options: ["Sloboda ravnodušnosti", "Sloboda za izvrsnost", "Sloboda kao odsustvo ograničenja"],
                        correct: 1,
                        feedback: "Sloboda za izvrsnost je moć da budemo ono što trebamo biti, a ne samo moć da radimo što god želimo."
                    },
                    {
                        q: "Prema Viktoru Franklu, što je 'posljednja ljudska sloboda'?",
                        options: ["Pravo glasa", "Izbor vlastitog stava u bilo kojim okolnostima", "Sloboda od fizičke boli"],
                        correct: 1,
                        feedback: "Frankl je tvrdio da čak i u Auschwitzu čovjek može izabrati svoj unutarnji stav prema patnji."
                    }
                ]
            }
        },
        "module4": {
            en: {
                title: "Knowledge Check: Module 4",
                questions: [
                    {
                        q: "What is the literal meaning of Gandhi's 'Satyagraha'?",
                        options: ["Passive Resistance", "Clinging to Truth", "Physical Force"],
                        correct: 1,
                        feedback: "Satyagraha means 'clinging to Truth' and is a weapon of the strong."
                    },
                    {
                        q: "Which movement represents a 'perfect storm' that dismantled communism in Poland?",
                        options: ["The Saffron Revolution", "The Solidarity Movement", "The 88 Generation"],
                        correct: 1,
                        feedback: "Solidarity (Solidarność) combined labor rights with religious and national identity to challenge the Soviet Bloc."
                    },
                    {
                        q: "What is described as the 'First School' of humanity?",
                        options: ["The University", "The Family", "The State"],
                        correct: 1,
                        feedback: "The family is where human dignity and the gift of self are first learned."
                    }
                ]
            }
        },
        "module5": {
            en: {
                title: "Knowledge Check: Module 5",
                questions: [
                    {
                        q: "According to Joseph Pieper, what is the 'first step' toward the primordial mental grasping of reality?",
                        options: ["To think deeply and logically", "To see things as they truly are", "To read as many books as possible"],
                        correct: 1,
                        feedback: "Pieper argues that 'To see things' is the essential first step in grasping reality as a spiritual being."
                    },
                    {
                        q: "What does Roger Scruton say about building for utility alone?",
                        options: ["It is the most efficient way", "It quickly becomes useless", "It is the root of beauty"],
                        correct: 1,
                        feedback: "Scruton argues that things built only for utility are quickly discarded, whereas beauty ensures preservation."
                    }
                ]
            },
            hr: {
                title: "Provjera znanja: Modul 5",
                questions: [
                    {
                        q: "Prema Josephu Pieperu, što je 'prvi korak' prema iskonskom mentalnom zahvaćanju stvarnosti?",
                        options: ["Duboko i logično razmišljanje", "Istinsko gledanje stvari", "Čitanje što većeg broja knjiga"],
                        correct: 1,
                        feedback: "Pieper tvrdi da je 'gledanje stvari' bitan prvi korak u zahvaćanju stvarnosti kao duhovno biće."
                    },
                    {
                        q: "Što Roger Scruton kaže o gradnji isključivo radi korisnosti?",
                        options: ["To je najučinkovitiji način", "Brzo postaje beskorisno", "To je korijen ljepote"],
                        correct: 1,
                        feedback: "Scruton tvrdi da se stvari izgrađene samo radi korisnosti brzo odbacuju, dok ljepota osigurava očuvanje."
                    }
                ]
            }
        },
        "module6": {
            en: {
                title: "Knowledge Check: Module 6",
                questions: [
                    {
                        q: "What is the key difference between Relationism and Relativism?",
                        options: ["Relativism uses fixed points; Relationism doesn't", "Relationism uses fixed points to find truth; Relativism denies truth", "There is no difference"],
                        correct: 1,
                        feedback: "Relationism is an objective method; Relativism is the radical claim that no ultimate truth is possible."
                    },
                    {
                        q: "What was the 'impossible miracle' of Hong Kong?",
                        options: ["Growth with no people", "Rapid income growth despite massive population increase", "Survival through heavy UN aid"],
                        correct: 1,
                        feedback: "Hong Kong proved that people are a resource, not a liability, by flourishing despite a population explosion."
                    }
                ]
            }
        },
        "module7": {
            en: {
                title: "Knowledge Check: Module 7",
                questions: [
                    {
                        q: "What is John Finnis's main argument regarding the legal order?",
                        options: ["Law is for the sake of the state", "Priority of the human person", "Law is a bundle of duties only"],
                        correct: 1,
                        feedback: "Finnis insists that 'All law is made for the sake of human beings' (The Priority of Persons)."
                    },
                    {
                        q: "What was Jacques Maritain's paradox about human rights?",
                        options: ["We agree on the 'Why' but not the 'What'", "We agree on the 'What' but not the 'Why'", "Human rights are impossible to define"],
                        correct: 1,
                        feedback: "Nations agreed on the practical list of rights while fundamentally disagreeing on their philosophical origins."
                    }
                ]
            }
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const lang = document.documentElement.lang || 'en';
    const path = window.location.pathname;
    const filename = path.substring(path.lastIndexOf('/') + 1).replace('-hr.html', '').replace('.html', '');
    
    initGlossary(lang);
    initQuiz(filename || 'module1', lang); // Default to module1 if empty (e.g. root)
});


/** 2. Glossary Tooltip System */
function initGlossary(lang) {
    const glossary = CTP_DATA.glossary[lang] || CTP_DATA.glossary['en'];
    if (!glossary) return;

    const mainContent = document.querySelector('main .max-w-4xl');
    if (!mainContent) return;

    const walker = document.createTreeWalker(mainContent, NodeFilter.SHOW_TEXT, null, false);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach(node => {
        let text = node.nodeValue;
        let modified = false;

        const sortedTerms = Object.keys(glossary).sort((a, b) => b.length - a.length);

        sortedTerms.forEach(term => {
            const regex = new RegExp(`\\b${term}\\b`, 'g');
            if (regex.test(text)) {
                modified = true;
                text = text.replace(regex, `<span class="glossary-term">${term}<span class="ctp-tooltip"><span class="ctp-tooltip-title">${term}</span><span class="ctp-tooltip-content">${glossary[term]}</span></span></span>`);
            }
        });

        if (modified) {
            const span = document.createElement('span');
            span.innerHTML = text;
            
            // Handle touch devices: toggle tooltip on click
            span.querySelectorAll('.glossary-term').forEach(term => {
                term.addEventListener('click', (e) => {
                    if (window.innerWidth <= 1024) {
                        e.stopPropagation();
                        // Close other open tooltips
                        document.querySelectorAll('.glossary-term.active').forEach(other => {
                            if (other !== term) other.classList.remove('active');
                        });
                        term.classList.toggle('active');
                    }
                });
            });
            
            node.parentNode.replaceChild(span, node);
        }
    });

    // Close tooltips when clicking outside
    document.addEventListener('click', () => {
        document.querySelectorAll('.glossary-term.active').forEach(term => {
            term.classList.remove('active');
        });
    });
}

/** 3. Interactive Quiz Engine */
function initQuiz(moduleId, lang) {
    const quizData = (CTP_DATA.quizzes[moduleId] && CTP_DATA.quizzes[moduleId][lang]) ? CTP_DATA.quizzes[moduleId][lang] : (CTP_DATA.quizzes[moduleId] ? CTP_DATA.quizzes[moduleId]['en'] : null);
    
    if (!quizData) return;

    const quizSection = document.createElement('section');
    quizSection.className = 'max-w-4xl mx-auto px-6 pb-20 mt-20';
    quizSection.style.display = 'block'; // Ensure it's visible
    quizSection.innerHTML = `
        <div class="quiz-container">
            <h2 class="text-3xl font-black text-slate-900 dark:text-white mb-10 text-center">${quizData.title}</h2>
            <div id="quiz-content-area"></div>
        </div>
    `;

    const main = document.querySelector('main');
    if (!main) return;
    main.appendChild(quizSection);

    const contentArea = quizSection.querySelector('#quiz-content-area');
    let currentQuestion = 0;

    function renderQuestion(index) {
        const q = quizData.questions[index];
        if (!q) return;

        contentArea.innerHTML = `
            <div class="quiz-question">${q.q}</div>
            <div class="space-y-3">
                ${q.options.map((opt, i) => `
                    <button class="quiz-option" data-idx="${i}">
                        <span class="w-8 h-8 rounded-full border-2 border-slate-200 dark:border-slate-700 flex items-center justify-center text-xs font-black">${String.fromCharCode(65 + i)}</span>
                        <span>${opt}</span>
                    </button>
                `).join('')}
            </div>
            <div id="feedback-panel" class="hidden mt-8"></div>
        `;

        contentArea.querySelectorAll('.quiz-option').forEach(btn => {
            btn.addEventListener('click', () => handleAnswer(parseInt(btn.dataset.idx)));
        });
    }

    function handleAnswer(choice) {
        const q = quizData.questions[currentQuestion];
        const buttons = contentArea.querySelectorAll('.quiz-option');
        const feedbackPanel = contentArea.querySelector('#feedback-panel');

        buttons.forEach((btn, i) => {
            btn.disabled = true;
            if (i === q.correct) btn.classList.add('correct');
            else if (i === choice) btn.classList.add('incorrect');
        });

        const isCorrect = choice === q.correct;
        feedbackPanel.innerHTML = `
            <div class="quiz-feedback ${isCorrect ? 'bg-emerald-500/10 text-emerald-600' : 'bg-rose-500/10 text-rose-600 animate-shake'}">
                <p class="font-bold mb-2">${isCorrect ? (lang === 'hr' ? 'Točno!' : 'Correct!') : (lang === 'hr' ? 'Netočno.' : 'Incorrect.')}</p>
                <p>${q.feedback}</p>
                <button id="next-question-btn" class="mt-6 px-6 py-3 bg-blue-900 text-white font-bold rounded-xl hover:bg-blue-800 transition-colors">
                    ${currentQuestion < quizData.questions.length - 1 ? (lang === 'hr' ? 'Sljedeće pitanje' : 'Next Question') : (lang === 'hr' ? 'Završi provjeru' : 'Finish Quiz')}
                </button>
            </div>
        `;
        feedbackPanel.classList.remove('hidden');

        feedbackPanel.querySelector('#next-question-btn').addEventListener('click', () => {
            if (currentQuestion < quizData.questions.length - 1) {
                currentQuestion++;
                renderQuestion(currentQuestion);
            } else {
                showCompletion();
            }
        });
    }

    function showCompletion() {
        contentArea.innerHTML = `
            <div class="text-center py-10">
                <div class="text-6xl mb-6">🏆</div>
                <h3 class="text-3xl font-black text-slate-900 dark:text-white mb-4">
                    ${lang === 'hr' ? 'Čestitamo!' : 'Congratulations!'}
                </h3>
                <p class="text-slate-600 dark:text-slate-400 mb-8">
                    ${lang === 'hr' ? 'Završili ste provjeru znanja za ovaj modul.' : 'You have successfully completed the knowledge check for this module.'}
                </p>
                <button onclick="location.reload()" class="px-8 py-4 bg-slate-100 dark:bg-slate-700 text-slate-900 dark:text-white font-bold rounded-2xl hover:bg-slate-200 dark:hover:bg-slate-600 transition-all">
                    ${lang === 'hr' ? 'Pokušaj ponovno' : 'Try Again'}
                </button>
            </div>
        `;
        localStorage.setItem(`ctp_completed_${moduleId}`, 'true');
    }

    renderQuestion(0);
    
    // Refresh AOS if available
    if (typeof AOS !== 'undefined') {
        setTimeout(() => AOS.refresh(), 100);
    }
}
