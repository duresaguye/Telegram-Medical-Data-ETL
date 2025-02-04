# 🚀 Telegram Medical Data ETL  

## 📌 Project Overview  
This project is  focuses on **building a data warehouse** for Ethiopian medical businesses by scraping data from **Telegram channels**.  

### 🎯 **Key Objectives**  
- Develop a **data scraping and collection pipeline** for Telegram channels.  
- Implement **data cleaning and transformation** using ETL processes.  
- Perform **object detection using YOLO** on collected images.  
- Design and implement a **data warehouse** for structured storage.  
- Develop an **API using FastAPI** to expose the collected data.  

---

## 🏢 Business Need  
Kara Solutions, a data science company, requires a **centralized data warehouse** to store and analyze Ethiopian medical business data from Telegram. The warehouse will:  
✅ Improve **data accessibility and organization**.  
✅ Enable **data analysis to detect trends and patterns**.  
✅ Enhance **decision-making** through structured data.  
✅ Allow **efficient querying and reporting**.  

---

## 🛠️ Technologies Used  
- **Python** (Beautiful Soup, Scrapy, Selenium, Telethon)  
- **YOLO** (Object Detection)  
- **PostgreSQL** (Data Storage)  
- **DBT** (Data Transformation)  
- **FastAPI** (API Development)  
- **SQLAlchemy** (Database ORM)  


---

## 📂 Project Structure  
```
Telegram-Medical-Data-ETL/
│── api/                  # API development using FastAPI
│── data_processing/      # ETL and DBT transformations
│── data_scraping/        # Telegram scraping scripts
│── deployment/           # Deployment configurations
│── docs/                 # Documentation
│── logs/                 # Logging and monitoring
│── notebooks/            # Jupyter notebooks for data exploration
│── object_detection/     # YOLO object detection implementation
│── photos/               # Collected images for processing
│── scripts/              # Utility scripts
│── setup.py              # Setup configurations
│── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 📌 Tasks & Implementation  

### 📝 **1. Data Scraping & Collection**  
- Extract medical business data from Telegram channels:  
  - [DoctorsET](https://t.me/DoctorsET)  
  - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)  
  - [Yetenaweg](https://t.me/yetenaweg)  
  - [EAHCI](https://t.me/EAHCI)  
  - And more from [et.tgstat.com](https://et.tgstat.com/medicine)  

- **Tools:** `Telethon`, `BeautifulSoup`, `Scrapy`, `Selenium`  
- **Storage:** Temporary local database or files  
- **Monitoring:** Implement logging for tracking and error handling  

### 🛠 **2. Data Cleaning & Transformation**  
- **Cleaning:** Remove duplicates, handle missing values, standardize formats  
- **Transformation:** Use **DBT** to define and execute SQL-based transformations  
- **Storage:** Store cleaned data in PostgreSQL  

### 🖼 **3. Object Detection Using YOLO**  
- **Setup YOLOv5:**  
  ```bash
  git clone https://github.com/ultralytics/yolov5.git
  cd yolov5
  pip install -r requirements.txt
  ```  
- **Process images** from **Telegram channels**  
- **Detect objects** and extract relevant data  
- **Store results** in the database  

### 🌐 **4. API Development Using FastAPI**  
- **Install FastAPI & Uvicorn:**  
  ```bash
  pip install fastapi uvicorn
  ```  
- **Create API Endpoints:**  
  - `GET /data` → Retrieve stored medical data  
  - `GET /images` → Retrieve processed images  
  - `POST /data` → Insert new data into the warehouse  
- **Use SQLAlchemy** for database interactions  
- **Implement logging & monitoring**  

---

## 📊 Learning Outcomes  
### 🧑‍💻 **Technical Skills**  
✅ **Web Scraping:** Telethon, BeautifulSoup, Scrapy, Selenium  
✅ **ETL Processes:** Extract, Transform, Load with DBT & SQL  
✅ **Database Design:** PostgreSQL, schema modeling  
✅ **Object Detection:** YOLOv5 for analyzing images  
✅ **API Development:** FastAPI, SQLAlchemy, Pydantic  
✅ **Logging & Monitoring:** Implementing robust tracking  




## 📚 References & Learning Resources  
### 📌 **Web Scraping**  
- [Beautiful Soup Guide](https://realpython.com/beautiful-soup-web-scraper-python/)  
- [Scrapy Documentation](https://scrapy.org/)  
- [Selenium Guide](https://www.selenium.dev/)  
- [Telethon Docs](https://docs.telethon.dev/en/stable/)  

### 📌 **ETL & DBT**  
- [DBT Documentation](https://docs.getdbt.com/docs/introduction)  
- [DBT Tutorial](https://www.startdataengineering.com/post/dbt-data-build-tool-tutorial/)  

### 📌 **YOLO (Object Detection)**  
- [YOLOv5 GitHub](https://github.com/ultralytics/yolov5)  
- [YOLO PyTorch Guide](https://docs.ultralytics.com/yolov5/tutorials/pytorch_hub_model_loading/)  

### 📌 **FastAPI**  
- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [FastAPI & Pydantic](https://medium.com/codenx/fastapi-pydantic-d809e046007f)  

---

## 🚀 Get Started  
1️⃣ Clone this repository:  
```bash
git clone https://github.com/duresaguye/Telegram-Medical-Data-ETL.git
cd Telegram-Medical-Data-ETL
```
2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```
3️⃣ Run data scraping:  
```bash
python data_scraping/scraper.py
```
4️⃣ Start API:  
```bash
uvicorn api.main:app --reload
```
5️⃣ Open API docs at:  

[http://127.0.0.1:8000/detections] (http://127.0.0.1:8000/detections)

---

