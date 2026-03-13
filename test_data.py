import pytest
from loguru import logger

# Настройка: логи будут писаться и в консоль, и в файл
logger.add("automation.log", rotation="1 MB") 

@pytest.mark.parametrize("status_code", [200, 404, 500])
def test_api_status_logic(status_code):
    # Логируем начало шага (как в Kibana)
    logger.info(f"СТАРТ: Проверка обработки статус-кода {status_code}")
    
    if status_code == 500:
        logger.error("ОБНАРУЖЕНА ОШИБКА: Сервер вернул 500")
        assert False, "Сервер упал"
    
    logger.success(f"ЗАВЕРШЕНО: Код {status_code} обработан корректно")
    assert status_code < 500
