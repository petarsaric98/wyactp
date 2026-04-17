import json
import os
import re

# Load JSON
with open('lectures.json', 'r', encoding='utf-8') as f:
    lectures = json.load(f)

def clean_lecture_text(title, text):
    # Extract the summary to put in the cards
    # We will assume everything after Executive Summary and before Roman Numeral I is the summary
    summary_match = re.search(r'Executive Summary(.*?)(?:I\.|Critical Takeaways:|Key takeaways include:|The primary takeaways are:)', text, re.DOTALL | re.IGNORECASE)
    summary = summary_match.group(1).strip() if summary_match else text[:300] + "..."
    # Make sure we don't have super long summaries
    if len(summary) > 600:
        summary = summary[:597] + "..."
    
    return summary

l1_text = clean_lecture_text("Lecture 1", lectures.get('WYA_lecture1_brief.docx', ''))
l2_text = clean_lecture_text("Lecture 2", lectures.get('WYA_lecture2dignity_brief.docx', ''))
l3_text = clean_lecture_text("Lecture 3", lectures.get('WYA_lecture3freedom_brief.docx', ''))
l4_text = clean_lecture_text("Lecture 4", lectures.get('WYA_lecture4solidarity_brief.docx', ''))

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World Youth Alliance Modules</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
        }}
        .module-card {{
            transition: all 0.5s ease;
        }}
        .module-card:hover {{
            transform: translateY(-8px);
        }}
        .nav-link.active {{
            border-bottom: 2px solid #06b6d4; /* cyan-500 */
            color: #06b6d4;
            font-weight: 600;
        }}
        .dark .nav-link.active {{
            border-bottom: 2px solid #22d3ee; /* cyan-400 */
            color: #22d3ee;
        }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300">

    <nav class="sticky top-0 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md shadow-sm z-50 border-b border-transparent dark:border-slate-800 transition-colors duration-300">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <!-- Logo and Branding -->
                <div class="flex items-center space-x-3 text-xl font-bold text-blue-900 dark:text-blue-400 transition-colors duration-300">
                    <a href="#" class="flex items-center hover:opacity-80 transition-opacity">
                        <img src="wyalogo.png" alt="WYA Logo" class="h-8 max-w-[auto] w-auto drop-shadow-sm rounded mr-3 bg-white" /> 
                        <span>WYA Academy</span>
                    </a>
                </div>
                
                <div class="flex items-center space-x-2 md:space-x-4">
                    <div class="hidden md:flex items-center space-x-6">
                        <a href="#hero" class="nav-link active text-slate-600 dark:text-slate-400 hover:text-cyan-600 dark:hover:text-cyan-400 px-1 py-2 transition-colors">Start</a>
                        <a href="#modules" class="nav-link text-slate-600 dark:text-slate-400 hover:text-cyan-600 dark:hover:text-cyan-400 px-1 py-2 transition-colors">Modules</a>
                    </div>
                    <!-- Theme Toggle -->
                    <button id="theme-toggle" type="button" class="text-slate-500 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-700 focus:outline-none rounded-lg text-sm p-2.5 transition-colors">
                        <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
                        <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-24 flex-grow w-full">

        <!-- HERO SECTION -->
        <section id="hero" class="scroll-mt-20 pt-8">
            <div class="relative rounded-[2rem] md:rounded-[2.5rem] overflow-hidden shadow-2xl h-[350px] md:h-[450px] flex items-center justify-start p-6 md:p-14">
                <div class="absolute inset-0 z-0 bg-blue-950">
                    <img src="wya_hero_bg.png" alt="WYA Hero Abstract" class="w-full h-full object-cover mix-blend-overlay opacity-90 scale-105" />
                    <div class="absolute inset-0 bg-gradient-to-r from-blue-900/80 to-transparent"></div>
                </div>
                
                <!-- Glassmorphism Content Box -->
                <div class="relative z-10 bg-white/10 backdrop-blur-xl border border-white/20 p-8 md:p-12 rounded-[1.5rem] md:rounded-3xl shadow-2xl max-w-3xl transform transition-all hover:scale-[1.01]">
                    <div class="inline-block px-4 py-1.5 md:px-5 md:py-2 bg-white/20 text-white rounded-full text-[10px] md:text-xs font-bold tracking-widest mb-4 md:mb-6 shadow-sm ring-1 ring-white/40 uppercase backdrop-blur-md">
                        FOUNDATIONAL TRAINING
                    </div>
                    <h1 class="text-3xl md:text-5xl font-extrabold text-white mb-4 md:mb-6 leading-tight drop-shadow-md">
                        Building a <span class="text-cyan-400">Culture of Life</span>
                    </h1>
                    <p class="text-base md:text-xl text-blue-50 font-medium leading-relaxed drop-shadow-sm max-w-2xl">
                        Explore the philosophical foundations of human dignity, objective value, freedom for excellence, and the power of solidarity that shape the mission of the World Youth Alliance.
                    </p>
                </div>
            </div>
        </section>

        <!-- MODULES DIRECTORY -->
        <section id="modules" class="scroll-mt-20 pb-16">
            <div class="mb-12 text-center md:text-left">
                <div class="inline-block px-3 py-1 bg-cyan-100 dark:bg-slate-800 text-cyan-700 dark:text-cyan-400 text-xs font-bold rounded-full mb-3 uppercase tracking-wider">Curriculum Path</div>
                <h2 class="text-3xl font-bold text-slate-800 dark:text-white mb-4">Core Educational <span class="text-blue-600 dark:text-cyan-400">Modules</span></h2>
                <p class="text-lg text-slate-600 dark:text-slate-400 max-w-3xl">
                    Our training is structured around four critical pillars that define what it means to be truly human. Click on each module to view the comprehensive briefing.
                </p>
            </div>

            <!-- CSS Grid for Module Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- MODULE 1 -->
                <div class="module-card group relative bg-white dark:bg-slate-800 rounded-[1.5rem] p-8 shadow-lg hover:shadow-2xl hover:shadow-cyan-500/10 border border-slate-100 dark:border-slate-700 overflow-hidden cursor-pointer flex flex-col h-full">
                    <!-- Decorative Blob -->
                    <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-50/80 dark:bg-cyan-500/10 rounded-bl-full -z-0 transition-transform group-hover:scale-110"></div>
                    
                    <div class="relative z-10 flex-grow">
                        <!-- Icon Gradient Box -->
                        <div class="w-16 h-16 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center text-white text-3xl mb-6 shadow-md shadow-cyan-500/30">
                            🛡️
                        </div>
                        <div class="inline-block text-[10px] px-3 py-1 bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 rounded-full font-bold tracking-wider mb-3">MODULE 1</div>
                        <h3 class="text-2xl font-bold text-slate-800 dark:text-white mb-4 group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition-colors">The Defense of Human Dignity</h3>
                        
                        <!-- Content Box Within a Box -->
                        <div class="bg-slate-50 dark:bg-slate-900/50 p-5 rounded-xl border border-slate-200 dark:border-slate-700 mb-6 flex-grow">
                            <span class="text-xs font-bold text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block mb-2">🎓 Executive Summary</span>
                            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">{l1_text}</p>
                        </div>
                    </div>
                    
                    <!-- Call to action micro-interaction -->
                    <div class="flex items-center text-cyan-600 dark:text-cyan-400 font-bold text-sm mt-auto">
                        <span class="group-hover:mr-2 transition-all">Read Briefing</span> 
                        <span class="opacity-0 group-hover:opacity-100 transform -translate-x-2 group-hover:translate-x-0 transition-all"> ➔</span>
                    </div>
                </div>

                <!-- MODULE 2 -->
                <div class="module-card group relative bg-white dark:bg-slate-800 rounded-[1.5rem] p-8 shadow-lg hover:shadow-2xl hover:shadow-blue-500/10 border border-slate-100 dark:border-slate-700 overflow-hidden cursor-pointer flex flex-col h-full">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-blue-50/80 dark:bg-blue-500/10 rounded-bl-full -z-0 transition-transform group-hover:scale-110"></div>
                    <div class="relative z-10 flex-grow">
                        <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center text-white text-3xl mb-6 shadow-md shadow-blue-500/30">
                            🤝
                        </div>
                        <div class="inline-block text-[10px] px-3 py-1 bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 rounded-full font-bold tracking-wider mb-3">MODULE 2</div>
                        <h3 class="text-2xl font-bold text-slate-800 dark:text-white mb-4 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">The Human Condition</h3>
                        <div class="bg-slate-50 dark:bg-slate-900/50 p-5 rounded-xl border border-slate-200 dark:border-slate-700 mb-6 flex-grow">
                            <span class="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-wider block mb-2">🎓 Executive Summary</span>
                            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">{l2_text}</p>
                        </div>
                    </div>
                    <div class="flex items-center text-blue-600 dark:text-blue-400 font-bold text-sm mt-auto">
                        <span class="group-hover:mr-2 transition-all">Read Briefing</span> 
                        <span class="opacity-0 group-hover:opacity-100 transform -translate-x-2 group-hover:translate-x-0 transition-all"> ➔</span>
                    </div>
                </div>

                <!-- MODULE 3 -->
                <div class="module-card group relative bg-white dark:bg-slate-800 rounded-[1.5rem] p-8 shadow-lg hover:shadow-2xl hover:shadow-amber-500/10 border border-slate-100 dark:border-slate-700 overflow-hidden cursor-pointer flex flex-col h-full">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-amber-50/80 dark:bg-amber-500/10 rounded-bl-full -z-0 transition-transform group-hover:scale-110"></div>
                    <div class="relative z-10 flex-grow">
                        <div class="w-16 h-16 bg-gradient-to-br from-amber-400 to-orange-500 rounded-2xl flex items-center justify-center text-white text-3xl mb-6 shadow-md shadow-amber-500/30">
                            🕊️
                        </div>
                        <div class="inline-block text-[10px] px-3 py-1 bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 rounded-full font-bold tracking-wider mb-3">MODULE 3</div>
                        <h3 class="text-2xl font-bold text-slate-800 dark:text-white mb-4 group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">Freedom and Meaning</h3>
                        <div class="bg-slate-50 dark:bg-slate-900/50 p-5 rounded-xl border border-slate-200 dark:border-slate-700 mb-6 flex-grow">
                            <span class="text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider block mb-2">🎓 Executive Summary</span>
                            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">{l3_text}</p>
                        </div>
                    </div>
                    <div class="flex items-center text-amber-600 dark:text-amber-400 font-bold text-sm mt-auto">
                        <span class="group-hover:mr-2 transition-all">Read Briefing</span> 
                        <span class="opacity-0 group-hover:opacity-100 transform -translate-x-2 group-hover:translate-x-0 transition-all"> ➔</span>
                    </div>
                </div>

                <!-- MODULE 4 -->
                <div class="module-card group relative bg-white dark:bg-slate-800 rounded-[1.5rem] p-8 shadow-lg hover:shadow-2xl hover:shadow-emerald-500/10 border border-slate-100 dark:border-slate-700 overflow-hidden cursor-pointer flex flex-col h-full">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-50/80 dark:bg-emerald-500/10 rounded-bl-full -z-0 transition-transform group-hover:scale-110"></div>
                    <div class="relative z-10 flex-grow">
                        <div class="w-16 h-16 bg-gradient-to-br from-teal-400 to-emerald-600 rounded-2xl flex items-center justify-center text-white text-3xl mb-6 shadow-md shadow-emerald-500/30">
                            🌍
                        </div>
                        <div class="inline-block text-[10px] px-3 py-1 bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 rounded-full font-bold tracking-wider mb-3">MODULE 4</div>
                        <h3 class="text-2xl font-bold text-slate-800 dark:text-white mb-4 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors">Principles of Solidarity</h3>
                        <div class="bg-slate-50 dark:bg-slate-900/50 p-5 rounded-xl border border-slate-200 dark:border-slate-700 mb-6 flex-grow">
                            <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider block mb-2">🎓 Executive Summary</span>
                            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">{l4_text}</p>
                        </div>
                    </div>
                    <div class="flex items-center text-emerald-600 dark:text-emerald-400 font-bold text-sm mt-auto">
                        <span class="group-hover:mr-2 transition-all">Read Briefing</span> 
                        <span class="opacity-0 group-hover:opacity-100 transform -translate-x-2 group-hover:translate-x-0 transition-all"> ➔</span>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <footer class="bg-slate-900 text-slate-400 py-10 border-t border-slate-800">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm md:flex md:justify-between md:items-center">
            <p>World Youth Alliance Educational Portal &copy; 2026</p>
            <div class="mt-4 md:mt-0 flex justify-center space-x-6">
                <a href="#" class="hover:text-white transition-colors">Privacy</a>
                <a href="#" class="hover:text-white transition-colors">Terms</a>
                <a href="#" class="hover:text-white transition-colors">Contact</a>
            </div>
        </div>
    </footer>

    <!-- Scripts for theme and scroll functionality -->
    <script>
        (function() {{
            // Smooth Scroll active state
            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('.nav-link');

            window.addEventListener('scroll', () => {{
                let current = '';
                sections.forEach(section => {{
                    const sectionTop = section.offsetTop;
                    if (scrollY >= sectionTop - 150) {{
                        current = section.getAttribute('id');
                    }}
                }});

                navLinks.forEach(link => {{
                    link.classList.remove('active');
                    if (link.getAttribute('href').includes(current)) {{
                        link.classList.add('active');
                    }}
                }});
            }});

            // Theme Toggle Logic
            const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
            const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
            const themeToggleBtn = document.getElementById('theme-toggle');

            if (themeToggleDarkIcon && themeToggleLightIcon && themeToggleBtn) {{
                if (localStorage.getItem('color-theme') === 'dark') {{
                    themeToggleLightIcon.classList.remove('hidden');
                    document.documentElement.classList.add('dark');
                }} else {{
                    themeToggleDarkIcon.classList.remove('hidden');
                    document.documentElement.classList.remove('dark');
                }}

                themeToggleBtn.addEventListener('click', function() {{
                    themeToggleDarkIcon.classList.toggle('hidden');
                    themeToggleLightIcon.classList.toggle('hidden');

                    if (localStorage.getItem('color-theme')) {{
                        if (localStorage.getItem('color-theme') === 'light') {{
                            document.documentElement.classList.add('dark');
                            localStorage.setItem('color-theme', 'dark');
                        }} else {{
                            document.documentElement.classList.remove('dark');
                            localStorage.setItem('color-theme', 'light');
                        }}
                    }} else {{
                        document.documentElement.classList.add('dark');
                        localStorage.setItem('color-theme', 'dark');
                    }}
                }});
            }}
        }})();
    </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("index.html created successfully.")
