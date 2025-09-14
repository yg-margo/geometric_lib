"""
Скрипт для запуска всех unit-тестов проекта geometric_lib.

Этот модуль обеспечивает автоматическое обнаружение и выполнение всех тестов
в директории tests/. Поддерживает подробный вывод результатов тестирования
и возвращает соответствующие коды завершения.

Функции:
    run_all_tests() - запускает все обнаруженные тесты

Использование:
    python run_tests.py

Возвращаемые коды:
    0 - все тесты прошли успешно
    1 - один или несколько тестов провалились
"""
import unittest
import sys
import os

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def run_all_tests():
    """
    Запускает все unit-тесты в проекте geometric_lib.

    Автоматически обнаруживает все тестовые файлы в директории tests/
    с паттерном test_*.py и выполняет их с подробным выводом результатов.
    Использует unittest.TestLoader для поиска тестов и unittest.TextTestRunner
    для их выполнения с детализированным отчетом.

    Процесс выполнения:
        1. Определяет путь к директории tests/
        2. Использует TestLoader.discover() для поиска всех test_*.py файлов
        3. Запускает найденные тесты с verbosity=2 для подробного вывода
        4. Анализирует результаты и возвращает статус успеха

    Возвращает:
        bool: True если все тесты прошли успешно, False если есть неудачи

    Исключения:
        FileNotFoundError: если директория tests/ не найдена
        ImportError: если не удается импортировать тестовые модули

    Пример использования:
        >>> success = run_all_tests()
        >>> if success:
        ...     print("Все тесты прошли!")
        ... else:
        ...     print("Есть проваленные тесты!")

    Пример вывода:
        test_area_positive_radius (tests.test_circle.CircleTestCase) ... ok
        test_area_zero_radius (tests.test_circle.CircleTestCase) ... ok
        ...
        Ran 28 tests in 0.003s
        OK
    """
    try:
        # Обнаруживаем и запускаем все тесты в директории tests
        loader = unittest.TestLoader()
        start_dir = os.path.join(os.path.dirname(__file__), 'tests')

        if not os.path.exists(start_dir):
            print(f"❌ Ошибка: Директория {start_dir} не найдена!")
            return False

        suite = loader.discover(start_dir, pattern='test_*.py')

        # Проверяем, что тесты найдены
        if suite.countTestCases() == 0:
            print("⚠️ Предупреждение: Тесты не найдены!")
            return False

        print(f"🔍 Найдено {suite.countTestCases()} тестов")
        print("=" * 60)

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        print("=" * 60)

        return result.wasSuccessful()

    except Exception as e:
        print(f"❌ Ошибка при выполнении тестов: {e}")
        return False


def print_test_summary(result):
    """
    Выводит краткую сводку результатов тестирования.

    Анализирует объект TestResult и выводит статистику по количеству
    пройденных, проваленных тестов и ошибок в удобочитаемом формате.

    Параметры:
        result (unittest.TestResult): результат выполнения тестов

    Возвращает:
        None

    Пример вывода:
        📊 Сводка тестирования:
        ✅ Пройдено: 25
        ❌ Провалено: 2
        ⚠️ Ошибки: 1
        📈 Процент успеха: 89.3%
    """
    if not result:
        return

    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total - failures - errors
    success_rate = (passed / total * 100) if total > 0 else 0

    print("📊 Сводка тестирования:")
    print(f"✅ Пройдено: {passed}")
    if failures > 0:
        print(f"❌ Провалено: {failures}")
    if errors > 0:
        print(f"⚠️ Ошибки: {errors}")
    print(f"📈 Процент успеха: {success_rate:.1f}%")


if __name__ == '__main__':
    """
    Точка входа в программу при запуске скрипта напрямую.

    Выполняет следующие действия:
        1. Запускает все тесты через run_all_tests()
        2. Выводит результирующее сообщение
        3. Завершает программу с соответствующим кодом возврата

    Коды возврата:
        0 - все тесты прошли успешно
        1 - один или несколько тестов провалились или произошла ошибка
    """
    print("🚀 Запуск unit-тестов проекта geometric_lib")
    print("=" * 60)

    success = run_all_tests()

    if success:
        print("\n✅ Все тесты прошли успешно!")
        print("🎉 Код готов к использованию!")
        sys.exit(0)
    else:
        print("\n❌ Некоторые тесты провалились!")
        print("🔧 Необходимо исправить ошибки перед релизом.")
        sys.exit(1)