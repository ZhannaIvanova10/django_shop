#!/usr/bin/env python
"""Команды для Django Shell - Домашнее задание №2"""

from catalog.models import Category, Product

print("=" * 50)
print("ДОМАШНЕЕ ЗАДАНИЕ №2 - DJANGO SHELL ОПЕРАЦИИ")
print("=" * 50)
# 1. Все категории
print("\n1. ВСЕ КАТЕГОРИИ:")
categories = Category.objects.all()
if categories:
    for cat in categories:
        print(f"   - ID: {cat.id}, Название: {cat.name}")
else:
    print("   Нет категорий")

# 2. Все продукты
print("\n2. ВСЕ ПРОДУКТЫ:")
products = Product.objects.all()
if products:
    for p in products:
        print(f"   - {p.name}: {p.price} руб. (Категория: {p.category.name})")
else:
    print("   Нет продуктов")
# 3. Продукты в категории "Электроника"
print("\n3. ПРОДУКТЫ В КАТЕГОРИИ 'ЭЛЕКТРОНИКА':")
try:
    electronics = Category.objects.get(name='Электроника')
    electronic_products = electronics.products.all()
    if electronic_products:
        for p in electronic_products:
            print(f"   - {p.name}: {p.price} руб.")
    else:
        print("   В этой категории нет продуктов")
except Category.DoesNotExist:
    print("   Категория 'Электроника' не найдена")

# 4. Создаем новую категорию и продукт
print("\n4. СОЗДАЕМ НОВУЮ КАТЕГОРИЮ И ПРОДУКТ:")
new_category, created = Category.objects.get_or_create(
    name='Тестовая категория',
    defaults={'description': 'Категория для тестирования'}
)
if created:
    print(f"   ✓ Создана категория: {new_category.name}")
else:
    print(f"   Категория уже существует: {new_category.name}")

new_product, created = Product.objects.get_or_create(
    name='Тестовый продукт',
    defaults={
        'description': 'Продукт для тестирования',
        'category': new_category,
        'price': 999.99
    }
)
if created:
    print(f"   ✓ Создан продукт: {new_product.name} - {new_product.price} руб.")
else:
    print(f"   Продукт уже существует: {new_product.name}")

# 5. Обновляем цену
print("\n5. ОБНОВЛЯЕМ ЦЕНУ ПРОДУКТА:")
if products:
    product_to_update = products.first()
    old_price = product_to_update.price
    product_to_update.price = old_price + 1000
    product_to_update.save()
    print(f"   ✓ Обновлен продукт: {product_to_update.name}")
    print(f"     Старая цена: {old_price} руб.")
    print(f"     Новая цена: {product_to_update.price} руб.")
else:
    print("   Нет продуктов для обновления")

# 6. Удаляем продукт
print("\n6. УДАЛЯЕМ ПРОДУКТ:")
count_before = Product.objects.count()
if count_before > 2:  # Оставляем минимум 2 продукта
    product_to_delete = Product.objects.last()
    print(f"   Удаляем: {product_to_delete.name}")
    product_to_delete.delete()
    print(f"   ✓ Продукт удален")
    print(f"     Было: {count_before} продуктов")
    print(f"     Стало: {Product.objects.count()} продуктов")
else:
    print(f"   Не удаляем - мало продуктов ({count_before} шт.)")

# 7. Итоги
print("\n" + "=" * 50)
print("ИТОГИ:")
print(f"Категорий в базе: {Category.objects.count()}")
print(f"Продуктов в базе: {Product.objects.count()}")
print("=" * 50)

print("\n✅ Все операции Django Shell выполнены успешно!")
