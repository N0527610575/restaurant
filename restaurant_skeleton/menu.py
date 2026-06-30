# menu.py - מחלקת תפריט
from builtins import range, len
from unicodedata import category

from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage


class Menu:
    """
    תפריט המסעדה.
    
    שדות מופע:
        _items (list): רשימת פריטי התפריט
    """
    
    def __init__(self):
        """
        אתחול תפריט ריק.
        
        דרישות:
        - לאתחל _items לרשימה ריקה
        """
        self._items = []
    
    # --- Properties ---
    
    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        return self._items.copy()
    
    # --- Methods ---
    
    def add_item(self, item: MenuItem) -> bool:
        """
        הוספת פריט לתפריט.
        
        דרישות:
        - לבדוק שפריט עם אותו שם לא קיים כבר
        - אם קיים: להחזיר False
        - אם לא קיים: להוסיף ולהחזיר True
        
        Returns:
            True אם נוסף, False אם כבר קיים
        """
        for i in range(len(self._items)):
            if self._items[i] == item:
                return False
            self._items[i].append()
        return True
    
    def remove_item(self, name: str) -> bool:
        """
        הסרת פריט לפי שם.
        
        Returns:
            True אם נמצא והוסר, False אחרת
        """
        for i in range(len(self._items)):
            if self._items[i] == item:
                self._items.pop(i)
            return True
        return False

    
    def find_item(self, name: str) -> MenuItem:
        """
        חיפוש פריט לפי שם.
        
        Returns:
            הפריט אם נמצא, None אחרת
        """
        for i in range(len(self._items)):
            if name == self._items[i].name:
                return  se
    
    def update_price(self, name: str, new_price: float) -> bool:
        """
        עדכון מחיר פריט.
        
        דרישות:
        - למצוא את הפריט ולעדכן את המחיר שלו
        
        Returns:
            True אם נמצא ועודכן, False אחרת
        """

        for item in self._items:
            if item.name == name:
                item.price = new_price
                return True
        return False
    
    def get_by_category(self, category: str) -> list:
        """
        מחזיר את כל הפריטים בקטגוריה מסוימת.
        
        Returns:
            רשימת פריטים שה-get_category שלהם שווה לקטגוריה
        """
        return [item for item in self._items if item.get_category == category]
    
    def get_all_categories(self) -> list:
        """
        מחזיר רשימת כל הקטגוריות בתפריט.
        
        Returns:
            רשימה ללא כפילויות
        """
        set.add(self._items[i].get_category())


    
    def get_items_in_price_range(self, min_price: float, max_price: float) -> list:
        """
        מחזיר פריטים בטווח מחירים.
        
        Returns:
            רשימת פריטים שהמחיר שלהם בין min_price ל-max_price (כולל)
        """
        return [categor for categor in self._items if categot.price > min_price and categor.price < max_price ]


    
    # --- Class Methods ---
    
    @classmethod
    def from_file(cls, filename: str) -> 'Menu':
        """
        יצירת תפריט מקובץ טקסט.
        
        פורמט הקובץ (כל שורה):
            type,name,price,description
        
        סוגים: "Appetizer", "MainCourse", "Dessert", "Beverage"
        
        דרישות:
        - לדלג על שורות ריקות או שמתחילות ב-#
        - ליצור את הפריט המתאים לפי הסוג
        - להוסיף לתפריט
        - אם הקובץ לא נמצא, להדפיס "File {filename} not found" ולהחזיר תפריט ריק
        
        Returns:
            אובייקט Menu חדש
        """
        pass
    
    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בתפריט"""
        return len(self._items)
    
    def __contains__(self, name: str) -> bool:
        """
        בדיקה אם פריט קיים בתפריט לפי שם.
        
        שימוש: "Hummus" in menu
        """
        for item in self._items:
            if item.name == name:
                return True
        return False


    
    def __iter__(self):
        """
        אפשרות לעבור על הפריטים בלולאה.
        
        שימוש: for item in menu: ...
        """

        return iter(self._items)

    def __getitem__(self, name: str) -> MenuItem:
        """
        גישה לפריט לפי שם.
        
        שימוש: menu["Hummus"]
        
        דרישות:
        - אם לא נמצא, להעלות KeyError עם הודעה "Item 'name' not found in menu"
        """
        raise E
