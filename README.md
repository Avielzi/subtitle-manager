# Subtitle Manager

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/Avielzi/subtitle-manager?style=for-the-badge)](LICENSE)



[English](#english) | [עברית](#hebrew)

<a name="english"></a>

## 🇬🇧 English

### Project Description

This project provides a robust Subtitle Manager, designed to simplify the process of handling subtitles for media files. It includes a setup and dependency management script to ensure a smooth installation and execution experience. The tool is built with Python and offers functionalities for checking system status, installing necessary packages, running the main application, and performing a clean uninstallation.

### Features

*   **Python Version Check**: Ensures compatibility with Python 3.8+.
*   **Dependency Management**: Automatically installs and tracks required Python packages (`subliminal`, `babelfish`).
*   **Tkinter Check**: Verifies the availability of Tkinter for the GUI.
*   **Interactive Menu**: Provides a command-line interface for easy interaction.
*   **Clean Uninstall**: Removes only the packages installed by this setup script, preventing interference with other user-installed packages.
*   **Application Launch**: Installs dependencies if needed and launches the main GUI application.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Avielzi/subtitle-manager.git
    cd subtitle-manager
    ```
2.  **Run the setup script**:
    ```bash
    python subtitle_manager_setup.py install
    ```
    This command will check your Python environment and install all necessary dependencies.

### Usage

After installation, you can use the `subtitle_manager_setup.py` script with various commands:

*   **Interactive Menu (Default)**:
    ```bash
    python subtitle_manager_setup.py
    ```
    This will launch an interactive menu allowing you to check status, install, run, or uninstall.

*   **Install Dependencies**:
    ```bash
    python subtitle_manager_setup.py install
    ```
    Installs all required Python packages.

*   **Run Application**:
    ```bash
    python subtitle_manager_setup.py run
    ```
    Installs dependencies (if not already installed) and then launches the main GUI application (`subtitle_manager_gui_single_file_v_1_python.py`).

*   **Uninstall Packages**:
    ```bash
    python subtitle_manager_setup.py uninstall
    ```
    Removes only the packages installed by this setup script.

*   **Check Status**:
    ```bash
    python subtitle_manager_setup.py check
    ```
    Performs a full system check, verifying Python version, pip, Tkinter, and required packages.

### Dependencies

The `subtitle_manager_setup.py` script manages the following Python packages:

*   `subliminal`
*   `babelfish`

It also requires `tkinter` for the GUI, which typically comes with Python but might need separate installation on some Linux distributions (e.g., `sudo apt install python3-tk`).

### Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<a name="hebrew"></a>

## 🇮🇱 עברית

### תיאור הפרויקט

פרויקט זה מספק מנהל כתוביות חזק, שנועד לפשט את תהליך הטיפול בכתוביות לקבצי מדיה. הוא כולל סקריפט התקנה וניהול תלויות כדי להבטיח חווית התקנה והפעלה חלקה. הכלי בנוי בפייתון ומציע פונקציונליות לבדיקת מצב המערכת, התקנת חבילות נדרשות, הפעלת היישום הראשי וביצוע הסרה נקייה.

### תכונות

*   **בדיקת גרסת פייתון**: מבטיח תאימות עם פייתון 3.8 ומעלה.
*   **ניהול תלויות**: מתקין ועוקב אוטומטית אחר חבילות פייתון נדרשות (`subliminal`, `babelfish`).
*   **בדיקת Tkinter**: מאמת את זמינות Tkinter עבור ממשק המשתמש הגרפי.
*   **תפריט אינטראקטיבי**: מספק ממשק שורת פקודה לאינטראקציה קלה.
*   **הסרה נקייה**: מסיר רק את החבילות שהותקנו על ידי סקריפט ההתקנה הזה, ומונע הפרעה לחבילות אחרות שהותקנו על ידי המשתמש.
*   **הפעלת יישום**: מתקין תלויות במידת הצורך ולאחר מכן מפעיל את יישום ממשק המשתמש הגרפי הראשי (`subtitle_manager_gui_single_file_v_1_python.py`).

### התקנה

1.  **שכפול המאגר**:
    ```bash
    git clone https://github.com/Avielzi/subtitle-manager.git
    cd subtitle-manager
    ```
2.  **הפעלת סקריפט ההתקנה**:
    ```bash
    python subtitle_manager_setup.py install
    ```
    פקודה זו תבדוק את סביבת הפייתון שלך ותתקין את כל התלויות הנדרשות.

### שימוש

לאחר ההתקנה, תוכל להשתמש בסקריפט `subtitle_manager_setup.py` עם פקודות שונות:

*   **תפריט אינטראקטיבי (ברירת מחדל)**:
    ```bash
    python subtitle_manager_setup.py
    ```
    זה יפעיל תפריט אינטראקטיבי שיאפשר לך לבדוק סטטוס, להתקין, להפעיל או להסיר התקנה.

*   **התקנת תלויות**:
    ```bash
    python subtitle_manager_setup.py install
    ```
    מתקין את כל חבילות הפייתון הנדרשות.

*   **הפעלת יישום**:
    ```bash
    python subtitle_manager_setup.py run
    ```
    מתקין תלויות (אם לא הותקנו כבר) ולאחר מכן מפעיל את יישום ממשק המשתמש הגרפי הראשי (`subtitle_manager_gui_single_file_v_1_python.py`).

*   **הסרת חבילות**:
    ```bash
    python subtitle_manager_setup.py uninstall
    ```
    מסיר רק את החבילות שהותקנו על ידי סקריפט ההתקנה הזה.

*   **בדיקת סטטוס**:
    ```bash
    python subtitle_manager_setup.py check
    ```
    מבצע בדיקת מערכת מלאה, מאמת את גרסת הפייתון, pip, Tkinter והחבילות הנדרשות.

### תלויות

סקריפט `subtitle_manager_setup.py` מנהל את חבילות הפייתון הבאות:

*   `subliminal`
*   `babelfish`

הוא דורש גם את `tkinter` עבור ממשק המשתמש הגרפי, אשר בדרך כלל מגיע עם פייתון אך ייתכן שידרוש התקנה נפרדת בהפצות לינוקס מסוימות (לדוגמה, `sudo apt install python3-tk`).

### תרומה לפרויקט

תרומות יתקבלו בברכה! אנא אל תהססו לפתוח בעיות או להגיש בקשות משיכה.

### רישיון

פרויקט זה מורשה תחת רישיון MIT - ראה את קובץ [LICENSE](LICENSE) לפרטים נוספים.
