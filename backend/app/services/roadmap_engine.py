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
                    {"week": 3, "title": "Kotlin Collections & Functional Ops", "topics": ["Lists", "Maps", "Sets", "Filter", "Map", "Reduce", "Null Safety"], "practice": "Build an in-memory inventory parser"},
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
                "phase_title": "Android Studio & Jetpack Compose UI",
                "duration_weeks": 4,
                "skills_covered": ["Android Studio IDE", "Jetpack Compose", "Layouts & Modifiers", "State Management", "Material Design 3"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Android Studio Setup & Compose Basics", "topics": ["Project Anatomy", "Composable Functions", "Preview Tool", "Text", "Button"], "practice": "Build a Business Card App"},
                    {"week": 6, "title": "Compose Layouts & Modifiers", "topics": ["Column", "Row", "Box", "LazyColumn", "Padding", "Alignment"], "practice": "Build a scrollable Recipe List App"},
                    {"week": 7, "title": "State Management in Compose", "topics": ["remember", "mutableStateOf", "State Hoisting", "Recomposition"], "practice": "Build an interactive Counter & Tip Calculator App"},
                    {"week": 8, "title": "Material Design 3 & Theming", "topics": ["Color Schemes", "Typography", "Cards", "TopAppBar", "BottomNavigation"], "practice": "Style a modern Shopping Cart UI"}
                ],
                "milestone_project": "Interactive Task Manager App with Jetpack Compose & Material 3",
                "learning_resources": [
                    {"title": "Android Jetpack Compose Docs", "url": "https://developer.android.com/jetpack/compose", "type": "DOCUMENTATION", "badge": "FREE"}
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
                    {"title": "Retrofit Documentation", "url": "https://square.github.io/retrofit/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Advanced Android Architecture & Testing",
                "duration_weeks": 4,
                "skills_covered": ["Hilt Dependency Injection", "WorkManager", "Unit Testing", "Compose Testing", "Clean Architecture"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Dependency Injection with Hilt", "topics": ["@HiltAndroidApp", "@Inject", "Modules", "@Provides", "@Singleton"], "practice": "Inject Retrofit & Room DB using Hilt"},
                    {"week": 14, "title": "Background Tasks & WorkManager", "topics": ["OneTimeWorkRequest", "PeriodicWorkRequest", "Constraints", "Notifications"], "practice": "Schedule daily notification updates"},
                    {"week": 15, "title": "Unit Testing & MockK", "topics": ["JUnit 5", "MockK", "Testing ViewModels", "Testing Repositories"], "practice": "Write unit tests for ViewModels"},
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
                "skills_covered": ["Google Play Console", "App Signing", "ProGuard/R8", "GitHub Portfolio", "Android Interview Prep"],
                "weekly_breakdown": [
                    {"week": 17, "title": "App Optimization & Security", "topics": ["ProGuard Rules", "Obfuscation", "Memory Leaks", "App Bundle (.aab)"], "practice": "Generate signed release APK & AAB bundle"},
                    {"week": 18, "title": "Play Store Submission", "topics": ["Play Console Setup", "Privacy Policy", "Store Listings", "Screenshots"], "practice": "Publish app to Google Play Store / Internal Testing"},
                    {"week": 19, "title": "GitHub Portfolio & Resume Tuning", "topics": ["Project READMEs", "Architecture Diagrams", "Quantified Achievements"], "practice": "Build impressive GitHub Android showcase"},
                    {"week": 20, "title": "Android Interview Preparation", "topics": ["Android Internal Questions", "Lifecycle edge cases", "Coroutines vs Threads"], "practice": "Complete 3 mock technical interviews"}
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
                    {"title": "Microsoft Excel Learning Hub", "url": "https://support.microsoft.com/en-us/excel", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "SQL & Relational Databases",
                "duration_weeks": 4,
                "skills_covered": ["SQL Queries", "JOINs (Inner, Left, Outer)", "GROUP BY & Aggregations", "Subqueries & CTEs", "Window Functions"],
                "weekly_breakdown": [
                    {"week": 5, "title": "SQL Core Syntax & Filtering", "topics": ["SELECT", "WHERE", "ORDER BY", "LIKE", "GROUP BY", "HAVING"], "practice": "Solve 15 SQL query exercises on LeetCode/Mode"},
                    {"week": 6, "title": "Database JOINs & Relationships", "topics": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "Self JOINs"], "practice": "Join customer, order, and product tables"},
                    {"week": 7, "title": "Subqueries & Common Table Expressions (CTEs)", "topics": ["Nested Queries", "WITH Clause (CTEs)", "Temporary Tables"], "practice": "Build multi-step analytical queries"},
                    {"week": 8, "title": "Advanced SQL Window Functions", "topics": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "LEAD()", "LAG()", "Running Totals"], "practice": "Compute month-over-month revenue growth"}
                ],
                "milestone_project": "Complex E-Commerce SQL Analytics Query Suite & Report",
                "learning_resources": [
                    {"title": "Mode Analytics SQL Tutorial", "url": "https://mode.com/sql-tutorial/", "type": "DOCUMENTATION", "badge": "FREE"}
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
                    {"title": "Pandas Official Documentation", "url": "https://pandas.pydata.org/docs/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Business Intelligence (Power BI / Tableau)",
                "duration_weeks": 4,
                "skills_covered": ["Power BI / Tableau", "Data Modeling", "DAX Formulas", "Interactive Reports", "Storytelling with Data"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Power BI Setup & Power Query", "topics": ["Connecting Data Sources", "Power Query ETL", "Data Transformations"], "practice": "Import SQL & Excel data into Power BI"},
                    {"week": 14, "title": "Data Modeling & DAX Syntax", "topics": ["Star Schema", "Relationships", "DAX Measures (CALCULATE, SUMX)"], "practice": "Create DAX measure suite for sales metrics"},
                    {"week": 15, "title": "Dashboard Design & Interactivity", "topics": ["Visual Cards", "Bar Charts", "Bookmarks", "Drill-through"], "practice": "Build executive interactive dashboard"},
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
    "AI Engineer": {
        "description": "Master Python, Mathematics for AI, Machine Learning (Scikit-Learn), Deep Learning (PyTorch), Large Language Models (LLMs), LangChain, Vector DBs, and MLOps.",
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
    },
    "Frontend Developer": {
        "description": "Master HTML5, CSS3, Modern JavaScript (ES6+), TypeScript, React 18, Tailwind CSS, Next.js, and Web Performance Optimization.",
        "prerequisites": "Basic computer operation & web browsing awareness",
        "weekly_hours": "10 - 15 hrs / week",
        "career_outcomes": ["Frontend Developer", "React Engineer", "UI Engineer", "Full Stack Developer"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Web Foundations & Responsive Design",
                "duration_weeks": 4,
                "skills_covered": ["HTML5 & CSS3", "Flexbox & Grid", "Responsive Design", "Git & GitHub", "Web Standards"],
                "weekly_breakdown": [
                    {"week": 1, "title": "HTML5 Semantic Markup", "topics": ["Semantic elements", "Forms & Validation", "Accessibility (a11y)"], "practice": "Build accessible portfolio skeleton"},
                    {"week": 2, "title": "CSS3 Layouts & Styling", "topics": ["Box Model", "Flexbox", "CSS Grid", "Animations"], "practice": "Build responsive landing page layout"},
                    {"week": 3, "title": "Modern CSS & Utility Frameworks", "topics": ["CSS Variables", "Tailwind CSS", "Sass/SCSS"], "practice": "Recreate popular website UI with Tailwind"},
                    {"week": 4, "title": "Git & Web Deployment", "topics": ["Git workflow", "GitHub Pages", "Vercel Deployment"], "practice": "Deploy responsive website live"}
                ],
                "milestone_project": "Responsive Corporate Portfolio Landing Page deployed on Vercel",
                "learning_resources": [
                    {"title": "MDN Web Docs HTML/CSS", "url": "https://developer.mozilla.org/en-US/docs/Learn", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "Modern JavaScript & TypeScript",
                "duration_weeks": 4,
                "skills_covered": ["JavaScript ES6+", "TypeScript", "DOM Manipulation", "Async/Await", "Fetch & REST APIs"],
                "weekly_breakdown": [
                    {"week": 5, "title": "JS Data Structures & Control Flow", "topics": ["Arrays", "Objects", "Arrow Functions", "Array Methods"], "practice": "Build an interactive Todo application"},
                    {"week": 6, "title": "Async JS & Promises", "topics": ["Event Loop", "Promises", "Async/Await", "Fetch API"], "practice": "Build Weather Dashboard using public REST API"},
                    {"week": 7, "title": "TypeScript Fundamentals", "topics": ["Types", "Interfaces", "Generics", "Type Assertions"], "practice": "Convert JS app to TypeScript"},
                    {"week": 8, "title": "DOM & Event Handling", "topics": ["Event Bubbling", "Local Storage", "Form Data"], "practice": "Build interactive Quiz Application"}
                ],
                "milestone_project": "Dynamic API-Driven Dashboard in Pure TypeScript & Fetch API",
                "learning_resources": [
                    {"title": "JavaScript.info", "url": "https://javascript.info/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "React 18 & Component Engineering",
                "duration_weeks": 4,
                "skills_covered": ["React 18", "JSX Syntax", "Hooks (useState, useEffect, useMemo)", "Zustand State", "React Router"],
                "weekly_breakdown": [
                    {"week": 9, "title": "React Core & Component Architecture", "topics": ["JSX", "Props & State", "Component Lifecycle", "Conditional Rendering"], "practice": "Build E-Commerce product catalog"},
                    {"week": 10, "title": "React Hooks & Customs Hooks", "topics": ["useEffect", "useRef", "useMemo", "Custom Hooks"], "practice": "Build custom API fetching hook"},
                    {"week": 11, "title": "Global State & Client Routing", "topics": ["Zustand / Redux Toolkit", "React Router v6", "Dynamic Routes"], "practice": "Build multi-page E-Commerce app with Shopping Cart"},
                    {"week": 12, "title": "API Integration & Form Management", "topics": ["Axios/TanStack Query", "React Hook Form", "Zod Validation"], "practice": "Connect React app to backend API"}
                ],
                "milestone_project": "Production E-Commerce Platform with Cart, Filters & API Integration",
                "learning_resources": [
                    {"title": "React Official Documentation", "url": "https://react.dev/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Next.js 14, SSR & Web Performance",
                "duration_weeks": 4,
                "skills_covered": ["Next.js App Router", "Server Components (RSC)", "Server Actions", "SEO & Core Web Vitals"],
                "weekly_breakdown": [
                    {"week": 13, "title": "Next.js App Router Architecture", "topics": ["Server Components", "Client Components", "Layouts", "Loading UI"], "practice": "Build Next.js blog application"},
                    {"week": 14, "title": "SSR, SSG & ISR Rendering", "topics": ["Static Generation", "Server-Side Rendering", "Revalidation"], "practice": "Implement dynamic CMS rendering"},
                    {"week": 15, "title": "Next.js Server Actions & API Routes", "topics": ["Server Actions", "Route Handlers", "Authentication"], "practice": "Implement user authentication in Next.js"},
                    {"week": 16, "title": "Core Web Vitals & Optimization", "topics": ["Image Optimization", "Bundle Splitting", "SEO Metadata"], "practice": "Achieve 95+ Lighthouse score"}
                ],
                "milestone_project": "Full Stack Next.js SaaS Web Application with Authentication & Database",
                "learning_resources": [
                    {"title": "Next.js Documentation", "url": "https://nextjs.org/docs", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Testing, CI/CD & Portfolio Prep",
                "duration_weeks": 4,
                "skills_covered": ["Jest & React Testing Library", "Playwright E2E", "GitHub Actions CI/CD", "Portfolio Showcase"],
                "weekly_breakdown": [
                    {"week": 17, "title": "Unit & Integration Testing", "topics": ["Jest", "React Testing Library", "Mocking APIs"], "practice": "Write test suite for React components"},
                    {"week": 18, "title": "End-to-End Testing", "topics": ["Playwright", "User flow automation", "CI test runs"], "practice": "Create Playwright E2E test suite"},
                    {"week": 19, "title": "CI/CD & Production Hosting", "topics": ["Vercel", "GitHub Actions", "Domain & SSL Setup"], "practice": "Automate build and deployment pipeline"},
                    {"week": 20, "title": "Frontend Interview Preparation", "topics": ["JavaScript coding challenges", "React System Design", "Mock Interviews"], "practice": "Complete 3 frontend technical interview rounds"}
                ],
                "milestone_project": "Deployed Modern Frontend Portfolio with Tested Apps & Live Demos",
                "learning_resources": [
                    {"title": "Vercel Docs", "url": "https://vercel.com/docs", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            }
        ]
    },
    "Cybersecurity Engineer": {
        "description": "Master Networking, Linux Systems, Security Architecture, OWASP Top 10, Network Pentesting, SOC Operations, SIEM Tools, and Threat Intelligence.",
        "prerequisites": "Basic computer hardware & networking awareness",
        "weekly_hours": "10 - 15 hrs / week",
        "career_outcomes": ["Cybersecurity Engineer", "Penetration Tester", "SOC Analyst", "Information Security Specialist"],
        "phases": [
            {
                "phase_number": 1,
                "phase_title": "Networking & Operating Systems Security",
                "duration_weeks": 4,
                "skills_covered": ["TCP/IP Stack", "Subnetting", "Wireshark", "Linux Administration", "Bash Scripting"],
                "weekly_breakdown": [
                    {"week": 1, "title": "Network Protocols & Architecture", "topics": ["OSI Model", "TCP/IP Stack", "DNS", "HTTP/HTTPS", "SSH"], "practice": "Capture and analyze network traffic in Wireshark"},
                    {"week": 2, "title": "Linux Systems Administration", "topics": ["Permissions", "User Access Control", "Process Management", "Log Files"], "practice": "Configure secure Linux server environment"},
                    {"week": 3, "title": "Bash & Python Scripting for Security", "topics": ["Automation", "File Manipulation", "Socket Programming"], "practice": "Write custom port scanner in Python"},
                    {"week": 4, "title": "Firewalls & Port Scanning", "topics": ["Nmap", "UFW/IPTables", "Port Scanning Techniques"], "practice": "Perform network audit using Nmap"}
                ],
                "milestone_project": "Network Security Audit & Automated Port Scanner Script Suite",
                "learning_resources": [
                    {"title": "TryHackMe Networking Fundamentals", "url": "https://tryhackme.com/", "type": "PRACTICE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 2,
                "phase_title": "Web Application Security & OWASP",
                "duration_weeks": 4,
                "skills_covered": ["OWASP Top 10", "SQL Injection", "XSS & CSRF", "Burp Suite", "API Security"],
                "weekly_breakdown": [
                    {"week": 5, "title": "Burp Suite & HTTP Inspection", "topics": ["Proxy configuration", "Request interception", "Repeater"], "practice": "Inspect HTTP headers and parameters"},
                    {"week": 6, "title": "SQL Injection & Database Attacks", "topics": ["Union-based SQLi", "Blind SQLi", "Mitigation & Parameterized Queries"], "practice": "Solve 10 SQLi challenges on PortSwigger Web Security Academy"},
                    {"week": 7, "title": "Cross-Site Scripting (XSS) & CSRF", "topics": ["Reflected XSS", "Stored XSS", "DOM XSS", "CSRF Tokens"], "practice": "Exploit and remediate XSS vulnerabilities"},
                    {"week": 8, "title": "Authentication & Authorization Bypasses", "topics": ["Session Management", "JWT Weaknesses", "IDOR Vulnerabilities"], "practice": "Perform IDOR security assessment"}
                ],
                "milestone_project": "Comprehensive Web Application Penetration Test Report on Vulnerable Target",
                "learning_resources": [
                    {"title": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "type": "PRACTICE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 3,
                "phase_title": "System Pentesting, Vulnerability Assessment & Exploitation",
                "duration_weeks": 4,
                "skills_covered": ["Metasploit", "Privilege Escalation", "Active Directory Security", "Reverse Shells"],
                "weekly_breakdown": [
                    {"week": 9, "title": "Vulnerability Scanning & Nessus", "topics": ["Vulnerability assessment", "CVE Database", "CVSS Scoring"], "practice": "Run system scan and generate vulnerability report"},
                    {"week": 10, "title": "Exploitation with Metasploit Framework", "topics": ["Msfconsole", "Payloads", "Exploit modules", "Listeners"], "practice": "Exploit known vulnerable service in lab environment"},
                    {"week": 11, "title": "Linux & Windows Privilege Escalation", "topics": ["SUID binaries", "Sudo abuse", "Unquoted Service Paths"], "practice": "Escalate privileges from user to root/admin"},
                    {"week": 12, "title": "Active Directory Fundamentals", "topics": ["Domain Controllers", "Kerberos", "BloodHound", "Pass-the-Hash"], "practice": "Map AD relationships using BloodHound"}
                ],
                "milestone_project": "Complete Network Capture-The-Flag (CTF) Box Machine Exploitation Report",
                "learning_resources": [
                    {"title": "Hack The Box Academy", "url": "https://academy.hackthebox.com/", "type": "PRACTICE", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 4,
                "phase_title": "Defensive Security, SOC & Incident Response",
                "duration_weeks": 4,
                "skills_covered": ["SIEM Tools (Splunk/Elastic)", "Log Analysis", "Threat Hunting", "Incident Response"],
                "weekly_breakdown": [
                    {"week": 13, "title": "SIEM Configuration & Splunk", "topics": ["Log Ingestion", "SPL Queries", "Creating Alerts & Dashboards"], "practice": "Create Splunk alert rule for brute-force logins"},
                    {"week": 14, "title": "Log Analysis & Digital Forensics", "topics": ["Sysmon logs", "Windows Event IDs", "Memory Analysis (Volatility)"], "practice": "Investigate compromised disk image"},
                    {"week": 15, "title": "Threat Intelligence & MITRE ATT&CK", "topics": ["ATT&CK Matrix", "IOCs (Indicators of Compromise)", "YARA Rules"], "practice": "Map attack scenario to MITRE ATT&CK framework"},
                    {"week": 16, "title": "Incident Handling & Playbooks", "topics": ["Containment", "Eradication", "Post-Incident Reporting"], "practice": "Draft Incident Response Playbook"}
                ],
                "milestone_project": "SOC Monitoring Dashboard & Incident Response Playbook",
                "learning_resources": [
                    {"title": "Splunk Free Education", "url": "https://www.splunk.com/en_us/training.html", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            },
            {
                "phase_number": 5,
                "phase_title": "Security Certifications & Professional Prep",
                "duration_weeks": 4,
                "skills_covered": ["Security+ / EJPT Prep", "Cybersecurity Interviewing", "Report Writing", "Job Placement"],
                "weekly_breakdown": [
                    {"week": 17, "title": "Industry Certifications Prep", "topics": ["CompTIA Security+", "eJPT", "PJPT exam objectives"], "practice": "Complete 3 practice certification exams"},
                    {"week": 18, "title": "Professional Penetration Testing Reports", "topics": ["Executive Summaries", "Risk Matrix", "Remediation Steps"], "practice": "Publish polished penetration testing report"},
                    {"week": 19, "title": "GitHub Portfolio & Lab Writeups", "topics": ["Documenting CTF walkthroughs", "Security tool development"], "practice": "Publish GitHub repository of security tools"},
                    {"week": 20, "title": "Cybersecurity Technical Interviews", "topics": ["Security Scenario Questions", "Live Coding / Analysis", "Mock Interviews"], "practice": "Complete 3 mock security interviews"}
                ],
                "milestone_project": "Professional Security Audit Portfolio & Certified Security Resume",
                "learning_resources": [
                    {"title": "OWASP Official Website", "url": "https://owasp.org/", "type": "DOCUMENTATION", "badge": "FREE"}
                ]
            }
        ]
    }
}

def generate_dynamic_curriculum(career: str) -> Dict[str, Any]:
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
                    {"title": f"Official {clean_career} Documentation", "url": "https://google.com", "type": "DOCUMENTATION", "badge": "FREE"}
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
    template = CAREER_CURRICULUM_TEMPLATES.get(target_career)
    if not template:
        for key, t in CAREER_CURRICULUM_TEMPLATES.items():
            if key.lower() in target_career.lower() or target_career.lower() in key.lower():
                template = t
                break

    if not template:
        template = generate_dynamic_curriculum(target_career)

    phases = template["phases"]
    if duration == "30-day":
        phases = phases[:2]
    elif duration == "3-month":
        phases = phases[:3]

    return {
        "target_career": target_career,
        "duration": duration,
        "level": level,
        "overview": template["description"],
        "prerequisites": template["prerequisites"],
        "weekly_hours": template["weekly_hours"],
        "career_outcomes": template["career_outcomes"],
        "phases": phases
    }
