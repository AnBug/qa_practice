import pytest
import allure  # Для отчетов Allure
from loguru import logger  # Для логов в Kibana

# Настраиваем запись логов в файл
logger.add("automation.log", rotation="1 MB")

@allure.feature("Параметризация данных")
@allure.story("Проверка базовых типов")
@pytest.mark.parametrize("test_input", [10, "слово", True])
def test_simple_types(test_input):
    
    # 1. Логируем в файл (для будущего в Kibana)
    logger.info(f"Старт теста с данными: {test_input}")
    
    # 2. Создаем шаг в Allure (для отчета в браузере)
    with allure.step(f"Валидация значения: {test_input}"):
        
        # Сама проверка
        result = test_input is not False
        
        if result:
            logger.success(f"Тест пройден для {test_input}")
        else:
            logger.error(f"Тест провален для {test_input}")
            
        assert result
