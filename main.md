# Linus Horn

site url: https://linush.org
github: https://github.com/MixoMax

19 years old, born May 2006 in Hamburg, Germany.

Timeline:

Education:
- 2012 - 2022: Primary school (Grundschule Forßmanstraße) and Gymnasium (Wilhelm-Gymnasium Hamburg)
- 2021 - 2022: Spent 7 Months at sea as part of "High seas High school" (HSHS) program on the Tallship Guulden Leeuw, where I took on Navigational and Seamanship duties
- 2022 - 2024: Abiutur at Wilhelm-Gymnasium Hamburg. Gradued with 1.9, Leistungskurse: Math, English, Physics, Geography
- WS 2024 - present: Studying Computer Science at University of Rostock (currently in my 3rd semester)

Work Experience:
- 2022 - 2023: 9 Months "minijob" at ITVT Süd GmbH, as a python backend developerand data analyst:
    - Python, Embedding models, vector databases, semantic search, Fastapi, dataprocessing and acquisition
    - Technologies used: Python, Fastapi, Tensorflow, Qdrant, Pinecone, Weaviate, Postgres, Pandas, Numpy
    - (as a small side project also helped write an automated testing framework for their existing web applications, testing response timeings and correctness of data to find API routes that were slow or broken)
- 2024: 2 Week internship at Formosa 2 Windpark in Taiwan, working with JERA Next as a data analyst intern, working on data pipelines and predictive maintenance models for wind turbines, based on lots of sensor data (47 Turbines, 150 sensors each, data points every 5 seconds = over 4 million data points per day)
    - Technologies used: Python, Pandas, Numpy, Scikit-learn, SQL, Jupyter Notebooks
    - Gained experience working with large datasets, cleaning and preprocessing data, feature engineering, live data pipelines, and building predictive models
    - Built live dashboards to monitor turbine performance and predict maintenance needs
    - Automated weekly reports for the weekly meetings with the Operations team


- Selfhosting enthusiast: I run a variety of selfhosted servers at home and on VPSs, including:
    - Obelix (main): Dual Xeon E5-2670v2, 128GB RAM, 1 TB SSD, 9 TB HDD, Tesla P40 GPU running:
        -  Pterodactyl for game servers (multiple Minecraft servers)
        -  Jupyter notebooks for data science and machine learning experiments
        -  SMB share as a local NAS
        -  Media server (Jellyfin)
        -  Windows and Ubuntu VMs for remote access from within my network (windows for gaming and software that only runs on windows, ubuntu to have a isolated linux environment)
        -  Ollama and llama.cpp for AI inference locally
        -  Qdrant vector database for embedding storage
        -  Self hosting my own websites and web apps (including this one)
    - J2: i7 7700hq, 16GB RAM, 512GB SSD, GTX 1050TI Currently offline, used to run minecraft servers, before Obelix was set up
    - J4: i7 7700, 16GB RAM, 256GB SSD: Currently offline, will be used to host some minecraft server, as it has a higher single core performance than Obelix
    - VPS (Hetzner CX22): 2vCPU, 4GB RAM, 80GB SSD, running:
        - Nginx reverse proxy
        - Port forwarding to my home servers using frp

Personal Projects:

## blog.linush.org
High-Performance Markdown CMS & API

**Description:**
A custom-built, flat-file Content Management System engineered with **Python** and **FastAPI**. By eliminating traditional database latency in favor of a file-system architecture, this application achieves sub-millisecond response times and perfect Lighthouse performance scores.

The system features a **hybrid rendering strategy**, utilizing a custom server-side pipeline to transform Markdown and Frontmatter into SEO-friendly HTML, while simultaneously exposing a RESTful JSON API for dynamic client-side interactions. The frontend is built with vanilla JavaScript and modern CSS3 (Flexbox/Grid), ensuring a lightweight footprint without the overhead of heavy UI frameworks.

**Key Technical Features:**
*   **Dual-Mode Architecture:** Supports both Server-Side Rendering (SSR) for SEO and asynchronous API endpoints for dynamic content.
*   **Advanced Content Pipeline:** Custom ingestion engine supporting technical documentation needs, including syntax highlighting (PrismJS), mathematical notation (KaTeX), and automatic metadata extraction.
*   **Zero-Dependency Templating:** A logic-less injection system developed to handle view generation with minimal processing overhead.


## globe.linush.org
**3D Geospatial Graph Traversal Engine**
**An interactive full-stack application that visualizes global land connectivity by modeling the world map as a traversable graph.**

*   **Data Pipeline:** Engineered a custom Python ETL pipeline to scrape unstructured Wikipedia data, normalize political borders, and construct a directed graph topology.
*   **Algorithmic Backend:** Developed a high-performance **FastAPI** server that utilizes Breadth-First Search (BFS) with **$O(V+E)$** time complexity to calculate shortest land-based routes between nations.
*   **3D Visualization:** Built an immersive frontend using **Globe.gl** and **D3.js**. Features include computational geometry logic for dynamic camera centering, MultiPolygon rendering, and a custom proxy for server-side asset caching.

**Tech Stack:** Python, FastAPI, Three.js, D3.js, BeautifulSoup.


## ping.linush.org
Real-Time Network Protocol Analyzer
**Technologies:** Python (FastAPI), WebSockets, Async I/O, Chart.js

**Project Overview:**
Engineered a high-performance telemetry tool designed to benchmark latency trade-offs between stateless HTTP requests and persistent WebSocket connections. Built on an asynchronous **FastAPI** architecture, the system handles high-concurrency traffic to measure precise Round Trip Time (RTT) and network jitter. The frontend features a custom **Chart.js** dashboard that renders live statistical data, allowing users to visualize protocol overhead and network stability in real-time.


## scryfall.linush.org
Local-Scryfall & Draft Simulator
**Stack:** Python, FastAPI, Recursive Descent Parsing, Concurrency

**Summary:**
"Engineered a high-performance search engine and multiplayer draft simulator designed to operate without external database dependencies. The core architecture features a **custom recursive descent parser** that tokenizes a **Domain Specific Language (DSL)** into an **Abstract Syntax Tree (AST)**, enabling the evaluation of nested boolean logic and operator precedence against an in-memory dataset. Beyond the search algorithms, the system utilizes a **multi-threaded ETL pipeline** for parallel asset ingestion and normalization, alongside a stateful backend that implements rarity-weighted probability algorithms to simulate accurate draft rotations."