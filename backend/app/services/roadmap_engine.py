from typing import Dict, Any, List

CAREER_CURRICULUM_TEMPLATES = {
    "Android Developer": {
        "description": "Master Kotlin, Android Studio, Jetpack Compose, ViewModel, Room DB, Retrofit REST APIs, MVVM Architecture, and Google Play Store deployment.",
        "prerequisites": "Basic programming logic & OOP concepts",
        "weekly_hours": "10 - 15 hrs / week",
        "career_outcomes": ["Android Developer", "Mobile App Engineer", "Kotlin Developer"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Programming & Kotlin Foundations",
                "duration_weeks": 4,
                "skills_covered": ["Kotlin 2.0+", "OOP in Kotlin", "Null Safety", "Collections & Lambdas", "Git & GitHub"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Kotlin Core Syntax & Variables", "topics": ["Variables", "Val vs Var", "Data Types", "Conditionals", "Functions"], "practice": "Build a CLI Math & String utility in Kotlin"},
                    {"week": 2, "title": "Object-Oriented Kotlin & Classes", "topics": ["Classes", "Constructors", "Inheritance", "Interfaces", "Data Classes"], "practice": "Create an OOP Student Management script"},
                    {"week": 3, "title": "Kotlin Collections & Functional Ops", "topics": ["Lists", "Maps", "Sets", "Filter", "Map", "Reduce", "Null Safety (?. ?: !!)"], "practice": "Build an in-memory inventory parser"},
                    {"week": 4, "title": "Coroutines Basics & Git Basics", "topics": ["Asynchronous Programming", "Dispatchers", "Git Branching", "Pull Requests"], "practice": "Solve 10 Kotlin coding challenges on HackerRank"}
                ],
                "milestone_project": "Custom Kotlin Algorithmic Problem Suite & CLI Application",
                "learning_resources": [
                    {"title": "Kotlin Official Documentation", "url": "https://kotlinlang.org/docs/home.html", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "Android Developer Kotlin Basics", "url": "https://developer.android.com/courses/kotlin-bootcamp/overview", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "Android Studio & UI Development",
                "duration_weeks": 4,
                "skills_covered": ["Android Studio IDE", "Jetpack Compose", "Layouts & Modifiers", "State Management", "Material Design 3"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Android Studio Setup & Compose Basics", "topics": ["Project Anatomy", "Composable Functions", "Preview Tool", "Text", "Button", "Image"], "practice": "Build a Business Card App"},
                    {"week": 6, "title": "Compose Layouts & Modifiers", "topics": ["Column", "Row", "Box", "LazyColumn (Lists)", "Padding", "Alignment"], "practice": "Build a scrollable Recipe List App"},
                    {"week": 7, "title": "State Management in Compose", "topics": ["remember", "mutableStateOf", "State Hoisting", "Recomposition"], "practice": "Build an interactive Counter & Tip Calculator App"},
                    {"week": 8, "title": "Material Design 3 & Theming", "topics": ["Color Schemes", "Typography", "Cards", "TopAppBar", "BottomNavigation"], "practice": "Style a modern Shopping Cart UI"}
                ],
                "milestone_project": "Interactive Task Manager App with Jetpack Compose & Material 3",
                "learning_resources": [
                    {"title": "Android Jetpack Compose Docs", "url": "https://developer.android.com/jetpack/compose", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "Google Android Compose Pathway", "url": "https://developer.android.com/courses/pathways/compose", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "Data Persistence, REST APIs & MVVM",
                "duration_weeks": 4,
                "skills_covered": ["Retrofit 2", "OkHttp", "JSON Parsing", "Room Database", "ViewModel & LiveData/Flow", "Repository Pattern"],
                "weekly_breakdown": [
                    {"week": 9, "title": "Networking with Retrofit", "topics": ["REST APIs", "GET/POST requests", "Moshi/Gson Converters", "OkHttp Interceptors"], "practice": "Fetch weather forecasts from OpenWeather API"},
                    {"week": 10, "title": "Local Storage with Room DB", "topics": ["Entities", "DAOs", "Room Database Instance", "Migrations", "DataStore"], "practice": "Build an offline Notes App"},
                    {"week": 11, "title": "ViewModel & Kotlin Flow", "topics": ["ViewModel Lifecycle", "StateFlow", "SharedFlow", "UI State handling"], "practice": "Connect Weather API to ViewModel"},
                    {"week": 12, "title": "MVVM & Repository Architecture", "topics": ["MVVM Pattern", "Single Source of Truth", "Repository Abstraction"], "practice": "Refactor Notes App to full MVVM Pattern"}
                ],
                "milestone_project": "Full MVVM News & Weather App with Offline Room Caching & REST API",
                "learning_resources": [
                    {"title": "Retrofit Documentation", "url": "https://square.github.io/retrofit/", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "Room DB Guide", "url": "https://developer.android.com/training/data-storage/room", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Advanced Android Architecture & Testing",
                "duration_weeks": 4,
                "skills_covered": ["Hilt / Dagger DI", "WorkManager", "Unit Testing", "UI Testing (Espresso/Compose Test)", "Clean Architecture"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Dependency Injection with Hilt", "topics": ["@HiltAndroidApp", "@Inject", "Modules", "@Provides", "@Singleton"], "practice": "Inject Retrofit & Room DB using Hilt"},
                    {"week": 14, "title": "Background Tasks & WorkManager", "topics": ["OneTimeWorkRequest", "PeriodicWorkRequest", "Constraints", "Notifications"], "practice": "Schedule daily notification updates"},
                    {"week": 15, "title": "Unit Testing & MockK", "topics": ["JUnit 5", "MockK", "Testing ViewModels", "Testing Repositories"], "practice": "Write 80%+ coverage unit tests for ViewModels"},
                    {"week": 16, "title": "Clean Architecture & Modularization", "topics": ["Domain Layer", "Use Cases", "Data Layer", "Presentation Layer"], "practice": "Structure project into Multi-module Clean Architecture"}
                ],
                "milestone_project": "Production-Grade E-Commerce Android App with Hilt, MVVM & Unit Tests",
                "learning_resources": [
                    {"title": "Dagger Hilt Docs", "url": "https://developer.android.com/training/dependency-injection/hilt-android", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "App Deployment, Portfolio & Job Preparation",
                "duration_weeks": 4,
                "skills_covered": ["Google Play Console", "App Signing (Keystore)", "ProGuard/R8", "GitHub Portfolio", "Android Interview Prep"],
                "weekly_breakdown": [
                    {"week": 17, "title": "App Optimization & Security", "topics": ["ProGuard Rules", "Obfuscation", "Memory Leaks (LeakCanary)", "App Bundle (.aab)"], "practice": "Generate signed release APK & AAB bundle"},
                    {"week": 18, "title": "Play Store Submission", "topics": ["Play Console Setup", "Privacy Policy", "Store Listings", "Screenshots & Graphic Assets"], "practice": "Publish app to Google Play Store / Internal Testing"},
                    {"week": 19, "title": "GitHub Portfolio & Resume Tuning", "topics": ["Project READMEs", "Architecture Diagrams", "Quantified Achievements"], "practice": "Build impressive GitHub Android showcase"},
                    {"week": 20, "title": "Android Interview Preparation", "topics": ["Android Internal Questions", "Lifecycle edge cases", "Coroutines vs Threads", "Mock Interviews"], "practice": "Complete 3 mock technical interviews"}
                ],
                "milestone_project": "Published Play Store App & Interactive GitHub Android Portfolio",
                "learning_resources": [
                    {"title": "Play Console Documentation", "url": "https://support.google.com/googleplay/android-developer", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            }
        ]
    },
    "Data Analyst": {
        "description": "Master Excel, Advanced SQL, Statistics, Data Manipulation with Python (Pandas/NumPy), Data Visualization (PowerBI / Tableau), and Business Analytics.",
        "prerequisites": "Basic spreadsheet awareness & analytical mindset",
        "weekly_hours": "8 - 12 hrs / week",
        "career_outcomes": ["Data Analyst", "Business Intelligence Analyst", "Analytics Consultant"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Excel & Statistical Foundations",
                "duration_weeks": 4,
                "skills_covered": ["Advanced Excel", "XLOOKUP / INDEX MATCH", "Pivot Tables", "Descriptive Statistics", "Probability"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Excel Data Cleaning & Functions", "topics": ["Text Functions", "Logical Functions (IF/AND/OR)", "XLOOKUP", "Conditional Formatting"], "practice": "Clean messy raw sales dataset in Excel"},
                    {"week": 2, "title": "Pivot Tables & Excel Dashboards", "topics": ["Pivot Charts", "Slicers", "Calculated Fields", "Dynamic Dashboards"], "practice": "Build an Executive Sales KPI Dashboard"},
                    {"week": 3, "title": "Descriptive Statistics for Data Analysis", "topics": ["Mean/Median/Mode", "Variance & Standard Deviation", "IQR & Outliers", "Distributions"], "practice": "Calculate statistical metrics on retail data"},
                    {"week": 4, "title": "Probability & Hypothesis Basics", "topics": ["Normal Distribution", "Z-Scores", "Correlation vs Causation", "A/B Testing Intuition"], "practice": "Conduct correlation analysis on marketing data"}
                ],
                "milestone_project": "Interactive Excel Financial & Sales Performance Dashboard",
                "learning_resources": [
                    {"title": "Microsoft Excel Learning Hub", "url": "https://support.microsoft.com/en-us/excel", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "SQL & Relational Databases",
                "duration_weeks": 4,
                "skills_covered": ["SQL Queries", "JOINs (Inner, Left, Outer)", "GROUP BY & Aggregations", "Subqueries & CTEs", "Window Functions"],
                "weekly_breakdown": [
                    {"week": 5, "title": "SQL Core Syntax & Filtering", "topics": ["SELECT", "WHERE", "ORDER BY", "LIKE", "IN", "BETWEEN", "GROUP BY", "HAVING"], "practice": "Solve 15 SQL query exercises on LeetCode/Mode"},
                    {"week": 6, "title": "Database JOINs & Entity Relationships", "topics": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "Self JOINs", "Foreign Keys"], "practice": "Join customer, order, and product tables"},
                    {"week": 7, "title": "Subqueries & Common Table Expressions (CTEs)", "topics": ["Nested Queries", "WITH Clause (CTEs)", "Temporary Tables"], "practice": "Build multi-step analytical queries"},
                    {"week": 8, "title": "Advanced SQL Window Functions", "topics": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "LEAD()", "LAG()", "Running Totals"], "practice": "Compute month-over-month revenue growth"}
                ],
                "milestone_project": "Complex E-Commerce SQL Analytics Query Suite & Report",
                "learning_resources": [
                    {"title": "Mode Analytics SQL Tutorial", "url": "https://mode.com/sql-tutorial/", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "PostgreSQL Tutorial", "url": "https://www.postgresqltutorial.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "Python for Data Analysis (Pandas & NumPy)",
                "duration_weeks": 4,
                "skills_covered": ["Python 3", "Pandas DataFrames", "NumPy Arrays", "Data Cleaning", "Matplotlib & Seaborn"],
                "weekly_breakdown": [
                    {"week": 9, "title": "Python Core for Data", "topics": ["Data Structures", "Functions", "Lambda Expressions", "File I/O"], "practice": "Write Python scripts to parse CSV files"},
                    {"week": 10, "title": "Data Wrangling with Pandas", "topics": ["Series & DataFrames", "loc & iloc", "Handling Missing Values", "Merging & GroupBy"], "practice": "Clean dataset of 100k records in Pandas"},
                    {"week": 11, "title": "NumPy Vectorized Computation", "topics": ["Ndarrays", "Indexing", "Broadcasting", "Math Functions"], "practice": "Perform matrix operations on analytical data"},
                    {"week": 12, "title": "Data Visualization with Seaborn", "topics": ["Histograms", "Scatter Plots", "Box Plots", "Heatmaps"], "practice": "Generate EDA report plots"}
                ],
                "milestone_project": "Exploratory Data Analysis (EDA) Jupyter Notebook on Real Dataset",
                "learning_resources": [
                    {"title": "Pandas Official Documentation", "url": "https://pandas.pydata.org/docs/", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "Kaggle Pandas Course", "url": "https://www.kaggle.com/learn/pandas", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Business Intelligence (Power BI / Tableau)",
                "duration_weeks": 4,
                "skills_covered": ["Power BI / Tableau", "Data Modeling", "DAX Formulas", "Interactive Reports", "Storytelling with Data"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Power BI Setup & Power Query", "topics": ["Connecting Data Sources", "Power Query ETL", "Data Transformations"], "practice": "Import SQL & Excel data into Power BI"},
                    {"week": 14, "title": "Data Modeling & DAX Syntax", "topics": ["Star Schema", "Relationships", "DAX Measures (CALCULATE, SUMX, ALL)"], "practice": "Create DAX measure suite for sales metrics"},
                    {"week": 15, "title": "Dashboard Design & Interactivity", "topics": ["Visual Cards", "Bar Charts", "Bookmarks", "Drill-through", "Filters"], "practice": "Build executive interactive dashboard"},
                    {"week": 16, "title": "Business Storytelling & Presentations", "topics": ["Insight Synthesis", "Stakeholder Communication", "Slide Decks"], "practice": "Present 5-minute data story to stakeholders"}
                ],
                "milestone_project": "End-to-End Power BI / Tableau Corporate Executive Dashboard",
                "learning_resources": [
                    {"title": "Microsoft Power BI Guided Learning", "url": "https://learn.microsoft.com/en-us/power-bi/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Portfolio, Interview Prep & Job Applications",
                "duration_weeks": 4,
                "skills_covered": ["GitHub Portfolio", "Kaggle Projects", "Data Analyst Interview Prep", "Resume Keyword Optimization"],
                "weekly_breakdown": [
                    {"week": 17, "title": "Portfolio Setup (GitHub + Medium)", "topics": ["Publishing EDA Notebooks", "Writing Data Case Studies", "Interactive Dashboard Hosting"], "practice": "Publish 3 completed data case studies"},
                    {"week": 18, "title": "SQL & Business Case Interviews", "topics": ["Live SQL Coding", "Metrics Definition Questions", "Case Study Frameworks"], "practice": "Solve 20 live SQL interview questions"},
                    {"week": 19, "title": "Resume & ATS Optimization", "topics": ["Quantifying Data Impact", "Keyword Alignment", "LinkedIn Profile Optimization"], "practice": "Tailor resume for Data Analyst applications"},
                    {"week": 20, "title": "Job Applications & Networking", "topics": ["LinkedIn Jobs", "Wellfound", "Internshala", "Cold Emailing Recruiters"], "practice": "Submit 5 tailored applications daily"}
                ],
                "milestone_project": "Published Online Data Analytics Portfolio & Certified Resume",
                "learning_resources": [
                    {"title": "Kaggle Datasets & Community", "url": "https://www.kaggle.com/datasets", "type": "PRACTICE", "badge": "FREE"}
                ]
            }
        ]
    },
    "Cybersecurity Engineer": {
        "description": "Master Computer Networking (TCP/IP), Linux Administration, Security Fundamentals, Cryptography, Web Security (OWASP Top 10), SIEM Log Analysis, Vulnerability Assessment, and Ethical Hacking.",
        "prerequisites": "Basic computer operating system literacy",
        "weekly_hours": "10 - 15 hrs / week",
        "career_outcomes": ["Cybersecurity Engineer", "Security Analyst", "SOC Analyst", "Penetration Tester"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Networking & Systems Foundations",
                "duration_weeks": 4,
                "skills_covered": ["TCP/IP Stack", "OSI Model", "DNS & DHCP", "Wireshark", "Linux CLI & Bash Scripting"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Computer Networking Core", "topics": ["OSI 7 Layers", "TCP/UDP", "IP Addressing & Subnetting", "DNS", "DHCP"], "practice": "Capture & analyze network packets using Wireshark"},
                    {"week": 2, "title": "Linux Systems Administration", "topics": ["Linux Terminal CLI", "File Permissions (chmod/chown)", "User Management", "Systemd"], "practice": "Set up a Linux server VM in VirtualBox"},
                    {"week": 3, "title": "Bash & Python Scripting for Security", "topics": ["Bash Shell Scripts", "Automation", "Python Sockets", "File Parsing"], "practice": "Write a custom Python Port Scanner script"},
                    {"week": 4, "title": "Network Utilities & Scanning", "topics": ["Nmap", "Netcat", "Ping", "Traceroute", "SSH Security"], "practice": "Scan home network lab using Nmap"}
                ],
                "milestone_project": "Custom Python Network Scanner & Wireshark Log Analysis Suite",
                "learning_resources": [
                    {"title": "Cisco Networking Academy", "url": "https://www.netacad.com/", "type": "COURSE", "badge": "FREE"},
                    {"title": "Linux Journey", "url": "https://linuxjourney.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "Security Fundamentals & Cryptography",
                "duration_weeks": 4,
                "skills_covered": ["Symmetric/Asymmetric Encryption", "Hashing (SHA/MD5)", "Public Key Infrastructure (PKI)", "TLS/SSL", "IAM"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Cryptography Principles", "topics": ["AES", "RSA", "Hashing vs Encryption", "Salting", "HMAC"], "practice": "Encrypt files using OpenSSL CLI"},
                    {"week": 6, "title": "PKI & Digital Certificates", "topics": ["Certificate Authorities", "X.509 Certificates", "SSL/TLS Handshake", "HTTPS"], "practice": "Set up SSL/TLS certificate on Nginx server"},
                    {"week": 7, "title": "Identity & Access Management (IAM)", "topics": ["Authentication vs Authorization", "MFA", "OAuth 2.0", "Active Directory Basics"], "practice": "Configure IAM roles & permissions lab"},
                    {"week": 8, "title": "Security Policies & Risk Assessment", "topics": ["CIA Triad", "Threat Vectors", "Risk Mitigation", "Security Controls"], "practice": "Draft a Corporate Security Policy document"}
                ],
                "milestone_project": "Enterprise PKI Certificate & Cryptographic Security Lab Setup",
                "learning_resources": [
                    {"title": "Coursera Cryptography Course", "url": "https://www.coursera.org/", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "Web Security & OWASP Top 10",
                "duration_weeks": 4,
                "skills_covered": ["OWASP Top 10", "SQL Injection (SQLi)", "Cross-Site Scripting (XSS)", "CSRF", "Burp Suite"],
                "weekly_breakdown": [
                    {"week": 9, "title": "Web Architecture & Burp Suite", "topics": ["HTTP Request/Response", "Burp Suite Proxy", "Intercepting Traffic"], "practice": "Set up Burp Suite Proxy and inspect browser requests"},
                    {"week": 10, "title": "SQL Injection & Database Attacks", "topics": ["Inband SQLi", "Blind SQLi", "SQLMap tool", "Parameterized Queries"], "practice": "Exploit SQLi vulnerabilities in DVWA lab"},
                    {"week": 11, "title": "Cross-Site Scripting (XSS) & CSRF", "topics": ["Reflected XSS", "Stored XSS", "DOM XSS", "CSRF Tokens", "Content Security Policy"], "practice": "Complete PortSwigger Web Security Academy XSS labs"},
                    {"week": 12, "title": "Authentication & Session Flaws", "topics": ["Session Hijacking", "Cookie Security", "Broken Access Control"], "practice": "Audit vulnerable web application for access control bugs"}
                ],
                "milestone_project": "PortSwigger Web Security Academy Labs Completion & Audit Report",
                "learning_resources": [
                    {"title": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "type": "PRACTICE", "badge": "FREE"},
                    {"title": "OWASP Top 10 Documentation", "url": "https://owasp.org/www-project-top-ten/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "SOC Analysis, SIEM & Threat Hunting",
                "duration_weeks": 4,
                "skills_covered": ["SIEM (Splunk / Elastic)", "Log Analysis", "Incident Response", "Snort / Suricata IDS", "Threat Intelligence"],
                "weekly_breakdown": [
                    {"week": 13, "title": "SIEM Fundamentals with Splunk", "topics": ["Log Ingestion", "SPL Queries", "Dashboards", "Alerting Rules"], "practice": "Analyze Windows Event Logs in Splunk"},
                    {"week": 14, "title": "Network Intrusion Detection (IDS/IPS)", "topics": ["Snort Rules", "Suricata", "Packet Inspection", "Signatures"], "practice": "Write custom Snort rules to detect attack patterns"},
                    {"week": 15, "title": "Incident Response Lifecycle", "topics": ["NIST Framework", "Preparation", "Detection", "Containment", "Eradication"], "practice": "Conduct simulated incident response exercise"},
                    {"week": 16, "title": "TryHackMe Security Labs", "topics": ["SOC Level 1 Pathway", "Malware Analysis Basics", "Memory Forensics (Volatility)"], "practice": "Complete TryHackMe SOC Analyst Room"}
                ],
                "milestone_project": "Deployed Splunk SIEM & Intrusion Detection Threat Hunting Lab",
                "learning_resources": [
                    {"title": "TryHackMe Cyber Security", "url": "https://tryhackme.com/", "type": "PRACTICE", "badge": "FREE"},
                    {"title": "Splunk Fundamentals", "url": "https://www.splunk.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Certifications, Portfolio & Career Preparation",
                "duration_weeks": 4,
                "skills_covered": ["CompTIA Security+", "EJPT / CEH Prep", "Security Audit Reports", "Cybersecurity Interviews"],
                "weekly_breakdown": [
                    {"week": 17, "title": "Security+ / eJPT Exam Prep", "topics": ["Domain Review", "Practice Exams", "Lab Challenges"], "practice": "Complete 3 full-length Security+ mock exams"},
                    {"week": 18, "title": "Vulnerability Assessment Reporting", "topics": ["CVSS Scoring", "Executive Summaries", "Remediation Steps"], "practice": "Write a professional Vulnerability Audit Report"},
                    {"week": 19, "title": "GitHub & HackTheBox Profile Setup", "topics": ["Publishing Security Tools", "Documenting Write-ups"], "practice": "Publish 5 CTF write-ups on GitHub"},
                    {"week": 20, "title": "Cybersecurity Interview Preparation", "topics": ["Technical Scenarios", "Network Troubleshooting", "Behavioral Rounds"], "practice": "Complete 3 mock security engineer interviews"}
                ],
                "milestone_project": "Published Security Audit Portfolio & Certified Resume",
                "learning_resources": [
                    {"title": "Hack The Box", "url": "https://www.hackthebox.com/", "type": "PRACTICE", "badge": "FREE"}
                ]
            }
        ]
    },
    "Frontend Developer": {
        "description": "Master HTML5, Modern CSS (Flexbox/Grid/Tailwind), JavaScript ES6+, TypeScript, React 18+, State Management, REST API Consumption, Web Performance, and Responsive UI Design.",
        "prerequisites": "Basic computer & web browser literacy",
        "weekly_hours": "8 - 12 hrs / week",
        "career_outcomes": ["Frontend Developer", "React Engineer", "UI Engineer"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "HTML5, Modern CSS & Tailwind CSS",
                "duration_weeks": 4,
                "skills_covered": ["Semantic HTML5", "CSS Flexbox", "CSS Grid", "Tailwind CSS", "Responsive Design"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Semantic HTML5 & Accessibility", "topics": ["HTML Elements", "Forms", "A11y", "ARIA Attributes", "SEO Meta Tags"], "practice": "Build an accessible multi-page personal website"},
                    {"week": 2, "title": "CSS Layouts: Flexbox & Grid", "topics": ["Box Model", "Flexbox", "CSS Grid", "Media Queries", "Positioning"], "practice": "Style a responsive 3-column landing page"},
                    {"week": 3, "title": "Tailwind CSS Utility Design", "topics": ["Tailwind Setup", "Utility Classes", "Custom Config", "Dark Mode"], "practice": "Recreate a sleek Glassmorphic UI layout with Tailwind"},
                    {"week": 4, "title": "CSS Animations & Transitions", "topics": ["Keyframes", "Transforms", "Transitions", "Hover States"], "practice": "Build animated component cards"}
                ],
                "milestone_project": "Responsive Multi-Page SaaS Landing Page with Tailwind CSS",
                "learning_resources": [
                    {"title": "MDN Web Docs - HTML & CSS", "url": "https://developer.mozilla.org/", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "freeCodeCamp Responsive Web Design", "url": "https://www.freecodecamp.org/", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "JavaScript ES6+ & DOM Manipulation",
                "duration_weeks": 4,
                "skills_covered": ["JavaScript Fundamentals", "DOM API", "Event Handling", "Async/Await & Fetch", "ES6 Modules"],
                "weekly_breakdown": [
                    {"week": 5, "title": "JavaScript Core Concepts", "topics": ["Variables (const/let)", "Data Types", "Functions", "Scope", "Closures"], "practice": "Build a JS Calculator & Quiz App"},
                    {"week": 6, "title": "DOM Manipulation & Events", "topics": ["querySelector", "createElement", "addEventListener", "Event Delegation"], "practice": "Build a dynamic To-Do App with LocalStorage"},
                    {"week": 7, "title": "Async JavaScript & Fetch API", "topics": ["Promises", "Async/Await", "Fetch API", "Handling HTTP Errors"], "practice": "Fetch & render live weather data from OpenWeather API"},
                    {"week": 8, "title": "ES6+ Modules & Data Structures", "topics": ["Destructuring", "Spread Operator", "Array Methods (map/filter/reduce)", "Modules"], "practice": "Build an e-commerce product filter script"}
                ],
                "milestone_project": "Interactive Weather & Movie Search Web App in Vanilla JS",
                "learning_resources": [
                    {"title": "JavaScript.info", "url": "https://javascript.info/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "React 18, TypeScript & Component Architecture",
                "duration_weeks": 4,
                "skills_covered": ["React 18", "JSX", "Hooks (useState, useEffect, useRef)", "TypeScript", "React Router v6"],
                "weekly_breakdown": [
                    {"week": 9, "title": "React Core & JSX", "topics": ["Components", "Props", "JSX Syntax", "Rendering Lists"], "practice": "Build a React Expense Tracker App"},
                    {"week": 10, "title": "React Hooks & Lifecycle", "topics": ["useState", "useEffect", "useRef", "Custom Hooks"], "practice": "Build a custom auto-saving form hook"},
                    {"week": 11, "title": "TypeScript Integration", "topics": ["Interfaces", "Types", "React Prop Types", "Generic Types"], "practice": "Migrate React Expense Tracker to TypeScript"},
                    {"week": 12, "title": "Routing with React Router v6", "topics": ["BrowserRouter", "Routes", "Route", "Link", "Params & Query Strings"], "practice": "Build a multi-view E-Commerce UI"}
                ],
                "milestone_project": "TypeScript + React E-Commerce Storefront with Shopping Cart",
                "learning_resources": [
                    {"title": "React Official Documentation", "url": "https://react.dev/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "State Management, Testing & Web Performance",
                "duration_weeks": 4,
                "skills_covered": ["Redux Toolkit / Context API", "Vitest & React Testing Library", "Web Vitals", "Code Splitting", "Git Workflow"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Global State Management", "topics": ["Context API", "Redux Toolkit", "createSlice", "useSelector/useDispatch"], "practice": "Manage global user session & cart state"},
                    {"week": 14, "title": "Component Testing", "topics": ["Vitest", "React Testing Library", "Mocking API Requests"], "practice": "Write unit tests for UI components"},
                    {"week": 15, "title": "Web Performance & Optimization", "topics": ["React.memo", "useMemo", "useCallback", "Lazy Loading & Suspense", "Lighthouse"], "practice": "Optimize page speed score to 90+"},
                    {"week": 16, "title": "Vite Build & Deployment", "topics": ["Vite Config", "Vercel / Netlify Deployment", "CI/CD GitHub Actions"], "practice": "Deploy live React app to Vercel"}
                ],
                "milestone_project": "Production-Grade React + TypeScript SaaS Application Deployed on Vercel",
                "learning_resources": [
                    {"title": "Vercel Deployment Docs", "url": "https://vercel.com/docs", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Portfolio, Interview Prep & Job Applications",
                "duration_weeks": 4,
                "skills_covered": ["GitHub Portfolio", "Frontend System Design", "Coding Challenges", "Resume Optimization"],
                "weekly_breakdown": [
                    {"week": 17, "title": "GitHub Portfolio Showcase", "topics": ["Clean Code", "Project READMEs", "Live Demos"], "practice": "Polish top 3 GitHub frontend projects"},
                    {"week": 18, "title": "Frontend Interview Coding", "topics": ["JS Polyfills", "Debounce/Throttle", "DOM Tree Operations"], "practice": "Implement Debounce & Event Emitter from scratch"},
                    {"week": 19, "title": "Frontend System Design", "topics": ["Component Design", "State Architecture", "Caching Strategies"], "practice": "Design infinite scroll newsfeed architecture"},
                    {"week": 20, "title": "Job Applications & Mock Interviews", "topics": ["LinkedIn Jobs", "Wellfound", "Mock Technical Interviews"], "practice": "Complete 3 mock frontend technical interviews"}
                ],
                "milestone_project": "Deploved Personal Portfolio Website & Interview Ready Resume",
                "learning_resources": [
                    {"title": "GreatFrontEnd Interview Guide", "url": "https://www.greatfrontend.com/", "type": "PRACTICE", "badge": "FREE"}
                ]
            }
        ]
    },
    "AI Engineer": {
        "description": "Master Python, Mathematics for AI, Machine Learning (Scikit-Learn), Deep Learning (PyTorch / TensorFlow), Large Language Models (LLMs), LangChain, Vector DBs, and MLOps.",
        "prerequisites": "Basic Python programming logic",
        "weekly_hours": "12 - 16 hrs / week",
        "career_outcomes": ["AI Engineer", "ML Engineer", "LLM Specialist", "AI Solutions Architect"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Python for AI, Math & Data Foundations",
                "duration_weeks": 4,
                "skills_covered": ["Python 3.11+", "NumPy & Pandas", "Linear Algebra", "Calculus & Probability", "Matplotlib"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Advanced Python & Data Structures", "topics": ["List Comprehensions", "Generators", "OOP in Python", "Type Hinting"], "practice": "Build a modular matrix processing script"},
                    {"week": 2, "title": "NumPy & Linear Algebra", "topics": ["Vectors", "Matrices", "Eigenvalues", "Vectorized Math"], "practice": "Implement Matrix Multiplication & SVD from scratch"},
                    {"week": 3, "title": "Calculus, Derivatives & Optimization", "topics": ["Gradient Descent", "Partial Derivatives", "Loss Functions"], "practice": "Implement Gradient Descent optimization algorithm"},
                    {"week": 4, "title": "Pandas & Exploratory Data Analysis (EDA)", "topics": ["Data Cleaning", "Feature Engineering", "Data Visualizations"], "practice": "Perform complete EDA on Kaggle dataset"}
                ],
                "milestone_project": "Custom Python Mathematical Engine & Automated EDA Notebook",
                "learning_resources": [
                    {"title": "Khan Academy Multivariable Calculus", "url": "https://www.khanacademy.org/", "type": "COURSE", "badge": "FREE"},
                    {"title": "NumPy Official Documentation", "url": "https://numpy.org/doc/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "Classical Machine Learning (Scikit-Learn)",
                "duration_weeks": 4,
                "skills_covered": ["Scikit-Learn", "Regression & Classification", "Random Forests", "XGBoost", "Model Evaluation"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Supervised Learning: Regression", "topics": ["Linear Regression", "Ridge/Lasso", "MSE", "R-squared"], "practice": "Build a House Price Prediction Model"},
                    {"week": 6, "title": "Supervised Learning: Classification", "topics": ["Logistic Regression", "Decision Trees", "SVMs", "Precision/Recall/F1"], "practice": "Build a Customer Churn Predictor"},
                    {"week": 7, "title": "Ensemble Methods & Boosting", "topics": ["Random Forest", "Gradient Boosting", "XGBoost", "Hyperparameter Tuning"], "practice": "Train XGBoost model on tabular data"},
                    {"week": 8, "title": "Unsupervised Learning & Clustering", "topics": ["K-Means Clustering", "PCA", "Dimensionality Reduction"], "practice": "Cluster customers based on purchasing behavior"}
                ],
                "milestone_project": "End-to-End Predictive Machine Learning Pipeline with Scikit-Learn",
                "learning_resources": [
                    {"title": "Scikit-Learn Documentation", "url": "https://scikit-learn.org/stable/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "Deep Learning & Neural Networks (PyTorch)",
                "duration_weeks": 4,
                "skills_covered": ["PyTorch", "Neural Networks (ANN)", "Convolutional Nets (CNN)", "Recurrent Nets (RNN/LSTM)", "Transfer Learning"],
                "weekly_breakdown": [
                    {"week": 9, "title": "PyTorch Tensors & Autograd", "topics": ["Tensors", "Automatic Differentiation", "Custom Dataset & DataLoader"], "practice": "Build a Perceptron from scratch in PyTorch"},
                    {"week": 10, "title": "Deep Neural Networks (DNN)", "topics": ["Activations (ReLU, Softmax)", "CrossEntropyLoss", "Adam Optimizer"], "practice": "Train Deep Neural Net on MNIST Digit Recognition"},
                    {"week": 11, "title": "Computer Vision with CNNs", "topics": ["Convolutions", "Pooling", "ResNet Architecture", "Transfer Learning"], "practice": "Build an Image Classification API with PyTorch ResNet"},
                    {"week": 12, "title": "Sequence Models (RNN / LSTM / Transformers)", "topics": ["Sequential Data", "Embeddings", "Self-Attention Mechanism"], "practice": "Build a Sentiment Analysis model"}
                ],
                "milestone_project": "Computer Vision & Natural Language Deep Learning Suite in PyTorch",
                "learning_resources": [
                    {"title": "Deep Learning with PyTorch Book", "url": "https://pytorch.org/deep-learning-with-pytorch", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Generative AI, LLMs & RAG Architectures",
                "duration_weeks": 4,
                "skills_covered": ["Hugging Face Transformers", "OpenAI / Anthropic APIs", "LangChain & LlamaIndex", "Vector DBs (Chroma/Pinecone)", "RAG Systems"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Hugging Face & Transformer Models", "topics": ["Tokenizers", "AutoModel", "Fine-tuning with PEFT/LoRA"], "practice": "Fine-tune an open-source LLM on custom dataset"},
                    {"week": 14, "title": "Prompt Engineering & Function Calling", "topics": ["System Prompts", "Structured Outputs", "Tools & Function Calling"], "practice": "Build an AI Agent with tool execution"},
                    {"week": 15, "title": "Retrieval-Augmented Generation (RAG)", "topics": ["Embeddings", "Vector Stores (Chroma)", "Chunking Strategies", "RAG Pipelines"], "practice": "Build a Document Q&A Chatbot over custom PDFs"},
                    {"week": 16, "title": "LangChain & Multi-Agent Frameworks", "topics": ["LangChain LCEL", "LangGraph", "Memory", "Agent Workflows"], "practice": "Build an Autonomous AI Research Agent"}
                ],
                "milestone_project": "Production-Grade Autonomous RAG AI Chatbot with LangChain & Vector DB",
                "learning_resources": [
                    {"title": "Hugging Face Course", "url": "https://huggingface.co/course", "type": "COURSE", "badge": "FREE"},
                    {"title": "LangChain Documentation", "url": "https://python.langchain.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "MLOps, Deployment & Portfolio",
                "duration_weeks": 4,
                "skills_covered": ["FastAPI", "Docker", "MLflow", "vLLM / Ollama Serving", "Model Monitoring", "Portfolio"],
                "weekly_breakdown": [
                    {"week": 17, "title": "AI API Development with FastAPI", "topics": ["REST Endpoints", "Streaming Responses (SSE)", "Async Execution"], "practice": "Expose PyTorch/LLM model via FastAPI stream"},
                    {"week": 18, "title": "Containerization & Local Serving", "topics": ["Dockerizing AI Services", "vLLM", "Ollama", "Gunicorn/Uvicorn"], "practice": "Package AI API into Docker container"},
                    {"week": 19, "title": "MLOps & Experiment Tracking", "topics": ["MLflow", "Weights & Biases", "Model Registry", "CI/CD Pipelines"], "practice": "Track hyperparameters and metrics using MLflow"},
                    {"week": 20, "title": "Portfolio Showcase & Interview Preparation", "topics": ["GitHub Repos", "System Design for AI", "Coding Interviews"], "practice": "Complete 3 AI System Design mock interviews"}
                ],
                "milestone_project": "Deployed Cloud AI Application with Production API, MLOps Tracking & Web UI",
                "learning_resources": [
                    {"title": "FastAPI Documentation", "url": "https://fastapi.tiangolo.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            }
        ]
    }
}


def generate_dynamic_curriculum(career: str) -> Dict[str, Any]:
    """Generates a structured, career-specific fallback curriculum for unlisted careers."""
    clean_career = career.strip().title()
    return {
        "description": f"Master foundational concepts, core specialized frameworks, practical projects, and professional job preparation tailored specifically for {clean_career}.",
        "prerequisites": "Basic computer literacy and enthusiasm to learn",
        "weekly_hours": "10 - 15 hrs / week",
        "career_outcomes": [clean_career, f"Junior {clean_career}", f"Specialist {clean_career}"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": f"{clean_career} Core Foundations",
                "duration_weeks": 4,
                "skills_covered": [f"{clean_career} Basics", "Tooling Setup", "Fundamental Principles", "Git & GitHub"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Environment & Core Concepts", "topics": ["Tool installation", "Syntax basics", "Directory setup"], "practice": "Build a hello-world CLI script"},
                    {"week": 2, "title": "Fundamental Building Blocks", "topics": ["Data types", "Control flows", "Logic structures"], "practice": "Complete 5 beginner exercises"},
                    {"week": 3, "title": "Core Library Usage", "topics": ["Standard library", "Package management", "Debugging"], "practice": "Build an in-memory utility"},
                    {"week": 4, "title": "Version Control & Project Setup", "topics": ["Git init", "Commits", "Branches", "GitHub repo"], "practice": "Push project to GitHub"}
                ],
                "milestone_project": f"Foundational {clean_career} CLI Utility & Exercise Suite",
                "learning_resources": [
                    {"title": f"Official {clean_career} Documentation", "url": "https://google.com", "type": "DOCUMENTATION", "badge": "FREE"},
                    {"title": "freeCodeCamp", "url": "https://www.freecodecamp.org/", "type": "COURSE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": f"Specialized {clean_career} Frameworks & Tools",
                "duration_weeks": 4,
                "skills_covered": ["Industry Frameworks", "API Integration", "Database Connection", "Best Practices"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Primary Framework Setup", "topics": ["Framework architecture", "Routing/Flow", "Configuration"], "practice": "Build a mini framework demo"},
                    {"week": 6, "title": "Data Persistence & Storage", "topics": ["Relational DBs", "JSON handling", "Querying"], "practice": "Connect application to database"},
                    {"week": 7, "title": "Third-Party API Consumption", "topics": ["HTTP Requests", "REST Endpoints", "Parsing responses"], "practice": "Fetch & render external API data"},
                    {"week": 8, "title": "Security & Validation", "topics": ["Input sanitization", "Error handling", "Validation schemas"], "practice": "Add security validation logic"}
                ],
                "milestone_project": f"Interactive {clean_career} Web/Data Application",
                "learning_resources": [
                    {"title": "Official Developer Guides", "url": "https://developer.mozilla.org/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "Advanced Architecture & Systems",
                "duration_weeks": 4,
                "skills_covered": ["Design Patterns", "Clean Code", "Testing & QA", "Performance Tuning"],
                "weekly_breakdown": [
                    {"week": 9, "title": "Architectural Design Patterns", "topics": ["MVC/MVVM", "Dependency Injection", "Repositories"], "practice": "Refactor codebase to clean architecture"},
                    {"week": 10, "title": "Unit & Integration Testing", "topics": ["Test runners", "Mocking", "Test coverage"], "practice": "Write unit tests for core modules"},
                    {"week": 11, "title": "Performance Optimization", "topics": ["Caching", "Profiling", "Latency reduction"], "practice": "Optimize application execution speed"},
                    {"week": 12, "title": "Containerization Basics", "topics": ["Dockerfiles", "Docker Compose", "Environment variables"], "practice": "Containerize application using Docker"}
                ],
                "milestone_project": f"Architected & Tested {clean_career} Enterprise Application",
                "learning_resources": [
                    {"title": "Docker Docs", "url": "https://docs.docker.com/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Portfolio Projects & Real-World Building",
                "duration_weeks": 4,
                "skills_covered": ["Full Application Building", "Documentation", "CI/CD", "Production Deployment"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Project Planning & Scope", "topics": ["Requirements", "DB Schema", "UI Wireframes"], "practice": "Draft project specification document"},
                    {"week": 14, "title": "Core Implementation", "topics": ["Feature building", "Integration", "Testing"], "practice": "Implement core product features"},
                    {"week": 15, "title": "Polishing & Documentation", "topics": ["README.md", "Setup guide", "System diagrams"], "practice": "Write comprehensive GitHub README"},
                    {"week": 16, "title": "Cloud Deployment", "topics": ["Cloud hosting", "Domain setup", "CI/CD pipelines"], "practice": "Deploy live application to cloud platform"}
                ],
                "milestone_project": f"Production-Grade Deployed {clean_career} SaaS/Portfolio Product",
                "learning_resources": [
                    {"title": "GitHub Guides", "url": "https://github.com/", "type": "PRACTICE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Interview Prep & Career Placement",
                "duration_weeks": 4,
                "skills_covered": ["Technical Interviews", "Resume ATS Tuning", "Portfolio Showcase", "Job Applications"],
                "weekly_breakdown": [
                    {"week": 17, "title": "Technical Question Review", "topics": ["Core concepts", "Edge cases", "System Design"], "practice": "Practice 15 technical interview questions"},
                    {"week": 18, "title": "Resume & ATS Tuning", "topics": ["Action verbs", "Quantification", "Keyword alignment"], "practice": "Tailor resume for target role"},
                    {"week": 19, "title": "Portfolio Optimization", "topics": ["Live demos", "Video walkthroughs", "LinkedIn profile"], "practice": "Publish complete portfolio"},
                    {"week": 20, "title": "Job Applications & Mock Practice", "topics": ["LinkedIn Jobs", "Wellfound", "Mock Interviews"], "practice": "Apply to 5 target positions daily"}
                ],
                "milestone_project": f"Certified {clean_career} Resume & Published Portfolio Showcase",
                "learning_resources": [
                    {"title": "LinkedIn Jobs", "url": "https://www.linkedin.com/jobs/", "type": "PRACTICE", "badge": "FREE"}
                ]
            }
        ]
    }


def generate_roadmap(target_career: str, duration: str = "6-month", level: str = "Beginner") -> Dict[str, Any]:
    # Lookup in explicit templates or generate dynamic curriculum
    template = CAREER_CURRICULUM_TEMPLATES.get(target_career)
    if not template:
        # Check alias keys
        for key, t in CAREER_CURRICULUM_TEMPLATES.items():
            if key.lower() in target_career.lower() or target_career.lower() in key.lower():
                template = t
                break

    if not template:
        template = generate_dynamic_curriculum(target_career)

    phases = template["phases"]
    # Filter or scale phases based on requested duration
    if duration == "30-day":
        phases = phases[:2]
    elif duration == "3-month":
        phases = phases[:3]

    return {
        "target_career": target_career,
        "duration": duration,
        "level": level,
        "overview": template.get("description", f"Comprehensive career roadmap for {target_career}."),
        "prerequisites": template.get("prerequisites", "Basic computer literacy"),
        "weekly_hours": template.get("weekly_hours", "10 - 15 hrs / week"),
        "career_outcomes": template.get("career_outcomes", [target_career]),
        "phases": phases
    }
