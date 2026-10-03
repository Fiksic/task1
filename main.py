
# ========================================================
# ПРАКТИЧЕСКАЯ РАБОТА: ОТЛАДКА ПРОГРАММНЫХ МОДУЛЕЙ
# ФАЙЛ: task1.py
# ЗАДАНИЕ: Найти и устранить логическую ошибку в расчете скидки
# ========================================================

def calculate_discount_price(price: float, discount_percent: float) -> float:
    """
    Функция рассчитывает итоговую стоимость товара с учетом скидки.
    
    Параметры:
        price (float): исходная цена товара в рублях
        discount_percent (float): размер скидки в процентах (от 0 до 100)
        
    Возвращает:
        float: итоговая цена товара после применения скидки
    """
    # 1. Вычисляем сумму скидки в рублях
    discount_rubles = price * (discount_percent / 100)
    
    # 2. Вычисляем цену со скидкой (ИСПРАВЛЕНО: было '+', стало '-')
    final_price = price - discount_rubles
    
    return final_price


# --- ТЕСТОВЫЙ БЛОК (для проверки работы модуля) ---
if __name__ == "__main__":
    test_price = 1000
    test_discount = 10
    
    print("--- ТЕСТИРОВАНИЕ МОДУЛЯ ---")
    print(f"Исходная цена: {test_price} руб.")
    print(f"Скидка: {test_discount}%")
    print(f"Ожидаемый результат: {test_price - (test_price * test_discount / 100)} руб.")
    
    # Вызов функции
    result = calculate_discount_price(test_price, test_discount)
    
    print(f"Фактический результат работы программы: {result} руб.")
    
    if result == 900:
        print("\n [УСПЕХ] Ошибка найдена и устранена верно!")
    else:
        print("\n [ОШИБКА] Программа считает неверно! Запустите отладчик (Debug).")
