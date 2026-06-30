# table.py - מחלקת שולחן


class Table:
    """
    שולחן במסעדה.
    
    שדות מחלקה:
        total_tables (int): סה"כ שולחנות שנוצרו (מתעדכן בכל יצירה)
    
    שדות מופע:
        _number (int): מספר השולחן (פרטי)
        _seats (int): כמות מקומות ישיבה (פרטי)
        _is_occupied (bool): האם תפוס (פרטי)
    """
    
    total_tables: int = 0
    
    def __init__(self, number: int, seats: int = 4):
        """
        אתחול שולחן.
        
        דרישות:
        - לשמור את number ב-_number
        - לשמור את seats ב-_seats
        - לאתחל _is_occupied ל-False
        - להעלות את total_tables ב-1
        
        Args:
            number: מספר השולחן
            seats: כמות מקומות (ברירת מחדל: 4)
        """
        self._number =number
        self._seats = seats
        self._is_occupied = False
        Table.total_tables += 1


    
    # --- Properties ---
    
    @property
    def number(self) -> int:
        """מחזיר את מספר השולחן"""
        return self._number
    
    @property
    def seats(self) -> int:
        """מחזיר את כמות המקומות"""
        return self._seats
    
    @property
    def is_occupied(self) -> bool:
        """מחזיר האם השולחן תפוס"""
        return self._is_occupied
    
    # --- Methods ---
    
    def occupy(self) -> bool:
        """
        סימון השולחן כתפוס.
        
        דרישות:
        - אם כבר תפוס: להחזיר False
        - אחרת: לסמן כתפוס ולהחזיר True
        
        Returns:
            True אם הצליח, False אם כבר היה תפוס
        """
        if not self._is_occupied:
            self._is_occupied = True
            return True
        return False



    def free(self):
        """סימון השולחן כפנוי"""
        self._is_occupied = False
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Table X (Y seats) - Free/Occupied"
        """
        if self._is_occupied:
            return f"Table {self._number} ({self._seats}) - Occupied"
        return f"Table {self._number} ({self._seats}) - Free"

